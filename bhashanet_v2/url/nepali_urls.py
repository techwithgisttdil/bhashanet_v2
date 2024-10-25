# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset

# -----ADDED BY SHWETA PATIL -------
Translation_urlpatterns_nepali = [
    path('होमनेपाली', preprocesslangset(core_views.home), name='home'),
    path('privacypolicyne', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('termsandconditionsne', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('uaindiaprogrammene', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('IDNCCTLDne', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('bestpracticesne', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('EAIne', preprocesslangset(core_views.EAI), name='EAI'),
    path('UAne', preprocesslangset(core_views.UA), name='UA'),
    path('toolsne', preprocesslangset(core_views.tools), name='tools'),
    path('unicode_punycode_generatorne', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('unicode_fontsne',preprocesslangset( core_views.unicode_fonts), name='unicode_fonts'),
    path('transliterationne', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('script_detectionne',preprocesslangset( core_views.script_detection), name='script_detection'),
    path('domain_validatorne',preprocesslangset( core_views.domain_validator), name='domain_validator'),
    path('email_validatorne',preprocesslangset( core_views.email_validator), name='email_validator'),
    path('feedbackne',preprocesslangset( core_views.feedback), name='feedback'),
    path('becomeuareadyne',preprocesslangset( core_views.becomeuaready), name='becomeuaready'),
    path('FAQSne',preprocesslangset( core_views.FAQs), name='FAQs'),
    path('documentPagene', preprocesslangset(core_views.documentPage), name='documentPage'),
    path('documentDatane', preprocesslangset(core_views.documentData), name='documentData'),
    path('supportne',preprocesslangset( core_views.support), name='support'),
    path('search_resultsne',preprocesslangset( core_views.search_results), name='search_results'),
    path('idn_websitesne/<int:id>', preprocesslangset(core_views.idn_websites), name='idn_websites'),
    path('eventne', preprocesslangset(core_views.event), name='event'),
    path('galleryne', preprocesslangset(core_views.gallery), name='gallery'),
    path('language_detectionne', preprocesslangset(core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardne', preprocesslangset(core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_tech_pagene', preprocesslangset(core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pagene',preprocesslangset( core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documentne', preprocesslangset(core_views.sop_document), name='sop_document'), 
    path('tld_validatorne', preprocesslangset(core_views.tld_validator), name='tld_validator'),
    path('dashboardne', preprocesslangset(core_views.dashboard), name='dashboard'),
    path('blogsne', preprocesslangset(core_views.blogs), name='blogs'),
    # path('cat_selectedne/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('blogsne/<str:id>', preprocesslangset(core_views.blogs), name='blogs'),
    path('blogne/<str:id>',preprocesslangset( core_views.blog), name='blog'),
    path('test_supportne',preprocesslangset( core_views.test_support), name='test_support'),
    path('idn_websites_requestne',preprocesslangset( core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_blogne',preprocesslangset( user_views.add_blog), name='add_blog'),
    path('edit_blogne/<str:id>',preprocesslangset(user_views.edit_blog), name='edit_blog'),
    path('delete_blogne/<str:id>', preprocesslangset(user_views.delete_blog), name='delete_blog'),
    path('blog_datatablene',preprocesslangset( user_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>',preprocesslangset( user_views.search_blog), name='search_blog'), # Pending in json file
    path('loginne',preprocesslangset( user_views.login_view), name='login_view'),
    path('registerne',preprocesslangset( user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutne', preprocesslangset(user_views.logout_view), name='logout_view'),
    path('change_passwordne',preprocesslangset( user_views.change_password_view), name='change_password'),
    path('forgot_passwordne',preprocesslangset( user_views.forgot_password_view), name='forgot_password'),
    path('password_creationne/<uid>/<token>',preprocesslangset( user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listne',preprocesslangset( topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listne', preprocesslangset(user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topicne', preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionne/<slug:topic_slug>',preprocesslangset( view_topic_discussion), name="view_topic_discussion"),
    path('submit_answerne/<slug:topic_slug>', preprocesslangset(submit_answer), name='submit_answer'),
    path('upvote_answerne',preprocesslangset( upvote_answer_view), name='upvote_answer_view'),
    path('user_profile',preprocesslangset( user_views.user_profile_view), name='user_profile'), # Pending in json file
]   

