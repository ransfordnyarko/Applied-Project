from django.shortcuts import render
from django.http import HttpResponse
from .models import *

firstName = ''
lastName = ''
businessName = ""
phoneNumber = 0
email = ""
tinNumber = ""
eArea = ""
Address = ""
rgdc = ""
classOfBusiness = ""
typeOfBusiness = ""
expectedFee = 0
Paid = ""
AmountPaid = 0
agent = ""

chk = 0

def home(request):
	return render(request, 'home.html')

def business(request):
	return render(request, 'business.html')

def form(request):
	if request.method == "POST":
		print(firstName)
		print("Hello")
		expectedFee = request.POST['ex-fee']
		Paid = request.POST['paid']
		AmountPaid = request.POST['amt-paid']
		agent = request.POST['agent']

		bus_info = Business(firstName=firstName, lastName=lastName, businessName=businessName, phoneNumber=phoneNumber, email=email, tinNumber=tinNumber, eArea=eArea, Address=Address, rgdc=rgdc, 
			classOfBusiness=classOfBusiness,typeOfBusiness=typeOfBusiness,expectedFee=expectedFee,Paid=Paid, AmountPaid=AmountPaid, agent=agent)
		bus_info.save()

		chk = 0

	return render(request, 'form.html')

def form2(request):
	firstName = request.POST['first-name']
	lastName = request.POST['last-name']
	businessName = request.POST['business-name']
	phoneNumber = request.POST['phone_num']
	email = request.POST['email']
	tinNumber = request.POST['tin-num']
	return render(request, 'form2.html')

def form3(request):
	eArea = request.POST['electoral-area'] 
	Address = request.POST['address']
	rgdc = request.POST['rgdc']
	classOfBusiness = request.POST['cob']
	typeOfBusiness = request.POST['tob']
	chk = 1
	return render(request, 'form3.html')

def locate(request):
	return render(request, 'locate.html')

def login(request):
	return render(request, 'login.html')

def statistics(request):
	return render(request, 'stats.html')