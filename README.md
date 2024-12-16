![Screenshot 2024-12-16 161003](https://github.com/user-attachments/assets/8530366d-539a-4771-84d4-e759dd178f73)![Screenshot 2024-12-16 161629](https://github.com/user-attachments/assets/e703614f-16bc-4a1f-b659-d41b7cf04530)# 💼 Loan Management System

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
  ![Screenshot 2024-12-16 074856](https://github.com/user-attachments/assets/425f333f-6638-4c20-8f99-90eedaa2cc30)

- **Lender Selection**  
 ![Screenshot 2024-12-16 160914](https://github.com/user-attachments/assets/2649b567-09e5-4fe6-921f-338613f3d176)

- **EMI Tracking**  
  ![Screenshot 2024-12-16 161629](https://github.com/user-attachments/assets/299b2a10-a335-4819-a2c9-9bf096bcb4dc)

- **Check Credit Score**
  ![Screenshot 2024-12-16 161548](https://github.com/user-attachments/assets/108f72aa-a7ea-449d-9d9e-13034fec5413)

- **Track Appliction Status**
  ![Screenshot 2024-12-16 161526](https://github.com/user-attachments/assets/6e60cec0-6193-4666-bd3b-8be5d091bb02)

- **Enter CustomerID**
  ![Screenshot 2024-12-16 161003](https://github.com/user-attachments/assets/884a0d24-4ecf-4c55-a58c-edd84f4d3fe1)

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
