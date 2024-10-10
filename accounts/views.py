# Create your views here.

# from django.shortcuts import render, redirect
# from django.contrib.auth import login, logout, authenticate
# from .forms import UserRegisterForm

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.set_password(user.password)
#             user.save()
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'accounts/register.html', {'form': form})

# def login_view(request):
#     return render(request, 'accounts/login.html')

# My working codes
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.decorators import login_required
# from requests import request
# from .forms import SignUpForm, ProfileForm

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)
#             return redirect('profile')
#     else:
#         form = SignUpForm()
#     return render(request, 'accounts/signup.html', {'form': form})

# My working codes
# def signup_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
            # Handle successful signup logic (e.g., save user data)
    #         return redirect('login')  # Redirect to login page after signup
    # else:
    #     form = SignUpForm()

    # context = {'form': form}
    # return render(request, 'signup.html', context)  # Render signup template

# Not to be added with working codes

# @login_required
# def profile(request):
#     user_profile = request.user.userprofile
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')  # Redirect to the dashboard after saving profile
#     else:
#         form = ProfileForm(instance=user_profile)
#     return render(request, 'accounts/profile.html', {'form': form})

# My working codes
# def profile_view(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         if form.is_valid():
            # Handle successful signup logic (e.g., save user data)
    #         return redirect('dashboard')  # Redirect to login page after signup
    # else:
    #     form = ProfileForm()

    # context = {'form': form}
    # return render(request, 'profile.html', context)  # Render signup template
    
    
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


#################### index####################################### 
def index(request):
	return render(request, 'accounts/index.html', {'title':'index'})

########### register here ##################################### 
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			######################### mail system #################################### 
			htmly = get_template('accounts/Email.html')
			d = { 'username': username }
			subject, from_email, to = 'welcome', 'your_email@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			################################################################## 
			messages.success(request, f'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'accounts/register.html', {'form': form, 'title':'register here'})

################ login forms################################################### 
def Login(request):
	if request.method == 'POST':

		# AuthenticationForm_can_also_be_used__

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('index')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form':form, 'title':'log in'})
