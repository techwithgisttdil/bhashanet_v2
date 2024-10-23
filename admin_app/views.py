from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from .forms import *
from django.conf import settings
from django.urls import reverse
from core_app.custom_captcha import captcha_img_generator, random_captcha_generator
import environ
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout
from json2html import *
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from core_app.token import account_activation_token
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import json
env = environ.Env()
environ.Env.read_env()
from .utility import generate_otp_for_user_registration,validate_otp_for_user_registration
from .tasks import User_Registration_With_OTP


from logging import exception
import pandas as pd
from bhashanet_v2.celery import *
from .forms import *
from .tasks import *
from django.contrib import messages
from .models import *
from urllib.parse import urlparse
from bhashanet_v2.logger import *
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
import idna
from celery.result import AsyncResult
from django.db.models import Count
from .utility import *
from collections import Counter
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


def login_view(request,flag=None):
    if flag == "for_user_login":
        base_template = 'core_app/base.html' 
    else:
        base_template = 'admin_app/base.html' 
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        form = LoginForm(request.POST.copy())
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                if User.objects.filter(username=username, is_active=False):
                    messages.info(request, "User is not Active, Please Activate or Register again", extra_tags="danger")
                else:
                    user = authenticate(username=username, password=password)
                    user_obj=User.objects.get(username=username)
                    user_role_obj = UserRoleMapping.objects.get(User_Id=user)
                    if user_role_obj.Role_Id.Role_Name != 'DjangoSuperAdmin' :   
                        try:
                            otp_obj = OTP_For_UserRegistration.objects.get(OTP_Email=user_obj)
                            if otp_obj.OTP_Status==False:
                                messages.error(request, 'Account Not Yet Verified with OTP', extra_tags="danger")
                                form = LoginForm()
                                captcha_value = random_captcha_generator()
                                captcha_img_generator(captcha_value)
                                form.fields['captcha_hidden'].initial = make_password(captcha_value)
                                return render(request, 'admin_app/AccountManagement/user_login.html', {"form": form,"base_template":base_template})
                        except:
                            messages.error(request, 'Account Not Yet Verified with OTP', extra_tags="danger") 
                    if user is not None :
                        login(request, user)
                        try:
                            user_role_obj = UserRoleMapping.objects.get(User_Id=user)     
                            if user_role_obj.Role_Id.Role_Name == 'nixi_admin':
                                print("Nixi admin")
                                return redirect('admin_app:dashboard2')
                            elif user_role_obj.Role_Id.Role_Name == 'ficci_admin':
                                print("Ficci admin")
                                return redirect('admin_app:dashboard2')
                            elif user_role_obj.Role_Id.Role_Name == 'main_admin':
                                print("main admin")
                                return redirect('admin_app:dashboard2')
                            elif user_role_obj.Role_Id.Role_Name == 'DjangoSuperAdmin':
                                return redirect('admin_app:dashboard2')
                            elif user_role_obj.Role_Id.Role_Name == 'Bhashanet_User':
                                return redirect('home')
                            else:
                                return redirect('home')
                        except:
                            return redirect('home')
                    else:
                        messages.error(request, 'Incorrect login credentials', extra_tags="danger")
            except:
                messages.error(request, "Something Went Wrong", extra_tags="danger")  
        else:
            messages.error(request, "Something Went Wrong", extra_tags="danger") 
        captcha_value = random_captcha_generator()
        captcha_img_generator(captcha_value)
        form.data['captcha_input'] = ''
        form.data['captcha_hidden'] = make_password(captcha_value)
    else:
        form = LoginForm()
        captcha_value = random_captcha_generator()
        captcha_img_generator(captcha_value)
        print("captcha value ", captcha_value)
        form.fields['captcha_hidden'].initial = make_password(captcha_value)
    return render(request, 'admin_app/AccountManagement/user_login.html', {"form": form,"base_template":base_template})


def register_view(request,flag=None):
    if flag == "for_user_register":
        base_template = 'core_app/base.html' 
    else:
        base_template = 'admin_app/base.html' 
    if request.user.is_superuser:
        if request.method == 'POST':
            form = RegistrationForm(request.POST.copy())
            email = request.POST.get("email")
            if form.is_valid():
                email = request.POST.get("email")
                password = request.POST.get("password1")
                password_confirm  = request.POST.get("password2")
                role  = request.POST.get("role")
                if not User.objects.filter(username=email).exists():
                    user = User.objects.create(email=email, username=email)       
                    user.set_password(password)     
                    user.is_active = True
                    user.save()

                    role_id=UserRole.objects.get(id=role)
                    UserRoleMapping.objects.create(User_Id=user,Role_Id=role_id)
                    
                    resp_data=generate_otp_for_user_registration(email,OTP_For_UserRegistration)
                    if resp_data['status'] == 'success' and resp_data['Email_status']=="success":
                        User_Registration_With_OTP.apply_async((email,), countdown=300)
                        messages.success(request, "OTP is sent to " + email, extra_tags="success")
                        return redirect("verify_user_otp",email=email)
                    elif resp_data['Email_status'] == 'error':
                        messages.success(request, resp_data['message'], extra_tags="danger")
                    elif resp_data['status'] == 'error':
                        messages.success(request, resp_data['message'], extra_tags="danger")
                else:
                    user = User.objects.get(username=email)
                    try:
                        user_obj=User.objects.get(username=email)
                        otp_user_obj=OTP_For_UserRegistration.objects.filter(OTP_Email=user_obj)
                    except:
                        otp_user_obj=''
                    if otp_user_obj:
                        if otp_user_obj.OTP_Status:
                            messages.error(request, 'Email address already exists', extra_tags="danger")
                            captcha_value = random_captcha_generator()
                            captcha_img_generator(captcha_value)
                            form.fields['captcha_hidden'].initial = make_password(captcha_value)
                            return render(request, "admin_app/AccountManagement/user_register.html", {'form': form,'base_template':base_template})  
                
                    resp_data=generate_otp_for_user_registration(email,OTP_For_UserRegistration)
                    if resp_data['status'] == 'success' and resp_data['Email_status']=="success":
                        User_Registration_With_OTP.apply_async((email,), countdown=300)
                        messages.success(request, "OTP is sent to" + email, extra_tags="success")
                        return redirect("verify_user_otp",email=email)
                    
                    elif resp_data['Email_status'] == 'error':
                        messages.success(request, resp_data['message'], extra_tags="danger")

                    elif resp_data['status'] == 'error':
                        messages.success(request, resp_data['message'], extra_tags="danger")
            else:
                messages.error(request, "Unsuccessful Registration. Invalid Information.", extra_tags='danger')
            captcha_value = random_captcha_generator()
            captcha_img_generator(captcha_value)
            form.data['captcha_input'] = ''
            form.data['captcha_hidden'] = make_password(captcha_value)
            return render(request, template_name="admin_app/AccountManagement/user_register.html", context={"form": form,'base_template':base_template})
        else:
            form = RegistrationForm()
            captcha_value = random_captcha_generator()
            form.data['captcha_input'] = ''
            form.data['captcha_hidden'] = make_password(captcha_value)
            captcha_img_generator(captcha_value)
            form.fields['captcha_hidden'].initial = make_password(captcha_value)
            return render(request, "admin_app/AccountManagement/user_register.html", {'form': form,'base_template':base_template})
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST.copy())
            email = request.POST.get("email")

            if form.is_valid():
                email = request.POST.get("email")
                password = request.POST.get("password1")
                password_confirm  = request.POST.get("password2")

                if not User.objects.filter(username=email).exists():
                    user = User.objects.create(email=email, username=email)       
                    user.set_password(password)     
                    user.is_active = True
                    user.save()

                    role_id=UserRole.objects.get(Role_Name='Bhashanet_User')
                    UserRoleMapping.objects.create(User_Id=user,Role_Id=role_id)
                    
                    resp_data=generate_otp_for_user_registration(email,OTP_For_UserRegistration)
                    if resp_data['status'] == 'success' and resp_data['Email_status']=="success":
                        User_Registration_With_OTP.apply_async((email,), countdown=300)
                        # User_Registration_With_OTP(email)
                        messages.success(request, "OTP is sent to " + email, extra_tags="success")
                        return redirect("verify_user_otp",email=email,flag='for_user_otp')
                    
                    elif resp_data['Email_status'] == 'error':
                        messages.success(request, resp_data['message'], extra_tags="danger")

                    elif resp_data['status'] == 'error':
                        messages.success(request, resp_data['message'], extra_tags="danger")
                    
                else:
                    user = User.objects.get(username=email)
                    try:
                        user_obj=User.objects.get(username=email)
                        otp_user_obj=OTP_For_UserRegistration.objects.filter(OTP_Email=user_obj)
                    except:
                        otp_user_obj=''
                    if otp_user_obj:
                        if otp_user_obj.OTP_Status:
                            messages.error(request, 'Email address already exists', extra_tags="danger")
                            captcha_value = random_captcha_generator()
                            captcha_img_generator(captcha_value)
                            form.fields['captcha_hidden'].initial = make_password(captcha_value)
                            return render(request, "admin_app/AccountManagement/user_register.html", {'form': form,'base_template':base_template})  
                
                    resp_data=generate_otp_for_user_registration(email,OTP_For_UserRegistration)
                    if resp_data['status'] == 'success' and resp_data['Email_status']=="success":
                        User_Registration_With_OTP.apply_async((email,), countdown=300)
                        messages.success(request, "OTP is sent to" + email, extra_tags="success")
                        return redirect("verify_user_otp",email=email,flag='for_user_otp')
                    
                    elif resp_data['Email_status'] == 'error':
                        messages.success(request, resp_data['message'], extra_tags="danger")

                    elif resp_data['status'] == 'error':
                        messages.success(request, resp_data['message'], extra_tags="danger")

            else:
                messages.error(request, "Unsuccessful Registration. Invalid Information.", extra_tags='danger')
            captcha_value = random_captcha_generator()
            captcha_img_generator(captcha_value)
            form.data['captcha_input'] = ''
            form.data['captcha_hidden'] = make_password(captcha_value)
            return render(request, template_name="admin_app/AccountManagement/user_register.html", context={"form": form,'base_template':base_template})
        else:
            form = RegistrationForm()
            captcha_value = random_captcha_generator()
            form.data['captcha_input'] = ''
            form.data['captcha_hidden'] = make_password(captcha_value)
            captcha_img_generator(captcha_value)
            print("captcha value ", captcha_value)
            form.fields['captcha_hidden'].initial = make_password(captcha_value)
            return render(request, "admin_app/AccountManagement/user_register.html", {'form': form,'base_template':base_template})


def verify_user_otp(request,email,flag=None):
    if flag == "for_user_otp":
        base_template = 'core_app/base.html' 
    else:
        base_template = 'admin_app/base.html' 
    otp_form=OTPForRegistrationForm()
    if request.method == 'POST' and 'submit' in request.POST:
        form = OTPForRegistrationForm(request.POST.copy())
        if form.is_valid():
            otp_value = request.POST.get("otp")
            status=validate_otp_for_user_registration(email, otp_value, OTP_For_UserRegistration)
            if status:
                user_obj=User.objects.get(username=email)
                otp_user_obj=OTP_For_UserRegistration.objects.filter(OTP_Email=user_obj)
                otp_user_obj.OTP_Status=True
                messages.success(request, "OTP Verified, Now user can login ", extra_tags="success")
                if flag == "for_user_otp":
                    return redirect("login_view",flag="for_user_login")
                else:
                    return redirect("login_view")
            else:
                messages.error(request, "Failed OTP Verification", extra_tags='danger')
                return render(request, "admin_app/AccountManagement/otp_form.html", {'form': otp_form,'base_template':base_template})
    if request.method == 'POST' and 'resent' in request.POST:
        otp_form=OTPForRegistrationForm()
        try: 
            user = User.objects.get(username=email)
            resp_data=generate_otp_for_user_registration(email,OTP_For_UserRegistration)
            if resp_data['status'] == 'success':
                messages.success(request, "OTP has been resent to " + email, extra_tags="success")
                return redirect("verify_user_otp",email=email,flag=flag)
            
            # elif resp_data['Email_status'] == 'error':
            #     messages.success(request, resp_data['message'], extra_tags="danger")

            elif resp_data['status'] == 'error':
                messages.success(request, resp_data['message'], extra_tags="danger")
            return render(request, "admin_app/AccountManagement/otp_form.html", {'form': otp_form,'base_template':base_template})
        except:
            messages.success(request, 'OTP generate limit exceeded, Register Again!', extra_tags="danger")
            return redirect('register_view')
    return render(request, "admin_app/AccountManagement/otp_form.html", {'form': otp_form,'base_template':base_template})


@login_required()
def logout_view(request,flag=None):
    logout(request)
    messages.success(request, "You are successfully logged Out", extra_tags="success")
    return redirect("login_view",flag=flag)

@login_required()
def change_password_view(request,flag=None):
    if flag == "for_user_change_pass":
        base_template = 'core_app/base.html' 
    else:
        base_template = 'admin_app/base.html'
    form = ChangePasswordUserForm()
    try:
        user = User.objects.get(username=request.user)
        if request.method == 'POST':
            form = ChangePasswordUserForm(request.POST)
            if form.is_valid():
                old_password = form.cleaned_data['old_password']
                new_password = form.cleaned_data['new_password']
                if user.check_password(old_password):
                    user.set_password(new_password)
                    user.save()
                    messages.success(request, 'Password changed successfully', extra_tags='success')
                    logout(request)
                    if flag == "for_user_change_pass":
                        return redirect('login_view',flag='for_user_login')
                    else:
                        return redirect('login_view')
                else:
                    messages.error(request, "Incorrect Old Password", extra_tags='danger')                
            else:
                messages.error(request, "Invalid Details", extra_tags='danger') 
    except:
        messages.error(request, "User Not Found", extra_tags='danger')

    return render(request, 'admin_app/AccountManagement/change_password.html', {'form':form,'base_template':base_template})


def forgot_password_view(request,flag=None):
    if flag == "for_user_forgot_password":
        base_template = 'core_app/base.html' 
    else:
        base_template = 'admin_app/base.html'
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST.copy())
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email)
            if user:
                domain = request.get_host()
                uid = urlsafe_base64_encode(force_bytes(user[0].pk))
                token = account_activation_token.make_token(user[0])
                link = reverse('password_creation', kwargs={"uid": uid, "token": token,"flag":flag})
                activate_link = "http://" + domain + link  
                try:
                    forgot_password_data = CustomForgotPassword.objects.filter(email=user[0])
                    if forgot_password_data:
                        prev_counter = forgot_password_data[0].counter
                        generated_date = forgot_password_data[0].generation_time.date()
                        current_date = datetime.now().date()
                        if generated_date == current_date:
                            if prev_counter < 10:
                                forgot_password_data[0].counter = prev_counter + 1
                            else:
                                captcha_value = random_captcha_generator()
                                captcha_img_generator(captcha_value)
                                form.data['captcha_input'] = ''
                                form.data['captcha_hidden'] = make_password(captcha_value)
                                messages.error(request, "Forgot password request daily limit exceeded, please try after some time.(max limit 10)", extra_tags="danger")
                                return render(request, 'admin_app/AccountManagement/forgot_password.html', {'form': form,'base_template':base_template})
                        else:
                            forgot_password_data[0].counter = 1
                        forgot_password_data[0].forgot_password_token = token
                        forgot_password_data[0].generation_time = datetime.now(timezone.utc)
                        forgot_password_data[0].save()
                    else:
                        data = CustomForgotPassword(email=user[0], forgot_password_token=token, generation_time=datetime.now(timezone.utc), counter=1)
                        data.save()
                except:
                    captcha_value = random_captcha_generator()
                    captcha_img_generator(captcha_value)
                    form.data['captcha_input'] = ''
                    form.data['captcha_hidden'] = make_password(captcha_value)
                    messages.error(request, "Something Went Wrong", extra_tags="danger")
                    return render(request, 'admin_app/AccountManagement/forgot_password.html', {'form': form,'base_template':base_template}) 
                try:
                    send_mail(
                    subject="Forgot Password",
                    message="",
                    from_email=env('SERVER_EMAIL'),
                    recipient_list=[email],
                    fail_silently=False,
                    html_message="<h4>Click <a href={0}>here</a> to reset your password. Link is valid for 2 hours.</h4>".format(activate_link)
                    )
                    messages.error(request, "Email sent to {}".format(email), extra_tags="success")
                except:
                    messages.error(request, "Email not send", extra_tags="danger") 
            else:
                messages.error(request, "User does not exists", extra_tags="danger")  
        else:
            messages.error(request, "Something Went Wrong")  
        captcha_value = random_captcha_generator()
        captcha_img_generator(captcha_value)
        form.data['captcha_input'] = ''
        form.data['captcha_hidden'] = make_password(captcha_value)
        return render(request, 'admin_app/AccountManagement/forgot_password.html', {'form': form,'base_template':base_template}) 
    else:
        form = ForgotPasswordForm()

    captcha_value = random_captcha_generator()
    captcha_img_generator(captcha_value)
    form.fields['captcha_hidden'].initial = make_password(captcha_value)
    return render(request, 'admin_app/AccountManagement/forgot_password.html', {'form': form,'base_template':base_template}) 


def password_creation_view(request, uid, token,flag=None):
    if flag == "for_user_forgot_password":
        base_template = 'core_app/base.html' 
    else:
        base_template = 'admin_app/base.html'
    if request.user.is_authenticated:
        return redirect("admin_app:dashboard2")
    form = PasswordCreationForm()
    id = urlsafe_base64_decode(uid).decode()
    user = User.objects.filter(id=id)
    if user:
        token_data = CustomForgotPassword.objects.filter(forgot_password_token=token)
        if token_data:
            token_generation_time = token_data[0].generation_time
            current_time = datetime.now(timezone.utc)
            time_threshold = current_time - timedelta(hours=2)  # change current time is 2 hour before
            if token_generation_time < time_threshold:
                return render(request, 'admin_app/AccountManagement/forgot_password_token_page.html', {'message': "Activation link Expired!", "link": "forgot_password",'base_template':base_template})
            else:
                if request.method == 'POST':
                    form = PasswordCreationForm(request.POST)
                    if form.is_valid():
                        password = form.cleaned_data['password']
                        confirm_password = form.cleaned_data['confirm_password']
                        if password != confirm_password:
                            messages.error(request, "Confirm Password must be same as New Password", extra_tags="danger")
                            return render(request, "admin_app/AccountManagement/password_creation.html", {'form': form,'base_template':base_template})

                        user[0].password = make_password(password)
                        user[0].save()
                        token_data[0].forgot_password_token = "none"
                        token_data[0].save()
                        logout(request)
                        return render(request, 'admin_app/AccountManagement/password_change_success_page.html', {'message': "Password Reset Successful",'base_template':base_template})
                    else:
                        return render(request, "admin_app/AccountManagement/password_creation.html", {'form': form,'base_template':base_template})
                return render(request, "admin_app/AccountManagement/password_creation.html", {'form': form,'base_template':base_template})
        else:
            return render(request, 'admin_app/AccountManagement/forgot_password_token_page.html', {'message': "Activation link Expired!", "link": 'forgot_password','base_template':base_template})
    else:
        return render(request, 'admin_app/AccountManagement/forgot_password_token_page.html', {'message': "User not exists", "link": 'login','base_template':base_template})


@login_required()
def user_profile_view(request,flag=None):
    if flag == "for_user_profile":
        base_template = 'core_app/base.html' 
    else:
        base_template = 'admin_app/base.html'
    
    user_profile_obj = UserProfile.objects.filter(UserProfile_user=request.user)
    if user_profile_obj:
        form = UserProfileForm(instance=user_profile_obj[0])
    else:
        form = UserProfileForm()
    if request.method == 'POST':
        if user_profile_obj:
            form = UserProfileForm(request.POST, request.FILES, instance=user_profile_obj[0])
        else:
            form = UserProfileForm(request.POST, request.FILES)
        
        if form.is_valid():
            user_obj = request.user
            form.instance.UserProfile_user = user_obj
            form.save()
            messages.success(request, "Profile Updated Successfully", extra_tags="success")
            if flag != "for_user_profile":
                return redirect('admin_app:dashboard2')
            else:
                return redirect('home')
        else:
            messages.error(request, "Invalid Details", extra_tags="danger")
    return render(request, 'admin_app/AccountManagement/user_profile.html', {'form' : form,'base_template':base_template}) 


# Create your views here.
@login_required
def home(request):
    return redirect('login_view')

# -----ADDED BY SANJAYB -------

@login_required
def idn_domain_forms(request):
    #log(request,"Calling idn_domain_forms view")
    English_Domain_Form_obj = English_Domain_Form()
    idn_dashboard_form_obj = idn_dashboard_form()
    
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'IDNDOMAINFORM':
            idn_dashboard_form_obj = idn_dashboard_form(request.POST)
            try:
             # Check if form is valid or not and any params is not null
                if idn_dashboard_form_obj.is_valid():
                    # Extract User Input Domain
                    user_input_domain = idn_dashboard_form_obj.cleaned_data['IDN_domain']
                    #log(request,f"User input Domain is {user_input_domain}")
                    user_input_domain_obj = URL_dashboard.objects.filter(IDN_domain=user_input_domain).exists()

                    if not user_input_domain_obj:
                        
                        form_obj = idn_dashboard_form_obj.save(commit=False)
                        try:
                            unicode_domain = idna.decode(user_input_domain.split('/')[2])
                        except:
                            unicode_domain = user_input_domain.split('/')[2]
                        
                        unicode_domain=user_input_domain.split('/')[0] + '//' + unicode_domain 
                        
                        # Perform any additional processing or modification of the instance here
                        form_obj.IDN_domain=unicode_domain
                        form_obj.content_language = ''
                        form_obj.ssl_configuration_status=''
                        form_obj.idn_domain_running_status=''
                        initial_remark = {
                            "General": "",
                            "Domain": "",
                            "SSL": "",
                            "Content": ""
                        }
                        # Serialize the dictionary to a JSON string
                        current_remark = json.dumps(initial_remark)    
                        # Assign the updated string back to the Remark field
                        form_obj.Remark = current_remark
                        form_obj.save()
                        messages.info(request, 'Domain Record Added Successfully..! Details would be updated within 24 Hours.')
                        logs(f"IDN Domain {unicode_domain} Saved in Database ")
                        
                        ###############################################33
                        # Call Celery Function to Check and set parameters 
                        logs(f"Calling Celery Functions to Check and Update parameters")
                        update_domain_parameters.delay(unicode_domain)
                        #######################################################
                        return redirect('admin_app:dashboard2')
                    else:
                        messages.info(request,"Entered IDN domain already exists !!")
                        return redirect('admin_app:idn_domain_forms')
                else:
                    #log(request,f"Please enter valid details")
                    return render(request,'admin_app/idn_domain_forms.html', {'idn_dashboard_form_obj': idn_dashboard_form_obj,'English_Domain_Form_obj':English_Domain_Form_obj})
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
                return redirect('admin_app:idn_domain_forms')
                
        elif form_type == 'ENGDOMAINFORM':
            logs(f"POST Request is coming from English Domain Form")
            English_Domain_Form_obj = English_Domain_Form(request.POST)
            try:
                if English_Domain_Form_obj.is_valid():
                    logs(f"English_Domain_Form_obj is valid")
                    English_Domain_Form_obj.save()
                    messages.success(request, 'Domain Added Successfully ')
                    logs(f"Domain Added Successfully")
                    return redirect('admin_app:idn_domain_forms')
                else:
                    #log(request,f"Please enter valid details")
                    logs(f"English_Domain_Form_obj is not valid")
                    return render(request,'admin_app/idn_domain_forms.html', {'idn_dashboard_form_obj': idn_dashboard_form_obj,'English_Domain_Form_obj':English_Domain_Form_obj})
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
                logs(f"Exception : An error occurred:")
                return redirect('admin_app:idn_domain_forms')
    else:
        return render(request, 'admin_app/idn_domain_forms.html', {'idn_dashboard_form_obj': idn_dashboard_form_obj,'English_Domain_Form_obj':English_Domain_Form_obj})
    
#--------Added By Sanjayb-------
@login_required
def dashboard(request):
    English_Domain_total_records = English_Domain.objects.count()
    URL_dashboard_total_records = URL_dashboard.objects.count()
    URL_dashboard_total_records_governmnet = English_Domain.objects.filter(category__category_name="Government").count()
    URL_dashboard_total_records_private = English_Domain.objects.filter(category__category_name="Private").count()
    URL_dashboard_obj = URL_dashboard.objects.all().order_by('-id')

    # Count occurrences of True and False in idn_domain_running_status
    running_counts_domain = URL_dashboard_obj.values_list('idn_domain_running_status', flat=True)
    true_count_domain = sum(1 for status in running_counts_domain if status=='True')
    false_count_domain = sum(1 for status in running_counts_domain if status=='False')

    # Prepare data for the pie chart
    labels_domain = ['True', 'False']
    data_domain = [true_count_domain, false_count_domain]
    
    # Count occurrences of True and False in SSL Status
    running_counts_ssl = URL_dashboard_obj.values_list('ssl_configuration_status', flat=True)
    logs(f" Running Counts Statistics are  {running_counts_ssl}")
    true_count_ssl = sum(1 for status in running_counts_ssl if status=='True')
    false_count_ssl = sum(1 for status in running_counts_ssl if status=='False')

    # Prepare data for the pie chart
    labels_ssl = ['True', 'False']
    data_ssl = [true_count_ssl, false_count_ssl]
    
    logs(f" SSL Statistics are {data_ssl}")
    # Prepare data for Bar Chart 
    # Query to get the count of records for each language
    
    language_counts = URL_dashboard.objects.values('Language__language_name').annotate(count=Count('Language'))

    logs(f" Language data retreived from database is -- {language_counts}")
    languages = ['Hindi', 'Marathi', 'Bengali', 'Malayalam','Tamil','Telugu','Bengali','Odia','Sanskrit','Kannada','Punjabi','Gujrati','Manipuri','Assamese','Bodo','Santhali','Dogri','Kashmiri','Maithili','Nepali','Sindhi','Urdu']
    counts = []

    # Extract languages and counts from the query result
    for item in language_counts:
        # languages.append(item['Language__language_name'])
        counts.append(item['count'])
    logs(f" Languages are {languages}")
    logs(f" Languages Count are {counts}")
    

    #Prepare data for category distribution chart

    # Count the number of English domains in each category
    category_counts = English_Domain.objects.values('category__category_name').annotate(count=Count('id'))

    # Prepare data for the chart
    distribution_categories = []
    distribution_counts = []
    for category_count in category_counts:
        distribution_categories.append(category_count['category__category_name'])
        distribution_counts.append(category_count['count'])

    context = {
        'URL_dashboard_obj':URL_dashboard_obj,
        'URL_dashboard_total_records':URL_dashboard_total_records,
        'English_Domain_total_records':English_Domain_total_records,
        'URL_dashboard_total_records_governmnet':URL_dashboard_total_records_governmnet,
        'URL_dashboard_total_records_private':URL_dashboard_total_records_private,
        'labels_domain': labels_domain,
        'data_domain': data_domain,
        'labels_ssl': labels_ssl,
        'data_ssl': data_ssl,
        'languages': languages, 
        'counts': counts,
        'distribution_categories': distribution_categories,
        'distribution_counts': distribution_counts

        }
    return render(request, 'admin_app/dashboard.html', context)    

#--------Added By Sanjayb-------
@login_required
def dashboard2(request):
   
    English_Domain_total_records = English_Domain.objects.all().count()
    URL_dashboard_total_records = URL_dashboard.objects.all().count()
    URL_dashboard_total_records_governmnet = English_Domain.objects.filter(category__category_name="Government").count()
    URL_dashboard_total_records_private = English_Domain.objects.filter(category__category_name="Private").count()
    URL_dashboard_obj = URL_dashboard.objects.all().order_by('-id')

    # Count occurrences of True and False in idn_domain_running_status
    running_counts_domain = URL_dashboard_obj.values_list('idn_domain_running_status', flat=True)
    true_count_domain = sum(1 for status in running_counts_domain if status=='True')
    false_count_domain = sum(1 for status in running_counts_domain if status=='False')

    # Prepare data for the pie chart
    labels_domain = ['True', 'False']
    data_domain = [true_count_domain, false_count_domain]
    
    # Count occurrences of True and False in SSL Status
    running_counts_ssl = URL_dashboard_obj.values_list('ssl_configuration_status', flat=True)
    logs(f" Running Counts Statistics are  {running_counts_ssl}")
    true_count_ssl = sum(1 for status in running_counts_ssl if status=='True')
    false_count_ssl = sum(1 for status in running_counts_ssl if status=='False')

    # Prepare data for the pie chart
    labels_ssl = ['True', 'False']
    data_ssl = [true_count_ssl, false_count_ssl]
    
    logs(f" SSL Statistics are {data_ssl}")
    # Prepare data for Bar Chart 
    # Query to get the count of records for each language
    # Define your predefined set of languages
    predefined_languages = ['Hindi', 'Marathi', 'Bengali', 'Malayalam','Tamil','Telugu','Odia','Sanskrit','Kannada','Punjabi','Gujarati','Manipuri','Assamese','Bodo','Santhali','Dogri','Kashmiri','Maithili','Nepali','Sindhi','Urdu']  # Add your predefined languages here

    language_counts = URL_dashboard.objects.values('Language__language_name').annotate(count=Count('Language'))
    
    # Create a dictionary with predefined languages, initializing counts to zero
    language_dict = {language: 0 for language in predefined_languages}

    # Update the dictionary with counts retrieved from the query
    for entry in language_counts:
        language = entry['Language__language_name']
        count = entry['count']
        if language in language_dict:
            language_dict[language] = count
            
            # Separate the dictionary into two lists: one for languages and one for counts
    languages = list(language_dict.keys())
    counts = list(language_dict.values())
        
    # logs(f" Language data retreived from database is -- {language_counts}")
    # languages = ['Hindi', 'Marathi', 'Bengali', 'Malayalam','Tamil','Telugu','Bengali','Odia','Sanskrit','Kannada','Punjabi','Gujrati','Manipuri','Assamese','Bodo','Santhali','Dogri','Kashmiri','Maithili','Nepali','Sindhi','Urdu']
    # counts = []

    # Extract languages and counts from the query result
    # for item in language_counts:
    #     # languages.append(item['Language__language_name'])
    #     counts.append(item['count'])
    logs(f" Languages are {languages}")
    logs(f" Languages Count are {counts}")
    

    #Prepare data for category distribution chart

    # Count the number of English domains in each category
    category_counts = English_Domain.objects.values('category__category_name').annotate(count=Count('id'))

    # Prepare data for the chart
    distribution_categories = []
    distribution_counts = []
    for category_count in category_counts:
        # distribution_categories.append(category_count['category__category_name'])
        distribution_categories = ['Government', 'Private', 'Other']
        distribution_counts.append(category_count['count'])

    ## Remark Data Chart Starts
    # Retrieve all records from URL_dashboard
    records = URL_dashboard.objects.all()

    # Initialize a Counter to count occurrences of each language
    language_counter = Counter()

    # Extract and parse the Remark field
    for record in records:
        try:
            # Convert single quotes to double quotes for JSON parsing
            remark_data = json.loads(record.Remark.replace("'", '"'))
            content_language = remark_data.get("Content", "").strip()
            logs(f"Content Langauges are ---- > {content_language}")
            if content_language:
                language_counter[content_language] += 1
        except json.JSONDecodeError:
            print(f"Invalid JSON format in record ID {record.id}")

    # Prepare data for the template
    Remark_languages = list(language_counter.keys())
    Remark_counts = list(language_counter.values())
    ## Remark Data CHart Ends 
    logs(f"Records are --->{Remark_languages}{Remark_counts}")
    
    
    
    ##Content Languages Chart Starts 
    # Retrieve all records from URL_dashboard
    records = URL_dashboard.objects.all()

    # Initialize a Counter to count occurrences of each language
    language_counter = Counter()

    # Extract and count the content_language field
    for record in records:
        content_language = record.content_language.strip()
        if content_language:
            language_counter[content_language] += 1

    # Prepare data for the template
    content_languages = list(language_counter.keys())
    content_counts = list(language_counter.values())

    ## Content Langauges Chart Ends 
    
    
    ##########################################################33
    # Retrieve all records
    records = URL_dashboard.objects.all()

    # Extract the content language from each record
    content_languages_obj = records.values_list('content_language', flat=True)

    # Count the occurrences of each content language
    content_language_counts = Counter(content_languages_obj)

    # Total number of records
    total_records = len(content_languages_obj)

    # Calculate the proportion for each content language
    content_language_proportions = {lang: count / total_records for lang, count in content_language_counts.items()}

    # Prepare data for Chart.js
    content_language_proportions_labels = list(content_language_proportions.keys())
    content_language_proportions_data = [count * 100 for count in content_language_proportions.values()]  # Proportions in percentage
    
    ##########################################################
    

    
    context = {
        'URL_dashboard_total_records':URL_dashboard_total_records,
        'English_Domain_total_records':English_Domain_total_records,
        'URL_dashboard_total_records_governmnet':URL_dashboard_total_records_governmnet,
        'URL_dashboard_total_records_private':URL_dashboard_total_records_private,
        'labels_domain': labels_domain,
        'data_domain': data_domain,
        'labels_ssl': labels_ssl,
        'data_ssl': data_ssl,
        'languages': languages, 
        'counts': counts,
        'distribution_categories': distribution_categories,
        'distribution_counts': distribution_counts,
        'Remark_languages':Remark_languages,
        'Remark_counts':Remark_counts,
        'content_languages':content_languages,
        'content_counts':content_counts,
        'content_language_proportions_labels':content_language_proportions_labels,
        'content_language_proportions_data':content_language_proportions_data
        
        }
    return render(request, 'admin_app/dashboard2.html', context)  

#--------Added By Sanjayb-------
@login_required
def email_compose(request):
    if request.method=='POST':
        logs(f" Bulk Mail POST Method ")
        BulkEmail_Form_obj = BulkEmail_Form(request.POST, request.FILES)
        
        # logs(f"{BulkEmail_Form_obj}")
        if BulkEmail_Form_obj.is_valid() :
            logs(f"Bulk Email Form Data is valid ")
            # Check if email_attachment_file1 was provided
            
            BulkEmail_instance = BulkEmail_Form_obj.save()
            folder = 'media/email_attachment'
            if request.FILES.getlist('email_attachment'):
                for file in request.FILES.getlist('email_attachment'):
                    valid_extensions = ['png', 'jpg', 'jpeg', 'pdf', 'doc', 'docx', 'txt', 'xlsx', 'xls']
                    if file.size < 1 * 1024 * 1024 and file.name.count('.')<2 and (file.name.split('.')[1]).lower() in valid_extensions:
                        fs = FileSystemStorage(location=folder)
                        filename = fs.save(file.name, file)
                        BulkEmailAttachments.objects.create(email_attachment=f'email_attachment/{filename}', bulk_email=BulkEmail_instance)
                    else:
                        BulkEmail.objects.get(id=BulkEmail_instance.id).delete()
                        messages.error(request, f"Invalid attachment file named {file.name}")
                        context = {
                        'BulkEmail_Form_obj':BulkEmail_Form_obj
                        }
                        return render(request, 'admin_app/email_compose.html',context)
            # Process Email Sending Function
            logs(f" Passing id in celery Function as {BulkEmail_instance.id}")
            Send_Bulk_Email.delay(BulkEmail_instance.id)
            
            messages.success(request,"Sending Email Process Initiated")
            logs(f" Sending Email Process Completed Successfully")
            return redirect('admin_app:sent_email_view')
        else:
            logs(f"Bulk Email Form Data is not valid ")
            logs(f"{BulkEmail_Form_obj.errors}")
            messages.error(request, "Please Fill Correct Details")
            context = {
            'BulkEmail_Form_obj':BulkEmail_Form_obj
            }
            return render(request, 'admin_app/email_compose.html',context)
    else:
        logs(f"Bulk Mail GET Method ")
        BulkEmail_Form_obj = BulkEmail_Form()
        context = {
            'BulkEmail_Form_obj':BulkEmail_Form_obj
            }
        return render(request, 'admin_app/email_compose.html',context)
        
#--------Added By Sanjayb-------
@login_required  
def sent_email_view(request):
    logs(f"Calling sent_email_view view")
    BulkEmail_obj = BulkEmail.objects.all()
    return render(request,'admin_app/sent_email_view.html',{'BulkEmail_obj':BulkEmail_obj})
   
#--------Added By Sanjayb-------
@login_required
def sent_email_view_detail(request,id):
    logs(f"Calling sent_email_view_detail view")
    BulkEmail_obj = BulkEmail.objects.get(id=id)
    return render(request,'admin_app/sent_email_view_detail.html',{"BulkEmail_obj":BulkEmail_obj})

#--------Added By Sanjayb-------

@login_required
def refresh_domain_parameters(request,id):
    English_Domain_total_records = English_Domain.objects.count()
    URL_dashboard_total_records = URL_dashboard.objects.count()
    URL_dashboard_total_records_governmnet = English_Domain.objects.filter(category__category_name="Government").count()
    URL_dashboard_total_records_private = English_Domain.objects.filter(category__category_name="Private").count()
    URL_dashboard_obj = URL_dashboard.objects.all()

    context = {
        'URL_dashboard_obj':URL_dashboard_obj,
        'URL_dashboard_total_records':URL_dashboard_total_records,
        'English_Domain_total_records':English_Domain_total_records,
        'URL_dashboard_total_records_governmnet':URL_dashboard_total_records_governmnet,
        'URL_dashboard_total_records_private':URL_dashboard_total_records_private
        }
    URL_dashboard_obj = URL_dashboard.objects.get(id=id)
    unicode_domain = URL_dashboard_obj.IDN_domain
    logs(f"Calling Refresh Function For {unicode_domain}")
    update_domain_parameters.delay(unicode_domain)
    messages.success(request,"Parameters are being updated. Please wait and refresh after 60 seconds.")
    return redirect('admin_app:dashboard2')


#-----Added By Sanjay Bhargava------
@login_required
def edit_idn_domain_forms(request,id):
    if request.method== 'POST':
        logs("In views.py File -- > In POST Request ")
        URL_dashboard_instance = URL_dashboard.objects.get(id=id)
        logs(f"In views.py file -- > Fetched Object is {URL_dashboard_instance}")
        idn_dashboard_form_obj = idn_dashboard_form(request.POST,instance=URL_dashboard_instance)
        if URL_dashboard_instance.IDN_domain==request.POST.get('IDN_domain'):
            logs(f"Inside has changed for field=== URL_dashboard_instance.IDN_domain {URL_dashboard_instance.IDN_domain},{request.POST.get('IDN_domain')}")
            idn_dashboard_form_obj = idn_dashboard_form(request.POST,instance=URL_dashboard_instance,is_new=False)
        else:
            idn_dashboard_form_obj = idn_dashboard_form(request.POST,instance=URL_dashboard_instance,is_new=True)

        
        if idn_dashboard_form_obj.has_changed():
            logs(f"In views.py file -- > User has changed details {idn_dashboard_form_obj.has_changed()}")
            if idn_dashboard_form_obj.is_valid():
                logs("Changes has been requested by user")
                user_input_domain = idn_dashboard_form_obj.cleaned_data['IDN_domain']
                try:
                    unicode_domain = idna.decode(user_input_domain.split('/')[2])
                except:
                    unicode_domain = user_input_domain.split('/')[2]       
                unicode_domain=user_input_domain.split('/')[0] + '//' + unicode_domain 
                #log(request,f"Updated User input Domain is {user_input_domain}")
                temp_idn_dashboard_form_obj = idn_dashboard_form_obj.save(commit=False)
                temp_idn_dashboard_form_obj.IDN_domain = unicode_domain
                temp_idn_dashboard_form_obj.content_language = ''
                temp_idn_dashboard_form_obj.ssl_configuration_status=''
                temp_idn_dashboard_form_obj.idn_domain_running_status=''
                initial_remark = {
                    "General": "",
                    "Domain": "",
                    "SSL": "",
                    "Content": ""
                }
                # Serialize the dictionary to a JSON string
                current_remark = json.dumps(initial_remark)    
                # Assign the updated string back to the Remark field
                temp_idn_dashboard_form_obj.Remark = current_remark
                temp_idn_dashboard_form_obj.save()
                messages.info(request,"Domain Updated Successfully. Parameters would be updated shortly.")
                ###############################################33
                # Call Celery Function to Check and set parameters 
                logs(f"Calling Celery Functions to Check and Update parameters")
                update_domain_parameters.delay(unicode_domain)
                #######################################################
                return redirect('admin_app:dashboard2')
            else:
                logs("Please provide correct details.")
                messages.error(request,"Please provide correct details.")
                return render(request,'admin_app/edit_idn_domain_forms.html', {'idn_dashboard_form_obj': idn_dashboard_form_obj})
        else:
            logs("No changes Detected")
            messages.info(request,"No changes Detected.")
            # return render(request,'admin_app/edit_idn_domain_forms.html', {'idn_dashboard_form_obj': idn_dashboard_form_obj})
            return render(request,'admin_app/edit_idn_domain_forms.html', {'idn_dashboard_form_obj': idn_dashboard_form_obj})
    else:
        logs("In views.py File -- > In else Request ")
        URL_dashboard_instance = URL_dashboard.objects.get(id=id)
        idn_dashboard_form_obj = idn_dashboard_form(instance=URL_dashboard_instance)
        logs(f"in views.py file -- Updating Details for id {id}")
        return render(request,'admin_app/edit_idn_domain_forms.html', {'idn_dashboard_form_obj': idn_dashboard_form_obj})
        
        
        #-----Added By Sanjay Bhargava------

#-----Added By Sanjay Bhargava------

@login_required   
def show_logs(request):
    file_path = os.path.join(settings.BASE_DIR, 'message.logs')
    file_content = []

    # Open the file and read its content line by line
   # Open the file and read its content line by line
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.readlines()

    # Reverse the order of lines
    file_content.reverse()

    # Render the template with the file content
    return render(request, 'admin_app/show_logs.html', {'file_content': file_content}) 

#-----Added By Sanjay Bhargava------
@login_required 
def clear_logs(request):
    file_path = os.path.join(settings.BASE_DIR, 'message.logs')
    file_content = []
    
    # Open the file in write mode to clear its content
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('')  # Writing an empty string clears the file content
    
    # Redirect back to the page displaying the file content
    return redirect('admin_app:show_logs')

#-----Added By Sanjay Bhargava------

@login_required 
def show_logs_last(request):
    file_path = os.path.join(settings.BASE_DIR, 'message.logs')
    file_content = []

     # Open the file and read its content in reverse order
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the last 50 lines
        lines = file.readlines()[-50:]
        # Reverse the order of lines
        lines.reverse()
        for line in lines:
            file_content.append(line.strip())

    # Render the template with the last 50 lines of the file content
    return render(request, 'admin_app/show_logs.html', {'file_content': file_content}) 

#-----Added By Sanjay Bhargava------
@login_required 
def upload_excel(request):
    if request.method == 'POST':
        logs(f" upload_excel file POST method calling")
        ExcelUploadForm_obj = ExcelUploadForm(request.POST, request.FILES)
        logs(f" {ExcelUploadForm_obj}")
        if ExcelUploadForm_obj.is_valid():
            user_uploaded_excel_file = request.FILES['excel_file']
            df = pd.read_excel(user_uploaded_excel_file)
            logs(f" Excel File Readed and converted to dataframe successfully {df}")
            # print("data",df)
            ###########################################################################
            logs(f"Records Values Are :")
            invalid_data=[]
            try:
                for index, row in df.iterrows():
                    logs(f"{row['Category']}--{row['Department']}--{row['English_Domain']}--{row['Language']}--{row['IDN_Domain']}")
                    
                    # Check For Null Value Empty Value 
                    fields_to_check = [row['Category'], row['Department'], row['English_Domain'], row['Language'], row['IDN_Domain']]
                    logs(f" Fields to check are : {fields_to_check}")
                
                    if all(pd.notna(field) and field != "" for field in fields_to_check): 
                        logs(f"valid -- > Fields are : {fields_to_check}")  
                        logs(f" Valid Record ")    
                        # Cleaning User Values 
                        try:
                            user_category=row['Category'].strip()
                            user_department=row['Department'].strip()
                            user_english_domain_name=row['English_Domain'].strip()
                            user_idn_domain_name = row['IDN_Domain'].strip()
                            user_language = row['Language'].strip()
                        except Exception as e:
                            logs(f"views.py striping all fields values failed -- > {e},{index}")
                            invalid_data.append(row) 
                            continue
                        #--- English Record Insertion Procedure ----
                        try:
                            category_obj = category_list.objects.get(category_name=user_category)
                            logs(f" category fetched is -- {category_obj}")
                        except Exception as e:
                            logs(f"views.py category not found -- > {e},{index}") 
                            invalid_data.append(row)
                            continue
                    
                        #Check if record already exist or not 
                        # Check english domain is valid or not
                        if not validate_english_domain_name(user_english_domain_name):
                            print("English domain is not valid : ", user_english_domain_name)
                            invalid_data.append(row)
                            continue
                        
                        
                        if "://www." in user_english_domain_name:
                            parsed_english_domain = user_english_domain_name.split('/')[0] + "//" + user_english_domain_name.split('/')[2].replace("www.", "")
                        else:
                            parsed_english_domain = user_english_domain_name.split('/')[0]+ "//www." + user_english_domain_name.split('/')[2] 

                        if English_Domain.objects.filter(domain_name=user_english_domain_name).exists() or English_Domain.objects.filter(domain_name=parsed_english_domain).exists():
                            logs(f" English domain {user_english_domain_name} record already exists")
                        else:
                            English_Domain.objects.create(
                                department_name=user_department,
                                domain_name=user_english_domain_name,
                                category=category_obj,
                                )
                        #--- URL Dashboard  Record Insertion Procedure ----
                        # check IDN domain is valid 
                        if not validate_IDN_domain_name(user_idn_domain_name):
                            print("IDN domain is not valid : ", user_idn_domain_name)
                            invalid_data.append(row)
                            continue
                        
                        ##Check if user input idn domain is in ascii 
                        try:
                            converted_unicode_domain = idna.decode(user_idn_domain_name.split('/')[2])
                            logs(f"Converted Unicode domain from punycode is -- {converted_unicode_domain}")
                        except:
                            converted_unicode_domain = user_idn_domain_name.split('/')[2]
                            logs(f"User has entered Unicode domain  -- {converted_unicode_domain}")

                        converted_unicode_domain=user_idn_domain_name.split('/')[0] + '//' + converted_unicode_domain  
                        logs(f"Final Converted Unicode Domain is {converted_unicode_domain}")

                        if "://www." in converted_unicode_domain:
                            parsed_idn_domain = converted_unicode_domain.split('/')[0] + "//" + converted_unicode_domain.split('/')[2].replace("www.", "")
                        else:
                            parsed_idn_domain = converted_unicode_domain.split('/')[0]+ "//www." + converted_unicode_domain.split('/')[2] 
                        logs(f" Parsed Domain is -- {parsed_idn_domain} and converted unicode domain is {converted_unicode_domain}")

                        if URL_dashboard.objects.filter(IDN_domain=converted_unicode_domain).exists() or URL_dashboard.objects.filter(IDN_domain=parsed_idn_domain).exists():
                            logs(f" IDN domain {converted_unicode_domain} record already exists")
                        else:
                            english_domain_obj = English_Domain.objects.get(domain_name=user_english_domain_name)
                            logs(f" English Domain fetched is -- {english_domain_obj}")
                            language_obj = language_list.objects.get(language_name=user_language)
                            logs(f" Language fetched is -- {language_obj}")
                            initial_remark = {
                                    "General": "",
                                    "Domain": "",
                                    "SSL": "",
                                    "Content": ""
                                }
                                # Serialize the dictionary to a JSON string
                            current_remark = json.dumps(initial_remark) 
                            URL_dashboard.objects.create(
                                English_domain = english_domain_obj,
                                Language = language_obj,
                                IDN_domain = converted_unicode_domain,
                                ssl_configuration_status='',
                                idn_domain_running_status='',
                                content_language='',
                                Remark=current_remark
                            )
                            #Send to celery For Updating Parameter #
                            update_domain_parameters.delay(converted_unicode_domain)
                    else:
                        logs(f" Invalid Record for {index}")
                        invalid_data.append(row)
            except Exception as e:
                logs(f"views.py -- > {e}")

            invalid_data_df = pd.DataFrame(invalid_data)
            print(invalid_data_df)
            invalid_data_df.to_excel("invalid_data.xlsx")

            #########################################################################################################
            messages.success(request,"File Uploaded Successfully")
            return render(request,'admin_app/upload_excel_file.html',{'ExcelUploadForm_obj' : ExcelUploadForm_obj})
        else:
            messages.error(request,"Invalid File")
            logs(f"views.py file---> {ExcelUploadForm_obj.errors}")
            return render(request,'admin_app/upload_excel_file.html',{'ExcelUploadForm_obj' : ExcelUploadForm_obj})
            
    else:
        logs(f" upload_excel file GET method calling")
        ExcelUploadForm_obj = ExcelUploadForm()
        return render(request,'admin_app/upload_excel_file.html',{'ExcelUploadForm_obj' : ExcelUploadForm_obj})
        
#-----Added By Sanjay Bhargava------
@login_required 
def idn_domain_list(request):
    URL_dashboard_obj = URL_dashboard.objects.all().order_by('-id')
    return render(request,'admin_app/idn_domain_list.html',{'URL_dashboard_obj':URL_dashboard_obj})


#-----Added By Sanjay Bhargava------
@login_required 
def english_domain_list(request):
    English_Domain_obj = English_Domain.objects.all().order_by('-id')
    return render(request,'admin_app/english_domain_list.html',{'English_Domain_obj':English_Domain_obj})

#-----Added By Sanjay Bhargava------

# def admin_login(request):
#     print("loging get called")
#     logs("admin_login view called ")
#     if request.user.is_authenticated and request.user.is_staff:
#         logs("Admin is already login")
#         return redirect('admin_app:dashboard2')
#     if request.method == 'POST':
#         logs("POST Method Called")
#         form = AdminLoginForm(request.POST)
#         if form.is_valid():
#             logs("Form is Valid ")
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None and user.is_staff:
#                 logs("user is not None and user is_staff")
#                 login(request, user)
#                 return redirect('admin_app:dashboard2')  # Change this to your admin dashboard URL
#             else:
#                 logs("user is  None and user is not staff")
#                 messages.error(request, 'Invalid username or password.')
#                 return render(request,'admin_app/admin_login.html', {'form': form})
#         else:
#             logs("Form is Not Valid ")
#             messages.error(request, 'Invalid username or password.')
#             return render(request,'admin_app/admin_login.html', {'form': form})
#     else:
#         logs("GET Method Called")
#         form = AdminLoginForm()
#         print("page will render")
#     return render(request,'admin_app/admin_login.html', {'form': form})

# #-----Added By Sanjay Bhargava------
# @login_required 
# def admin_logout(request):
#     if request.user.is_authenticated and request.user.is_staff:
#         logout(request)
#         return redirect('login_view')  # Redirect to the login page after logging out
#     else:
#         return redirect('login_view')
        

#-------- Added By Sanjay Bhargava--------

def update_all_domains(request):
    IDN_domain_list = URL_dashboard.objects.values_list('IDN_domain', flat=True)
    logs(f"IDN List is -- {IDN_domain_list}")
    # Updating Parameters for All IDN Doamin Names
    for domain in IDN_domain_list:
        logs(f"Updating parameters for -- {domain}")
        update_domain_parameters.delay(domain)
    pass



def add_blog(request):
    if request.user.is_authenticated:
        user_obj=User.objects.get(id=request.user.id)
        UserProfile_obj=''
        try:
            UserProfile_obj=UserProfile.objects.get(UserProfile_user=user_obj)
        except:
            pass
        if UserProfile_obj:
            Blog_form_obj=Blog_form()
            if request.method == 'POST':
                    user_obj=User.objects.get(id=request.user.id)
                    Blog_form_obj = Blog_form(request.POST, request.FILES)
                    if Blog_form_obj.is_valid():
                        temp_obj = Blog_form_obj.save(commit=False)
                        temp_obj.Blog_Author = user_obj
                        temp_obj.save()
                        try:
                            RecipentMessage = """
                                Dear Sir/Ma'am,
                                We wanted to inform you that your blog has been successfully submitted for verification.
                                Our team will now review it to ensure compliance with our guidelines. Once verified by our admin panel, 
                                your blog will be promptly published on our website.

                                Best regards,
                                Bhashanet Team
                                """
                            send_mail("Submission: Blog Verification Request", RecipentMessage, env('SERVER_EMAIL'), [user_obj.email])
                            blog_link = 'http://bhashanet.in/admin/core_app/blog/' + str(temp_obj.id) + '/change/'
                            AdminMessage = f"""
                                        Please verify the following blog and update its status:
                                        Blog Link: {blog_link}
                                    """
                            email_sent_to_admin = send_mail("Action Required: New Blog for Verification", AdminMessage, env('SERVER_EMAIL'), ['pshweta@cdac.in'])
                        except:
                            print("error while sending email")
                        return redirect('admin_blog_datatable')
                    else:
                        #  #  print("Error")
                        context={
                            'Blog_form_obj':Blog_form_obj,
                            'flag_blog':'Add'
                        }
                        return render(request,'admin_app/add_blog.html',context)
            else:
                context={
                    'Blog_form_obj':Blog_form_obj,
                    'flag_blog':'Add'
                }
                return render(request,'admin_app/add_blog.html',context)
        else:
            messages.error(request, "To add a blog, please update your profile details first", extra_tags="danger")
            return redirect('user_profile')
    else:
        return redirect('login_view')



def edit_blog(request,id):
    #  print("id for blog edit",id)
    if request.user.is_authenticated:
        Blog_obj = Blog.objects.get(id=id)
        #  print("blog edit",Blog_obj)
        if request.method == 'POST':
            #  print("Inside post method of edit")
            user_obj=User.objects.get(id=request.user.id)
            Blog_form_obj = Blog_form(request.POST,request.FILES, instance=Blog_obj)
            #  print("Blog obj",Blog_form_obj)
            if Blog_form_obj.is_valid():
                temp_obj = Blog_form_obj.save(commit=False)
                if temp_obj.Blog_Author == user_obj:
                    temp_obj.save()
                    return redirect('admin_blog_datatable')
                else:
                    messages.error(request, "Invalid user for this blog", extra_tags="danger")
                    Blog_form_obj = Blog_form(request.POST,request.FILES,instance=Blog_obj)
                    return render(request, 'admin_app/add_blog.html', {'Blog_form_obj': Blog_form_obj,'flag_blog':'Edit'})
            else:
                Blog_form_obj = Blog_form(request.POST,request.FILES,instance=Blog_obj)
                return render(request, 'admin_app/add_blog.html', {'Blog_form_obj': Blog_form_obj,'flag_blog':'Edit'})
        else:
            Blog_form_obj = Blog_form(instance=Blog_obj)
            return render(request, 'admin_app/add_blog.html', {'Blog_form_obj': Blog_form_obj,'flag_blog':'Edit'})
    else:
        return redirect('blogs')



def delete_blog(request,id):
    if request.user.is_authenticated:
        user_obj=User.objects.get(id=request.user.id)
        try:
            Blog.objects.filter(id=id,Blog_Author=user_obj).delete()
        except:
            pass
        blog_data=Blog.objects.filter(Blog_Author=user_obj)
        context={
            'blog_data':blog_data
        }
        return render(request, 'admin_app/admin_blog_datatable.html',context)
    else:
        return redirect('blogs')



def admin_blog_datatable(request):
    if request.user.is_authenticated:
        user_obj=User.objects.get(id=request.user.id)
        blog_data=Blog.objects.filter(Blog_Author=user_obj)
        context={
            'blog_data':blog_data
        }
        return render(request, 'admin_app/admin_blog_datatable.html',context)
    else:
        return redirect('blogs')





def search_blog(request,id):
    blogname=id
    request.session['search_blog_string'] = blogname
    blog_cat=[]
    pagination=False
    Blog_Category_with_satus_true=BlogCategory.objects.filter(BlogCategory_Status=True)
    if Blog_Category_with_satus_true:
            for category in Blog_Category_with_satus_true:
                blog_cat.append(category.id)
            cat_id=blog_cat[0]
            pagination= True
    BlogCategory_data=BlogCategory.objects.all()
    if request.method == 'POST':
        try:
            blogname = request.POST.get('blogname')
        except:
            blogname=''
            return redirect('blogs')
        #  print("blogname==========",blogname)
        request.session['search_blog_string'] = blogname
        blog_cat=[]
        Blog_Category_with_satus_true=BlogCategory.objects.filter(BlogCategory_Status=True)
        if Blog_Category_with_satus_true and blogname != 'none':
            for category in Blog_Category_with_satus_true:
                blog_cat.append(category.id)
            cat_id=blog_cat[0]
            blogs_data=Blog.objects.none()
            status=True
            for cat_id in blog_cat:
                blog_cat_obj=BlogCategory.objects.get(id=cat_id)
                blogs_data = blogs_data | Blog.objects.filter(Blog_Title__contains = blogname,Blog_CategoryType=blog_cat_obj)
        else:
            cat_id=None
            status=False
            blogs_data=Blog.objects.none()
            blogs_data = blogs_data | Blog.objects.filter(Blog_Title__contains = blogname)
        #  print("blogs_data",blogs_data)
        BlogCategory_data=BlogCategory.objects.all()
        page = Paginator(blogs_data, 2)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        count = blogs_data.count()
        context={
        'blogs_data':blogs_data,
        'BlogCategory_data':BlogCategory_data,
        'Status':status,
        'page':page,
        'selected_id':cat_id,
        'all_data': 'Search',
        'blog_title' : blogname,
        }
        return render(request,'core_app/blog_list.html',context)
    if pagination:
        status=True
        blogs_data=Blog.objects.none()
        for cat_id in blog_cat:
            blog_cat_obj=BlogCategory.objects.get(id=cat_id)
            blogs_data = blogs_data | Blog.objects.filter(Blog_Title__contains = blogname,Blog_CategoryType=blog_cat_obj)
        page = Paginator(blogs_data, 2)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        count = blogs_data.count()
        context={
        'blogs_data':blogs_data,
        'BlogCategory_data':BlogCategory_data,
        'Status':status,
        'page':page,
        'selected_id':cat_id,
        'all_data': 'Search',
        'blog_title' : blogname,
        }
    else:
        status=False
        cat_id=None
        blogs_data=Blog.objects.none()
        blogs_data = blogs_data | Blog.objects.filter(Blog_Title__contains = blogname)
        page = Paginator(blogs_data, 2)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        count = blogs_data.count()
        context={
        'blogs_data':blogs_data,
        'BlogCategory_data':BlogCategory_data,
        'Status':status,
        'page':page,
        'selected_id':cat_id,
        'all_data': 'Search',
        'blog_title' : blogname,
        }
    return render(request,'core_app/blog_list.html',context)

