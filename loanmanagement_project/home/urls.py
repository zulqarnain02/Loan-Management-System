from django.urls import path
from . import views 
# from .views import home,openLoanForm 


# url configuration
urlpatterns = [
    path('', views.home),
    path('form/', views.loanform, name='loanform'),
    path('transaction/', views.transaction,name='transaction'),
    path('creditscore/', views.creditscore, name='creditscore'),
    path('contact/', views.contact),
    path('select/', views.select, name='select'),
    path('update_user_with_lender/', views.update_user_with_lender, name='update_user_with_lender'),
    path('loan_status/', views.loan_status, name='loan_status'),
]
