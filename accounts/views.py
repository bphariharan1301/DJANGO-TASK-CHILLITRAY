
from random import choice
import string
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from base.settings import EMAIL_HOST_USER
from .var import user_email
# Create your views here.

def login(request):
  print('INSIDE LOGIN FUNCTION')
  if request.method == 'POST':
    print('INSIDE POST IF')
    email = request.POST['email']
    password = request.POST['password']
    print(email, password)

    username = email

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      print(user.get_username())
      return redirect('login')
    else:
      return render(request, 'login.html')

  return render(request, 'login.html')

email = ''
random_otp = ''
username = ''
password = ''
email = ''
first_name = ''
last_name = ''

def register(request):
  print('INSIDE REGISTER FUNCTION')
  if request.method == "POST":

    global first_name
    global last_name
    global password
    global username
    global email
        
    print('INSIDE POST IF')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    global email 
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # user_email = email

    # register.user_email = user_email


    # Check if passwords match
    if password == password2:
      # Check for email 
      if User.objects.filter(email=email).exists():
        messages.error(request, 'That email is already taken')
        print('That email is already taken')
        return redirect('register')
      else:
        # if everything is fine
        current_user = User.objects.create_user(username=email, password=password, email=email, first_name=first_name, last_name=last_name)

        global random_otp
        global user 
        user = current_user

        chars = string.digits
        random = ''.join(choice(chars) for i in range(4))
        random_otp = int(random)
        # user_otp = random_otp
        print(random_otp)
    
        print('EMAIL GIVEN BY USER IS: ', email)
        

        send_mail(
            'RANDOM OTP',
            'The OTP is: '+random,
            EMAIL_HOST_USER,
            [email, ],
            # ['t@gmail.com'],
            fail_silently=False,
        )

        # save the user
        
        return redirect('verify')
    else:
      messages.error(request, 'Passwords do not match')
      print('Passwords do not match')
      return redirect('register')

  return render(request, 'register.html')
  
# def verify(request):
#   User = get_user_model()
#   try:
#       uid = force_text(urlsafe_base64_decode(uidb64))
#       user = User.objects.get(pk=uid)
#   except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#     user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')


def verify(request):
  if request.method == 'POST':
    otp = request.POST['otp']
    if otp!=0:
      print(otp)
    else:
      print('OTP not recieved from form')

    if random_otp == otp:
      print(otp)
      user = User.objects.create_user(username=email, password=password, email=email, first_name=first_name, last_name=last_name)
      user.save()
      messages.success(request, 'You are now registered and can log in')
      print('You are now registered and can verify to log in')
      return redirect('login')
    else:
      messages.error(request, 'Invalid OTP')
      return redirect('verify')
  
  print(random_otp)
  return render(request, 'verify.html')
  


def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'Successfully Logged out')
    return redirect('login')
