from django import forms
from django.forms import ModelForm, Form
from .models import *
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextFormField
from .validate import *
from django.core import validators
from django.contrib.auth.forms import UserCreationForm


class Feedback_form(ModelForm):
    Feedback_FirstName = forms.CharField(label="Name", max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Name', 'id': 'Feedback_FirstName', 'class': 'form-control form-control-lg',
               'autocomplete': 'off'}))
    Feedback_Email = forms.CharField(label="Name", max_length=300, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Email ID', 'id': 'Feedback_Email', 'class': 'form-control form-control-lg',
               'autocomplete': 'off'}))
    Feedback_Related_To = forms.ModelChoiceField(label='Select Category', required=True,
                                            help_text='Select Category',
                                            queryset=FeedbackCategory.objects.all(), widget=forms.Select(
            attrs={'style': 'border-color: grey ;margin-bottom:20px', 'placeholder': 'select',
                   'id': 'Feedback_Category', 'class': 'form-control form-control-lg', 'autocomplete': 'off'}), )
    Feedback_Message = forms.CharField(label=" Your Feedback", widget=forms.Textarea(
        attrs={'style': 'border-color: grey ;margin-bottom:20px', 'placeholder': 'Enter Your Feedback',
               'id': 'Feedback_Message', 'class': 'NALOC form-control form-control-lg', 'autocomplete': 'off'}))

    captcha_hidden = forms.CharField(widget=forms.HiddenInput(), required="False")
    captcha_input = forms.CharField(max_length=5, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'inputCaptcha', 'placeholder': 'Enter Captcha', 'name': 'captcha'}))

    class Meta:
        model = UserFeedbackData
        fields = [
            'Feedback_FirstName',
            'Feedback_Email',
            'Feedback_Related_To',
            'Feedback_Message'
        ]

    def clean(self):
        print("FORMS.PY FILE : CLEAN METHOD CALLING")
        # data is feteched using the super function of django
        super(Feedback_form, self).clean()
        validate_feedbackform(self)

# ---------------------------------------------------------------------------------------------------

class Domain_Syntax_Check_form(ModelForm):
    Domain_Name = forms.CharField(label="Domain", max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your domain', 'id': 'Domain', 'class': 'form-control form-control-lg',
               'autocomplete': 'off'}))

    class Meta:
        model = DomainSyntax
        fields = [
            'Domain_Name'
        ]

    def clean(self):
        print("FORMS.PY FILE : CLEAN METHOD CALLING")
        # data is feteched using the super function of django
        super(Domain_Syntax_Check_form, self).clean()
        validate_domain(self)

# ---------------------------------------------------------------------------------------------------

class Email_Syntax_Check_form(ModelForm):
    Email_Address = forms.CharField(label="Email", max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Email', 'id': 'email', 'class': 'form-control form-control-lg',
               'autocomplete': 'off'}))

    class Meta:
        model = EmailSyntax
        fields = [
            'Email_Address'
        ]

    def clean(self):
        print("FORMS.PY FILE : CLEAN METHOD CALLING")
        # data is feteched using the super function of django
        super(Email_Syntax_Check_form, self).clean()
        validate_email(self)

# ---------------------------------------------------------------------------------------------------

class IDN_Ready_Websites(Form):
    select_category = forms.ModelMultipleChoiceField(queryset=IDNReadyWebsitesCategory.objects.all(), widget=forms.CheckboxSelectMultiple)
    select_language = forms.ModelMultipleChoiceField(queryset=IDNReadyWebsitesLanguages.objects.all(), widget=forms.CheckboxSelectMultiple)

# ---------------------------------------------------------------------------------------------------

class IDNRequestForUserWebsitesForm(ModelForm):
    IDN_Email = forms.CharField(max_length=500, required=True, 
                                widget=forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Enter Email Address"}))
    IDN_Category = forms.ModelChoiceField(queryset=IDNRequestForUserWebsitesCategories.objects.filter(website_status="Active"), required=True, empty_label="Please Select",
                                     widget=forms.Select(attrs={"class" : "form-control", "placeholder" : "Domain Name (English)"}))
    IDN_English_Domain = forms.CharField(max_length=600, required=True, 
                                         widget=forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Enter Domain Name (English)"}))
    
    
    captcha_hidden = forms.CharField(widget=forms.HiddenInput(), required="False")
    captcha_input = forms.CharField(max_length=5, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'inputCaptcha', 'placeholder': 'Enter Captcha', 'name': 'captcha'}))
    
    class Meta:
        model = IDNRequestForUserWebsites
        fields = [ "IDN_Email", "IDN_Category", "IDN_English_Domain" ]

   
    def clean(self):
        print("FORMS.PY FILE : CLEAN METHOD CALLING")
        super(IDNRequestForUserWebsitesForm, self).clean()
        validate_IDNRequestForUserWebsitesForm(self)

