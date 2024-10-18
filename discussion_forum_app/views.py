from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .validate import validate_search_term
from .forms import *
from admin_app.models import UserProfile
from django.core.mail import send_mail
import environ

env = environ.Env()
environ.Env.read_env()

################################################################################
'''
Topic List Function :: ADDED BY SHHIVAM SHARMA
==> 
'''
def topic_list(request):
  print('Topic List ')
  search_term = request.GET.get("search_term")
  page_number = request.GET.get('page')
  print("search term : ", search_term)
  
  
  
  ## if search term is not given
  if search_term == "" or search_term is None or search_term == 'None':
    print("search term not found")
    search_term=""
    all_topics = Topic.objects.all().order_by('-creation_date')
  else:
    if not validate_search_term(search_term):
      messages.error(request, 'Invalid Search Term', extra_tags='danger')
      all_topics = Topic.objects.all().order_by('-creation_date')
    else:
      all_topics = Topic.objects.filter(topic_name__icontains=search_term).order_by('-creation_date')
    
  fetched_data = []
  for topic in all_topics:
    user_obj = UserProfile.objects.get(UserProfile_user=topic.user_id)
    fetched_data.append({"topic":topic, "user_profile": user_obj})
    
  paginator = Paginator(fetched_data, 10)
  page_obj = paginator.get_page(page_number)
  
    
  return render(request, 'discussion_forum/topic_list.html', {'all_topics': page_obj, 'search_term': search_term})

'''
User Topic List Function :: ADDED BY SHHIVAM SHARMA
==> 
'''
@login_required()
def user_topic_list(request):
  search_term = request.GET.get("search_term")
  page_number = request.GET.get('page')
  print("search term : ", search_term)
  
  ## if search term is not given
  if search_term == "" or search_term is None or search_term == 'None':
    print("search term not found")
    search_term=""
    all_topics = Topic.objects.filter(user_id=request.user).order_by('-creation_date')
  else:
    if not validate_search_term(search_term):
      messages.error(request, 'Invalid Search Term', extra_tags='danger')
      all_topics = Topic.objects.filter(user_id=request.user).order_by('-creation_date')
    else:
      all_topics = Topic.objects.filter(user_id=request.user, topic_name__icontains=search_term).order_by('-creation_date')
      
  if len(all_topics) > 0:
    user_profile_obj = UserProfile.objects.filter(UserProfile_user=request.user)[0]
  else:
    user_profile_obj = []
    
  paginator = Paginator(all_topics, 10)
  page_obj = paginator.get_page(page_number)
  
    
  return render(request, 'discussion_forum/user_topic_list.html', {'all_topics': page_obj, 'search_term': search_term, "user_profile": user_profile_obj})


################################################################################
'''
Topic Add Function :: ADDED BY SHHIVAM SHARMA
==> 
'''
@login_required()
def add_topic(request):
  ## check User Profile
  user_profile_obj = UserProfile.objects.filter(UserProfile_user=request.user)
  if not user_profile_obj:
    messages.success(request, "** To add a discussion topic, Please update your profile details first. **", extra_tags="warning")
    return redirect("user_profile")
    
  if request.method == 'POST':
    print("In POST Request")
    form = TopicForm(request.POST)
    
    if form.is_valid():
      try:
        temp_obj = form.save(commit=False)
        temp_obj.user_id = request.user
        temp_obj.topic_slug = slugify(temp_obj.topic_name)
        temp_obj.save()     
        form = TopicForm()
        
        ## sent mail
        subject = "New Discussion Topic Added"
        RecipentMessage = f"New discussion topic has been added to the platform."; 
        try:
          send_mail(subject=subject, message="", html_message=RecipentMessage, from_email=env('SERVER_EMAIL'),  recipient_list=['sshivam@cdac.in',])
        except Exception as e:
          print("Error in sending mail.", e)                
        messages.success(request, "Topic Added Successfully", extra_tags="success")     
      except:
        messages.error(request, "Something Went Wrong", extra_tags='danger')
    else:
      print("Form invalid")
  else:
    form = TopicForm()
  return render(request, 'discussion_forum/add_topic.html', {'form': form})


################################################################################
'''
Topic Discussion Function :: ADDED BY SHHIVAM SHARMA
==> 
'''
@login_required()
def view_topic_discussion(request, topic_slug):
  
  if UserProfile.objects.filter(UserProfile_user=request.user).exists():
    profile_updated = True
  else:
    profile_updated = False
    messages.error(request, "** Please update your profile details first to view the conversation. **", extra_tags="warning")
    return redirect("user_profile")
  
  print("Topic  : ", topic_slug)
  if not Topic.objects.filter(topic_slug=topic_slug).exists():
    return render(request, 'core_app/errors/400.html')
  
  topic_data = Topic.objects.get(topic_slug=topic_slug)
  user_profile = UserProfile.objects.get(UserProfile_user=topic_data.user_id)
  
  
  # Reply on topic
  replies = TopicAnswer.objects.filter(topic_id=topic_data)
  answers = []
  
  for data in replies:
    reply = AnswerReplies.objects.filter(answer_id=data.id)
    total_up_vote = AnswerUserReview.objects.filter(answer_id=data.id, status='UPVOTE').count()
    total_down_vote = AnswerUserReview.objects.filter(answer_id=data.id, status='DOWNVOTE').count()
    
    ## Check user upvoted status
    upvoted = AnswerUserReview.objects.filter(answer_id=data.id, user_id=request.user)
    
    if len(upvoted) > 0: # if user already upvoted
      answers.append({'answer':data, 'reply': reply, 'upvote': total_up_vote, 'downvote': total_down_vote, "vote_status": upvoted[0]})
    else:
      answers.append({'answer':data, 'reply': reply, 'upvote': total_up_vote, 'downvote': total_down_vote})

  return render(request, 'discussion_forum/view_topic_discussion.html', {"topic_data": topic_data, 'answers': answers, "user_profile": user_profile, "profile_updated": profile_updated})


@login_required()
def submit_answer(request, topic_slug):
  print("Topic ID : ", topic_slug)
  topic_data = Topic.objects.get(topic_slug=topic_slug)
  
  if request.method == 'POST':
    response = request.POST.get('answer')
    print("response : ", response)

    topic_ans = TopicAnswer.objects.create(topic_id=topic_data , answer=response , user_id=User.objects.get(pk=request.user.id))
    topic_ans.save()
    
  return redirect('view_topic_discussion', topic_slug=topic_slug)


"""
  This view is used to answer the questions only
"""
@login_required()
def submit_reply_to_answer(request, topic_slug, answer_id):
  print("Topic topic_slug : ", topic_slug)
  print("Answer ID : ", answer_id)
  answer_data = TopicAnswer.objects.get(id=answer_id)
  
  if request.method == 'POST':
    response = request.POST.get('answer')
    print("response : ", response)

    reply_to_ans = AnswerReplies.objects.create(answer_id=answer_data , reply=response , user_id=User.objects.get(pk=request.user.id))
    reply_to_ans.save()
    
  return redirect('view_topic_discussion', topic_slug=topic_slug)

"""
  This view is used to reply to the answer already given by user
"""
@login_required()
def submit_reply_to_answer_2(request, topic_slug, answer_id, reply_id):
  print("Topic topic_slug : ", topic_slug)
  print("Answer ID : ", answer_id)
  answer_data = TopicAnswer.objects.get(id=answer_id)
  replied_to = AnswerReplies.objects.get(id=reply_id)
  
  if request.method == 'POST':
    response = request.POST.get('answer')
    print("response : ", response)

    reply_to_ans = AnswerReplies.objects.create(answer_id=answer_data , reply=response , user_id=User.objects.get(pk=request.user.id), replied_to=replied_to)
    reply_to_ans.save()
    
  return redirect('view_topic_discussion', topic_slug=topic_slug)


@csrf_exempt
@login_required
def upvote_answer_view(request):
  print("in LIKE view")
  
  if request.method == 'POST':
    print("in True")
    answer_id = request.POST.get('answer_id')
    status = request.POST.get('status')
    
    print("answer ID : ", answer_id, " status : ", status)
    
    answer_obj = TopicAnswer.objects.get(id=answer_id)
    user_resp = AnswerUserReview.objects.filter(answer_id=answer_id, user_id=request.user)
    
    if user_resp:
      print("user resp is already given")
      if user_resp[0].status == 'UPVOTE' and status == 'UPVOTE': ## UPVOTE already selected
        obj, created = AnswerUserReview.objects.update_or_create(answer_id=answer_obj, user_id=request.user, defaults={'status': 'NULL'})
        # return JsonResponse({"status": 'True', })
      elif user_resp[0].status == 'DOWNVOTE' and status == 'DOWNVOTE': ## DOWNVOTE already selected
        obj, created = AnswerUserReview.objects.update_or_create(answer_id=answer_obj, user_id=request.user, defaults={'status': 'NULL'})
      else: 
        ## UPVOTE / DOWNVOTE updated successfully 
        obj, created = AnswerUserReview.objects.update_or_create(answer_id=answer_obj, user_id=request.user, defaults={'status': status})
    else: ## extra validation
      obj, created = AnswerUserReview.objects.update_or_create(answer_id=answer_obj, user_id=request.user, defaults={'status': status})
      print("obj ", obj)
      print("Created ", created)
  
  
  
  return JsonResponse({"status": 'True'})