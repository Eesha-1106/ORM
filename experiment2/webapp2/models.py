from django.db import models
from django.contrib import admin
class loan (models.Model):
    Loan_Id=models.CharField(max_length=20,primary_key=True)
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Salary=models.IntegerField()
    Loan_applied_date=models.DateField()
    Loan_amount=models.IntegerField()
    Email=models.EmailField()
    Phone_no=models.IntegerField()


class loanAdmin(admin.ModelAdmin):
    list_display=('Loan_Id','Name','Age','Salary','Loan_applied_date','Loan_amount','Email','Phone_no')
    



# Create your models here.
