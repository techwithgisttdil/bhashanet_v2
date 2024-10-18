from django import forms
from .models import *
from .validate import *
from django.utils.text import slugify

class TopicForm(forms.ModelForm):
    topic_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'topicName', 'placeholder': 'Enter Topic/Query To Discuss: ', 'name': 'topic_name'}))
    
    topic_categories = forms.ModelChoiceField(queryset=TopicCategory.objects.filter(),empty_label="Select Topic category", widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'solutionCategory', 'autocomplete': 'off', 'name': 'topic_category'}))
    
    class Meta:
        model = Topic
        fields = ['topic_name', 'topic_categories']
        
    def clean(self):
        super(TopicForm, self).clean()
        validate_topic_form(self)
