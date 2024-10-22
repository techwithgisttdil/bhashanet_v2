
from celery import shared_task
import requests
from .models import *
from bhashanet_v2.logger import *
from .helper import *    
import environ

env = environ.Env()
environ.Env.read_env()


# CELERY SCRIPT FUNCTION TO UPDATE PARAMETERS OF DOMAIN AFTER ADDING IN RECORD

@shared_task(bind=True)
def update_domain_parameters(self,unicode_domain):
    logs(f"Checking and Updating Parameters for IDN Domain {unicode_domain}")
    # Fetch object from Database 
    instance = URL_dashboard.objects.get(IDN_domain=unicode_domain)
    update_status(instance)
    return "---- All Domain Parameters Updated ----"
    

# CELERY SCRIPT FUNCTION TO SEND BULK MAIL TO USERS
   
@shared_task(bind=True) 
def Send_Bulk_Email(self,id):
    bulk_email_instance = BulkEmail.objects.get(id=id)
    logs(f"Extracting Email Details")
     
    user_email_subject = bulk_email_instance.email_subject
    user_email_message =  bulk_email_instance.email_message
    email_receipient_list =  bulk_email_instance.email_receipient_list
    # email_attachment_file1 =  bulk_email_instance.email_attachment_file1
    # email_attachment_file2 =  bulk_email_instance.email_attachment_file2
    # email_attachment_file3 =  bulk_email_instance.email_attachment_file3
    # email_attachment_file4 =  bulk_email_instance.email_attachment_file4
    # email_attachment_file5 =  bulk_email_instance.email_attachment_file5
    email_attatchments = BulkEmailAttachments.objects.filter(bulk_email=bulk_email_instance)
    logs(f"Email Subject is {user_email_subject}")
    logs(f"Email Message is {user_email_message}")
    logs(f"Email Receipient List is {email_receipient_list}")
    logs(f"Email attachment is {email_attatchments}")
    # logs(f"Email Attachment1 File is {email_attachment_file1}")
    # logs(f"Email Attachment2 File is {email_attachment_file2}")
    # logs(f"Email Attachment3 File is {email_attachment_file3}")
    # logs(f"Email Attachment4 File is {email_attachment_file4}")
    # logs(f"Email Attachment5 File is {email_attachment_file5}")
    
    # Process Email Sending Function
    receipients = Process_Excel_Receipient_list(email_receipient_list)
    logs(f"List of all receipients is -- {receipients}")
    
    Email_sent_status = Process_Email_Sending(user_email_subject, user_email_message, receipients,email_attatchments)
    if Email_sent_status == True:
        logs(f"Email has been sent to all users")
        return "---- Email has been sent to all users  ----"
    else:
        logs(f"Email has Not been sent to all users")
        return "---- Email has Not been sent to all users  ----"


@shared_task
def User_Registration_With_OTP(email):
    print("Inside celery with otp function",email)
    user = User.objects.get(username=email)
    user.delete()
    user_obj=OTP_For_UserRegistration.objects.get(OTP_Email=email)
    user_obj.delete()
  
    return "DELETED"+str(user_obj)