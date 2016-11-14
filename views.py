from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import PictureForm,UserRegForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from instagram.models import Picture,Friend
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.auth.models import User 

# Create your views here.
def home(request):
	return render(request, "instagram/home.html")

def upload(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/instagram/login")

	form = PictureForm(request.POST or None , request.FILES or None , initial={"user":request.user})
		# if Request.method == "POST":
		# 	print Request.POST.get("Content")
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully created")

		return HttpResponseRedirect("/instagram/profile")

	else:
		messages.error(request,"Not Successfully created")
		context = {
		"form" : form,
		"user" : request.user
			}
		return render(request, "instagram/upload.html",context)

def profile(request):
	# username = Picture.objects.get(user.user='jamespatel37')
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/instagram/login")

	print request.user
	images = Picture.objects.filter(user = request.user)
	context = {
		"user" : request.user,
		"images":images
	}
	return render(request, "instagram/profile.html", context)


def register(request):
	if request.method == "POST":
		form = UserRegForm(request.POST or None)
			# if Request.method == "POST":
			# 	print Request.POST.get("Content")
		if form.is_valid():
			instance = form.save(commit=False)

			username1 = form.cleaned_data['username']
			password1 = form.cleaned_data['password']
			email = form.cleaned_data['email']
			instance.set_password(password1)
			instance.save()


			instance = authenticate(username=username1 , password=password1)

			# login
			if instance is not None:
				if instance.is_active:
					login(request,instance)
								# # send an email
					subject =  """Welcome to Instagram
								""" 
								

					fromaddress = 'inst.insta123@gmail.com'
					toaddress = email
					username = 'inst.insta123@gmail.com'
					password =''
					msg = MIMEMultipart()
					msg['From'] =fromaddress
					msg['To'] = toaddress
					msg['Subject'] = subject
					msg.attach(MIMEText("""Welcome to Instagram.
								Login info:
								Username:%s
								Password:%s
								Email:%s
								""" % (username1,password1,email)))

					try:
						server = smtplib.SMTP('smtp.gmail.com')
						server.ehlo()
						server.starttls()
						server.ehlo()
						server.login(username,password)
						server.sendmail(fromaddress,toaddress,msg.as_string())
						server.quit()
						print "Successfully sent email"
					except:
						print "Error: unable to send email"
					return HttpResponseRedirect("/instagram/profile")

			messages.success(request,"Successfully created")

			return HttpResponseRedirect("/instagram/profile")

	else:
		form = UserRegForm()
		messages.error(request,"Not Successfully created")
		context = {
		"form" : form,
		"user" : request.user
			}
		return render(request, "instagram/register.html",context)

def loginpage(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/instagram/profile")

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect("/instagram/profile")

		messages.success(request,"Successfully created")

		return HttpResponseRedirect("/instagram/login")

	else:
		form = LoginForm()
		messages.error(request,"Not Successfully created")
		context = {
		"form" : form,
		"user" : request.user
			}
		return render(request, "instagram/login.html",context)

def logoutpage(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/instagram/login")
	logout(request)
	return HttpResponseRedirect("/instagram/login")

def friends(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/instagram/login")
	
	friends_list = Friend.objects.filter(user=request.user)
	friends_list1 = Friend.objects.filter(friend=request.user)

	context={
			"friends":friends_list,
			"friends1":friends_list1
	}

	return render(request, "instagram/friends.html",context)

def profileRequest(request,username,friend1):
	# username = Picture.objects.get(user.user='jamespatel37')
	username = User.objects.get(username = username)
	if request.user == username:
		friend1 = User.objects.get(username = friend1)
		images = Picture.objects.filter(user = friend1)
		context = {
			"user" : friend1,
			"images":images
		}
		return render(request, "instagram/profile.html", context)
	
	return render(request, "instagram/profile.html", {"user" : "Access Denied!!!!!!"})

def search(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/instagram/login")
	query = request.GET.get('q')

	# queryset = User.objects.all()
	if query:
		queryset = Friend.objects.filter(user.username__icontains = query)
		context={
			"user":request.user,
			"results":queryset
		}

		return render(request, "instagram/search.html",context)
	# friends_list = Friend.objects.filter(user=request.user)
	# friends_list1 = Friend.objects.filter(friend=request.user)

	context={
			"user":request.user
		}

	return render(request, "instagram/search.html",context)