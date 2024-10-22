# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset



Translation_urlpatterns_urdu = [
    path('گھر', preprocesslangset(core_views.home), name='home'),
    path('privacypolicyUR', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('termsandconditionsUR', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('uaindiaprogrammeUR', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('IDNCCTLDUR', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('bestpracticesUR', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('EAIUR', preprocesslangset(core_views.EAI), name='EAI'),
    path('UAUR', preprocesslangset(core_views.UA), name='UA'),
    path('toolsUR', preprocesslangset(core_views.tools), name='tools'),
    path('unicode_punycode_generatorUR', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('unicode_fontsUR', preprocesslangset(core_views.unicode_fonts), name='unicode_fonts'),
    path('transliterationUR', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('script_detectionUR', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('domain_validatorUR', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('email_validatorUR',preprocesslangset( core_views.email_validator), name='email_validator'),
    path('feedbackUR', preprocesslangset(core_views.feedback), name='feedback'),
    path('becomeuareadyUR', preprocesslangset(core_views.becomeuaready), name='becomeuaready'),
    path('FAQSUR', preprocesslangset(core_views.FAQs), name='FAQs'),
    path('documentPageUR', preprocesslangset(core_views.documentPage), name='documentPage'),
    path('documentDataUR', preprocesslangset(core_views.documentData), name='documentData'),
    path('supportUR', preprocesslangset(core_views.support), name='support'),
    path('search_resultsUR', preprocesslangset(core_views.search_results), name='search_results'),
    path('ఐడిఎన్వెబ్‌సైట్‌లు/<int:id>',preprocesslangset( core_views.idn_websites), name='idn_websites'),
    path('eventUR',preprocesslangset( core_views.event), name='event'),
    path('galleryUR',preprocesslangset( core_views.gallery), name='gallery'),
    path('language_detectionUR', preprocesslangset(core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardur',preprocesslangset( core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_tech_pageur',preprocesslangset( core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pageur', preprocesslangset(core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documentur', preprocesslangset(core_views.sop_document), name='sop_document'), 
    path('tld_validatorur',preprocesslangset( core_views.tld_validator), name='tld_validator'),
    path('dashboardur', preprocesslangset(core_views.dashboard), name='dashboard'),
    path('blogsur',preprocesslangset( core_views.blogs), name='blogs'),
    # path('cat_selectedUR/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('blogsur/<str:id>',preprocesslangset( core_views.blogs), name='blogs'),
    path('blogur/<str:id>',preprocesslangset( core_views.blog), name='blog'),
    path('test_supportboro',preprocesslangset( core_views.test_support), name='test_support'),
    path('idn_websites_requestur', preprocesslangset(core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_blogur', preprocesslangset(user_views.add_blog), name='add_blog'),
    path('edit_blogur/<str:id>',preprocesslangset( user_views.edit_blog), name='edit_blog'),
    path('delete_blogur/<str:id>', preprocesslangset(user_views.delete_blog), name='delete_blog'),
    path('blog_datatableur', preprocesslangset(user_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>',preprocesslangset( user_views.search_blog), name='search_blog'), # Pending in json file
    path('loginur', preprocesslangset(user_views.login_view), name='login_view'),
    path('registerur', preprocesslangset(user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutur', preprocesslangset(user_views.logout_view), name='logout_view'),
    path('change_passwordur', preprocesslangset(user_views.change_password_view), name='change_password'),
    path('forgot_passwordur', preprocesslangset(user_views.forgot_password_view), name='forgot_password'),
    path('password_creationur/<uid>/<token>',preprocesslangset( user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listur', preprocesslangset(topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listur', preprocesslangset(user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topicur', preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionur/<slug:topic_slug>', preprocesslangset(view_topic_discussion), name="view_topic_discussion"),
    path('submit_answerur/<slug:topic_slug>',preprocesslangset( submit_answer), name='submit_answer'),
    path('upvote_answerur', preprocesslangset(upvote_answer_view), name='upvote_answer_view'),
    path('test_taskur', preprocesslangset(core_views.test_celery), name="test_task"),
    path('user_profile',preprocesslangset( user_views.user_profile_view), name='user_profile'), # Pending in json file
]   