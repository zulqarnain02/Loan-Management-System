from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Form, Lender
import random
import MySQLdb
from django.db import connection
from django.conf import settings
# from twilio.rest import Client

# Create your views here.
def home(request):
    return render(request, 'home.html')

def loanform(request):
    if request.method == 'POST':
        loanAmount = request.POST['loanAmount']
        employeeType = request.POST['employeeType']
        netincome = request.POST['netMonthlyIncome']
        full_name = request.POST['fullName']
        phone_no = request.POST['phoneNumber']
        email = request.POST['email']
        pan_no = request.POST['panNumber']
        dob = request.POST['dob']
        pin = request.POST['pinCode']
        gender = request.POST.get('gender', False)
        address = request.POST['residingCity']
        past_loan = request.POST.get('loanHistory', False)
        credit_card = request.POST.get('creditCard', False)
        purpose_of_loan = request.POST['loanPurpose']
        lenderID = request.POST.get('lenderID')
        # If the purpose is 'Other', get the value from the textarea
        if purpose_of_loan == 'Other':
            purpose_of_loan = request.POST.get('otherPurpose', '')
        
        # Generate a random credit score between 600 and 950
        credit_score = random.randint(600, 850)
        # Save the form data to the database using MySQLdb
        print("Credit Score:", credit_score)
        conn = MySQLdb.connect(
            host='localhost',
            user='root',
            password='Zulqar@123',
            database='loanmanagement',
            use_unicode=True,
            charset='utf8mb4',
        )

        with conn.cursor() as cursor:
            cursor.execute(
        
                "INSERT INTO user (loanAmount, employeeType, netincome, full_name, phone_no, email, pan_no, DOB, pin, gender, address, past_loan, credit_card,purpose_of_loan,credit_score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)",
                [loanAmount, employeeType, netincome, full_name, phone_no, email, pan_no, dob, pin, gender, address, past_loan, credit_card, purpose_of_loan,credit_score]

            )

        conn.commit()
        conn.close()

        # Store credit_score in the session
        request.session['credit_score'] = credit_score
        request.session['phone_no']=phone_no
        request.session['lenderID'] = lenderID

        return redirect('select')

    return render(request, 'form1.html')



# def transaction(request):
#     return render(request, 'transaction.html')


def contact(request):
    return render(request, 'contact.html')


# def creditscore(request):
#     return render(request, 'creditscore.html')


from django.db import connection

def select(request):
    # Retrieve credit_score from the session
    credit_score = request.session.get('credit_score', None)
    phone_no = request.session.get('phone_no', None)
    loan_amount=request.session.get('loanAmount',None);
    customer_id = None

    if credit_score is not None:
        # Execute a raw SQL query to retrieve user details and eligible lenders
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT user.customerID, user.full_name, user.phone_no, user.loanAmount,user.credit_score, Lenders.*
                FROM user
                INNER JOIN Lenders ON user.credit_score >= Lenders.min_creditscore 
                WHERE user.credit_score = %s AND user.phone_no=%s AND user.loanAmount<=Lenders.max_amount
                """,
                [credit_score, phone_no]
            )
            # Fetch the column names
            columns = [col[0] for col in cursor.description]

            # Fetch the actual data
            user_and_lenders = [dict(zip(columns, row)) for row in cursor.fetchall()]

            # Get customer_id from the first row (if available)
            if user_and_lenders:
                customer_id = user_and_lenders[0].get('customerID')

        # Send SMS if customer_id and phone_no are available

        # **********************************************twilio message sender***************************************************
        # if customer_id and phone_no:
        #     message = f"Your loan application status is ready. Customer ID: {customer_id}"
        #     send_sms(phone_no, message)


        print("User and Eligible Lenders:", user_and_lenders)

        # Render the 'select' template with the user details and eligible lenders
        return render(request, 'select.html', {'user_and_lenders': user_and_lenders, 'customer_id': customer_id})
    else:
        # Handle the case when credit_score is not available
        return HttpResponse("Credit score not found.")


def update_user_with_lender(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        print(customer_id)
        lender_id = request.POST.get('lender_id')

        # Update the user table with the selected lender's ID
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE user
                SET lenderID = %s
                WHERE customerID = %s
                """,
                [lender_id, customer_id]
            )

            # add customerID in status table
            cursor.execute(
                """
                insert into status(customerID) values(%s)
                """,
                [customer_id]
            )

            cursor.execute(
                """
                insert into loan(customerID,lenderID) values(%s,%s)
                """,
                [customer_id,lender_id]
            )
       

        return render(request, 'requestaccepted.html')
    else:
        return HttpResponse("Invalid request method.")
    

def loan_status(request):
    customer_id = request.GET.get('customerID', None)

    if customer_id:
        # Fetch the loan status from the database
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM status
                WHERE customerID = %s
                """,
                [customer_id]
            )
            columns = [col[0] for col in cursor.description]
            status_data = cursor.fetchone()

        if status_data:
            # If the result is not empty, convert it to a dictionary
            status_data = dict(zip(columns, status_data))
            return render(request, 'status.html', {'status': status_data})
        else:
            # If the result is empty, display an error message
            return render(request, 'status.html', {'status': None, 'error_message': 'Invalid customerID. Please retry !'})
    else:
        return render(request, 'status.html', {'status': None})
    


def creditscore(request):
    if request.method == 'GET':
        customer_id = request.GET.get('customerID', None)

        if customer_id is not None:
            # Fetch the credit score from the database
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT credit_score
                    FROM user
                    WHERE customerID = %s
                    """,
                    [customer_id]
                )
                credit_score_data = cursor.fetchone()

            if credit_score_data is not None:
                # If credit score is found, render the template with the credit score
                credit_score = credit_score_data[0]

                # Render the 'creditscore.html' template with the credit score
                return render(request, 'creditscore.html', {'credit_score': credit_score, 'customer_id': customer_id})
            else:
                # If no credit score is found, display an error message
                return render(request, 'creditscore.html', {'error_message': 'Credit score not found for the provided customerID.', 'customer_id': customer_id})
        else:
            # If customer_id is not provided, render the form to enter customerID
            return render(request, 'creditscore.html', {'show_form': True})
    else:
        # If the request method is not GET, return an error response
        return HttpResponse("Invalid request method.", status=400)
    

# **********************************************twilio message sender***************************************************
# message sending
# views.py
# from twilio.rest import Client
# from django.conf import settings

# def send_sms(to, message):
#     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

#     message = client.messages.create(
#         body=message,
#         from_=settings.TWILIO_PHONE_NUMBER,
#         to=to
#     )

#     return message.sid


# transaction
def calculate_emi(loan_amount, interest_rate):
    # Assuming a monthly interest rate
    monthly_interest_rate = interest_rate / 12 / 100
    # Assuming a loan term of 12 months
    loan_term = 12

    # EMI Calculation formula
    emi_amount = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate)**loan_term / ((1 + monthly_interest_rate)**loan_term - 1)

    return round(emi_amount, 2)


# views.py

from django.db.models import Count

def transaction(request):
    show_transaction_details = False
    emi_amount = 0
    emi_count = 0
    pending_emis = 0
    payment_history = [] # Initialize payment_history
    

    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')

        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT lender_approvel
                FROM status
                WHERE customerID = %s
                """,
                [customer_id]
            )
            status_data = cursor.fetchone()

        if status_data and status_data[0] == 'approved':
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT loanAmount, lenderID
                    FROM user
                    WHERE customerID = %s
                    """,
                    [customer_id]
                )
                loan_data = cursor.fetchone()

            if loan_data:
                loan_amount, lender_id = loan_data

                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT interest_rate
                        FROM Lenders
                        WHERE lenderID = %s
                        """,
                        [lender_id]
                    )
                    interest_rate_data = cursor.fetchone()

                if interest_rate_data:
                    interest_rate = interest_rate_data[0]
                    emi_amount = calculate_emi(loan_amount, interest_rate)
                    show_transaction_details = True
                    

                    with connection.cursor() as cursor:
                        cursor.execute(
                            """
                            SELECT COUNT(*) 
                            FROM payment 
                            WHERE customerID = %s
                            """,
                            [customer_id]
                        )
                        emi_count = cursor.fetchone()[0]
                    
                    # Fetch payment history
                    with connection.cursor() as cursor:
                        cursor.execute(
                            """
                            SELECT payment_amount, payment_date, payment_time, payment_type
                            FROM payment
                            WHERE customerID = %s
                            """,
                            [customer_id]
                        )
                        # payment_history = cursor.fetchall()
                        # Fetch the column names
                        columns = [col[0] for col in cursor.description]
                        # Fetch the actual data
                        payment_history = [dict(zip(columns, row)) for row in cursor.fetchall()]

                        
                    #Check if all EMIs are paid
                    if emi_count < 12:
                        with connection.cursor() as cursor:
                            cursor.execute(
                                """
                                INSERT INTO payment (payment_amount,
                                payment_date, payment_time, payment_type, customerID, lenderID)
                                VALUES (%s, CURDATE(), CURTIME(), 'deposit', %s, %s)
                                """,
                                [emi_amount, customer_id, lender_id]
                        )
                    else:
                        return render(request, 'transaction.html', {
                               'show_transaction_details': True,  # You might need to set this to True depending on your logic
                               'emi_amount': emi_amount,
                               'emi_count': emi_count,
                               'pending_emis': pending_emis,
                               'payment_history': payment_history,
                               'error_message': "You have already paid all your EMIs.",
                        })


                    pending_emis = 12 - emi_count

        else:
            return render(request, 'transaction.html', {
                'show_transaction_details': False,
                'emi_amount': emi_amount,
                'emi_count': emi_count,
                'pending_emis': pending_emis,
                'error_message': 'Loan not approved. Please retry!',
            })
    print("Payment History:", payment_history)

    return render(request, 'transaction.html', {
        'show_transaction_details': show_transaction_details,
        'emi_amount': emi_amount,
        'emi_count': emi_count,
        'pending_emis': pending_emis,
        'payment_history': payment_history,
        'error_message': 'Invalid customerID. Please retry !' if not show_transaction_details and request.method == 'POST' else None,
    })




