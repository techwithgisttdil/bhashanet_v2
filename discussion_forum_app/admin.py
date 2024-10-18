from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(TopicCategory)
admin.site.register(Topic)
admin.site.register(TopicAnswer)
admin.site.register(AnswerReplies)
admin.site.register(AnswerUserReview)