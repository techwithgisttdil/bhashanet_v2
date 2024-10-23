from django import forms
from django.forms import ModelForm, Form
from .models import *
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextFormField
from .validate import *
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.core.exceptions import ValidationError
from bhashanet_v2.logger import *
from urllib.parse import urlparse
import idna
import unicodedata
import dns.resolver
import dns.exception
from .utility import *
from .utility import validate_English_Domain_Form_Category,validate_English_Domain_Form_Department,validate_English_Domain_Form_Domain_Name
from .validation import *





# Below Forms are being used for admin App only 
class idn_dashboard_form(forms.ModelForm):
    IDN_domain = forms.CharField(label="Enter Idn Domain", max_length=200, widget=forms.TextInput(
        attrs={"class": "form-control", 'id': 'inputIdnDomain', "placeholder": "Enter domain",
               'autocomplete': 'off', 'required': True}))
    English_domain = forms.ModelChoiceField(label="Select English Domain",
                                            queryset=English_Domain.objects.all(),
                                            widget=forms.Select(
                                                attrs={"class": "form-control",
                                                       'id': 'inputEnglishDomain',
                                                       'autocomplete': 'off'}))

    Language = forms.ModelChoiceField(label="Select Language",
                                      queryset=language_list.objects.all(),
                                      widget=forms.Select(
                                          attrs={"class": "form-control",
                                                 'id': 'inputLanguage',
                                                 'autocomplete': 'off'}))

    class Meta:
        model = URL_dashboard
        fields = ['IDN_domain', 'English_domain', 'Language']
        
    def __init__(self, *args, **kwargs):
        # Accepts any positional (*args) and keyword (**kwargs) arguments
        # Pop the 'is_new' keyword argument from kwargs and assign its value to self.is_new,
        # defaulting to False if it's not provided 
        self.is_new = kwargs.pop('is_new', False)
        # Call the __init__ method of the parent class (superclass) with any remaining
        # positional and keyword arguments 
        super(idn_dashboard_form, self).__init__(*args, **kwargs) 

    def clean(self):
        logs("forms.py file --  Inside Clean method of idn_dashboard_form ")
        super(idn_dashboard_form, self).clean()
        logs("forms.py file --  Function validate_idn_dashboard_form is being called for validations ")
        validate_idn_dashboard_form(self)
        logs("forms.py file --  All Validation Successfull For IDN Form")
        
#################################################
        
class English_Domain_Form(forms.ModelForm):
    category = forms.ModelChoiceField(label="Select Website Category",
                                      queryset=category_list.objects.all(),
                                      widget=forms.Select(
                                          attrs={"class": "form-control",
                                                 'id': 'EnglishCategory',
                                                 'autocomplete': 'off'}))

    domain_name = forms.CharField(label="Enter English Domain", max_length=256, widget=forms.TextInput(
        attrs={"class": "form-control", 'id': 'inputengDomain', "placeholder": "Enter english domain",
               'autocomplete': 'off', 'required': True}))

    department_name = forms.CharField(label="Enter Department Name", max_length=300, widget=forms.TextInput(
        attrs={"class": "form-control", 'id': 'inputengDomain', "placeholder": "Enter Department Name",
               'autocomplete': 'off', 'required': True}))

    class Meta:
        model = English_Domain
        fields = ['department_name', 'domain_name', 'category']

    def clean(self):
        logs("forms.py file --  Inside Clean method of English_Domain_Form ")
        super(English_Domain_Form, self).clean()
        logs("forms.py file --  Function validate_English_Domain_Form is being called for validations ")
        validate_English_Domain_Form(self)
        logs("forms.py file --  All Validation Successfull For English Form")

#################################################

class BulkEmail_Form(forms.ModelForm):
    email_subject = forms.CharField(label="Enter Subject", max_length=800, widget=forms.TextInput(
        attrs={"class": "form-control", 'id': 'email_subject', "placeholder": "Enter Email Subject",
               'autocomplete': 'off', 'required': True}))
    
    email_receipient_list = forms.FileField(label="Upload Receipient List", widget=forms.FileInput(
        attrs={'style': 'border-radius:6px', 'class': 'form-control','id':"Receipient_list",'required': True}))
    
      
    class Meta:
        model = BulkEmail
        fields = ['email_subject', 'email_message', 'email_receipient_list']
    
    def clean(self):
        logs("forms.py file --  Inside Clean method of BulkEmail_Form ")
        super(BulkEmail_Form, self).clean()
        logs("forms.py file --  Function BulkEmail_Form is being called for validations ")
        # validate_English_Domain_Form(self)
        logs("forms.py file --  All Validation Successfull For BulkEmail_Form")



#################################################

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label="Upload Excel File", widget=forms.FileInput(
        attrs={'style': 'border-radius:6px', 'class': 'form-control','id':"ExcelFile"}))
 
#################################################

class AdminLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        label='Username'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label='Password'
    )
 




##################################


# Below Forms are being used for blog and user related 

class Blog_form(ModelForm):
    Blog_Title = forms.CharField(label="Blog Title", max_length=800, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Blog Title', 'id': 'Blog_Title', 'class': 'form-control form-control-lg'}))
    Blog_Description = forms.CharField(label="Blog Description", max_length=2000, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Blog Description', 'id': 'Blog_Description', 'class': 'form-control form-control-lg',}))
    Blog_Body: RichTextFormField()
    Blog_CategoryType = forms.ModelChoiceField(required=True, queryset=BlogCategory.objects.all(),
                                                   widget=forms.Select(
                                                       attrs={'class': 'form-control', 'id': 'Blog_CategoryType',
                                                            }))
    Blog_Status = (('Published', 'PUBLISHED'),
                       ('Unpublished', 'UNPUBLISHED'))
    Blog_PublishedStatus = forms.ChoiceField(validators=[validators.MaxLengthValidator(15)], required=True,
                                            help_text='Select Status',
                                            choices=Blog_Status, widget=forms.Select(
            attrs={'style': 'border-color: grey ;margin-bottom:20px', 'placeholder': 'select',
                   'id': 'Blog_PublishedStatus', 'class': 'form-control form-control-lg', 'autocomplete': 'off'}), )
    

    class Meta:
        model = Blog
        fields = [
            'Blog_Title',
            'Blog_Description',
            'Blog_Body',
            'Blog_CategoryType',
            'Blog_PublishedStatus',
            'Blog_Thumbnail',
            'Blog_DocumentFile'
        ]
       
    def clean(self):
        super(Blog_form, self).clean()
        validate_Blog_form(self)


#### ---------------- Added by shivam sharma


class RegistrationForm(forms.Form):
    email = forms.CharField(max_length=60, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'inputEmail', 'placeholder': 'Enter Email', 'autocomplete': 'off'}))

    password1 = forms.CharField(required=True, strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'inputPassword', 'placeholder': 'Enter Password', 'name': 'password1'}))
    password2 = forms.CharField(required=True, strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'inputPassword1', 'placeholder': 'Confirm Password'}))
    
    role = forms.ModelChoiceField(required=False, queryset=UserRole.objects.exclude(id=4),widget=forms.Select(attrs={'class': 'form-control',
                                                                                                             'id': 'UserRole',}))

    captcha_hidden = forms.CharField(widget=forms.HiddenInput(), required="False")
    captcha_input = forms.CharField(max_length=5, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'inputCaptcha', 'placeholder': 'Enter Captcha', 'name': 'captcha'}))

    # class Meta:
    #     model = User
    #     # model._meta.get_field('email')._unique = True
    #     fields = ("email", "password1", "password2")
     

    def clean(self):
        super(RegistrationForm, self).clean()
        validate_registerform(self)

    # def save(self, email, commit=True):
    #     print("jjjjj")
    #     user = super(RegistrationForm, self).save(commit=False)
    #     print("email ", User.objects.exclude(
    #         pk=self.instance.pk).filter(username=email).exists())
    #     if not User.objects.exclude(pk=self.instance.pk).filter(username=email).exists():
    #         user.username = self.cleaned_data['email']
    #         user.email = self.cleaned_data['email']
    #         user.password1 = self.cleaned_data['password1']
    #         user.password2 = self.cleaned_data['password2']
    #         if commit:
    #             user.is_active = False
    #             user.save()
    #         return user
    #     else:
    #         duplicate_user = User.objects.get(username=email)
    #         print("duplicate_user ", duplicate_user.is_active)

    #         if not duplicate_user.is_active:
    #             duplicate_user.password1 = self.cleaned_data['password1']
    #             duplicate_user.password2 = self.cleaned_data['password2']
    #             if commit:
    #                 duplicate_user.save()
    #             return duplicate_user
    #         else:
    #             return self.add_error('email', "email address already exists")


class LoginForm(forms.Form):
    # username = forms.EmailField(max_length=60, required=True, widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'id': 'inputEmail', 'placeholder': 'Enter Email', 'autocomplete': 'off'}))
    
    username = forms.CharField(max_length=60, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'inputEmail', 'placeholder': 'Enter Email', 'autocomplete': 'off'}))

    password = forms.CharField(required=True, strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'inputPassword', 'placeholder': 'Enter Password', 'name': 'password'}))

    captcha_hidden = forms.CharField(widget=forms.HiddenInput(), required="False")
    captcha_input = forms.CharField(max_length=5, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'inputCaptcha', 'placeholder': 'Enter Captcha', 'name': 'captcha'}))

    def clean(self):
        print("FORMS.PY FILE : CLEAN METHOD CALLING")
        # data is feteched using the super function of django
        super(LoginForm, self).clean()
        validate_login_form(self)
    

## ----- Change Password 
class ChangePasswordUserForm(forms.Form):
    old_password = forms.CharField(min_length=3, max_length=20, required=True, strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', id: "inputOldPassword", 'placeholder': 'Enter Old Password',
               'name': 'old_password'}))
    new_password = forms.CharField(min_length=8, max_length=20, required=True, strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', id: "inputNewPassword", 'placeholder': 'Enter New Password',
               'name': 'new_password'}))
    confirm_password = forms.CharField(min_length=8, max_length=20, required=True, strip=False,
                                       widget=forms.PasswordInput(
                                           attrs={'class': 'form-control', id: "inputConfirmPassword",
                                                  'placeholder': 'Enter Confirm Password', 'name': 'confirm_password'}))

    def clean(self):
        print("FORMS.PY FILE : CLEAN METHOD CALLING")
        super(ChangePasswordUserForm, self).clean()
        validate_change_password_user_form(self)
        
        

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(max_length=60, required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'inputEmail', 'placeholder': 'Enter Email', 'autocomplete': 'off'}))
    
    captcha_hidden = forms.CharField(widget=forms.HiddenInput(), required="False")
    captcha_input = forms.CharField(max_length=5, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'inputCaptcha', 'placeholder': 'Enter Captcha', 'name': 'captcha'}))
    
    def clean(self):
        print("FORMS.PY FILE : CLEAN METHOD CALLING")
        # data is feteched using the super function of django
        super().clean()
        validate_forgot_password_form(self)


class PasswordCreationForm(forms.Form):
    password = forms.CharField(min_length=8, max_length=20, required=True, strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': "inputNewPassword", 'placeholder': 'Enter Password', 'name': 'password'}))
    confirm_password = forms.CharField(min_length=8, max_length=20, required=True, strip=False,
                                       widget=forms.PasswordInput(
                                           attrs={'class': 'form-control', 'id': "inputConfirmPassword",
                                                  'placeholder': 'Enter Confirm Password', 'name': 'confirm_password'}))

    def clean(self):
        print("FORMS.PY FILE : CLEAN METHOD CALLING")
        # data is feteched using the super function of django
        super(PasswordCreationForm, self).clean()
        validate_password_creation_form(self)



class UserProfileForm(ModelForm):
    UserProfile_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Enter Full Name", 'autocomplete': 'off'}))
    UserProfile_designation = forms.CharField(required=True, widget=forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Enter Designation", 'autocomplete': 'off'}))
    UserProfile_organization = forms.CharField(required=True, widget=forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Enter Organization Name", 'autocomplete': 'off'}))
    UserProfile_Bio = forms.CharField(label="Your Feedback", widget=forms.Textarea(
        attrs={'style': "height: 100px;", 'placeholder': 'Enter Bio', 'class': 'form-control', 'autocomplete': 'off'}))
    UserProfile_organization_logo = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={"class" : "form-control", "id": "profile_image"}))
    
    
    class Meta:
        model = UserProfile
        fields = ["UserProfile_name", "UserProfile_designation", "UserProfile_organization", "UserProfile_organization_logo", "UserProfile_Bio"]

   
    def clean(self):
        print("FORMS.PY FILE : CLEAN METHOD CALLING")
        super(UserProfileForm, self).clean()
        validate_user_profile_form(self)



class OTPForRegistrationForm(forms.Form):
    
    otp=forms.IntegerField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'inputOTP', 'placeholder': 'Enter OTP', 'autocomplete': 'off'}))

    
    def clean(self):
        super(OTPForRegistrationForm, self).clean()
        

