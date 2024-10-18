from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect
import re
import whois
import random
from django.core.mail import send_mail
import environ
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User
env = environ.Env()
environ.Env.read_env()
import smtplib
############################################################################3

# ADDED BY SANJAYB
def validateFile(file, extensions, maxSize):
    receivedFileExtension = file.name.split('.')[-1].lower()
    print("in validate file ",receivedFileExtension)
    print("File size : ", file.size)
    if file.size < maxSize:
        for extension in extensions:
            if extension.lower()==receivedFileExtension:
                return True
    else:
      raise forms.ValidationError('File Size Limit Exceeded : Max Limit - {}MB'.format(maxSize/(1024*1024)))
    return False


def regex_check(input_field, regex_pattern):
  print("REGEX PATTERN : ",regex_pattern)
  pattern = re.compile(regex_pattern)
  
  # VALIDATING STRING WITH PATTERN
  valid_input = re.fullmatch(pattern, input_field)
  print("CHECKING VALIDATION RESULT : " , valid_input)
    
  if not valid_input:
    return False
  else:
    return True 
  
## validate domain name registered or not
def is_domain_registered(domain_name):
    try:
        whois_info = whois.whois(domain_name)
        print("who is info : ", whois_info)
        # Check if the domain has creation_date, which indicates it is registered
        return bool(whois_info.creation_date)
    except whois.parser.PywhoisError as e:
        # Handle the case where the domain is not registered or WHOIS information is not available
        print(f"Error checking WHOIS for {domain_name}: {e}")
        return False
    

