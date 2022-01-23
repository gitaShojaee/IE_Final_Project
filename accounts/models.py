from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # important fields that are stored in User model:
    #  first_name, last_name, email, date_joined

    mobile = models.CharField(max_length=11, blank=True)

    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)

    birth_date = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='users/profile_images/', null=True, blank=True)

    # fields related to tickets
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.user.get_full_name()

    def get_balance_display(self):
        return self.balance

    # behaviors
    def deposit(self, amount):
        self.balance += amount
        self.save()

    def spend(self, amount):
        if self.balance < amount:
            return False
        self.balance -= amount
        self.save()
        return True


class Payment(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    transaction_time = models.DateTimeField(auto_now_add=True)
    transaction_code = models.CharField(max_length=30)



