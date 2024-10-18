# Image size validation
from django.core.exceptions import ValidationError
from django.utils.html import escape
from django import forms
import re
from datetime import *
from django.contrib.auth.hashers import check_password
from core_app.utility import validateFile




def validate_Blog_form(self):
    print("VALIDATE.PY FILE: in validate_feedbackform function")
    Blog_Title = self.cleaned_data.get('Blog_Title')
    Blog_Description = self.cleaned_data.get('Blog_Description')
    Blog_Body = self.cleaned_data.get('Blog_Body')
    Blog_CategoryType = self.cleaned_data.get('Blog_CategoryType')
    # Blog_PublishedStatus = self.cleaned_data.get('Blog_PublishedStatus')
    Blog_Thumbnail = self.cleaned_data.get('Blog_Thumbnail')
    Blog_DocumentFile = self.cleaned_data.get('Blog_DocumentFile')
    
    print("VALIDATE.PY FILE : BLOG FORM BLOG TITLE --- ", Blog_Title)
    print("VALIDATE.PY FILE : BLOG FORM DESCRIPTION --- ", Blog_Description)
    print("VALIDATE.PY FILE : BLOG FORM BODY --- ", Blog_Body)
    print("VALIDATE.PY FILE : BLOG FORM CATEGORY TYPE --- ", Blog_CategoryType)
    # print("VALIDATE.PY FILE : BLOG FORM PUBLISH STATUS --- ", Blog_PublishedStatus)
    print("VALIDATE.PY FILE : BLOG FORM THUMBNAIL --- ", type(Blog_Thumbnail),Blog_Thumbnail)
    print("VALIDATE.PY FILE : BLOG FORM DOCUMENT FILE --- ", Blog_DocumentFile)


    if Blog_Title is None or len(Blog_Title) < 3:
        print("VALIDATE.PY FILE : BLOG FORM BLOG TITLE ERROR ")
        raise forms.ValidationError("Please enter valid blog title")
    
    if Blog_Description is None or len(Blog_Description) < 3:
        print("VALIDATE.PY FILE : BLOG FORM BLOG DESCRIPTION ERROR ")
        raise forms.ValidationError("Please enter valid blog description")
    
    if Blog_Body is None or len(Blog_Body) < 3:
        print("VALIDATE.PY FILE : BLOG FORM BLOG BODY ERROR ")
        raise forms.ValidationError("Please enter valid blog body")
    
    if Blog_CategoryType is None:
        print("VALIDATE.PY FILE : BLOG FORM BLOG CATEGIRY TYPE ERROR ")
        raise forms.ValidationError("Please select valid blog category")
    
  
    if Blog_Thumbnail is not None:
        # print("inside validate thumbnail",validateFile(Blog_Thumbnail, [ 'jpeg', 'jpg', 'png'], 5 * 1024 * 1024))
        if not validateFile(Blog_Thumbnail, [ 'jpeg', 'jpg', 'png'], 5 * 1024 * 1024):
            print("VALIDATE.PY FILE : Blog Thumbnail File extention VALIDATION FAILED ERROR RAISED ")
            raise forms.ValidationError(
                "The selected project image '{}' could not be uploaded.\n Only files with the following extensions are allowed [  'jpeg', 'jpg', 'png' ] with size 5MB".format(
                    Blog_Thumbnail.name))
    else:
        raise forms.ValidationError("Please select valid blog thumbnail")
   
        

    if Blog_DocumentFile is not None:
        if not validateFile(Blog_DocumentFile, [ 'pdf'], 10 * 1024 * 1024):
            print("VALIDATE.PY FILE : Blog DocumentFile File extention VALIDATION FAILED ERROR RAISED ")
            raise forms.ValidationError(
                "The selected project document '{}' could not be uploaded.\n Only files with the following extensions are allowed [  'pdf' ] with size 10MB".format(
                    Blog_DocumentFile.name))
    
        

    return self.cleaned_data


# REGISTRATION FORM VALIDATION

def validate_registerform(self):
    print("VALIDATE.PY FILE: in validate_registerform function")
    register_user_name = self.cleaned_data.get('email')
    register_user_password = self.cleaned_data.get('password1')
    register_user_confirm_password = self.cleaned_data.get('password2')
    captcha_hidden = self.cleaned_data.get('captcha_hidden')
    captcha_input = self.cleaned_data.get('captcha_input')

    print("VALIDATE.PY FILE : REGISTER FORM USERNAME --- ", register_user_name)
    print("VALIDATE.PY FILE : REGISTER FORM PASSWORD --- ", register_user_password)
    print("VALIDATE.PY FILE : REGISTER FORM CONFIRM PASSWORD --- ", register_user_confirm_password)
    print("VALIDATE.PY FILE : REGISTER FORM CAPTCHA HIDDEN CHECK --- ", captcha_hidden)
    print("VALIDATE.PY FILE : REGISTER FORM CAPTCHA INPUT CHECK --- ", captcha_input)
    

    # email_regex = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
    
    ## email reg with NON-ASCII characters
    email_regex = re.compile(r'^[\w]+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
    # password_regex =  re.compile(r'(?=[A-Za-z0-9@#$%^&+!=]+$)^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&+!=])(?=.{7,17}).*$') # added by tanvi
    password_regex = re.compile(
        r'(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+!=])[a-zA-Z0-9@#$%^&+!=]{8,20}')  # added by shivam

    # if register_user_name == None or not re.fullmatch(email_regex, register_user_name) or len(register_user_name) > 60:
    #     print("VALIDATE.PY FILE : REGISTER FORM USERNAME VALIDATION FAILED ERROR RAISED")
    #     raise forms.ValidationError("Enter Valid Email")

    if register_user_name == None or len(register_user_name) > 60:
        print("VALIDATE.PY FILE : REGISTER FORM USERNAME VALIDATION FAILED ERROR RAISED")
        raise forms.ValidationError("Enter Valid Email")
    
    if register_user_password == None or not re.fullmatch(password_regex, register_user_password):
        print("VALIDATE.PY FILE : REGISTER FORM PASSWORD VALIDATION FAILED ERROR RAISED")
        raise forms.ValidationError("Enter Valid Password")
    
    if register_user_confirm_password == None or not re.fullmatch(password_regex, register_user_password):
        print("VALIDATE.PY FILE : REGISTER FORM CONFIRM PASSWORD VALIDATION FAILED ERROR RAISED")
        raise forms.ValidationError("Enter valid confirm password")
    
    if register_user_password != register_user_password:
        print("VALIDATE.PY FILE : REGISTER FORM MACHING PASSWORDS FAILED ERROR RAISED")
        raise forms.ValidationError("The passwords do not match")
    
    if captcha_input is None:
        print("VALIDATE.PY FILE : REGISTER FORM captcha_input VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please Enter Captcha")
    
    if len(captcha_input) > 5:
        print("VALIDATE.PY FILE : REGISTER FORM captcha_input VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Captcha value must be of 5 charatcters only")
    
    print("Captcha check ", check_password(captcha_input,captcha_hidden))
    if not check_password(captcha_input,captcha_hidden):
        print("VALIDATE.PY FILE : REGISTER FORM captcha_hidden VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Invalid Captcha")
    
    print("VALIDATE.PY FILE : REGISTER FORM VALIDATION PASSED : RETURNING CLEAN DATA  ")
    return self.cleaned_data


# LOGIN FORM VALIDATION
def validate_login_form(self):
    print("VALIDATE.PY FILE: in validate_loginform function")
    email = self.data.get('username')
    password = self.cleaned_data.get('password')
    captcha_hidden = self.cleaned_data.get('captcha_hidden')
    captcha_input = self.cleaned_data.get('captcha_input')

    print("VALIDATE.PY FILE : LOGIN FORM EMAIL --- ", email)
    print("VALIDATE.PY FILE : LOGIN FORM RELATED TO --- ", password)
    print("VALIDATE.PY FILE : LOGIN FORM RELATED TO --- ", captcha_hidden)
    print("VALIDATE.PY FILE : LOGIN FORM RELATED TO --- ", captcha_input)
    

    email_regex = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')

    password_regex = re.compile(r'(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$])[a-zA-Z0-9@#$*&]{8,20}')
    
    if email == '':
        print("VALIDATE.PY FILE : LOGIN FORM EMAIL VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please Enter Email Address")
              
    if password is None:
        print("VALIDATE.PY FILE : LOGIN FORM PASSWORD VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please Enter Password")
    
    if captcha_input is None:
        print("VALIDATE.PY FILE : LOGIN FORM captcha_input VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please Enter Captcha")
    
    if len(captcha_input) > 5:
        print("VALIDATE.PY FILE : LOGIN FORM captcha_input VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Captcha value must be of 5 charatcters only")
    
    print("captcha validation ", check_password(captcha_input,captcha_hidden))
    
    if not check_password(captcha_input,captcha_hidden):
        print("VALIDATE.PY FILE : LOGIN FORM captcha_hidden VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Invalid Captcha")
    
    # if email is None or not re.fullmatch(email_regex, email):
    #     # self._errors['feedback_user_name'] = self.error_class(['3 characters and more is required for this field'])
    #     print("VALIDATE.PY FILE : LOGIN FORM EMAIL VALIDATION FAILED ERROR RAISED ")
    #     raise forms.ValidationError("Incorrect login credentials")
    
    if email is None :
        # self._errors['feedback_user_name'] = self.error_class(['3 characters and more is required for this field'])
        print("VALIDATE.PY FILE : LOGIN FORM EMAIL VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Incorrect login credentials")

    if len(email) > 60:
        print("VALIDATE.PY FILE : LOGIN FORM EMAIL VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("The maximum total length of a email is 60 characters.")

    # if password is None or not re.fullmatch(password_regex, password):
    #     # self._errors['feedback_message'] = self.error_class(['3 characters and more is required for this field'])
    #     print("VALIDATE.PY FILE : LOGIN FORM PASSWORD VALIDATION FAILED ERROR RAISED 111")
    #     raise forms.ValidationError("Incorrect login credentials")
    
    print("VALIDATE.PY FILE : LOGIN FORM VALIDATION PASSED : RETURNING CLEAN DATA  ")
    return self.cleaned_data



# CHANGE PASSWORD FOR AGENT FROM VALIDATION
def validate_change_password_agent_form(self):
    print("VALIDATE.PY FILE: in change_password_creation_form_for_agent function")
    new_password = self.cleaned_data.get('new_password')
    confirm_password = self.cleaned_data.get('confirm_password')

    print("VALIDATE.PY FILE : CHANGE PASSWORD FORM new_password --- ", new_password)
    print("VALIDATE.PY FILE : CHANGE PASSWORD FORM confirm_password --- ", confirm_password)

    password_regex = re.compile(r'(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+!=])[a-zA-Z0-9@#$%^&+!=]{8,20}')
    # password_regex = re.compile(r'(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$])[a-zA-Z0-9@#$*&]{8,20}')

    if new_password is None or not re.fullmatch(password_regex, new_password):
        # self._errors['feedback_message'] = self.error_class(['3 characters and more is required for this field'])
        print("VALIDATE.PY FILE : CHANGE PASSWORD FORM NEW_PASSWORD VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please Enter valid new password")

    if confirm_password is None or not re.fullmatch(password_regex, confirm_password):
        # self._errors['feedback_message'] = self.error_class(['3 characters and more is required for this field'])
        print("VALIDATE.PY FILE : CHANGE PASSWORD FORM CONFIRM_PASSWORD VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please Enter valid confirm password")

    if new_password != confirm_password:
        print(
            "VALIDATE.PY FILE : CHANGE PASSWORD FORM NEW_PASSWORD AND CONFIRM_PASSWORD VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Confirm Password must be same as New Password")

    else:
        print("VALIDATE.PY FILE : CHANGE PASSWORD FORM VALIDATION PASSED : RETURNING CLEAN DATA  ")
        return self.cleaned_data
    


# CHANGE PASSWORD FOR USER
def validate_change_password_user_form(self):
    print("VALIDATE.PY FILE: in change_password_creation_form function")
    old_password = self.cleaned_data.get('old_password')
    new_password = self.cleaned_data.get('new_password')
    confirm_password = self.cleaned_data.get('confirm_password')

    print("VALIDATE.PY FILE : CHANGE PASSWORD FORM old_password --- ", old_password)
    print("VALIDATE.PY FILE : CHANGE PASSWORD FORM new_password --- ", new_password)
    print("VALIDATE.PY FILE : CHANGE PASSWORD FORM confirm_password --- ", confirm_password)

    password_regex = re.compile(r'(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+!=])[a-zA-Z0-9@#$%^&+!=]{8,20}')

    if old_password is None:
        # self._errors['feedback_message'] = self.error_class(['3 characters and more is required for this field'])
        print("VALIDATE.PY FILE : CHANGE PASSWORD FORM OLD_PASSWORD VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please Enter valid old password")

    if new_password is None or not re.fullmatch(password_regex, new_password):
        # self._errors['feedback_message'] = self.error_class(['3 characters and more is required for this field'])
        print("VALIDATE.PY FILE : CHANGE PASSWORD FORM NEW_PASSWORD VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please Enter valid new password")

    if confirm_password is None or not re.fullmatch(password_regex, confirm_password):
        # self._errors['feedback_message'] = self.error_class(['3 characters and more is required for this field'])
        print("VALIDATE.PY FILE : CHANGE PASSWORD FORM CONFIRM_PASSWORD VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please Enter valid confirm password")

    if new_password != confirm_password:
        print(
            "VALIDATE.PY FILE : CHANGE PASSWORD FORM NEW_PASSWORD AND CONFIRM_PASSWORD VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Confirm Password must be same as New Password")

    if new_password == old_password == confirm_password:
        print(
            "VALIDATE.PY FILE : CHANGE PASSWORD FORM OLD_PASSWORD AND CONFIRM_PASSWORD VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("New Password can't be same as old password")

    else:
        print("VALIDATE.PY FILE : CHANGE PASSWORD FORM VALIDATION PASSED : RETURNING CLEAN DATA  ")
        return self.cleaned_data
    

    
# FORGOT PASSWORD FORM VALIDATION
def validate_forgot_password_form(self):
    print("VALIDATE.PY FILE: in validate_forgot_password_form function")
    email = self.cleaned_data.get('email')
    captcha_hidden = self.cleaned_data.get('captcha_hidden')
    captcha_input = self.cleaned_data.get('captcha_input')
    
    print("VALIDATE.PY FILE : FORGOT PASSWORD FORM EMAIL --- ", email)
    print("VALIDATE.PY FILE : FORGOT PASSWORD FORM EMAIL --- ", captcha_hidden)
    print("VALIDATE.PY FILE : FORGOT PASSWORD FORM EMAIL --- ", captcha_input)

    email_regex = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')

    if email is None or not re.fullmatch(email_regex, email):
        # self._errors['feedback_user_name'] = self.error_class(['3 characters and more is required for this field'])
        print("VALIDATE.PY FILE : FORGOT PASSWORD FORM EMAIL VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Invalid Email Address")

    if len(email) > 60:
        print("VALIDATE.PY FILE : FORGOT PASSWORD FORM EMAIL VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("The maximum total length of a email is 60 characters.")
    
    if captcha_input is None:
        print("VALIDATE.PY FILE : LOGIN FORM captcha_input VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please Enter Captcha")
    
    if len(captcha_input) > 5:
        print("VALIDATE.PY FILE : LOGIN FORM captcha_input VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Captcha value must be of 5 charatcters only")
    
    if not check_password(captcha_input,captcha_hidden):
        print("VALIDATE.PY FILE : LOGIN FORM captcha_hidden VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Invalid Captcha")
    
    print("VALIDATE.PY FILE : FORGOT PASSWORD FORM VALIDATION PASSED : RETURNING CLEAN DATA  ")
    return self.cleaned_data


# PASSWORD CREATION FORM VALIDATION
def validate_password_creation_form(self):
    print("VALIDATE.PY FILE: in validate_password_creation_form function")
    password = self.cleaned_data.get('password')
    confirm_password = self.cleaned_data.get('confirm_password')

    print("VALIDATE.PY FILE : PASSWORD CREATION FORM password --- ", password)
    print("VALIDATE.PY FILE : PASSWORD CREATION FORM confirm_password --- ", confirm_password)

    password_regex = re.compile(r'(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$])[a-zA-Z0-9@#$*&]{8,20}')

    if password is None or not re.fullmatch(password_regex, password):
        # self._errors['feedback_message'] = self.error_class(['3 characters and more is required for this field'])
        print("VALIDATE.PY FILE : PASSWORD CREATION FORM PASSWORD VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please Enter valid password")

    if confirm_password is None or not re.fullmatch(password_regex, confirm_password):
        # self._errors['feedback_message'] = self.error_class(['3 characters and more is required for this field'])
        print("VALIDATE.PY FILE : PASSWORD CREATION FORM CONFIRM_PASSWORD VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please Enter valid confirm password")

    if password != confirm_password:
        print("VALIDATE.PY FILE : CHANGE PASSWORD FORM PASSWORD AND CONFIRM_PASSWORD VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Confirm Password must be same as New Password")

    else:
        print("VALIDATE.PY FILE : PASSWORD CREATION FORM VALIDATION PASSED : RETURNING CLEAN DATA  ")
        return self.cleaned_data



def validate_user_profile_form(self):
    print("User Profile Validation ")
    UserProfile_name = self.cleaned_data.get('UserProfile_name')
    UserProfile_designation = self.cleaned_data.get('UserProfile_designation')
    UserProfile_organization = self.cleaned_data.get('UserProfile_organization')
    UserProfile_Bio = self.cleaned_data.get('UserProfile_Bio')
    UserProfile_organization_logo = self.cleaned_data.get('UserProfile_organization_logo')
    
    print("User Profile Validation ", UserProfile_organization_logo)
    
    
    name_regex = re.compile(r'^[A-Za-z ]{2,100}$')
    regex = "^[0-9]*[a-zA-Z]+[a-zA-Z0-9 \r\n&()\-',./]*$"
    allowed_extensions = ['jpg', 'jpeg', 'png']
    
    if UserProfile_name is None:
        raise forms.ValidationError("Full Name is required")
    elif len(UserProfile_name) < 2 or len(UserProfile_name) > 100:
        raise forms.ValidationError("Length of Name should be between 2 and 100 characters")
    elif (True):
        if not re.fullmatch(name_regex, UserProfile_name):
            raise forms.ValidationError(
                "Please enter a valid name consisting of uppercase letters (A-Z), lowercase letters (a-z), and spaces only.")
            
    if UserProfile_designation is None:
        raise forms.ValidationError("Designation is required")
    elif len(UserProfile_designation) < 2 or len(UserProfile_designation) > 50:
        raise forms.ValidationError("Length of Designation should be between 2 and 100 characters")
    elif (True):
        if not re.fullmatch(regex, UserProfile_designation):
            raise forms.ValidationError("Invalid Designation format. Please enter a valid Designation.")
        
    if UserProfile_organization is None:
        raise forms.ValidationError("Organization Name is required")
    elif len(UserProfile_organization) < 2 or len(UserProfile_organization) > 50:
        raise forms.ValidationError("Length of Organization Name should be between 2 and 100 characters")
    elif (True):
        if not re.fullmatch(regex, UserProfile_organization):
            raise forms.ValidationError("Invalid Organization Name format. Please enter a valid Organization Name.")
        
    if UserProfile_Bio is None:
        raise forms.ValidationError("Profile Bio is required")
    elif len(UserProfile_Bio) < 2 or len(UserProfile_Bio) > 50:
        raise forms.ValidationError("Length of Profile Bio should be between 2 and 100 characters")
    elif (True):
        if not re.fullmatch(regex, UserProfile_Bio):
            raise forms.ValidationError("Invalid Profile Bio format. Please enter a valid Profile Bio.")
        
    
    if UserProfile_organization_logo is None:
        # raise forms.ValidationError("Profile Image is required")
        pass
    else:
        file_extension = UserProfile_organization_logo.name.lower().split('.')[-1]
        print("file_extension: ", file_extension)
        if not file_extension in allowed_extensions:
            raise forms.ValidationError("Only JPG, JPEG, and PNG files are allowed.")

        # Define the maximum file size (in bytes)
        max_size = 5 * 1024 * 1024  # 5 MB
        # Check if the file size exceeds the maximum size
        if UserProfile_organization_logo.size > max_size:
            raise ValidationError("The file size should not exceed 5 MB.")
        
    