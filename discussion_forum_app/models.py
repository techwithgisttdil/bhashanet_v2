from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#----------------------------------------------------------------------

class TopicCategory(models.Model):
  category_name = models.CharField(max_length=50, blank=True, null=True)
  creation_date = models.DateField(auto_now_add=True)  

  class Meta:
    verbose_name = "Topic Category"
    verbose_name_plural = "Topic Categories"

  def __str__(self):
    return self.category_name

#----------------------------------------------------------------------

class Topic(models.Model):
  topic_name = models.CharField(max_length=255,unique=True)
  topic_categories = models.ForeignKey(TopicCategory, verbose_name="Topic Categories", on_delete=models.CASCADE)  
  user_id = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
  creation_date = models.DateField(auto_now_add=True)
  topic_slug = models.SlugField(max_length=255, unique=True, blank=False, null=False)

  class Meta:
    verbose_name ="Topic"
    verbose_name_plural ="Topics"

  def __str__(self):
    return self.topic_name
  
#----------------------------------------------------------------------
#   
class TopicAnswer(models.Model):
  topic_id = models.ForeignKey(Topic, verbose_name="Topic", on_delete=models.CASCADE)
  answer = models.TextField(blank=True, null=True)
  user_id = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
  reply_date = models.DateField(auto_now_add=True)

  class Meta:
    verbose_name = "Topic Answer"
    verbose_name_plural = "Topic Answers"

  def __str__(self):
    return self.answer + " " + str(self.id)
  
#----------------------------------------------------------------------

class AnswerReplies(models.Model):
  answer_id = models.ForeignKey(TopicAnswer, verbose_name="Topic Answer", on_delete=models.CASCADE)
  reply = models.TextField(blank=True, null=True)
  user_id = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
  replied_to = models.ForeignKey('self', verbose_name="replied to", on_delete=models.CASCADE, blank=True, null=True)
  reply_date = models.DateField(auto_now_add=True)

  class Meta:
    verbose_name = "Answer Replies"
    verbose_name_plural = "Answer Replies"

  def __str__(self):
    return self.reply + " " + str(self.id)

#----------------------------------------------------------------------

class AnswerUserReview(models.Model):
  answer_id = models.ForeignKey(TopicAnswer, verbose_name="Topic Answer", on_delete=models.CASCADE)
  user_id = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
  status = models.CharField(max_length=50, choices=(('UPVOTE', 'UPVOTE'),('DOWNVOTE', 'DOWNVOTE'),('NULL', 'NULL')), blank=True, null=True)
  reply_date = models.DateField(auto_now_add=True)

  class Meta:
    verbose_name = "User Review On Answer"
    verbose_name_plural = "User Review On Answer"

  def __str__(self):
    return str(self.answer_id.answer)