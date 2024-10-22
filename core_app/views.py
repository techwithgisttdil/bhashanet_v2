from django.shortcuts import render, redirect
from .models import *
from admin_app.models import *
import requests
from django.contrib import messages
from django.core.mail import send_mail
from .forms import *
from django.http import HttpResponseRedirect
from django.conf import settings
from django.urls import reverse
from django.core.paginator import Paginator
from .custom_captcha import captcha_img_generator, random_captcha_generator
from django.http import JsonResponse
import json
from django.utils import translation
from email_validator import validate_email, EmailNotValidError
import validators
import idna
import unicodedata
from typing import TypedDict
import environ
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout
from django.apps import apps
# from Wappalyzer import Wappalyzer, WebPage
from json2html import *
# import whois
from collections import Counter
from tld import get_tld
# from collections import Counter
# import subprocess
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token import account_activation_token
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from .decorator import preprocesslangset
# import xmltojson
from django.urls import resolve
import mysql.connector
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import random
from bson import json_util
env = environ.Env()
environ.Env.read_env()
from django.http import JsonResponse
from .utility import *
from .tasks import test_func 


import ssl
from bs4 import BeautifulSoup
import certifi



# -------------HOME PAGE STARTS-----------------------

def landingfunction(request):
    domain=''
    maindomain = request.build_absolute_uri().split('/')[2]
    requesteddomainwithoutport=maindomain.split(':')[0]
    #  print("requested domain",requesteddomainwithoutport)
    with open(env('LANGUAGE_DOMAINS'), 'r',encoding="utf8") as j:
            dom = json.loads(j.read())
    for data in range(len(dom)):
        for key,value in dom[data].items():
            filterdomain1=value.split('/')[2]
            filterdomain2=filterdomain1.split(':')[0]
            if requesteddomainwithoutport == filterdomain2 :
                lang=key
                domain=value
                #  print("requested domain ijnside for loop",value,key)
                status=True
    returndomain='https://'+ maindomain.split(':')[0]
    requesteddomainwithoutport=maindomain.split(':')[0]
    if requesteddomainwithoutport =='xn--c2bro4b8ab8d.xn--h2brj9c': #Hindi
        response = HttpResponseRedirect(domain+'/होम')
        return response
    elif requesteddomainwithoutport == 'xn--d2b1ag0dl.xn--c2bro4b8ab8d.xn--h2brj9c': # Marathi  
        response = HttpResponseRedirect(domain+'/मुख्यपान')
        return response
    elif requesteddomainwithoutport == 'xn--gecho4b8a6c.xn--gecrj9c': # Gujarati 
        response = HttpResponseRedirect(domain+"/ઘર")
        return response
    elif requesteddomainwithoutport == 'bhashanet.in':  #English
        response = HttpResponseRedirect(domain+'/home')
        return response
    elif requesteddomainwithoutport == 'bhashanet.com':  #English
        response = HttpResponseRedirect(domain+'/home')
        return response
    elif requesteddomainwithoutport == 'xn--xscro4b8ab1dzc.xn--2scrj9c': #kannada
        #  print("inside kannada")
        response = HttpResponseRedirect(domain+'/ಮುಖಪುಟ')
        return response
    elif requesteddomainwithoutport == 'xn--uwcjna1a5bb9d4cb.xn--rvc1e0am3e': #Malayalam
        response = HttpResponseRedirect(domain+'/വീട്')
        return response
    elif requesteddomainwithoutport == 'xn--z5bro4b8ab8d.xn--45brj9c': #Bengali
        response = HttpResponseRedirect(domain+'/বাড়ি')
        return response
    elif requesteddomainwithoutport == 'localhost': #Bengali
        response = HttpResponseRedirect(domain+'/home')
        return response
    elif requesteddomainwithoutport == 'xn--mgbbh8aygy7awa.xn--hhbf40a': #Urdu
        response = HttpResponseRedirect(domain+'/homeUR')
        return response
    elif requesteddomainwithoutport == 'xn--becro4b8ab8d.xn--gecrj9c': #Gujarati
        response = HttpResponseRedirect(domain+'/ઘર')
        return response
    elif requesteddomainwithoutport == 'xn--35bokk7eif.xn--z5bro4b8ab8d.xn--45brj9c': #Manipuri
        response = HttpResponseRedirect(domain+"/মরুওইবা_লৈমাই")
        return response
    elif requesteddomainwithoutport == 'xn--n9bro8bukc7e.xn--s9brj9c': #Panjabi
        response = HttpResponseRedirect(domain+'/ਘਰ')
        return response
    elif requesteddomainwithoutport == 'xn--9ocro4b8ab1dzc.xn--fpcrj9c3d': #Telugu
        response = HttpResponseRedirect(domain+'/homeTE')
        return response
    elif requesteddomainwithoutport == 'xn--mlcrf6c8ab1dzc.xn--xkc2dl3a5ee0h': #Tamil
        response = HttpResponseRedirect(domain+'/homeTA')
        return response
    elif requesteddomainwithoutport == 'xn--z5bro4b8ab8d.xn--45br5cyl': #Assamese
        response = HttpResponseRedirect(domain+'/homeASS')
        return response
    elif requesteddomainwithoutport == 'xn--i1b1bb0d0hoc.xn--c2bro4b8ab8d.xn--h2brj9c': #Konkani
        response = HttpResponseRedirect(domain+'/homekon')
        return response
    elif requesteddomainwithoutport == '10.208.10.201': #Kannada test
        response = HttpResponseRedirect(domain+'/home')
        return response
    else:
        response = render(request, 'core_app/errors/404.html')
        response.status_code = 404
        return response



def home(request):
    obj_testimonialsMessages=TestimonialsMessages.objects.all().filter(TestimonialsMessages_PublishStatus='Published').order_by('id').reverse()
    obj_announcements=Announcements.objects.all().filter(Announcement_PublishStatus='Published').order_by('id').reverse()
    obj_Objectives=Objectives.objects.all().filter(Objectives_PublishedStatus='Published')
    obj_Stackholder=Stackholder.objects.all().filter(Stackholder_PublishedStatus='Published')
    faq_data=Faqs.objects.all().filter(Faqs_PublishStatus='Published')[:4]
    SOPTechnologyDocumentData = SOPTechnologyDocument.objects.filter(SOPTechnologyDocument_PublishedStatus='Published')
    response = render(request, 'core_app/home.html',
                {'obj_testimonialsMessages': obj_testimonialsMessages, 'obj_announcements': obj_announcements,
                'obj_Objectives': obj_Objectives,
                'obj_Stackholder': obj_Stackholder, 'faq_data': faq_data,'SOPTechnologyDocumentData':SOPTechnologyDocumentData})
    return response
    

    

# -------------PRIVACY POLICY STARTS-----------------------

def privacypolicy(request):
    obj_data = PrivacyPolicy.objects.get(id=1)
    print(obj_data)
    return render(request, 'core_app/privacypolicy.html', {'obj_data': obj_data})


# -------------TERMS AND CONDITION  STARTS-----------------------

def termsandconditions(request):
    obj_data = TermsAndConditions.objects.get(id=1)
    print(obj_data)
    return render(request, 'core_app/termsandconditions.html', {'obj_data': obj_data})


# -------------  STARTS-----------------------

def uaindiaprogramme(request):
    print("inside uaindiaprogrammeor")
    obj_data = UAIndiaProgramme.objects.get(id=1)
    return render(request, 'core_app/uaindiaprogramme.html', {'obj_data': obj_data})


# -------------  STARTS-----------------------

def IDNCCTLD(request):
    obj_data = IDNccTLDs.objects.get(id=1)
    obj_data_2 = IDNLanguages.objects.filter(IDNLanguages_PublishStatus='Published')

    return render(request, 'core_app/IDN_CCTLD.html', {'obj_data': obj_data, 'obj_data_2': obj_data_2})


# -------------  STARTS-----------------------

def bestpractices(request):
    obj_data = BestPractices.objects.filter(BestPractices_PublishStatus='Published')
    return render(request, 'core_app/best_practices.html', {'obj_data': obj_data})


# -------------  STARTS-----------------------

def EAI(request):
    obj_data = EmailAddressInternationalization.objects.get(id=1)
    return render(request, 'core_app/EAI.html', {'obj_data': obj_data})


# -------------  STARTS-----------------------
def UA(request):
    obj_data = UniversalAcceptance.objects.get(id=1)
    list_data = GenericList.objects.get(id=1)
    return render(request, 'core_app/UA.html', {'obj_data': obj_data, 'list_data': list_data})


# -------------  STARTS-----------------------

def tools(request):
    tool_detail = Tools.objects.filter(Tools_PublishStatus='Published')
    return render(request, 'core_app/tools.html', {'tool_detail': tool_detail})


# -------------  STARTS-----------------------

def unicode_punycode_generator(request):
    if request.method == "POST":
        if 'punycode_convert' in request.POST:
            unicode_value = request.POST.get('unicode_value')
            print("unicode text ", unicode_value)
            try:
                punycode_data = unicode_value.encode('idna').decode()
            except:
                print("unicode value error")
                return render(request, 'core_app/unicode_punnycode_generator.html',
                              {'unicode_error': "Invalid unicode value"})

            return render(request, 'core_app/unicode_punnycode_generator.html',
                          {'punycode_data': punycode_data, 'unicode_data': unicode_value})
        elif 'unicode_convert' in request.POST:
            punycode_value = request.POST.get('puny_value')
            print("punycode text ", punycode_value)
            try:
                unicode_data = punycode_value.lower().encode().decode('idna')
            except:
                print("punycode value error")
                return render(request, 'core_app/unicode_punnycode_generator.html',
                              {'punycode_error': "Invalid punycode value"})
            return render(request, 'core_app/unicode_punnycode_generator.html',
                          {'unicode_data': unicode_data, 'punycode_data': punycode_value})
        else:
            return render(request, 'core_app/unicode_punnycode_generator.html')
    return render(request, 'core_app/unicode_punnycode_generator.html')


# -------------  STARTS-----------------------

def transliteration(request):
    return render(request, 'core_app/transliteration.html')


# -------------  STARTS-----------------------

def unicode_fonts(request):
    return render(request, 'core_app/unicode_fonts.html')


# -------------  STARTS-----------------------

def script_detection(request):
    return render(request, 'core_app/script_detection.html')


# -------------  STARTS-----------------------

def language_detection(request):
    return render(request, 'core_app/language_detection.html')


# -------------  STARTS-----------------------

def cdac_keyboard(request):
    return render(request, 'core_app/cdac_keyboard.html')


# -------------  STARTS-----------------------

def email_validator(request):
    email_form_obj = Email_Syntax_Check_form(request.POST)

    print("Inside view")
    if request.method == "POST":
        email_form_obj = Email_Syntax_Check_form(request.POST)
        email = email_form_obj.data['Email_Address']
            
        print("Email Address from form : " + email)
        print("In POST method")
        if email_form_obj.is_valid():
            try:
                if validate_email(email):
                    print("Valid")
            
                email_form_obj.save()
                messages.success(request, "Valid Email Address Format", extra_tags="success")
            except EmailNotValidError as e:
                messages.error(request, " " + str(e), extra_tags="danger")

        
                return render(request, 'core_app/email_validator.html',{'email_form_obj':email_form_obj})
    
    return render(request, 'core_app/email_validator.html',{'email_form_obj':email_form_obj})


# -------------  STARTS-----------------------
def success_stories(request):
    return render(request, 'core_app/idn_ready_websites.html')


def idn_websites(request, id):
    id=int(id)
    form = IDN_Ready_Websites()
    success_stories = IDNReadyWebsitesLangugeURLMapping.objects.all().filter(IDNReadyWebsites_LangURLMapping_Publish_Status="Published")
    idn_websites = IDNReadyWebsites.objects.all().filter(IDNReadyWebsites_Publish_Status="Published").order_by('IDNReadyWebsites_Title')
    paginator = Paginator(idn_websites, per_page=5)
    page_object = paginator.get_page(id)
    selected_categories = []
    selected_languages = []

    if request.method == "POST":
        form = IDN_Ready_Websites(request.POST)
        if request.POST.get('filter') == 'filter':
            selected_categories = request.POST.getlist('select_category')
            selected_languages =  request.POST.getlist('select_language')
            success_stories = IDNReadyWebsitesLangugeURLMapping.objects.none()
            idn_websites = IDNReadyWebsites.objects.none()
            if not selected_categories and selected_languages:
                for language in selected_languages:
                    mappedUrls = IDNReadyWebsitesLangugeURLMapping.objects.filter(IDNReadyWebsites_lang = IDNReadyWebsitesLanguages.objects.get(id=language), IDNReadyWebsites_LangURLMapping_Publish_Status="Published")
                    for url in mappedUrls:
                        idn_websites |= IDNReadyWebsites.objects.filter(id=IDNReadyWebsitesLangugeURLMapping.objects.get(IDNReadyWebsites_url=url).IDNReadyWebsites_id, IDNReadyWebsites_Publish_Status="Published").order_by('IDNReadyWebsites_Title')
                    success_stories |= IDNReadyWebsitesLangugeURLMapping.objects.filter(IDNReadyWebsites_lang = IDNReadyWebsitesLanguages.objects.get(id=language), IDNReadyWebsites_LangURLMapping_Publish_Status="Published")
                paginator = Paginator(idn_websites, per_page=5)
                page_object = paginator.get_page(id)
                request.session['languages'] = selected_languages
                request.session['categories'] = selected_categories
            elif not selected_languages and selected_categories:
                for category in selected_categories:
                    idn_websites |= IDNReadyWebsites.objects.filter(IDNReadyWebsites_Category=category, IDNReadyWebsites_Publish_Status="Published").order_by('IDNReadyWebsites_Title')
                    websites = IDNReadyWebsites.objects.filter(IDNReadyWebsites_Category = IDNReadyWebsitesCategory.objects.get(id=category), IDNReadyWebsites_Publish_Status="Published")
                    for website in websites:
                        success_stories |= IDNReadyWebsitesLangugeURLMapping.objects.filter(IDNReadyWebsites = website, IDNReadyWebsites_LangURLMapping_Publish_Status="Published")
                paginator = Paginator(idn_websites, per_page=5)
                page_object = paginator.get_page(id)
                request.session['languages'] = selected_languages
                request.session['categories'] = selected_categories
            elif selected_languages and selected_categories:
                for language in selected_languages:
                    for category in selected_categories:
                        mappedUrls = IDNReadyWebsitesLangugeURLMapping.objects.filter(IDNReadyWebsites_lang = IDNReadyWebsitesLanguages.objects.get(id=language), IDNReadyWebsites_LangURLMapping_Publish_Status="Published")
                        for url in mappedUrls:
                            idn_websites |= IDNReadyWebsites.objects.filter(id=IDNReadyWebsitesLangugeURLMapping.objects.get(IDNReadyWebsites_url=url).IDNReadyWebsites_id, IDNReadyWebsites_Publish_Status="Published").order_by('IDNReadyWebsites_Title') & IDNReadyWebsites.objects.filter(IDNReadyWebsites_Category=category).order_by('IDNReadyWebsites_Title')
                        websites = IDNReadyWebsites.objects.filter(IDNReadyWebsites_Category = IDNReadyWebsitesCategory.objects.get(id=category), IDNReadyWebsites_Publish_Status="Published")
                        for website in websites:
                            success_stories |= IDNReadyWebsitesLangugeURLMapping.objects.filter(IDNReadyWebsites = website, IDNReadyWebsites_LangURLMapping_Publish_Status="Published") & IDNReadyWebsitesLangugeURLMapping.objects.filter(IDNReadyWebsites_lang = IDNReadyWebsitesLanguages.objects.get(id=language), IDNReadyWebsites_LangURLMapping_Publish_Status="Published")
                paginator = Paginator(idn_websites, per_page=5)
                page_object = paginator.get_page(id)
                request.session['languages'] = selected_languages
                request.session['categories'] = selected_categories
            else:
                # success_stories = IDNReadyWebsitesLangugeURLMapping.objects.all()
                # idn_websites = IDNReadyWebsites.objects.all()
                # paginator = Paginator(idn_websites, per_page=5)
                # page_object = paginator.get_page(id)
                success_stories = IDNReadyWebsitesLangugeURLMapping.objects.all().filter(IDNReadyWebsites_LangURLMapping_Publish_Status="Published").order_by('IDNReadyWebsites')
                idn_websites = IDNReadyWebsites.objects.all().filter(IDNReadyWebsites_Publish_Status="Published").order_by('IDNReadyWebsites_Title')
                paginator = Paginator(idn_websites, per_page=5)
                page_object = paginator.get_page(id)
                try:
                    del request.session['languages']
                    del request.session['categories']
                except Exception as e:
                    success_stories = IDNReadyWebsitesLangugeURLMapping.objects.all().filter(IDNReadyWebsites_LangURLMapping_Publish_Status="Published")
                    idn_websites = IDNReadyWebsites.objects.all().filter(IDNReadyWebsites_Publish_Status="Published").order_by('IDNReadyWebsites_Title')
                    paginator = Paginator(idn_websites, per_page=5)
                    page_object = paginator.get_page(id)

        elif request.POST.get('filter') == 'reset':
            success_stories = IDNReadyWebsitesLangugeURLMapping.objects.all().filter(IDNReadyWebsites_LangURLMapping_Publish_Status="Published")
            form = IDN_Ready_Websites()
            paginator = Paginator(idn_websites, per_page=5)
            page_object = paginator.get_page(id)
            try:
                del request.session['languages']
                del request.session['categories']
            except Exception as e:
                success_stories = IDNReadyWebsitesLangugeURLMapping.objects.all().filter(IDNReadyWebsites_LangURLMapping_Publish_Status="Published")
                form = IDN_Ready_Websites()
                paginator = Paginator(idn_websites, per_page=5)
                page_object = paginator.get_page(id)
    elif id :
            try:
                # del request.session['languages']
                # del request.session['categories']
                print("selected lang ", request.session['languages'])
                selected_languages =  request.session['languages']
                selected_categories = request.session['categories']
                success_stories = IDNReadyWebsitesLangugeURLMapping.objects.none()
                idn_websites = IDNReadyWebsites.objects.none()
                if not selected_categories and selected_languages:
                    for language in selected_languages:
                        mappedUrls = IDNReadyWebsitesLangugeURLMapping.objects.filter(IDNReadyWebsites_lang = IDNReadyWebsitesLanguages.objects.get(id=language), IDNReadyWebsites_LangURLMapping_Publish_Status="Published")
                        for url in mappedUrls:
                            idn_websites |= IDNReadyWebsites.objects.filter(id=IDNReadyWebsitesLangugeURLMapping.objects.get(IDNReadyWebsites_url=url).IDNReadyWebsites_id, IDNReadyWebsites_Publish_Status="Published").order_by('IDNReadyWebsites_Title')
                        success_stories |= IDNReadyWebsitesLangugeURLMapping.objects.filter(IDNReadyWebsites_lang = IDNReadyWebsitesLanguages.objects.get(id=language), IDNReadyWebsites_LangURLMapping_Publish_Status="Published")
                    paginator = Paginator(idn_websites, per_page=5)
                    page_object = paginator.get_page(id)
                    # request.session['languages'] = selected_languages
                    # request.session['categories'] = selected_categories
                elif not selected_languages and selected_categories:
                    for category in selected_categories:
                        idn_websites |= IDNReadyWebsites.objects.filter(IDNReadyWebsites_Category=category, IDNReadyWebsites_Publish_Status="Published").order_by('IDNReadyWebsites_Title')
                        websites = IDNReadyWebsites.objects.filter(IDNReadyWebsites_Category = IDNReadyWebsitesCategory.objects.get(id=category), IDNReadyWebsites_Publish_Status="Published")
                        for website in websites:
                            success_stories |= IDNReadyWebsitesLangugeURLMapping.objects.filter(IDNReadyWebsites = website, IDNReadyWebsites_LangURLMapping_Publish_Status="Published")
                    paginator = Paginator(idn_websites, per_page=5)
                    page_object = paginator.get_page(id)
                elif selected_languages and selected_categories:
                    for language in selected_languages:
                        for category in selected_categories:
                            mappedUrls = IDNReadyWebsitesLangugeURLMapping.objects.filter(IDNReadyWebsites_lang = IDNReadyWebsitesLanguages.objects.get(id=language), IDNReadyWebsites_LangURLMapping_Publish_Status="Published")
                            for url in mappedUrls:
                                idn_websites |= IDNReadyWebsites.objects.filter(id=IDNReadyWebsitesLangugeURLMapping.objects.get(IDNReadyWebsites_url=url).IDNReadyWebsites_id, IDNReadyWebsites_Publish_Status="Published").order_by('IDNReadyWebsites_Title') & IDNReadyWebsites.objects.filter(IDNReadyWebsites_Category=category, IDNReadyWebsites_Publish_Status="Published").order_by('IDNReadyWebsites_Title')
                            websites = IDNReadyWebsites.objects.filter(IDNReadyWebsites_Category = IDNReadyWebsitesCategory.objects.get(id=category), IDNReadyWebsites_Publish_Status="Published")
                            for website in websites:
                                success_stories |= IDNReadyWebsitesLangugeURLMapping.objects.filter(IDNReadyWebsites = website, IDNReadyWebsites_LangURLMapping_Publish_Status="Published") & IDNReadyWebsitesLangugeURLMapping.objects.filter(IDNReadyWebsites_lang = IDNReadyWebsitesLanguages.objects.get(id=language), IDNReadyWebsites_LangURLMapping_Publish_Status="Published")
                    paginator = Paginator(idn_websites, per_page=5)
                    page_object = paginator.get_page(id)
            except Exception as e:
                print("error ",e)
                success_stories = IDNReadyWebsitesLangugeURLMapping.objects.all().filter(IDNReadyWebsites_LangURLMapping_Publish_Status="Published").order_by('IDNReadyWebsites')
                form = IDN_Ready_Websites()
                paginator = Paginator(idn_websites, per_page=5)
                page_object = paginator.get_page(id)

    last_updated_date = []
    for web in idn_websites:
        temp_list = []
        temp_list_url = []
        for story in success_stories:
            if(story.IDNReadyWebsites.id == web.id):
                temp_list.append(story.IDNReadyWebsites_LangURLMapping_Last_Updated_Date)
        

        if temp_list:
            urls = IDNReadyWebsitesLangugeURLMapping.objects.filter(Q(IDNReadyWebsites=web) & Q(IDNReadyWebsites_LangURLMapping_Last_Updated_Date=max(temp_list)))
            # for url in urls:
            #     print("url ", url)
            last_updated_date.append({"web": web.IDNReadyWebsites_Title, "date": max(temp_list), "urls": urls})
            
 
    print("IDN Websites URL Mapping",page_object )
    return render(request, 'core_app/idn_ready_websites.html',{'success_stories': success_stories, 'form': form, 'idn_websites': idn_websites, 'page':page_object, 'paginator':paginator, 'selected_languages':selected_languages, 'selected_categories': selected_categories, 'last_updated_date':last_updated_date})
    # else:
    #     path=''
    #     with open(env('LANGUAGE_PATHS'), 'r',encoding="utf8") as j:
    #         contents = json.loads(j.read())
    #     for content in range(len(contents)):
    #         for cont in range(len(contents[content])):
    #             for key, value in contents[content]['mainpath'].items():
    #                 if value=='/home':
    #                     path=contents[content]['mainpath'][lang_domain]
    #     print("Return redirect path",path)
    #     return redirect(path)


def domain_validator(request):
    domain_form_obj = Domain_Syntax_Check_form()
    #domain_name = domain_form_obj.data['Domain_Name']
    print("Inside view")
    try:
        if request.method == "POST":
            domain_form_obj = Domain_Syntax_Check_form(request.POST)
            domain_name = domain_form_obj.data['Domain_Name']
            print("Data from form : "+domain_name)
            print("In POST method")
            if domain_form_obj.is_valid():
                domain_form_obj.save()
               
                messages.success(request, "Valid Domain", extra_tags="success")
                #domain_name = domain_form_obj.data['Domain_Name']
                #return render(request, 'core_app/domain_validator.html',{'domain_form_obj': domain_form_obj})
        
                return render(request, 'core_app/domain_validator.html',{'domain_form_obj': domain_form_obj})
    except:
        messages.error(request, "Domain is invlaid", extra_tags="danger")
    return render(request, 'core_app/domain_validator.html',{'domain_form_obj': domain_form_obj})
    
# -------------  STARTS-----------------------

# captcha refresh 
def captcha_refresh(request):
    print("In captcha refresh method")

    captcha_value = random_captcha_generator()
    captcha_img_generator(captcha_value)
    print("captcha Value ", captcha_value)

    return JsonResponse({'captcha_value': f'{make_password(captcha_value)}', 'captcha_url': '/captcha_images/CAPTCHA.png'})


# -------------  STARTS-----------------------
# @throttle(zone='default')

def rateLimitEmails(throttle_email):
    
    current_date = datetime.now().date()
    
    if LimitCheck.objects.filter(Email = throttle_email).exists() != True:
        print("First Time check !!")
        limit_check_object = LimitCheck(Email=throttle_email,Counter=1)
        limit_check_object.save()
        return True
    else:
        limit_check_data = LimitCheck.objects.get(Email=throttle_email)
        time = limit_check_data.Generation_Time
        count = limit_check_data.Counter
        if time == current_date:
           # print("Already Exsist and not the first Entry : " + str(time) + " current Date : " + str(current_date))
            #print("Same day new mail" + count)
            if count < 100:
                print("Can send mail")
                count = count + 1
                user_object = LimitCheck.objects.get(Email=throttle_email)                  
                user_object.Counter = count
                # user_object.Generation_Time = date.now()
                user_object.save()
                user_object = LimitCheck.objects.get(Email=throttle_email)      
                #print("Updated count object : " + str(user_object.Counter))
                return True
            else:
                print("Cant send mail")
                return False
        else:
            print("Change Count to 1")
            user_object = LimitCheck.objects.get(Email=throttle_email)                  
            user_object.Counter = 1
            user_object.Generation_Time = datetime.now().date()
            user_object.save()
            return True




def feedback(request):
    feedback_form_obj = Feedback_form(request.POST or None)

    if request.method == "POST":
        if feedback_form_obj.is_valid():
            try:
                # Fetch and process form data
                mail = feedback_form_obj.cleaned_data['Feedback_Email'].strip()
                feedback_related_to_id = feedback_form_obj.cleaned_data['Feedback_Related_To']
                print("Feedback Related ID: ",feedback_related_to_id)
                
    
                feedback_category = FeedbackCategory.objects.get(FeedbackCategory_Name=feedback_related_to_id)
                subject = feedback_category.FeedbackCategory_Name  # Use a field, not the whole object

                message = feedback_form_obj.cleaned_data['Feedback_Message'].strip()

                if rateLimitEmails(mail):
                    try:
                        validate_email(mail)
                    except EmailNotValidError as e:
                        messages.error(request, f"Invalid email: {str(e)}")
                        return render(request, 'core_app/feedback.html', {'feedback_form_obj': feedback_form_obj})


                    feedback_form_obj.save()

                    # Send emails
                    RecipentMessage = "Thank you for your " + subject + " We Appriciate your concern!!"; 
                    recipient_list = ['gist-tdil@cdac.in', 'support@bhashanet.in']
                    send_mail(subject, message, env('SERVER_EMAIL'), recipient_list)
                    send_mail(subject, RecipentMessage, env('SERVER_EMAIL'), [mail])

                    messages.success(request, "Feedback Successfully Submitted")

                else:
                    messages.error(request, "Email limit exceeded. Please try again later.")

            except FeedbackCategory.DoesNotExist:
                messages.error(request, "Invalid category selected.")
            except Exception as e:
                print(f"Error: {str(e)}")
                messages.error(request, "There was an issue submitting your feedback.")
        else:
            messages.error(request, "Please provide valid data in all fields.")

    # Generate and initialize captcha on GET request
    if request.method == "GET" or request.method == "POST":
        captcha_value = random_captcha_generator()
        captcha_img_generator(captcha_value)
        feedback_form_obj.fields['captcha_hidden'].initial = make_password(captcha_value)

    return render(request, 'core_app/feedback.html', {'feedback_form_obj': feedback_form_obj})


# -------------  STARTS-----------------------

def becomeuaready(request):
    obj_data = Article.objects.get(id=1)
    list_data = GenericList.objects.get(id=2)
    return render(request, 'core_app/becomeuaready.html', {'obj_data': obj_data, 'list_data': list_data})


# -------------  STARTS-----------------------

def FAQs(request):
    faq_categories = FaqCategory.objects.filter(FaqCategory_PublishStatus='Published')

    # faqs_obj = {}
    # for cat in faq_categories:
    #     faq = Faqs.objects.get(Faqs_Category=cat)
    #     faqs_obj[cat.FaqCategory_Name] = faq

    faqs = Faqs.objects.filter(Faqs_PublishStatus='Published')
    developer_faqs = []
    idn_faqs = []
    general_faqs = []
    ua_faqs = []
    
    developer_faq_category = ['Developer', 'विकासक', 'विकासक', 'ഡെവലപ്പർ', 'ಡೆವಲಪರ್', 'বিকাশকারী', 'দেবলপর','ڈویلپر']
    IDN_faq_category = ['IDN', 'आईडीएन', 'आईडीएन', 'ഐഡിഎൻ', 'ಐಡಿಎನ್', 'আইডিএন', 'আইদীএন','آئی ڈی این']
    general_faq_category = ['General', 'सामान्य', 'सामान्य', 'പൊതുവായ', 'ಸಾಮಾನ್ಯ', 'সাধারণ', 'ময়ামগী ওইবা','عام']
    UA_faq_category = ['Universal Acceptance', 'सार्वभौमिक स्वीकृति', 'सार्वत्रिक मान्यता', 'സാർവത്രിക സ്വീകാര്യത', 'ಸಾರ್ವತ್ರಿಕ ಸ್ವೀಕೃತಿ', 'সর্বজনীন গ্রহণযোগ্যতা', 'য়ূনিভরসেল এসেপতেন্স','عالمی قبولیت']
    for faq in faqs:
        if faq.Faqs_Category.FaqCategory_Name in developer_faq_category:
            developer_faqs.append(faq)
        elif faq.Faqs_Category.FaqCategory_Name in IDN_faq_category:
            idn_faqs.append(faq)
        elif faq.Faqs_Category.FaqCategory_Name in general_faq_category:
            general_faqs.append(faq)
        elif faq.Faqs_Category.FaqCategory_Name in UA_faq_category:
            ua_faqs.append(faq)

    return render(request, 'core_app/FAQs.html',
                  {'faq_categories': faq_categories, 'developer_faqs': developer_faqs, 'general_faqs': general_faqs,
                   'idn_faqs': idn_faqs, 'ua_faqs': ua_faqs})


# -------------  STARTS-----------------------

def search_results(request):
    return render(request, 'core_app/search_results.html')


def home1(request):
    return render(request, 'core_app/home1.html')


# -------------  STARTS-----------------------

# def set_language(request):
#     domain = request.build_absolute_uri().split('/')[2]
#     if domain == 'xn--c2bro4b8ab8d.xn--h2brj9c:8001':
#         request.session[settings.LANGUAGE_SESSION_KEY] = 'hi'
#         response = HttpResponseRedirect(request.META.get('HTTP_REFERER', 'घर/'))
#         response.set_cookie(settings.LANGUAGE_COOKIE_NAME, 'hi')
#         return response
#     else:
#         request.session[settings.LANGUAGE_SESSION_KEY] = 'en'
#         response = HttpResponseRedirect(request.META.get('HTTP_REFERER', 'home'))
#         response.set_cookie(settings.LANGUAGE_COOKIE_NAME, 'en')
#         return response


# def HindiRenderPageWithPathAndLang(request, path):
#     requestcode=request.path.split('/')[2]
#     if requestcode == 'hi':
#         translation.activate('hi')
#         request.session[settings.LANGUAGE_SESSION_KEY] ='hi'
#         domain = request.build_absolute_uri().split('/')[2]
#         langhi=None
#         if domain == 'xn--c2bro4b8ab8d.xn--h2brj9c:8001':
#             print("hindi and marathi")
#             with open('core\paths.json', 'r',encoding="utf8") as j:
#                 contents = json.loads(j.read())
#             pathrender='/'
#             print("request session code",request.session.get(settings.LANGUAGE_SESSION_KEY))
#             for content in range(len(contents)):
#                 for cont in range(len(contents[content])):
#                     for key, value in contents[content]['mainpath'].items():
#                         if value == '/'+request.path.split('/')[1]:
#                             pathrender=contents[content]['mainpath']['hi']
#                             langhi='hi'
#             print("final path render and lang9099090909090900",pathrender,langhi)
#             request.session[settings.LANGUAGE_SESSION_KEY] = langhi
#             response = HttpResponseRedirect('http://xn--c2bro4b8ab8d.xn--h2brj9c:8001'+pathrender)
#             response.set_cookie(settings.LANGUAGE_COOKIE_NAME, langhi)
#             return response
#     else:
#         response = render(request, 'core_app/errors/404.html')
#         response.status_code = 404
#         return response





# def MrRenderPageWithPathAndLang(request, path):
#     requestcode=request.path.split('/')[2]
#     if requestcode == 'mr':
#         translation.activate('mr')
#         request.session[settings.LANGUAGE_SESSION_KEY] ='mr'
#         domain = request.build_absolute_uri().split('/')[2]
#         print("domain", domain)
#         lang=None
#         if domain == 'xn--c2bro4b8ab8d.xn--h2brj9c:8001':
#             print("hindi and marathi")
#             with open('core\paths.json', 'r',encoding="utf8") as j:
#                 contents = json.loads(j.read())
#             pathrendermr='/'
#             print("request session code",request.session.get(settings.LANGUAGE_SESSION_KEY))
#             for content in range(len(contents)):
#                 for cont in range(len(contents[content])):
#                     for key, value in contents[content]['mainpath'].items():
#                         if value == '/'+request.path.split('/')[1]:
#                             print("valueeee",value,'/'+request.path.split('/')[1])
#                             pathrendermr=contents[content]['mainpath']['mr']
#                             lang='mr'
#             print("final path render and lang9099090909090900",pathrendermr,lang)
#             request.session[settings.LANGUAGE_SESSION_KEY] = lang
#             response = HttpResponseRedirect('http://xn--c2bro4b8ab8d.xn--h2brj9c:8001'+pathrendermr)
#             response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
#             return response
#     else:
#         response = render(request, 'core_app/errors/404.html')
#         response.status_code = 404
#         return response






def bad_request(request, exception):
    print("inside page not found")
    return redirect(reverse('set_language'))




def documentPage(request):
    DocumentCategory.objects.update(DocumentCategory_Status=False)
    documentData=Document.objects.all()
    categoryData=DocumentCategory.objects.all()
    page = Paginator(documentData, 3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    count = documentData.count()
    context = {
        'categoryData': categoryData,
        'page': page,
        'count': count,
        'Pagination_Type': 'All_Data',
    }
    return render(request, 'core_app/uadocument.html', context)


def documentData(request):
    print("==============================",len(request.get_full_path().split('?')))
   # DocumentCategory.objects.update(DocumentCategory_Status=False)
    if len(request.get_full_path().split('?')) == 1:
        print("inside ===================")
        DocumentCategory.objects.update(DocumentCategory_Status=False)
        categoryData=DocumentCategory.objects.all()
        documentData = Document.objects.all()
        pagestatus = False
    else:
        documentData = Document.objects.all()
        categoryData=DocumentCategory.objects.all()
        pagestatus = False
        for cat in DocumentCategory.objects.all():
            if cat.DocumentCategory_Status == True:
                pagestatus = True
    if request.method == 'POST' and 'filter-button' in request.POST:
        print("==============================",request)
        print("Inside filter button called")
        DocumentCategory.objects.update(DocumentCategory_Status=False)
        filtered_DocumentDataWithCategory = Document.objects.none()
        checklist = request.POST.getlist('select_specialist')
        for category_name in checklist:
                DocumentCategory.objects.filter(
                DocumentCategory_Name=category_name).update(DocumentCategory_Status=True)
                pagestatus = True
        categorydata = DocumentCategory.objects.all()
        filtered_DocumentDataWithCategory = Document.objects.filter(Document_CategoryType__DocumentCategory_Status=True)
        if pagestatus == True:
            page = Paginator(filtered_DocumentDataWithCategory, 3)
            page_list = request.GET.get('page')
            page = page.get_page(page_list)
            count = filtered_DocumentDataWithCategory.count()
            context = {
                'categoryData': categorydata,
                'Pagination_Type': 'Category_Data',
                'count': count,
                'page': page,
                'document_title': 'none',
            }
        else:
            documentData = Document.objects.all()
            categoryData=DocumentCategory.objects.all()
            page = Paginator(documentData, 3)
            page_list = request.GET.get('page')
            page = page.get_page(page_list)
            count = documentData.count()
            context = {
                'categoryData': categorydata,
                'Pagination_Type': 'All_Data',
                'count': count,
                'page': page,
                'document_title': 'none',
            }
        return render(request, 'core_app/uadocument.html', context)
    if request.method == 'POST' and 'reset-button' in request.POST:
        DocumentCategory.objects.update(DocumentCategory_Status=False)
        documentData=Document.objects.all()
        categoryData=DocumentCategory.objects.all()
        page = Paginator(documentData, 3)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        count = documentData.count()
        context = {
            'categoryData': categoryData,
            'page': page,
            'count': count,
            'Pagination_Type': 'All_Data',
        }
        return render(request, 'core_app/uadocument.html', context)

    if pagestatus == True:
        filtered_DocumentDataWithCategoryPage = Document.objects.filter(Document_CategoryType__DocumentCategory_Status=True)
        page = Paginator(filtered_DocumentDataWithCategoryPage, 3)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        count = filtered_DocumentDataWithCategoryPage.count()
        context = {
            'categoryData': categoryData,
            'Pagination_Type': 'Category_Data',
            'count': count,
            'page': page,
            'document_title': 'none',
        }
    else:
        page = Paginator(documentData, 3)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        count = documentData.count()
        context = {
            'categoryData': categoryData,
            'Pagination_Type': 'All_Data',
            'count': count,
            'page': page,
            'document_title': 'none',
        }
    return render(request, 'core_app/uadocument.html', context)


def support(request):
    return render(request, 'core_app/support.html')


# -------------  STARTS-----------------------

def custom_page_not_found_view(request, exception=None):
    print("inside 404")
    return render(request, "core_app/errors/404.html", {})


def custom_error_view(request, exception=None):
    print("inside 500")
    return render(request, "core_app/errors/500.html", {})


def custom_permission_denied_view(request, exception=None):
    print("inside 403")
    return render(request, "core_app/errors/403.html", {})


def custom_bad_request_view(request, exception=None):
    print("inside 400")
    return render(request, "core_app/errors/400.html", {})




def testimonial(request):
    obj_testimonialsMessages = TestimonialsMessages.objects.filter(
        TestimonialsMessages_PublishStatus='Published')
    return render(request, "core_app/testimonials.html", {'obj_testimonialsMessages':obj_testimonialsMessages})


# def check():
#     print("pass")
#     pass
# -------------  STARTS-----------------------

def testimonials(request):
     return render(request, 'core_app/testimonials.html')
# -------------  STARTS-----------------------

def event(request):
     return render(request, 'core_app/event.html')
# -------------  STARTS-----------------------

def gallery(request):
    gallery_video_headings = GalleryHeadings.objects.all()
    gallery_videos = GalleryVideos.objects.all()
    return render(request, 'core_app/gallery.html', {'gallery_videos': gallery_videos, 'gallery_video_headings': gallery_video_headings})
# -------------  STARTS-----------------------



def SOPTechnalogyPage(request):
    SOPArticle = Article.objects.get(id=2)
    SOPTechnologyDocumentData = SOPTechnologyDocument.objects.all()
    count = SOPTechnologyDocumentData.count()
    context = {
        'SOPArticle': SOPArticle,
        'count': count,
    }
    return render(request, 'core_app/sop_tech_document.html', context)


def sop_document_page(request, id=None):
        SOPTechnologyDocumentData = SOPTechnologyDocument.objects.all()
        SOPTechnologyCategory.objects.all().update(SOPTechnologyCategory_Status=False)
        SOPTechnologyCategoryData = SOPTechnologyCategory.objects.all()
        page = Paginator(SOPTechnologyDocumentData, 3)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        count = SOPTechnologyDocumentData.count()
        context = {
            'SOPTechnologyCategoryData':SOPTechnologyCategoryData,
            'tools_title': 'none',
            "page": page,
            'status_All_Checked': 'True',
            'Pagination_Type': 'All_Data',
            'count': count,
        }
        return render(request, 'core_app/sop_docuemnts_page.html', context)


def sop_document(request):
    if len(request.get_full_path().split('?')) == 1:
        print("inside ===================")
        SOPTechnologyCategory.objects.all().update(SOPTechnologyCategory_Status=False)
        SOPTechnologyDocumentData = SOPTechnologyDocument.objects.all()
        SOPTechnologyCategoryData = SOPTechnologyCategory.objects.all()
        pagestatus = False
    else:
        SOPTechnologyDocumentData = SOPTechnologyDocument.objects.all()
        SOPTechnologyCategoryData = SOPTechnologyCategory.objects.all()
        pagestatus = False
        page = Paginator(SOPTechnologyDocumentData, 3)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        count = SOPTechnologyDocumentData.count()
        for category in SOPTechnologyCategoryData:
            if category.SOPTechnologyCategory_Status == True:
                pagestatus = True
    if request.method == 'POST' and 'filter-button' in request.POST:
        print("Hellooooo Inside post method ")
        SOPTechnologyCategory.objects.all().update(SOPTechnologyCategory_Status=False)
        SOPTechnologyDocumentData = SOPTechnologyDocument.objects.none()
        checklist = request.POST.getlist('select_specialist')
        if checklist:
            for category_name in checklist:
                print("Selected category")
                print(category_name)
                SOPTechnologyCategory.objects.filter(
                    SOPTechnologyCategory_Name=category_name).update(SOPTechnologyCategory_Status=True)
                pagestatus = True
            SOPTechnologyCategoryData = SOPTechnologyCategory.objects.all()
            for category_name in checklist:
                SOPTechnologyDocumentData = SOPTechnologyDocumentData | SOPTechnologyDocument.objects.filter(
                    SOPTechnologyDocument_CategoryType__SOPTechnologyCategory_Name__contains=category_name)
            for data in SOPTechnologyDocumentData:
                print(data)
            if pagestatus == True:
                page = Paginator(SOPTechnologyDocumentData, 3)
                page_list = request.GET.get('page')
                page = page.get_page(page_list)
                count = SOPTechnologyDocumentData.count()
                context = {
                    'SOPTechnologyCategoryData':SOPTechnologyCategoryData,
                    'Pagination_Type': 'Category_Data',
                    'count': count,
                    'page': page,
                }
            else:
                page = Paginator(SOPTechnologyDocumentData, 3)
                page_list = request.GET.get('page')
                page = page.get_page(page_list)
                count = SOPTechnologyDocumentData.count()
                context = {
                'SOPTechnologyCategoryData':SOPTechnologyCategoryData,
                    'Pagination_Type': 'All_Data',
                    'count': count,
                    'page': page,
                }
        else:
            SOPTechnologyCategoryData = SOPTechnologyCategory.objects.all()
            SOPTechnologyDocumentData = SOPTechnologyDocument.objects.all()
            page = Paginator(SOPTechnologyDocumentData, 3)
            page_list = request.GET.get('page')
            page = page.get_page(page_list)
            count = SOPTechnologyDocumentData.count()
            context = {
                'SOPTechnologyCategoryData':SOPTechnologyCategoryData,
                    'Pagination_Type': 'All_Data',
                    'count': count,
                    'page': page,
                }
        return render(request, 'core_app/sop_docuemnts_page.html', context)
    
    if request.method == 'POST' and 'reset-button' in request.POST:
        SOPTechnologyDocumentData = SOPTechnologyDocument.objects.all()
        SOPTechnologyCategory.objects.all().update(SOPTechnologyCategory_Status=False)
        SOPTechnologyCategoryData = SOPTechnologyCategory.objects.all()
        page = Paginator(SOPTechnologyDocumentData, 3)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        count = SOPTechnologyDocumentData.count()
        context = {
            'SOPTechnologyCategoryData':SOPTechnologyCategoryData,
            'tools_title': 'none',
            "page": page,
            'status_All_Checked': 'True',
            'Pagination_Type': 'All_Data',
            'count': count,
        }
        return render(request, 'core_app/sop_docuemnts_page.html', context)
    
    if pagestatus == True:
        SOPTechnologyDocumentData = SOPTechnologyDocument.objects.filter(
            SOPTechnologyDocument_CategoryType__SOPTechnologyCategory_Status=True)
        page = Paginator(SOPTechnologyDocumentData, 3)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        count = SOPTechnologyDocumentData.count()
        context = {
            'SOPTechnologyCategoryData':SOPTechnologyCategoryData,
            'Pagination_Type': 'Category_Data',
            'count': count,
            'page': page,
        }
    else:
        page = Paginator(SOPTechnologyDocumentData, 3)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        count = SOPTechnologyDocumentData.count()
        context = {
            'SOPTechnologyCategoryData':SOPTechnologyCategoryData,
            'Pagination_Type': 'All_Data',
            'count': count,
            'page': page,
        }
    return render(request, 'core_app/sop_docuemnts_page.html', context)






def SopDownloadCounter(request,id):
    # url = resolve(request.path_info).url_name
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # print("SopDownloadCounter==================",url, x_forwarded_for,request.META.get('REMOTE_ADDR'))
    # return redirect('sop_tech_page')
  
    url = resolve(request.path_info).url_name
    request.session['requested_url'] = url
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = ''
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    saved_ip = None
    session_ip=request.session.get('sopDownloadCounter_ip')
    if session_ip == ip:
        time_posted = request.session.get('sop_Download_time')
        Heading = request.session.get('sopDownloadCounter_sopHeading')
    else:
        Heading=None
        time_posted=None


    sop_obj = SOPTechnologyDocument.objects.get(pk=id)
    sop_requested_title = sop_obj.SOPTechnologyDocument_Name
    
    print("Heading",Heading)
    savedTimeInSession = None
    time_diff = 0
    
    if sop_requested_title == Heading:
        if time_posted is not None:
            savedTimeInSession = datetime.fromisoformat(time_posted[:-1])
            dataCurrentTime = datetime.now()
            print("-=-=-=-",dataCurrentTime,savedTimeInSession,dataCurrentTime - savedTimeInSession)
            timediff = dataCurrentTime - savedTimeInSession
            time_diff = timediff.total_seconds()
            print("time_diff",time_diff)
        else:
            time_diff = 70
    else:
        time_diff = 60
    if time_diff < 60:
        saved_ip = request.session.get('sopDownloadCounter_ip')
    else:
        request.session['sopDownloadCounter_ip'] = None
    print("+++++++++++",ip,saved_ip)
    if ip != saved_ip:
        request.session['sopDownloadCounter_ip'] = ip
        data = datetime.now()
        data1 = json.dumps(data, default=json_util.default)
        aList = json.loads(data1)
        testdata = aList['$date']
        request.session['sop_Download_time'] = testdata
        sop_obj = SOPTechnologyDocument.objects.get(pk=id)
        try:
            sop_download_obj=SOPDownloadCounter.objects.get(SOPTechnologyDocument_Obj=sop_obj)
            sop_download_obj.DownloadCounter = sop_download_obj.DownloadCounter + 1
            print("Inside if download counter with copunt 1st",sop_download_obj.DownloadCounter)
            sop_download_obj.save()
        except:
            sop_download_obj=SOPDownloadCounter.objects.create(SOPTechnologyDocument_Obj=sop_obj,DownloadCounter=1)
            print("Inside if download counter with copunt 2nd",sop_download_obj.DownloadCounter)
            sop_download_obj.save()

        request.session['sopDownloadCounter_sopHeading'] = sop_download_obj.SOPTechnologyDocument_Obj.SOPTechnologyDocument_Name
        return redirect('sop_document')
    else:
        print("Inside if download counter")
        # sop_obj = SOPTechnologyDocument.objects.get(pk=id)
        # data = datetime.now()
        # data1 = json.dumps(data, default=json_util.default)
        # aList = json.loads(data1)
        # testdata = aList['$date']
        return redirect('sop_document')
   






###DASHBOARD
def RegistryIDNDomainAPIEndpoint():
    response = requests.post("https://registry.gov.in/getidndomaininfo_public_process.php", 
        data="region=&filterform=filterform&current_page=",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    response_data =  response.json()
    return response_data['message']

def passHTMLData():
    html_file_path = './output_table.html'
    # Read the HTML content from the file
    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()   
    return html_content

def dashboard(request):
  
    # Dashboad Count Section Data
    IDN_Ready_Website_data = IDNReadyWebsites.objects.all()
    Total_SOP_Documents_Count = len(SOPTechnologyDocument.objects.all())
    Total_Tools_Count = Tools.objects.filter(Tools_PublishStatus='Published')
    Total_Resource_Count = Document.objects.filter(Document_PublishedStatus='Published')

    # Dashboard Pie Chat Data
    IDN_Websites_Language_Data = IDNReadyWebsitesLanguages.objects.all()
    TLDs = []
    Language_Graph_data = []
    
    # Function to call API for IDN Websites Domains  ( Registry )
    Registry_IDN_API_Data = RegistryIDNDomainAPIEndpoint()
    
    # file_path = '/var/www/html/BHASHANET_PROD_CODE/BHASHANET_PROD/core_app/registry.txt'
    # file_path = env("REGISTRY_FILE_PATH")
    # with open(file_path, 'r', encoding='utf-8') as file:
    #     Registry_IDN_API_Data = file.read()
    
    try:
        infile=open(env('TLD_DATA'), "r")
        for line in infile:
            TLDs.append(get_tld(line))
        infile.close()
    except IOError as err:
        print(err) 

    # TLD Distribution Pie Chart Data
    TLD_COUNT = Counter(TLDs)
    TLD_KEY = list(Counter(TLDs).keys())
    TLD_DATA = list(Counter(TLDs).values())
    
    # Language Wise Websites Count Section 
    for data in IDN_Websites_Language_Data:
        Language_Graph_data.append(len(IDNReadyWebsitesLangugeURLMapping.objects.filter(IDNReadyWebsites_lang=data.id)))
    
    #POST Request 
    if request.method == "POST":
        Selected_Language = request.POST.get('select_data')
        Language_id = Selected_Language.split(",")    
        Test_data = IDNReadyWebsitesLangugeURLMapping.objects.filter(IDNReadyWebsites_lang=Language_id[0])
        Overall_count = len(IDN_Ready_Website_data)
        Selected_count = len(Test_data)
        Remaining_Websites =  Overall_count - Selected_count
        URL_Mapping_data = IDNReadyWebsitesLangugeURLMapping.objects.all()

        context = {
            'Total_IDN_Ready_Websited':len(IDN_Ready_Website_data),
            'Total_SOPs':Total_SOP_Documents_Count,
            'Total_Tools':len(Total_Tools_Count),
            'Total_Resources':len(Total_Resource_Count),
            'Languages': IDN_Websites_Language_Data,
            "URL":URL_Mapping_data,
            "Result":Test_data,
            "ResultCount":len(Test_data),
            "Remaining_Websites":Remaining_Websites,
            "Selected_Language":Language_id[1],
            "TLD_COUNT":TLD_COUNT,
            'TLD_KEY':TLD_KEY,
            'TLD_VAL':TLD_DATA,
            'LGData':Language_Graph_data,
            'Registry_IDN_API_Data':Registry_IDN_API_Data
        }

        return render(request,'core_app/dashboard.html',context)
    
    context = {
            'Total_IDN_Ready_Websited':len(IDN_Ready_Website_data),
            'Total_SOPs':Total_SOP_Documents_Count,
            'Total_Tools':len(Total_Tools_Count),
            "Remaining_Websites":0,
            'Total_Resources':len(Total_Resource_Count),
            'Languages': IDN_Websites_Language_Data,
            "ResultCount":0, 
            "TLD_COUNT":TLD_COUNT,
            'TLD_KEY':TLD_KEY,
            'TLD_VAL':TLD_DATA,
            'LGData':Language_Graph_data,
            'Registry_IDN_API_Data':Registry_IDN_API_Data,
        }
    
    return render(request,'core_app/dashboard.html',context)


##-----------------------------------------TLD VALIDATOR--------------------------------------------------##
def tld_validator(request):
    return render(request, 'core_app/tld_validator.html')


def cat_selected(request):
    blogs_data=Blog.objects.all()
    BlogCategory.objects.update(BlogCategory_Status=False)
    BlogCategory_data=BlogCategory.objects.all()
    page = Paginator(blogs_data, 2)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    count = blogs_data.count()
    context={
        'blogs_data':blogs_data,
        'BlogCategory_data':BlogCategory_data,
        'Status':False,
        'page':page,
        'all_data': 'all_data',
        'selected_id':None,
        'blog_title' : 'none'
    }
    return render(request,'core_app/blog_list.html',context)



def blogs(request,id=None):
    if id:
        blogname = request.session.get('search_blog_string')
        if blogname:
            blog_title=blogname
        else:
            blog_title='none'
            request.session['search_blog_string']='none'
        BlogCategory.objects.update(BlogCategory_Status=False)
        BlogCategory_obj=BlogCategory.objects.get(id=id)
        BlogCategory_obj.BlogCategory_Status=True
        BlogCategory_obj.save()
        BlogCategory_obj=BlogCategory.objects.get(id=id)
        BlogCategory_data=BlogCategory.objects.all()

        if request.method == 'POST' and 'Search-button' in request.POST:
            blogname = request.POST.get('blogname')
            if blogname:
                blog_title=blogname
            else:
                blog_title='none'
            request.session['search_blog_string'] = blogname
            print("Inside cate post search",blogname)

        if blog_title=='none' or blog_title=='':
            blogs_data=Blog.objects.filter(Blog_CategoryType__BlogCategory_Name=BlogCategory_obj.BlogCategory_Name)
        else:
            blogs_data=Blog.objects.filter(Q(Blog_CategoryType__BlogCategory_Name__icontains=BlogCategory_obj.BlogCategory_Name) | Q(Blog_Title__icontains = blogname))
        page = Paginator(blogs_data, 2)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        count = blogs_data.count()
        context={
            'blogs_data':blogs_data,
            'BlogCategory_data':BlogCategory_data,
            'Status':True,
            'page':page,
            'all_data': 'cat_data',
            'selected_id':id,
            'blog_title' : blog_title
        }
        return render(request,'core_app/blog_list.html',context)
    elif request.method == 'POST' and 'Search-button' in request.POST:
        try:
            blogname = request.POST.get('blogname')
        except:
            blogname=''
            return redirect('blogs')
        request.session['search_blog_string'] = blogname
        blog_cat=[]
        Blog_Category_with_satus_true=BlogCategory.objects.filter(BlogCategory_Status=True)
        if Blog_Category_with_satus_true and blogname != 'none':
            for category in Blog_Category_with_satus_true:
                blog_cat.append(category.id)
            cat_id=blog_cat[0]
            blogs_data=Blog.objects.none()
            status=True
            for cat_id in blog_cat:
                blog_cat_obj=BlogCategory.objects.get(id=cat_id)
                blogs_data = blogs_data | Blog.objects.filter(Blog_Title__contains = blogname,Blog_CategoryType=blog_cat_obj)
        else:
            cat_id=None
            status=False
            blogs_data=Blog.objects.none()
            blogs_data = blogs_data | Blog.objects.filter(Blog_Title__contains = blogname)
        #  print("blogs_data",blogs_data)
        BlogCategory_data=BlogCategory.objects.all()
        page = Paginator(blogs_data, 2)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        count = blogs_data.count()
        context={
        'blogs_data':blogs_data,
        'BlogCategory_data':BlogCategory_data,
        'Status':status,
        'page':page,
        'selected_id':cat_id,
        'all_data': 'Search',
        'blog_title' : blogname,
        }
        return render(request,'core_app/blog_list.html',context)  
    else:
        request.session['search_blog_string']='none'
        blogs_data=Blog.objects.all()
        BlogCategory.objects.update(BlogCategory_Status=False)
        BlogCategory_data=BlogCategory.objects.all()
        page = Paginator(blogs_data, 2)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        count = blogs_data.count()
        context={
            'blogs_data':blogs_data,
            'BlogCategory_data':BlogCategory_data,
            'Status':False,
            'page':page,
            'all_data': 'all_data',
            'selected_id':None,
            'blog_title' : 'none'
        }
        return render(request,'core_app/blog_list.html',context)

    

def blog(request,id):
    try:
        blog_data=Blog.objects.get(id=id)
        user_obj=User.objects.get(id=blog_data.Blog_Author.id)
        profile_of_user_obj=UserProfile.objects.get(UserProfile_user=user_obj)
        blogs_data=Blog.objects.filter(Blog_Author=user_obj).order_by('-id')
        context={
            'blog_data':blog_data,
            'blogs_data':blogs_data,
            'profile_of_user_obj':profile_of_user_obj
        }
        return render(request,'core_app/blog_details.html',context)
    except:
        return redirect('blogs')



    

def generate_otp(email):
    #  print("In generate otp")
    
    ## Generate OTP for 
    fixed_digits = 6 
    otp_value = random.randrange(111111, 999999, fixed_digits)
    ## Save OTP Value
    otp_already_exists = OTP_For_IDNRequestForUserWebsites.objects.filter(OTP_Email=email)
    
    if otp_already_exists:
        #  print("email already exists")
        # check OTP count 
        if otp_already_exists[0].OTP_Entered_Count < 10:
            # check time difference between current otp and last otp
            
                #  print("OTP count for this email is less than max count")
                otp_already_exists[0].OTP_Value = otp_value
                otp_already_exists[0].OTP_Entered_Count+=1
                otp_already_exists[0].save()
                
                data={'status': 'success', 'message': "OTP generated"}
                
        else:
            #  print("OTP count limit exceeded")
            expiry_time = otp_already_exists[0].OTP_Created_Date + timedelta(minutes=120) ## timedelta is of 2 hours
            current_time = datetime.now(timezone.utc)
            
            #  print("expiry_time : ", expiry_time)
            #  print("current_time : ", current_time)
            
            time_diff = current_time - expiry_time 
            #  print("Time difference : ", time_diff)
            
            if expiry_time > current_time:
                #  print("OTP count limit exceeded and offset time still not reached")
                data={'status': 'error', 'message': "OTP generate limit exceeded"}
            else:
                otp_already_exists[0].OTP_Value = otp_value
                otp_already_exists[0].OTP_Entered_Count = 1
                otp_already_exists[0].save()
                data={'status': 'success', 'message': "OTP generated"}
    else:
        #  print("email not exists")
        otp_obj = OTP_For_IDNRequestForUserWebsites.objects.create(
            OTP_Email = email,
            OTP_Value = otp_value,
            OTP_Entered_Count = 1
        )
        otp_obj.save()
        data={'status': 'success', 'message': "OTP generated"}
        
        
    # send mail to email address
    RecipentMessage = "OTP for IDN websites request is " + str(otp_value); 
    try:
        email_sent_status = send_mail("OTP for IDN wesbites request", RecipentMessage, env('SERVER_EMAIL'), [email])
        #  print("email status : ", email_sent_status)
    except:
        print("error while sending email")

    return data
        

def validate_otp(email, otp_value):
    #  print("in validate OTP for IDN website request")
    #  print("Email : ", email)
    #  print("OTP value : ", otp_value)
    
    # check email exists
    otp_obj = OTP_For_IDNRequestForUserWebsites.objects.filter(OTP_Email=email)
    
    if otp_obj:
        otp = otp_obj[0].OTP_Value
        otp_status = otp_obj[0].OTP_Status
        otp_generation_date = otp_obj[0].OTP_Created_Date
        
        # check otp is expired
        current_time = datetime.now(timezone.utc)
        expiry_time = otp_generation_date + timedelta(minutes=5) ## otp expiry time is 5 minutes
        
        if expiry_time > current_time:
            #  print("OTP not expired")
            if otp_value == otp:
                if otp_status == True:
                    #  print("OTP expired: Already verified")
                    return False
                else:
                    #  print("OTP verified")
                    return True
            else:
                #  print("wrong OTP")
                return False
        else:
            #  print("OTP expired")
            return False 
    
# # not in use
def idn_websites_request1(request):
    if request.method == 'POST':
        #  print("In POST Request")
        form = IDNRequestForUserWebsitesForm(request.POST)
        email = request.POST.get('IDN_Email')
        otp_value = request.POST.get('otp_value')
        
        # submit form with data
        if 'formsubmit' in request.POST:
            #  print("In POST Request : formsubmit")
            # Check OTP is valid 
            if validate_otp(email, otp_value):
                #  print("OTP valid")
                form.save()
                messages.success(request, "Your request for IDN website submitted successfully", extra_tags="success")
            else:
                messages.error(request, "Invalid OTP", extra_tags="error")
                    
        # submit form for OTP send
        elif 'otpsend' in request.POST:
            #  print("In POST request: otpsend")
            
            if form.is_valid():
                #  print("send OTP")
                for field in form:
                    field.field.widget.attrs['disabled'] = 'disabled'
                ## generate OTP
                resp_data = generate_otp(email)
                #  print("email ", email)
                #  print("Response Data : ", resp_data)
                
                if resp_data['status'] == 'success':
                    messages.success(request, "OTP is sent to " + email, extra_tags="success")
                elif resp_data['status'] == 'error':
                    messages.success(request, resp_data['message'], extra_tags="success")
                    
                return render(request, 'core_app/idn_websites_request.html', {'form': form})
            else:
                # #  print("error ", form.errors)
                #  print("Invalid Form")
                captcha_value = random_captcha_generator()
                captcha_img_generator(captcha_value)
                form.data['captcha_input'] = ''
                form.data['captcha_hidden'] = make_password(captcha_value)
        
    else:
        #  print("In GET request")
        form = IDNRequestForUserWebsitesForm()
        captcha_value = random_captcha_generator()
        captcha_img_generator(captcha_value)
        #  print("captcha value ", captcha_value)
        form.fields['captcha_hidden'].initial = make_password(captcha_value)
         
    return render(request, 'core_app/idn_websites_request.html', {'form': form})


@csrf_exempt
def idn_websites_request_AJAX(request):
    categories = IDNRequestForUserWebsitesCategories.objects.filter(website_status="Active")
    #  print("categories: ", categories)
    
    if request.method == 'POST':
        #  print("In POST Request")
        org_name = request.POST.get('orgName')
        email = request.POST.get('email')
        category = request.POST.get('categories')
        IDN_English_Domain = request.POST.get('englishDomain')
        idn_lang = request.POST.getlist('selectedLang')
        idn_urls = request.POST.getlist('inputData')
        captcha_value = request.POST.get('captcha_value')
        captcha_hidden = request.POST.get('captcha_hidden')
        assistance = request.POST.get('assistance')
        assistLang = request.POST.get('assistLang')
        remark = request.POST.get('remark')
        
        #  print("ORG Name ", org_name)
        #  print("Email ", email)
        #  print("Category ", category)
        #  print("IDN_English_Domain ", IDN_English_Domain)
        #  print("IDN categories ", idn_lang)
        #  print("IDN categories ", idn_urls)
        #  print("assistance ", assistance)
        #  print("captcha_hidden ", assistLang)
        #  print("captcha_hidden ", remark)
        #  print("captcha_value ", captcha_value)
        #  print("captcha_hidden ", captcha_hidden)
        
        # validate the form data
        response = validate_IDNRequestForUserWebsitesAJAXForm(org_name, email, category, IDN_English_Domain, captcha_value, captcha_hidden, assistance, assistLang, remark)
        if response['status'] == 'error':
            #  print("error in field : ", response['field_name'])
            #  print("error message : ", response['message'])
            return JsonResponse({'message': response['message']}, status=400)
        
        # get all IDN URLs 
        my_list = []
        for k, v in zip(idn_lang, idn_urls):
            if k and v:
                my_list.append({"language": k, "url": v})
        print(my_list)
        
        # check domain already exists or not
        ## clean domain url
        cleaned_eng_domain = clean_URL(IDN_English_Domain)
        if IDNRequestForUserWebsites.objects.filter(IDN_English_Domain=cleaned_eng_domain).exists():
            return JsonResponse({'message': "Domain with name '" + IDN_English_Domain + "' already exists"}, status=400)
        if assistance == 'yes':
            need_assistance=True
        else:
            need_assistance=False
            
        idn_request_obj = IDNRequestForUserWebsites.objects.create(
            submitter_name = org_name,
            IDN_Email = email,
            IDN_Category = IDNRequestForUserWebsitesCategories.objects.get(IDN_category_name=category),
            IDN_English_Domain = cleaned_eng_domain,
            IDN_URLS = my_list,
            need_assistance = need_assistance,
            assist_langs = assistLang,
            assist_remark = remark
        )
        idn_request_obj.save()

        return JsonResponse({'message': "Your request for IDN website submitted successfully"}, status=200)
        # messages.success(request, "Your request for IDN website submitted successfully", extra_tags="success")
    else:
        print("In GET request")
        
    captcha_value = random_captcha_generator()
    captcha_img_generator(captcha_value)
    captcha_hidden = make_password(captcha_value)
    return render(request, 'core_app/idn_websites_request_AJAX.html', {'categories': categories, 'captcha_value' : captcha_value, 'captcha_hidden': captcha_hidden})



#----------------------------------------TEST_SUPPORT PAGE --------------------- #

def test_support(request):
    
    return render(request, 'core_app/support_new.html')

@login_required(login_url="login_view")
def admindashboard(request):
    
    Registry_IDN_API_Data = RegistryIDNDomainAPIEndpoint()
    # Registry_IDN_API_Data = passHTMLData()
    
    myconn = mysql.connector.connect(host = env('OS_DB_HOST'), user = env('OS_DB_USER'), passwd = env('OS_DB_PASSWORD'),database = env('OS_DB_NAME'))  
    Open_Ticket_count = 0
    Closed_Ticket_count = 0
    Resolved_Ticket_count = 0
    cur = myconn.cursor()  

    try:  
        cur.execute("select name from  ost_ticket_status INNER JOIN ost_ticket ON ost_ticket_status.id = ost_ticket.status_id")  
        open_ticket_data = cur.fetchall()
        #  print(open_ticket_data)
        for x in open_ticket_data: 
            if x[0] == "Open":
                Open_Ticket_count += 1 
            elif x[0] == "Closed":
                Closed_Ticket_count += 1
            elif x[0] == "Resolved":
                Resolved_Ticket_count += 1

    except:  
        myconn.rollback()  
    
    cur2 = myconn.cursor()  
    
    try:  
        cur2.execute("SELECT ost_ticket_status.name AS ticket_status, ost_ticket.lastupdate AS ticket_lastupdate_date,ost_user.name AS assigned_user,ost_ticket.created AS ticket_created ,ost_ticket.number AS ticket_number FROM ost_ticket JOIN ost_ticket_status ON ost_ticket.status_id = ost_ticket_status.id JOIN ost_user ON ost_ticket.user_id = ost_user.id")  
        ticket_data = cur2.fetchall()
        #  print(ticket_data)

    except:  
        myconn.rollback()  
        
    myconn.close()  

    #  print(Open_Ticket_count)
    
    with open('updated_file.json') as f:
        Tabledata = json.load(f) 
        
    context = {
        "Open_Ticket_count":Open_Ticket_count,
        'Closed_Ticket_count':Closed_Ticket_count,
        'Resolved_Ticket_count':Resolved_Ticket_count,
        'ticket_data':ticket_data,
        'Registry_IDN_API_Data':Registry_IDN_API_Data,
        'Tabledata': Tabledata,

    }
  
    return render(request, 'core_app/Admin_Dashboard.html',context)




# CELERY TASKS

def test_celery(request):
    data = test_func.delay()
    response = data.get()
    #  print("Return Data : ", response)
    return HttpResponse("Done")


    
    
# IDN READINESS VIEWS

def update_json(request):
    new_url = request.POST.get('url')
    new_lang = request.POST.get('language')
   
    # Read the JSON file
    with open('file.json', encoding='utf-8' ) as f:
        data = json.load(f)

    # Add new key-value pair
    data[new_url] = {
        "Language": new_lang,
        "domain_token": "",
        "ssl_token": "",
        "content_token": ""
    }

    # Write the updated JSON data back to the file
    with open('file.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # Convert dictionary back to JSON
    updated_json_data = json.dumps(data)
    # crawler_task.delay()
    messages.info(request,"Your data would be populated in IDN Readiness Index List within 24 Hours ")
    return redirect('display_table2')

def display_table2(request):
    with open('updated_file.json') as f:
        Tabledata = json.load(f) 
    return render(request, 'core_app/Admin_Dashboard.html', {'Tabledata': Tabledata})


def idn_rediness_dashboard(request):
    # Read the JSON file
    with open('file.json', encoding='utf-8' ) as f:
        data = json.load(f)
        timeout_seconds = 10  # Set the timeout period to 10 seconds

        # Fetch all keys in the JSON data
        keys = data.keys()
        
        # Print all keys
        for url in keys:
            # CHECK IF URL RUNS OR NOT 
            try:    
                response = requests.get(url, verify=False,timeout=timeout_seconds)
                if response.status_code == 200:
                    data[url]["domain_token"] = True
        
            except requests.ConnectionError as e:
                data[url]["domain_token"] =  False    

            # CHECK IF SSL IS VALID OR NOT 
            try:
                response = requests.get(url,verify=certifi.where())
                #  print("SSL RESPONSE ", response)
                if response.status_code == 200:
                    data[url]["ssl_token"] =  True                  
            except requests.ConnectionError:
                data[url]["ssl_token"] =  False
            except ssl.SSLError:
                data[url]["ssl_token"] =  False
       
            # CHECK LANGUAGE OF CONTENT 
            try:
                # Fetch HTML content from the URL
                response = requests.get(url,verify=False)
                #  print("RESPONSE CODE ---------------------------- ",response.status_code)
                if response.status_code == 200:
                    # Parse HTML content
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Extract text content from HTML
                    text = soup.get_text()
                   
                    # Detect language of the text
                    try:
                        service_url = 'http://gist-nlp-cip:8080/languageIdentify'
                        headers = {'User-Agent': 'Mozilla/5.0'}  # Example of headers
                        myobj = {"ip_text": text}
                        x = requests.post(service_url, headers=headers, json= myobj)
                        data[url]["content_token"] = json.loads(x.text)['Output']
                    except requests.ConnectionError as e:
                        #  print("Exception -----", e)
                        #  print("Service Not Available ")
                        data[url]["content_token"] = "Service Not Available"
                else:
                    #  print(f"Failed to fetch URL. Status code: {response.status_code}")
                    data[url]["content_token"] = False

            except requests.ConnectionError as e:
                #  print(f"Connection error: {e}")
                data[url]["content_token"] = False

            except Exception as e:
                #  print(f"Error occurred: {e}")
                data[url]["content_token"] = False
    # Convert dictionary back to JSON
    updated_json_data = json.dumps(data)

    # Write updated JSON data to a new file
    with open('updated_file.json', 'w') as outfile:
        outfile.write(updated_json_data)
    # Print updated JSON
    #  print(updated_json_data)
    return render(request,'core_app/home.html',{'updated_json_data':updated_json_data})





def RenderPageWithPathAndLang(request, path):
    lang=''
    domain=''
    status1=False
    status2=False
    maindomain = request.build_absolute_uri().split('/')[2]
    requesteddomainwithoutport=maindomain.split(':')[0]
    with open(env('LANGUAGE_DOMAINS'), 'r',encoding="utf8") as j:
            dom = json.loads(j.read())
    for data in range(len(dom)):
        for key,value in dom[data].items():
            filterdomain1=value.split('/')[2]
            filterdomain2=filterdomain1.split(':')[0]
            # print("domain from file",filterdomain2)
            if requesteddomainwithoutport == filterdomain2 :
                domain=value
                lang=key
                status1=True
    
    with open(env('LANGUAGE_PATHS'), 'r',encoding="utf8") as j:
        contents = json.loads(j.read())
    pathrender='/'
    for content in range(len(contents)):
        for cont in range(len(contents[content])):
            for key, value in contents[content]['mainpath'].items():
                if value == request.path:
                    #  print("valueeee",value,request.path)
                    pathrender=value
                    lang=key
                    status2=True
                    #  print("pathhgcffgjgjhfhgffcjv",pathrender,lang)
    if status1 and status2:
        #  print("final path render and lang9099090909090900",domain+pathrender)
        response = HttpResponseRedirect(domain+pathrender)
        return response
    else:
        response = render(request, 'core_app/errors/404.html')
        response.status_code = 404
        return response



def RenderPageWithPathAndLangId(request, path,id):
    lang=''
    domain=''
    status1=False
    status2=False
    maindomain = request.build_absolute_uri().split('/')[2]
    requesteddomainwithoutport=maindomain.split(':')[0]
    with open(env('LANGUAGE_DOMAINS'), 'r',encoding="utf8") as j:
            dom = json.loads(j.read())
    for data in range(len(dom)):
        for key,value in dom[data].items():
            filterdomain1=value.split('/')[2]
            filterdomain2=filterdomain1.split(':')[0]
            # print("domain from file",filterdomain2)
            if requesteddomainwithoutport == filterdomain2 :
                domain=value
                lang=key
                status1=True
    
    with open(env('LANGUAGE_PATHS'), 'r',encoding="utf8") as j:
        contents = json.loads(j.read())
    pathrender='/'
    for content in range(len(contents)):
        for cont in range(len(contents[content])):
            for key, value in contents[content]['mainpath'].items():
                if value == '/'+request.path.split('/')[1]:
                    #  print("valueeee",value,request.path)
                    pathrender=value
                    lang=key
                    status2=True
                    #  print("pathhgcffgjgjhfhgffcjv",pathrender,lang)

    if status1 and status2:
        #  print("final path render and lang9099090909090900",domain+pathrender+'/'+id)
        response = HttpResponseRedirect(domain+pathrender+'/'+id)
        return response
    else:
        response = render(request, 'core_app/errors/404.html')
        response.status_code = 404
        return response



def RenderPageWithPathAndLangIdToken(request,path,uid,token):
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
    lang=''
    domain=''
    status1=False
    status2=False
    maindomain = request.build_absolute_uri().split('/')[2]
    requesteddomainwithoutport=maindomain.split(':')[0]
    with open(env('LANGUAGE_DOMAINS'), 'r',encoding="utf8") as j:
            dom = json.loads(j.read())
    for data in range(len(dom)):
        for key,value in dom[data].items():
            filterdomain1=value.split('/')[2]
            filterdomain2=filterdomain1.split(':')[0]
            # print("domain from file",filterdomain2)
            if requesteddomainwithoutport == filterdomain2 :
                domain=value
                lang=key
                status1=True
    
    with open(env('LANGUAGE_PATHS'), 'r',encoding="utf8") as j:
        contents = json.loads(j.read())
    pathrender='/'
    for content in range(len(contents)):
        for cont in range(len(contents[content])):
            for key, value in contents[content]['mainpath'].items():
                if value == '/'+request.path.split('/')[1]:
                    # print("valueeee",value,request.path)
                    pathrender=value
                    lang=key
                    status2=True
                    # print("pathhgcffgjgjhfhgffcjv",pathrender,lang)

    if status1 and status2:
        # print("final path render and lang9099090909090900",domain+pathrender+'/'+uid +'/'+token)
        response = HttpResponseRedirect(domain+pathrender+'/'+uid+'/'+token)
        return response
    else:
        response = render(request, 'core_app/errors/404.html')
        response.status_code = 404
        return response
    
    


    