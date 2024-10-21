
from celery import shared_task
import requests
from .models import *
from bhashanet_v2.logger import *
from .helper import *    
import environ

env = environ.Env()
environ.Env.read_env()


@shared_task
def User_Registration_With_OTP(email):
    print("Inside celery with otp function",email)
    user = User.objects.get(username=email)
    user.delete()
    user_obj=OTP_For_UserRegistration.objects.get(OTP_Email=email)
    user_obj.delete()
  
    return "DELETED"+str(user_obj)