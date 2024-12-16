# 💼 Loan Management System

Welcome to the Loan Management System 🚀 built using Django, HTML, CSS, JavaScript, and MySQL! This project streamlines loan management, tracking, and repayment processes with an intuitive UI.

## 🌟 Features

### Loan Categories 📊
- Personal Loan
- Micro Loan (Under ₹50K)
- Business Loan
- Home Loan
- Education Loan

### User Loan Details 📝
- View customer information, loan amount, and credit score.
- Lender selection with loan limits, interest rates, and eligibility.

### EMI Management 📅
- Calculate monthly EMI 💰.
- Track pending and paid EMIs.
- View payment history.

### Other Features ✨
- Loan Application Form 📄
- Application Status Tracking 🚦
- Credit Score Integration 📈

## 🛠 Technologies Used

| Technology  | Description               |
|-------------|---------------------------|
| **Django**  | Backend framework 🐍      |
| **HTML/CSS**| Frontend design 🎨        |
| **JavaScript** | Interactive UI 🖱       |
| **MySQL**   | Database Integration 🗄   |
| **mysqlclient** | MySQL Connector 📦     |

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/loan-management-system.git
cd loan-management-system
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
Ensure you have `mysqlclient` installed. If not:
```bash
pip install mysqlclient
```

### 4. Configure Database
Open the project settings file (`settings.py`) and update the MySQL database configuration:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Migrate the Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```
Open the app in your browser: 🌐 [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🎥 Screenshots

- **Home Page**: Loan Categories  
  ![Home Page](Screenshot-2024-12-16-074856.png)  
- **Lender Selection**  
  ![Lender Selection](Screenshot-2024-12-16-160914.png)  
- **EMI Tracking**  
  ![EMI Tracking](Screenshot-2024-12-16-161629.png)  

## 💡 How It Works

1. **Select Loan Type** from the homepage.  
2. **Enter Loan Details**: Loan amount, credit score, and customer information.  
3. **Choose a Lender** based on interest rates and eligibility.  
4. **Track Loan Repayment**:  
   - View EMI details 📆.  
   - Pay EMIs and track pending payments.  
5. **Check Application Status** and monitor your credit score.

## 📂 Project Structure

```
loan-management-system/
├── templates/           # HTML templates
├── static/              # CSS and JavaScript files
├── loan_app/            # Django app
│   ├── models.py        # Database models
│   ├── views.py         # Views for the app
│   ├── urls.py          # App-level routes
│   ├── forms.py         # Loan forms
├── db.sqlite3           # Database (optional)
├── manage.py            # Django management script
└── requirements.txt     # Required dependencies
```

## 👨‍💻 Developer

- **Name**: Your Name  
- **Email**: your-email@example.com  
- **GitHub**: [@your-username](https://github.com/your-username)  

## 🤝 Contributing

1. Fork the repository.  
2. Create a new branch: `git checkout -b feature-branch`.  
3. Commit changes: `git commit -m "Add new feature"`.  
4. Push to the branch: `git push origin feature-branch`.  
5. Submit a pull request.  

## ⭐ Support

If you like the project, don't forget to ⭐ star the repository ⭐!

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

🎉 **Happy Coding!** 🚀
