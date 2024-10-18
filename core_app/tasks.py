from celery import shared_task
import requests
import environ
env = environ.Env()
environ.Env.read_env()
from .models import *

@shared_task(bind=True)
def test_func(self):
    print("Example Task...")
    response = requests.post("https://registry.gov.in/getidndomaininfo_public_process.php", 
        data="region=&filterform=filterform&current_page=",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    response_data =  response.json()
    message = response_data['message']
        
    file_path = env("REGISTRY_FILE_PATH")  # Update with your desired file path
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(message + '\n')
    return message




