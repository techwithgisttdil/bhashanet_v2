
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



def generate_otp_for_user_registration(email,OTP_For_UserRegistration):
    print("Inside generate_otp_for_user_registration")
    fixed_digits = 6 
    otp_value = random.randrange(111111, 999999, fixed_digits)
    otp_already_exists = OTP_For_UserRegistration.objects.filter(OTP_Email=email)
    
    if otp_already_exists:
        if otp_already_exists[0].OTP_Entered_Count < 10:
            # check time difference between current otp and last otp
              
                #  print("OTP count for this email is less than max count")
                otp_already_exists[0].OTP_Value = otp_value
                otp_already_exists[0].OTP_Entered_Count+=1
                otp_already_exists[0].save()
                
                data={'status': 'success', 'message': "OTP generated"}
                
        else:
            print("OTP count limit exceeded")
            expiry_time = otp_already_exists[0].OTP_Created_Date + timedelta(minutes=5) ## timedelta is of 2 hours
            current_time = timezone.now()
            print("OTP count limit expiry_time",expiry_time,current_time,current_time-expiry_time)
            if expiry_time < current_time:
                #  print("OTP count limit exceeded and offset time still not reached")
                data={'status': 'error', 'message': "OTP generate limit exceeded"} 
            else:
                otp_already_exists[0].OTP_Value = otp_value
                otp_already_exists[0].OTP_Entered_Count = 1
                otp_already_exists[0].save()
                data={'status': 'success', 'message': "OTP generated"}
    else:
        #  print("email not exists")
        otp_obj = OTP_For_UserRegistration.objects.create(
            OTP_Email = email,
            OTP_Value = otp_value,
            OTP_Entered_Count = 1
        )
        otp_obj.save()
        data={'status': 'success', 'message': "OTP generated"}
        
        
    # send mail to email address
    print("opt valueeeee",otp_value,"===========================",env('SERVER_EMAIL'))
    RecipentMessage = "OTP For User Registration On Bhashanet Portal is " + str(otp_value); 
    try:
        email_sent_status = send_mail("OTP For User Registration On Bhashanet Portal", RecipentMessage, 'pshweta@cdac.in', [email])
        print("email status : ", email_sent_status)
        data['Email_status']="success"
    except:
        print("error while sending email")
        data['Email_status']="error"
        data['message']="Error while sending email"

    return data




def validate_otp_for_user_registration(email, otp_value,OTP_For_UserRegistration):
    print("Inside validate_otp_for_user_registration")
    # check email exists
    otp_obj = OTP_For_UserRegistration.objects.filter(OTP_Email=email)
    print("otp obj",otp_obj)
    if otp_obj:
        otp = otp_obj[0].OTP_Value
        otp_status = otp_obj[0].OTP_Status
        otp_generation_date = otp_obj[0].OTP_Created_Date
        
        # check otp is expired
        current_time = timezone.now()
        expiry_time = otp_generation_date + timedelta(minutes=5) ## otp expiry time is 5 minutes
        print("otp expiry_time",expiry_time - current_time)
        if expiry_time > current_time:
            print("otp_value",otp_value,otp)
            if str(otp_value) == str(otp):
                print("OTP otp_status",otp_status)
                if otp_status == True:
                    #  print("OTP expired: Already verified")
                    return False
                else:
                    print("OTP verified")
                    return True
            else:
                #  print("wrong OTP")
                return False
        else:
            #  print("OTP expired")
            return False 