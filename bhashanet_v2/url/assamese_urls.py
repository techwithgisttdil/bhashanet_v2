# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset


Translation_urlpatterns_assamese = [
    path('গৃহ', preprocesslangset(core_views.home), name='home'),
    path('privacypolicyas', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('termsandconditionsas', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('uaindiaprogrammeas', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('IDNCCTLDas', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('bestpracticesas', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('EAIas', preprocesslangset(core_views.EAI), name='EAI'),
    path('UAas', preprocesslangset(core_views.UA), name='UA'),
    path('toolsas', preprocesslangset(core_views.tools), name='tools'),
    path('unicode_punycode_generatoras', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('unicode_fontsas', preprocesslangset(core_views.unicode_fonts), name='unicode_fonts'),
    path('transliterationas', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('script_detectionas', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('domain_validatoras', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('email_validatoras', preprocesslangset(core_views.email_validator), name='email_validator'),
    path('feedbackas', preprocesslangset(core_views.feedback), name='feedback'),
    path('becomeuareadyas', preprocesslangset(core_views.becomeuaready), name='becomeuaready'),
    path('FAQSas', preprocesslangset(core_views.FAQs), name='FAQs'),
    path('documentPageas', preprocesslangset(core_views.documentPage), name='documentPage'),
    path('documentDataas', preprocesslangset(core_views.documentData), name='documentData'),
    path('supportas', preprocesslangset(core_views.support), name='support'),
    path('search_resultsas', preprocesslangset(core_views.search_results), name='search_results'),
    path('idn_websitesas/<int:id>', preprocesslangset(core_views.idn_websites), name='idn_websites'),
    path('eventas', preprocesslangset(core_views.event), name='event'),
    path('galleryas', preprocesslangset(core_views.gallery), name='gallery'),
    path('language_detectionas', preprocesslangset(core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardas', preprocesslangset(core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_tech_pageas', preprocesslangset(core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pageas', preprocesslangset(core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documentas', preprocesslangset(core_views.sop_document), name='sop_document'), 
    path('tld_validatoras', preprocesslangset(core_views.tld_validator), name='tld_validator'),
    path('dashboardas', preprocesslangset(core_views.dashboard), name='dashboard'),
    path('blogsas', preprocesslangset(core_views.blogs), name='blogs'),
    # path('cat_selectedas/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('blogsas/<str:id>', preprocesslangset(core_views.blogs), name='blogs'),
    path('blogas/<str:id>', preprocesslangset(core_views.blog), name='blog'),
    path('test_supportASS', preprocesslangset(core_views.test_support), name='test_support'),
    path('idn_websites_requestas', preprocesslangset(core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_blogas', preprocesslangset(user_views.add_blog), name='add_blog'),
    path('edit_blogas/<str:id>', preprocesslangset(user_views.edit_blog), name='edit_blog'),
    path('delete_blogas/<str:id>', preprocesslangset(user_views.delete_blog), name='delete_blog'),
    path('blog_datatableas', preprocesslangset(user_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>', preprocesslangset(user_views.search_blog), name='search_blog'), # Pending in json file
    path('loginas', preprocesslangset(user_views.login_view), name='login_view'),
    path('registeras', preprocesslangset(user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutas', preprocesslangset(user_views.logout_view), name='logout_view'),
    path('change_passwordas', preprocesslangset(user_views.change_password_view), name='change_password'),
    path('forgot_passwordas', preprocesslangset(user_views.forgot_password_view), name='forgot_password'),
    path('password_creationas/<uid>/<token>', preprocesslangset(user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listas', preprocesslangset(topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listas', preprocesslangset(user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topicas', preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionas/<slug:topic_slug>', preprocesslangset(view_topic_discussion), name="view_topic_discussion"),
    path('submit_answeras/<slug:topic_slug>', preprocesslangset(submit_answer), name='submit_answer'),
    path('upvote_answeras', preprocesslangset(upvote_answer_view), name='upvote_answer_view'),
    path('test_taskas', preprocesslangset(core_views.test_celery), name="test_task"),
    path('user_profile', preprocesslangset(user_views.user_profile_view), name='user_profile'), # Pending in json file
    
]   