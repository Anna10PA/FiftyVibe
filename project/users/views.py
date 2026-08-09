from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import User
import uuid

def log_in(req):
    if req.method == 'POST':
        user = req.POST['user']
        password = req.POST['password']

        if '@' in user:
            user_info = User.objects.get(email = user)
            login_user = authenticate(req, username = user_info.username, password = password)
        else: 
            login_user = authenticate(req, username = user, password = password)

        if login_user:
            login(req, login_user)
            return redirect('user_page')
        else:
            return render(req, 'main.html', {'message': 'user not found'})
        
    return render(req, 'main.html')

def sign_up(req):
    if req.method == 'POST':

        first_name = req.POST['name']
        last_name = req.POST['lastname']
        email = req.POST['email']
        username = req.POST['username']
        password = req.POST['password']
        rep_password = req.POST['rep_password']
        gender = req.POST['gender']
        b_day = req.POST['b_day']

        if User.objects.filter(email=email).exists():
            return render(req, 'sign_up.html', {
                'error': 'There is already a user registered with this email address'
            })

        if User.objects.filter(email=email).exists():
            return render(req, 'sign_up.html', {
                'error': 'There is already a user registered with this username'
            })

        if rep_password != password:
            return render(req, 'sign_up.html', {
                'error': 'repeat password and password must be same'
            })

        if username.isdigit() or '@' in username:
            return render(req, 'sign_up.html', {
                'error': 'repeat password and password must be same'
            }) 

        verification_code = str(uuid.uuid4()).split('-')[0]

        req.session['reg_info'] = {
            'first_name': first_name,
            'last_name': last_name,
            'gender': gender,
            'b_day': b_day,
            'username': username,
            'email': email,
            'password': password,
            'code': verification_code
        }

        send_mail(
            subject='FiftyVibe',
            message=f'{verification_code}',
            from_email='puturidzeana0210@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )

        return redirect('verify_code')
    return render(req, 'sign_up.html')

def verify_code(req):
    if req.session['reg_info']:
        reg_info = req.session['reg_info']
        code = reg_info['code']

        if req.method == 'POST':
            user_code = req.POST['code']
            if code == user_code:
                User.objects.create_user(first_name = reg_info['first_name'], last_name = reg_info['last_name'], username = reg_info['username'], password = reg_info['password'], b_day = reg_info['b_day'], gender = reg_info['gender'], email = reg_info['email'])
                return redirect('user_page')
            else:
                return render(req, 'verify_code.html', {'message': 'Code is not correct'})
    return render(req, 'verify_code.html')

def user_page(req):
    if req.user.is_authenticated:
        return render(req, 'user_page.html')
    else:
        return redirect('log_in')

def log_out(req):
    logout(req)
    return redirect('log_in')

def user_profile(req, username):
    return render(req, 'user_profile.html', {'username': username})