# Ex02 Django ORM Web Application
# Date:29-11-24
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
```
admin.py

from django.contrib import admin
from .models import loan,loanAdmin
admin.site.register(loan,loanAdmin)

models.py

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

```
# OUTPUT

![alt text](../Capture.PNG)


# RESULT
Thus the program for creating a database using ORM hass been executed successfully
