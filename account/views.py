from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def login(request):
    if request.user.is_authenticated:
        return redirect('/findfriend')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('user: ', user.first_name)
            return redirect('/findfriend')
        else:
            messages.info(request, 'ชื่อผู้ใช้หรือรหัสผ่านผิดพลาด')
            return redirect('login')

    else:
        return render(request, 'base/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

# def priv_error(request):
#     message = 'คุณไม่มีสิทธิ์เข้าถึงหน้าดังกล่าว'
#     return render(request, 'base/priv_error.html', {'message': message})
