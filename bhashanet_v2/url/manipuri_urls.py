# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset


Translation_urlpatterns_manipuri = [
    path('মরুওইবা_লৈমাই', preprocesslangset(core_views.home), name='home'),
    path('প্রাইবেসী_পোলিসী', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('তর্ম্স_এন্দ_কন্দিসন্স', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('য়ুএআইইন্দিয়াপ্রোগ্রাম', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('আইদীএনসীসীতীএলদী', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('খ্বাইদগী_ফবা_প্রাক্তিক্সসিং', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('ইএআই', preprocesslangset(core_views.EAI), name='EAI'),
    path('য়ূএ', preprocesslangset(core_views.UA), name='UA'),
    path('খুৎলাইসিং', preprocesslangset(core_views.tools), name='tools'),
    path('য়ূনিকোদ_পুনিকোদ_জেনেরেতর', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('য়ূনিকোদ_ফোন্ত্স', preprocesslangset(core_views.unicode_fonts), name='unicode_fonts'),
    path('ত্রান্সলিতরেসন', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('ময়েক_খংদোকপা', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('দোমেন_ভেলিদেতর', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('ইমেল_ভেলিদেতর', preprocesslangset(core_views.email_validator), name='email_validator'),
    path('ফিদবেক', preprocesslangset(core_views.feedback), name='feedback'),
    path('বিকময়ুএরেদি', preprocesslangset(core_views.becomeuaready), name='becomeuaready'),
    path('এফএক্য়ূএস', preprocesslangset(core_views.FAQs), name='FAQs'),
    path('চে-চাংগীলৈমাই', preprocesslangset(core_views.documentPage), name='documentPage'),
    path('চে-চাং_দেতা', preprocesslangset(core_views.documentData), name='documentData'),
    path('সপোর্ত', preprocesslangset(core_views.support), name='support'),
    path('সর্চ_রিজল্তসিং', preprocesslangset(core_views.search_results), name='search_results'),
    path('idn_websitesMn/<int:id>', preprocesslangset(core_views.idn_websites), name='idn_websites'),
    path('থৌরম', preprocesslangset(core_views.event), name='event'),
    path('gallerymni', preprocesslangset(core_views.gallery), name='gallery'),
    path('language_detectionm', preprocesslangset(core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardmni', preprocesslangset(core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_tech_pagemni', preprocesslangset(core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pagemni',preprocesslangset( core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documentmni', preprocesslangset(core_views.sop_document), name='sop_document'), 
    path('tld_validatormni',preprocesslangset( core_views.tld_validator), name='tld_validator'),
    path('dashboardmni',preprocesslangset( core_views.dashboard), name='dashboard'),
    path('blogsmni', preprocesslangset(core_views.blogs), name='blogs'),
    # path('cat_selectedmni/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('blogsmni/<str:id>', preprocesslangset(core_views.blogs), name='blogs'),
    path('blogmni/<str:id>',preprocesslangset( core_views.blog), name='blog'),
    path('test_supportmni',preprocesslangset( core_views.test_support), name='test_support'),
    path('idn_websites_requestmni', preprocesslangset(core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_blogmni',preprocesslangset( user_views.add_blog), name='add_blog'),
    path('edit_blogmni/<str:id>', preprocesslangset(user_views.edit_blog), name='edit_blog'),
    path('delete_blogmni/<str:id>', preprocesslangset(user_views.delete_blog), name='delete_blog'),
    path('blog_datatablemni', preprocesslangset(user_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>',preprocesslangset( user_views.search_blog), name='search_blog'), # Pending in json file
    path('loginmni', preprocesslangset(user_views.login_view), name='login_view'),
    path('registermni',preprocesslangset( user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutmni',preprocesslangset( user_views.logout_view), name='logout_view'),
    path('change_passwordmni',preprocesslangset( user_views.change_password_view), name='change_password'),
    path('forgot_passwordmni',preprocesslangset( user_views.forgot_password_view), name='forgot_password'),
    path('password_creationmni/<uid>/<token>',preprocesslangset( user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listmni',preprocesslangset( topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listmni',preprocesslangset( user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topicmni',preprocesslangset( add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionmni/<slug:topic_slug>',preprocesslangset( view_topic_discussion), name="view_topic_discussion"),
    path('submit_answermni/<slug:topic_slug>', preprocesslangset(submit_answer), name='submit_answer'),
    path('upvote_answermni',preprocesslangset(upvote_answer_view), name='upvote_answer_view'),
    path('test_taskmni', preprocesslangset(core_views.test_celery), name="test_task"),
    path('user_profile',preprocesslangset( user_views.user_profile_view), name='user_profile'), # Pending in json file
]   
