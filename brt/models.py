from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator



class Business(models.Model):
	firstName = models.CharField(max_length = 25)
	lastName = models.CharField(max_length = 25)
	businessName = models.CharField(max_length = 50)
	phoneNumber = models.IntegerField(validators=[MinLengthValidator(10, MaxLengthValidator(10))])
	email = models.TextField()
	tinNumber = models.IntegerField(validators=[MinLengthValidator(10)])
	eArea = models.TextField()
	Address = models.TextField()
	rgdc = models.TextField()
	classOfBusiness = models.CharField(max_length = 25)
	typeOfBusiness = models.CharField(max_length = 25)
	expectedFee = models.IntegerField()
	Paid = models.CharField(max_length = 10)
	AmountPaid = models.IntegerField()
	agent = models.CharField(max_length = 25)

	def __str__(self):
		return self.businessName



