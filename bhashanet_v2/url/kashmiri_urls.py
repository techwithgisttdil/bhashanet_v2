# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset

# -----ADDED BY SHWETA PATIL -------
Translation_urlpatterns_kashmiri = [
    path('گَرٕ', preprocesslangset(core_views.home), name='home'),
    path('privacypolicyks', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('termsandconditionsks', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('uaindiaprogrammeks', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('IDNCCTLDks', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('bestpracticesks', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('EAIks', preprocesslangset(core_views.EAI), name='EAI'),
    path('UAks', preprocesslangset(core_views.UA), name='UA'),
    path('toolsks', preprocesslangset(core_views.tools), name='tools'),
    path('unicode_punycode_generatorks', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('unicode_fontsks',preprocesslangset( core_views.unicode_fonts), name='unicode_fonts'),
    path('transliterationks', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('script_detectionks', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('domain_validatorks',preprocesslangset( core_views.domain_validator), name='domain_validator'),
    path('email_validatorks', preprocesslangset(core_views.email_validator), name='email_validator'),
    path('feedbackks',preprocesslangset( core_views.feedback), name='feedback'),
    path('becomeuareadyks',preprocesslangset( core_views.becomeuaready), name='becomeuaready'),
    path('FAQSks',preprocesslangset( core_views.FAQs), name='FAQs'),
    path('documentPageks',preprocesslangset( core_views.documentPage), name='documentPage'),
    path('documentDataks', preprocesslangset(core_views.documentData), name='documentData'),
    path('supportks', preprocesslangset(core_views.support), name='support'),
    path('search_resultsks', preprocesslangset(core_views.search_results), name='search_results'),
    path('idn_websitesks/<int:id>', preprocesslangset(core_views.idn_websites), name='idn_websites'),
    path('eventks', preprocesslangset(core_views.event), name='event'),
    path('galleryks', preprocesslangset(core_views.gallery), name='gallery'),
    path('language_detectionks', preprocesslangset(core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardks', preprocesslangset(core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_tech_pageks', preprocesslangset(core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pageks', preprocesslangset(core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documentks', preprocesslangset(core_views.sop_document), name='sop_document'), 
    path('tld_validatorks', preprocesslangset(core_views.tld_validator), name='tld_validator'),
    path('dashboardks',preprocesslangset( core_views.dashboard), name='dashboard'),
    path('blogsks',preprocesslangset( core_views.blogs), name='blogs'),
    # path('cat_selectedks/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('blogsks/<str:id>',preprocesslangset( core_views.blogs), name='blogs'),
    path('blogks/<str:id>',preprocesslangset( core_views.blog), name='blog'),
    path('test_supportboro',preprocesslangset( core_views.test_support), name='test_support'),
    path('idn_websites_requestks',preprocesslangset( core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_blogks',preprocesslangset( user_views.add_blog), name='add_blog'),
    path('edit_blogks/<str:id>',preprocesslangset( user_views.edit_blog), name='edit_blog'),
    path('delete_blogks/<str:id>',preprocesslangset( user_views.delete_blog), name='delete_blog'),
    path('blog_datatableks',preprocesslangset( user_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>',preprocesslangset( user_views.search_blog), name='search_blog'), # Pending in json file
    path('loginks',preprocesslangset( user_views.login_view), name='login_view'),
    path('registerks', preprocesslangset(user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutks',preprocesslangset( user_views.logout_view), name='logout_view'),
    path('change_passwordks',preprocesslangset( user_views.change_password_view), name='change_password'),
    path('forgot_passwordks',preprocesslangset( user_views.forgot_password_view), name='forgot_password'),
    path('password_creationks/<uid>/<token>',preprocesslangset( user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listks',preprocesslangset( topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listks',preprocesslangset( user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topicks', preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionks/<slug:topic_slug>',preprocesslangset( view_topic_discussion), name="view_topic_discussion"),
    path('submit_answerks/<slug:topic_slug>',preprocesslangset( submit_answer), name='submit_answer'),
    path('upvote_answerks',preprocesslangset( upvote_answer_view), name='upvote_answer_view'),
    path('user_profile',preprocesslangset( user_views.user_profile_view), name='user_profile'), # Pending in json file
]   