# Image size validation
from django.core.exceptions import ValidationError
from django.utils.html import escape
from django import forms
from email_validator import validate_email, EmailNotValidError
import re
from datetime import *
import idna
from django.contrib.auth.hashers import check_password
from .utility import validateFile
import requests
from django.http import JsonResponse

def validate_image(fieldfile_obj):
    if fieldfile_obj:
        print("Inside fieldObj")
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("File size exceeds %sMB" % str(megabyte_limit))


def validate_feedbackform(self):
    print("VALIDATE.PY FILE: in validate_feedbackform function")
    Feedback_FirstName = self.data.get('Feedback_FirstName')
    Feedback_Related_To = self.data.get('Feedback_Related_To')
    Feedback_Message = self.data.get('Feedback_Message').strip()
    Feedback_Email = self.data.get('Feedback_Email').strip()
    
    captcha_hidden = self.cleaned_data.get('captcha_hidden')
    captcha_input = self.cleaned_data.get('captcha_input')
    
    print("VALIDATE.PY FILE : LOGIN FORM RELATED TO --- ", captcha_hidden)
    print("VALIDATE.PY FILE : LOGIN FORM RELATED TO --- ", captcha_input)

    print("VALIDATE.PY FILE : FEEDBACK FORM NAME --- ", Feedback_FirstName)
    print("VALIDATE.PY FILE : FEEDBACK FORM RELATED TO --- ", Feedback_Related_To)
    print("VALIDATE.PY FILE : FEEDBACK FORM MESSAGE --- ", Feedback_Message)
    print("VALIDATE.PY FILE : FEEDBACK FORM EMAIL --- ", Feedback_Email)
    
    email_regex = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
    name_regex = re.compile(r'^.{1,50}[^<>()+@%\-=\_#[\]{};“,.”’:$%]$')
    desc_regex = re.compile(r'^.{1,50}[^<>()+@%\-=\_#[\]{};“,.”’:$%]$')
    #message_regex = re.compile(r'^.|\n{5,1000}[^()<>+%\-=\[\]{};“”’:$%]$')
    #reg = "^[0-9]*[a-zA-Z]+[a-zA-Z0-9! \r\n&()+@%\-=\[\]{};“”'’:\\|,.<>/?]*$"
    message_regex_1 = re.compile(desc_regex)
    

    
    if Feedback_FirstName is None or len(Feedback_FirstName) < 3:
        print("VALIDATE.PY FILE : FEEDBACK FORM NAME VALIDATION FAILED ERROR RAISED BECAUSE OF LENGTH ISSUE ")
        raise forms.ValidationError("Name should have 3 or more character ")
    else:
        validate_name_regex = re.search(name_regex, Feedback_FirstName)
        if validate_name_regex == None:
            print("VALIDATE.PY FILE : FEEDBACK FORM NAME VALIDATION FAILED ERROR RAISED BECAUSE OF REGEX FAILED ")
            raise forms.ValidationError('Please enter valid name')

    if Feedback_Email is "" :
        raise forms.ValidationError("Please Enter email address")
    # if Feedback_Email is not None:
    #     if validate_email(Feedback_Email):
    #             print("valid")
    #     else :
    #         raise EmailNotValidError("Email is not valid ")
        
   
    if Feedback_Message is None or len(Feedback_Message) > 501 or len(Feedback_Message) < 3:
        print("VALIDATE.PY FILE : FEEDBACK FORM MESSAGE VALIDATION FAILED ERROR RAISED BECAUSE OF LENGTH ISSUE")
        raise forms.ValidationError("Characters should be atleast 3 or more in Message Field ")
    else:
        # reg = "^[0-9]*[a-zA-Z]+[a-zA-Z0-9! \r\n&()+@%\-=\[\]{};“”'’:\\|,.<>/?]*$"
        # pat = re.compile(reg)
        validation_result_with_regex = re.search(message_regex_1, Feedback_Message)
        print("inside validate py file checking validation for feedback message ", validation_result_with_regex)
        if validation_result_with_regex == None:
            print("VALIDATE.PY FILE : FEEDBACK FORM MESSAGE VALIDATION FAILED ERROR RAISED BECAUSE OF REGEX FAILED ")
            raise forms.ValidationError('Special symbols like- # $ ~ \ are not allowed in description field')

    if Feedback_Related_To is None:
        print("VALIDATE.PY FILE : FEEDBACK FORM FEEDBACK RELATED TO VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please Select Feedback category")
    
    if captcha_input is None:
        print("VALIDATE.PY FILE : LOGIN FORM captcha_input VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please Enter Captcha")
    
    if len(captcha_input) > 5:
        print("VALIDATE.PY FILE : LOGIN FORM captcha_input VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Captcha value must be of 5 Charatcters only")
    print("captcha validation ", check_password(captcha_input,captcha_hidden))
    if not check_password(captcha_input,captcha_hidden):
        print("VALIDATE.PY FILE : LOGIN FORM captcha_hidden VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Invalid Captcha")

    else:
        print("VALIDATE.PY FILE : FEEDBACK FORM VALIDATION PASSEDD : RETURNING CLEAN DATA  ")
        return self.cleaned_data


def validate_domain(self):
    print("Indise validate function")
    Domain_Name = self.data.get('Domain_Name')
    print("Domain Name from form : " + str(Domain_Name))
 
    # The domain part of the email address, after IDNA (ASCII) encoding,
    # must also satisfy the requirements of RFC 952/RFC 1123 which restrict
    # the allowed characters of hostnames further. The hyphen cannot be at
    # the beginning or end of a *dot-atom component* of a hostname either.
    ATEXT_HOSTNAME = r'(?:(?:[a-zA-Z0-9][a-zA-Z0-9\-]*)?[a-zA-Z0-9])'
    
    if Domain_Name == "" or Domain_Name == None:
        print("form valid")
        raise forms.ValidationError('Please enter domain name')
    else:
            domain_test = idna.uts46_remap(Domain_Name, std3_rules=False, transitional=False)
            if domain_test:
                pass
            else:
                raise ValidationError("The domain name "  + Domain_Name + "contains invalid characters." )
            
            if Domain_Name.endswith("."):
                raise ValidationError("An domain cannot end with a period.")
            if Domain_Name.startswith("."):
                raise ValidationError("An domain cannot have a period ")
            if ".." in Domain_Name:
                raise ValidationError("An domain cannot have two periods in a row.")
            
            domain_smtp = idna.encode(Domain_Name,uts46=False).decode("ascii")
            print("Domain name : "+ domain_smtp)
            if domain_smtp:
                pass
            else:
                raise ValidationError("The domain name "  + Domain_Name + " contains invalid characters ")
            

            if len(Domain_Name) > 255:
                raise ValidationError("The domain is too long.")
		        
            # A "dot atom text", per RFC 2822 3.2.4, but using the restricted
	        # characters allowed in a hostname (see ATEXT_HOSTNAME above).
            DOT_ATOM_TEXT = ATEXT_HOSTNAME + r'(?:\.' + ATEXT_HOSTNAME + r')*'
	  
	        # Check the regular expression. This is probably entirely redundant
	        # with idna.decode, which also checks this format.
	       
            # m = re.match(DOT_ATOM_TEXT + "$", Domain_Name)
            
            # if not m:
            #     raise ValidationError("Domain contains invalid characters")
	        
            try:
                    domain_i18n = idna.decode(domain_smtp.encode('ascii'))
                    print("Converted Domain name : " + domain_i18n)
            except:
                    raise ValidationError("The domain name " + Domain_Name +" is not valid IDNA.")
             
            if "." not in Domain_Name:
                raise ValidationError("The domain name " + Domain_Name +" is not valid. It should have a period.")
            if not re.search(r"[A-Za-z]$", domain_smtp):
	            raise ValidationError("The domain name " + Domain_Name +" is not valid. It is not within a valid top-level domain.")
 
            
                #return self.data
        
  

def validate_email(self):
    print("Indise validate function")
    Email_Address = self.data.get('Email_Address')
    # print("Domain Name from form : " + Email_Address)
    # print("VALIDATE.PY FILE : DOMAIN NAME  --- " + Email_Address)
    
    if Email_Address == "":
        print("form valid")
        raise forms.ValidationError('Please enter email address')
    
    return self.data


# PASSWORD CREATION FORM VALIDATION
def validate_IDNRequestForUserWebsitesForm(self):
    print("VALIDATE.PY FILE: in validate_IDN_request_for_user_websites_form function")
    IDN_Email = self.cleaned_data.get('IDN_Email')
    IDN_Category = self.cleaned_data.get('IDN_Category')
    IDN_English_Domain = self.cleaned_data.get('IDN_English_Domain')

    
    captcha_hidden = self.cleaned_data.get('captcha_hidden')
    captcha_input = self.cleaned_data.get('captcha_input')
    

    print("VALIDATE.PY FILE : validate_IDN_request_for_user_websites_form Email--- ", IDN_Email)
    print("VALIDATE.PY FILE : validate_IDN_request_for_user_websites_form category --- ", IDN_Category)
    print("VALIDATE.PY FILE : validate_IDN_request_for_user_websites_form category English URL --- ", IDN_English_Domain)
    
    
    print("VALIDATE.PY FILE : validate_IDN_request_for_user_websites_form FORM RELATED TO --- ", captcha_hidden)
    print("VALIDATE.PY FILE : validate_IDN_request_for_user_websites_form FORM RELATED TO --- ", captcha_input)

    
    # check email validation
    email_regex = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')

    if IDN_Email is None or not re.fullmatch(email_regex, IDN_Email):
        print("VALIDATE.PY FILE : in validate_IDN_request_for_user_websites_form FORM IDN_Email VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Invalid Email Address")

    if len(IDN_Email) > 60:
        print("VALIDATE.PY FILE : in validate_IDN_request_for_user_websites_form FORM IDN_Email VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("The maximum total length of a email is 60 characters.")
    
    # Check category is selected or not
    if IDN_Category is None:
        print("VALIDATE.PY FILE : in validate_IDN_request_for_user_websites_form FORM IDN_category VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please select the category")
    
    
    # Check ENGLISH URL validation
    english_url_regex = "^((ftp|http|https):\/\/)?(www.)?(?!.*(ftp|http|https|www.))[a-zA-Z0-9_-]+(\.[a-zA-Z-]+)+((\/)[\w#]+)*(\/\w+\?[a-zA-Z0-9_]+=\w+([a-zA-Z0-9_-]+)(&[a-zA-Z0-9_]+=\w+)*)?$"
    if IDN_English_Domain is None:
        print("VALIDATE.PY FILE : in validate_IDN_request_for_user_websites_form IDN_Englsh_URL validation failed")
        raise forms.ValidationError("Please Enter Website English domain")
    
    elif not re.fullmatch(english_url_regex, IDN_English_Domain):
        raise forms.ValidationError("Invalid Website English domain")
    
    # if not IDN_Hindi_Domain and not IDN_Marathi_Domain and not IDN_Malayalam_Domain and not IDN_Kannada_Domain and not IDN_Gujarati_Domain and not IDN_Bengali_Domain and not IDN_Urdu_Domain and not IDN_Manipuri_Domain and not IDN_Telugu_Domain and not IDN_Panjabi_Domain and not IDN_Tamil_Domain and not IDN_Konkani_Domain and not IDN_Kashmiri_Domain and not IDN_Assamese_Domain and not IDN_Sindhi_Domain and not IDN_Oriya_Domain and  not IDN_Sanskrit_Domain and not IDN_Maithili_Domain and not IDN_Santali_Domain and not IDN_Bodo_Domain and not IDN_Dogri_Domain and not IDN_Nepali_Domain:
    #     raise forms.ValidationError("Atleast one IDN URL field is required")
    # check validation for other IDN domain URLs
    # language_code = language_detection(IDN_Hindi_Domain)
    # print("Language Code : ", language_code)
    # clean_URL()
    
    if captcha_input is None:
        print("VALIDATE.PY FILE : LOGIN FORM captcha_input VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Please Enter Captcha")
    
    if len(captcha_input) > 5:
        print("VALIDATE.PY FILE : LOGIN FORM captcha_input VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Captcha value must be of 5 charatcters only")
    
    if not check_password(captcha_input,captcha_hidden):
        print("VALIDATE.PY FILE : LOGIN FORM captcha_hidden VALIDATION FAILED ERROR RAISED ")
        raise forms.ValidationError("Invalid Captcha")


# PASSWORD CREATION FORM VALIDATION
def validate_IDNRequestForUserWebsitesAJAXForm(org_name, email, category, IDN_English_Domain, captcha_value, captcha_hidden, assistance, assistLang, remark):
    print("In Validate.py : validate_IDNRequestForUserWebsitesAJAXForm function")
    print("organisation name : ", org_name)
    print("Email : ", email)
    print("Category : ", category)
    print("IDN_English_Domain : ", IDN_English_Domain)
    print("assistance with IDN enablement : ", assistance)
    print("assist_lang : ", assistLang)
    print("remark : ", remark)
    print("captcha_value : ", captcha_value)
    print("captcha_hidden : ", captcha_hidden)
    
    
    # check email validation
    email_regex = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
    org_name_regex = "^[a-zA-Z]+[a-zA-Z ]*$"
    languages_regex = "^[a-zA-Z]+[a-zA-Z ,]*$"
    remark_regex = "^[a-zA-Z]+[a-zA-Z0-9 ,\-_'@';:\.\[\]()]*$"
    
    if org_name == "":
        print("VALIDATE.PY FILE : PROFILE ORGANIZATION NAME VALIDATION FAILED ERROR RAISED ")
        return {'status': 'error', 'field_name':'org_name', 'message': 'Please enter name'}
    elif len(org_name) < 2:
        print("VALIDATE.PY FILE : PROFILE ORGANIZATION NAME VALIDATION FAILED ERROR RAISED ")
        # raise forms.ValidationError("Organization name should have 2 or more character")
        return {'status': 'error', 'field_name':'org_name', 'message': 'Name should have 2 or more character'}
    else:
        pattern = re.compile(org_name_regex)
        valid_organization_name = re.search(pattern, org_name)
        print(valid_organization_name)
        if valid_organization_name is None:
            # raise forms.ValidationError("Please enter valid organization name")
            return {'status': 'error', 'field_name':'org_name', 'message': 'Name field must contain only alphabets and space'}

    if email == "" or not re.fullmatch(email_regex, email):
        print("VALIDATE.PY FILE : in validate_IDN_request_for_user_websites_form FORM IDN_Email VALIDATION FAILED ERROR RAISED ")
        # raise forms.ValidationError("Invalid Email Address")
        return {'status': 'error', 'field_name':'email', 'message': 'Invalid Email Address'}

    if len(email) > 60:
        print("VALIDATE.PY FILE : in validate_IDN_request_for_user_websites_form FORM IDN_Email VALIDATION FAILED ERROR RAISED ")
        # raise forms.ValidationError("The maximum total length of a email is 60 characters.")
        return {'status': 'error', 'field_name':'email', 'message': 'The maximum total length of a email is 60 characters.'}
    
    # Check category is selected or not
    if category == '':
        print("VALIDATE.PY FILE : in validate_IDN_request_for_user_websites_form FORM IDN_category VALIDATION FAILED ERROR RAISED ")
        # raise forms.ValidationError("Please select the category")
        return {'status': 'error', 'field_name':'category', 'message': 'Please select the category.'}
    
    
    # Check ENGLISH URL validation
    english_url_regex = "^((ftp|http|https):\/\/)?(www.)?(?!.*(ftp|http|https|www.))[a-zA-Z0-9_-]+(\.[a-zA-Z-]+)+((\/)[\w#]+)*(\/\w+\?[a-zA-Z0-9_]+=\w+([a-zA-Z0-9_-]+)(&[a-zA-Z0-9_]+=\w+)*)?$"
    if IDN_English_Domain == "":
        print("VALIDATE.PY FILE : in validate_IDN_request_for_user_websites_form IDN_Englsh_URL validation failed")
        # raise forms.ValidationError("Please Enter Website English domain")
        return {'status': 'error', 'field_name':'IDN_English_Domain', 'message': 'Please Enter Website English domain.'}
    
    elif not re.fullmatch(english_url_regex, IDN_English_Domain):
        # raise forms.ValidationError("Invalid Website English domain")
        return {'status': 'error', 'field_name':'IDN_English_Domain', 'message': 'Invalid Website English domain'}
    
    
    if assistance is None:
        return {'status': 'error', 'field_name':'assistLang', 'message': 'Please select YES/NO to proceed '}
    
    ## check assist language
    if assistance == 'yes':
        if assistLang == '':
            return {'status': 'error', 'field_name':'assistLang', 'message': 'Preferred language for assistance can not be empty'}
        elif len(assistLang) < 3 or len(assistLang) > 500:
            return {'status': 'error', 'field_name':'assistLang', 'message': 'Preferred language for assistance must be between 3 to 500 characters long'}
        elif not re.fullmatch(languages_regex, assistLang):
            return {'status': 'error', 'field_name':'assistLang', 'message': 'Preferred language for assistance can only contains alphabets space and comma[,]'}

        if remark == '':
            return {'status': 'error', 'field_name':'remark', 'message': 'Specific questions or requests  can not be empty'}
        elif len(remark) < 3 or len(remark) > 500:
            return {'status': 'error', 'field_name':'remark', 'message': 'Specific questions or requests  must be between 3 to 500 characters long'}
        elif not re.fullmatch(remark_regex, remark):
            return {'status': 'error', 'field_name':'remark', 'message': 'Specific questions or requests is invalid'}

    if captcha_value == '':
        print("VALIDATE.PY FILE : LOGIN FORM captcha_input VALIDATION FAILED ERROR RAISED ")
        # raise forms.ValidationError("Please Enter Captcha")
        return {'status': 'error', 'field_name':'captcha_value', 'message': 'Please Enter Captcha'}
    
    if len(captcha_value) > 5:
        print("VALIDATE.PY FILE : LOGIN FORM captcha_input VALIDATION FAILED ERROR RAISED ")
        # raise forms.ValidationError("Captcha value must be of 5 charatcters only")
        return {'status': 'error', 'field_name':'captcha_value', 'message': 'Captcha value must be of 5 charatcters only'}
    
    if not check_password(captcha_value, captcha_hidden):
        print("VALIDATE.PY FILE : LOGIN FORM captcha_hidden VALIDATION FAILED ERROR RAISED ")
        # raise forms.ValidationError("Invalid Captcha")
        return {'status': 'error', 'field_name':'captcha_value', 'message': 'Invalid Captcha'}
    
    return {'status': 'success'}
    
def clean_URL(url):
    
    url = url.replace("http://www.","")
    url = url.replace("https://www.","")
    url = url.replace("www.","")
    url = url.replace("http://","")
    url = url.replace("https://","")
    print("url = ", url)
    
    return url

    
    
def language_detection(input_text):
    api_url  ="https://meity-auth.ulcacontrib.org/ulca/apis/v0/model/compute"
    model_id = "631736990154d6459973318e"
    
    payload = {
        "modelId": model_id,
        "task": "txt-lang-detection",
        "input": [{"source": input_text}],
        "userId": None
    }
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(api_url, json=payload,headers=headers)
        response.raise_for_status()
        
        data = response.json()
        print("Data : ", data)
        lang_code = data['output'][0]['langPrediction'][0]['langCode']
        lang_score = data['output'][0]['langPrediction'][0]['langScore']
        print("language code ; ", lang_code)
        print("language score ; ", lang_score)
        return lang_code
    except:
        print("Error from ")

    
