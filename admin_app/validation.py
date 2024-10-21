from .forms import *
from django.core.exceptions import ValidationError
from django import forms
from bhashanet_v2.logger import *
from urllib.parse import urlparse
from .models import *
import idna
import unicodedata
import dns.resolver
import dns.exception
from .utility import *
from .utility import validate_English_Domain_Form_Category,validate_English_Domain_Form_Department,validate_English_Domain_Form_Domain_Name

#################################################  

def validate_English_Domain_Form(self):
    logs("validation starts for English Domain Form ")

    department_name  = self.cleaned_data.get('department_name')
    domain_name  = self.cleaned_data.get('domain_name')
    category  = self.cleaned_data.get('category')
    
    logs(f"Department Name is - {department_name}")
    logs(f"Category Name is - {category}")
    logs(f"Domain Name is - {domain_name}")
    
    # Validate Category 
    validate_English_Domain_Form_Category(category)
    
    # Validate Department Name
    validate_English_Domain_Form_Department(department_name)
    
    # Validate English Domain 
    validate_English_Domain_Form_Domain_Name(domain_name)
    

#################################################  

def validate_idn_dashboard_form(self):
    logs(f"file -- Self object is {self.is_new}")
    logs("validation starts for IDN Domain Form ")

    English_domain  = self.cleaned_data.get('English_domain')
    Language  = self.cleaned_data.get('Language')
    IDN_domain  = self.cleaned_data.get('IDN_domain')
    
    logs(f"English Domain selected by user is - {English_domain}")
    logs(f"Category selected by user is - {Language}")
    logs(f"IDN Domain entered by user is - {IDN_domain}")
    
    # Validate English Domain
    validate_idn_dashboard_form_English_domain(English_domain)
    
    #Validate Language
    validate_idn_dashboard_form_Language(Language)
    
    #Validate IDN Domain
    if self.is_new:
        validate_idn_dashboard_form_IDN_domain(self,IDN_domain)