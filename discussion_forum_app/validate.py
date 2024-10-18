from django.core.exceptions import ValidationError
from django import forms
from .utils import *


# BELOW REGEX IS BEING USED FOR TITLE/HEADING/SUBHEADING VALIDATIONS
Title_regex = "^[0-9]*[a-zA-Z]+[\sa-zA-Z0-9!\-,.()?]*$"


# # Validate Search Term 
def validate_search_term(search_term):
  return regex_check(search_term, Title_regex)


# # Validate Topic form
def validate_topic_form(self):
    print("VALIDATE.PY FILE : IN VALIDATE_UTILITY FUNCTION ")
    topic_name = self.cleaned_data.get('topic_name')
    topic_categories = self.cleaned_data.get('topic_categories')
    
    print("VALIDATE.Py :: Topic Name : ", topic_name)
    print("VALIDATE.Py :: Topic categories : ", topic_categories)
    
    if topic_name is None or (len(topic_name) < 10 or len(topic_name) > 250):
        print("VALIDATE.PY FILE : Topic Name VALIDATION :: title length failed")
        raise forms.ValidationError("Length of Topic Name must be between 10-250 characters")
    
    if not regex_check(topic_name, Title_regex):
        print("VALIDATE.PY FILE : Topic Name VALIDATION FAILED ERROR RAISED :: Title invalid")
        raise forms.ValidationError("Invalid Field Topic Name")
    
    if topic_categories is None:
        print("VALIDATE.PY FILE : Topic Categories VALIDATION FAILED ERROR RAISED :: Title invalid")
        raise forms.ValidationError("Please Select  Topic Related Category")