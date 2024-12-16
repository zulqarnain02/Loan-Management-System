from django.db import models
import random

# makemighration - reate changes and store in a File
# migrate - apply the pending changes created by makemighration
# Create your models here.
class Form(models.Model):
    loanAmount = models.DecimalField(max_digits=10, decimal_places=2)
    employeeType = models.CharField(max_length=100)
    netincome = models.DecimalField(max_digits=10, decimal_places=2)
    full_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    email = models.EmailField()
    pan_no = models.CharField(max_length=10)
    DOB = models.DateField()
    pin = models.CharField(max_length=6)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    past_loan = models.BooleanField(default=False)
    credit_card = models.BooleanField(default=False)
    purpose_of_loan = models.CharField(max_length=100)
    credit_score = models.IntegerField(blank=True, null=True)

    @classmethod
    def create(cls, loanAmount, employeeType, netincome, full_name, phone_no, email, pan_no, dob, pin, gender, address, past_loan, credit_card, purpose_of_loan):
        form = cls(
            loanAmount=loanAmount,
            employeeType=employeeType,
            netincome=netincome,
            full_name=full_name,
            phone_no=phone_no,
            email=email,
            pan_no=pan_no,
            dob=dob,
            pin=pin,
            gender=gender,
            address=address,
            past_loan=past_loan,
            credit_card=credit_card,
            purpose_of_loan=purpose_of_loan,
            credit_score=random.randint(600, 950)
        )
        form.save()
        return form


class Lender(models.Model):
    lenderID = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=10)
    lender_phone_no = models.IntegerField()
    max_amount = models.IntegerField()
    interest_rate = models.IntegerField()
    min_creditscore = models.IntegerField()