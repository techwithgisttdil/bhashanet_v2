import json
from time import sleep
import pandas as pd
from bhashanet_v2 import settings
from bhashanet_v2.logger import *
import requests
from requests.exceptions import RequestException
from .models import * 
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, FieldError, ValidationError
from django.db import DatabaseError
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
from django.core.mail import send_mail
# from django.conf import settings
from bhashanet_v2.settings import *
from django.core.mail import EmailMessage
#############################################################################

def update_status(instance):
    logs(f"Checking and Updating Parameters for IDN Domain in instance {instance}")
    
    # Fetching URL of the Instance
    unicode_url = instance.IDN_domain
    
    # Deserialize the JSON string to a dictionary
    current_remark = json.loads(instance.Remark)
    logs(f"current Remark in dictionary format is {current_remark}")
    
    # Domain Operation Starts Here 
    try:
        # Try making a HEAD request
        response = requests.head(unicode_url, timeout=5,verify=False)
        logs(f"Response Code For IDN Domain {unicode_url} by HEAD Method is {response.status_code}")
        if response.status_code == 200:
            logs(f"HEAD Method -- Website is up and running.")
            instance.idn_domain_running_status = 'True'
            current_remark["Domain"] = "Success"
        else:
            # If HEAD request fails, fall back to GET request
            response = requests.get(unicode_url, timeout=5, verify=False)
            logs(f"Response Code For IDN Domain {unicode_url} by GET Method is {response.status_code}")
            if response.status_code == 200:
                logs(f"GET Method -- Website is up and running.")
                instance.idn_domain_running_status = 'True'
                current_remark["Domain"] = "Success"
            else:
                logs(f"GET Method -- Website is not up and running.")
                instance.idn_domain_running_status = 'False'
                current_remark["Domain"] = "Error"
    except requests.exceptions.Timeout as e:
        logs(f"Exception Timeout Occurred: {e}")
        instance.idn_domain_running_status = 'False'
        current_remark["Domain"] = "Timeout Error"
    except requests.exceptions.ConnectionError as e:
        logs(f"Exception Connection error Occurred: {e}")
        instance.idn_domain_running_status = 'False'
        current_remark["Domain"] = "Connection Error"
    except requests.exceptions.HTTPError as e:
        logs(f"Exception HTTP error Occurred: {e}")
        instance.idn_domain_running_status = 'False'
        current_remark["Domain"] = "HTTP Error"
    except requests.exceptions.TooManyRedirects as e:
        logs(f"Exception Too many redirects Occurred: {e}")
        instance.idn_domain_running_status = 'False'
        current_remark["Domain"] = "TooManyRedirects Error"
    except requests.exceptions.RequestException as e:
        logs(f"Exception Any Other Request Occurred: {e}")
        instance.idn_domain_running_status = 'False'
        current_remark["Domain"] = "Unknown Error"
    logs(f"Current Remark After Domain operation is {current_remark}")
    
    # Domain Operation Ends Here 
    
    # SSL Operation Starts From Here  
    
    try:
        response = requests.get(unicode_url, verify=True)
        if response.status_code == 200:
            # Check if the URL uses HTTPS
            if response.url.startswith('https://'):
                logs(f"helper.py file --> IDN Domain {unicode_url} running on SSL")
                instance.ssl_configuration_status = 'True'
                current_remark["SSL"] = 'Valid'
                logs(f"SSL has been set to Valid in  {current_remark}")
            else:
                logs(f"IDN Domain {unicode_url} Not running on SSL")
                instance.ssl_configuration_status = 'False'
                current_remark["SSL"] = "SSL Error"
                logs(f"SSL Error has been set  {current_remark}")
        else:
            logs(f"IDN Domain {unicode_url} Not running on SSL Reponse code is not 200")
            instance.ssl_configuration_status = 'False'
            current_remark["SSL"] = "SSL Error Not 200"
            logs(f"SSL Error Not 200 has been set  {current_remark}")
    except requests.exceptions.RequestException as e:
        logs("helper.py file --> SSL running Exception: " + str(e))
        logs(f"IDN Domain {unicode_url} Exception for SSL")
        instance.ssl_configuration_status = 'False'
        current_remark["SSL"] = "SSL Exception"
        logs(f"SSL Exception has been set  {current_remark}")
    
    logs(f"Current Remark After SSL operation is {current_remark}")
    
    # SSL Operation Ends Here 
        
    # Language Content Operation Starts From Here  
    
    try:
        if unicode_url.startswith('https://'):
            verify_ssl = True
        else:
            verify_ssl = False
        
        logs(f"unicode url and and verify ssl value are ---{unicode_url} -- {verify_ssl}")
        response = requests.get(unicode_url, verify=False)
        
        logs(f"Response Code is {response}")
        if response.status_code == 200:
            parsed_html_content = BeautifulSoup(response.content, 'html.parser')
            parsed_text_content = parsed_html_content.get_text()
           
            # Creating File for Home Page Content
            try: 
                create_file(parsed_text_content, unicode_url)
                logs(f"File created For Content Successfully")
            except Exception as e:
                logs(f"File Not created For Content {e}")
            try:
                service_url = 'http://gist-nlp-cip:8080/languageIdentify'
                headers = {'User-Agent': 'Mozilla/5.0'}  # Example of headers
                home_page_data = {"ip_text": parsed_text_content}
                language_service_response = requests.post(service_url, headers=headers, json=home_page_data)
                lang_received = json.loads(language_service_response.text)['Output']
                logs(f"Language Service API is working and response has been received as {lang_received} ")
                
                if lang_received == 'latin':
                    instance.content_language = 'English'
                    current_remark["Content"] = 'Success'
                else:
                    instance.content_language = lang_received.capitalize()
                    current_remark["Content"] = 'Success'

            except requests.ConnectionError as e:
                instance.content_language = 'False'
                current_remark["Content"] = 'Language Service API Error'
        else:
            instance.content_language = 'False'
            current_remark["Content"] = "Connection Error"
            logs(f"URL Not accessible. Response Code is {response.status_code}")    
    except requests.exceptions.Timeout as e:
        logs(f"Exception Timeout Occurred: {e}")
        instance.content_language = 'False'
        current_remark["Content"] = "Timeout Error"
    except requests.exceptions.ConnectionError as e:
        logs(f"Exception Connection error Occurred: {e}")
        instance.content_language = 'False'
        current_remark["Content"] = "Connection Error"
    except requests.exceptions.HTTPError as e:
        logs(f"Exception HTTP error  Occurred: {e}")
        instance.content_language = 'False'
        current_remark["Content"] = "HTTP Error"
    except requests.exceptions.TooManyRedirects as e:
        logs(f"Exception Too many redirects Occurred: {e}")
        instance.content_language = 'False'
        current_remark["Content"] = "TooManyRedirects Error"
    except requests.exceptions.RequestException as e:
        logs(f"Exception Any Other Request Occurred: {e}")
        instance.content_language = 'False'
        current_remark["Content"] = "Unknown Error"

    logs(f"Current Remark After Content Langauge operation is {current_remark}")
       
    # Language Content Operation Ends Here 
    
    # Serialize the dictionary to a JSON string
    updated_remark = json.dumps(current_remark)
    logs(f"--> Updated Remark in dictionary format is {updated_remark}")
    # Assign the updated string back to the Remark field
    instance.Remark = updated_remark
    logs(f"--> Remark Has been updated for instance as {instance.Remark}")
    # Save the instance
    instance.save()
     

#############################################################################

def create_file(content, filename):
    logs(f"--->File is being created for content to be written")
    
    # Encode the filename using urllib.parse.quote() to handle non-ASCII characters
    filename = filename.replace("http://", "").replace("https://", "")
    filename = str(filename) 
    logs(f"--> file name is renamed to doman name without protocol {filename}")
    
    # Remove excessive spaces but preserve newlines
    cleaned_lines = []
    for line in content.splitlines():
         if line.strip():
            cleaned_line = ' '.join(line.split())
            cleaned_lines.append(cleaned_line)

    # Join the cleaned lines with newline characters
    cleaned_content = '\n'.join(cleaned_lines)
    
    # Construct the full path of the file in the media directory
    media_path = os.path.join(settings.MEDIA_ROOT, filename)
    # Ensure the directory structure exists if not it will create 
    os.makedirs(os.path.dirname(media_path), exist_ok=True)
    # Open the file in write mode (creates a new file if it doesn't exist)
    logs(f"--> MEDIA Path is {media_path}")
    
    # Writing content in Files in that media folder with domain name as filename 
    with open(media_path, "w",encoding="utf-8") as file:
        # Write cleaned content into the file
        file.write(cleaned_content)
        logs(f"File Created Successfully with content written")
        
#############################################################################

def Process_Excel_Receipient_list(email_receipient_list):
    logs(f"Function Process_Excel_Receipient_list called ")
    column_name = 'USER_EMAILS_IDS'
    try:
        # Read the Excel file with no header
        df = pd.read_excel(email_receipient_list, header=None, names=[column_name])
        
        # Extract the specified column into a list, starting from the second row
        receipient = df.iloc[1:, 0].tolist()
        
        # Remove NaN values from the list
        receipient = [email for email in receipient if not pd.isna(email)]
        
        logs("helper.py file --> Excel processed successfully, and a list of recipients is being returned")
        return receipient
    except FileNotFoundError:
        logs("helper.py file --> Excel File not found. Please verify the file path.")
        return []
    except Exception as e:
        logs(f"An error occurred: {str(e)}")
        return []

#############################################################################

def Process_Email_Sending(user_email_subject, user_email_message, recipients, email_attatchments):
    logs("helper.py file --> Function Process_Email_Sending called")
    Email_Count = 0
    email_sent_counter = 0
    from_email = settings.EMAIL_HOST_USER
    email_pause_threshold = 5
    logs(f"Sending Email From Email ID {from_email}")
    # if email_attachment_file3==None or not email_attachment_file3:
    #     logs(f"User did not upload attachement 3 ")
     # Retrieve the instance you want to update
    bulk_email_instance = BulkEmail.objects.get(email_subject=user_email_subject)
    
    try:
        logs(f"Inside try")
        for recipient_email in recipients:
            logs(f"Sending Email to {recipient_email}")
            email = EmailMessage(user_email_subject, user_email_message, from_email, [recipient_email])

            # Set content type to HTML
            email.content_subtype = "html"
            
            # Attach the provided file
            for attachment in email_attatchments:
                logs(f"attachment is --  {attachment}")
                mail_attachment = os.path.join(settings.MEDIA_ROOT, str(attachment))
                email.attach_file(mail_attachment)

            email.send()
            Email_Count += 1
            email_sent_counter+=1
            # Update the field value
            bulk_email_instance.email_status = "In Process"
            bulk_email_instance.emails_sent_count = Email_Count
            # Save the instance to apply the changes
            bulk_email_instance.save()
            if email_sent_counter == email_pause_threshold:
                logs(f"SLEEPING FOR 5 SECONDS")
                sleep(email_pause_threshold)
                email_sent_counter = 0
            logs(f"Email sent successfully to {recipient_email}")
        logs(f"Total Emails Sent: {Email_Count}")
        bulk_email_instance.email_status = "All Mails Sent"
        bulk_email_instance.save()
        return True
    except Exception as e:
        logs(f"An error occurred while sending emails: {str(e)}")
        return False       
   
############################################################################# 
    