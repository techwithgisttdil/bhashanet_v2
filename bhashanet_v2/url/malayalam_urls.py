# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset



Translation_urlpatterns_malayalam = [
    path('വീട്', preprocesslangset(core_views.home), name='home'),
    path('സ്വകാര്യതാനയം', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('ഉപാധികളുംനിബന്ധനകളും', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('യുഎഐഇന്ത്യപ്രോഗ്രാം', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('ഐഡിഎൻസിടിഎൽഡി', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('നല്ലശീലങ്ങൾ', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('വരിക', preprocesslangset(core_views.EAI), name='EAI'),
    path('സാർവത്രികസ്വീകാര്യത', preprocesslangset(core_views.UA), name='UA'),
    path('ഉപകരണങ്ങൾ', preprocesslangset(core_views.tools), name='tools'),
    path('യൂണികോഡ്പ്യൂണിക്ക്കോഡ്ജനറേറ്റർ',preprocesslangset( core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('യൂണികോഡ്ഫോണ്ട്', preprocesslangset(core_views.unicode_fonts), name='unicode_fonts'),
    path('ലിപ്യന്തരണം', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('സ്ക്രിപ്റ്റ്കണ്ടെത്തൽ',preprocesslangset( core_views.script_detection), name='script_detection'),
    path('ഡൊമെയ്ൻചെക്കർ', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('ഇമെയിൽവാലിഡേറ്റർ', preprocesslangset(core_views.email_validator), name='email_validator'),
    path('പ്രതികരണം', preprocesslangset(core_views.feedback), name='feedback'),
    path('തയ്യാറാകും',preprocesslangset( core_views.becomeuaready), name='becomeuaready'),
    path('ചോദിക്കേണ്ടചോദ്യങ്ങൾ',preprocesslangset( core_views.FAQs), name='FAQs'),
    path('പ്രമാണപേജ്', preprocesslangset(core_views.documentPage), name='documentPage'),
    path('ഡോക്യുമെന്റ്ഡാറ്റ', preprocesslangset(core_views.documentData), name='documentData'),
    path('പിന്തുണ', preprocesslangset(core_views.support), name='support'),
    path('തിരയൽഫലങ്ങൾ', preprocesslangset(core_views.search_results), name='search_results'),
    path('ഐഡിഎൻ_വെബ്സൈറ്റുകൾ/<int:id>', preprocesslangset(core_views.idn_websites), name='idn_websites'),
    path('സംഭവം', preprocesslangset(core_views.event), name='event'),
    path('ഗാലറി', preprocesslangset(core_views.gallery), name='gallery'),
    path('language_detectionml',preprocesslangset( core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardml',preprocesslangset( core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_tech_pageml', preprocesslangset(core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pageMalayalam', preprocesslangset(core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documentml',preprocesslangset( core_views.sop_document), name='sop_document'), 
    path('tld_validatorml', preprocesslangset(core_views.tld_validator), name='tld_validator'),
    path('ഡാഷ്ബോർഡ്', preprocesslangset(core_views.dashboard), name='dashboard'),
    path('ബ്ലോഗ്', preprocesslangset(core_views.blogs), name='blogs'),
    # path('വിഭാഗംതിരഞ്ഞെടുത്തു/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('ബ്ലോഗ്/<str:id>', preprocesslangset(core_views.blogs), name='blogs'),
    path('ബ്ലോഗ്സിംഗിൾ/<str:id>',preprocesslangset( core_views.blog), name='blog'),
    path('test_supportml', preprocesslangset(core_views.test_support), name='test_support'),
    path('idn_websites_requestml',preprocesslangset( core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_blogml', preprocesslangset(core_views.add_blog), name='add_blog'),
    path('edit_blogml/<str:id>', preprocesslangset(core_views.edit_blog), name='edit_blog'),
    path('delete_blogml/<str:id>', preprocesslangset(core_views.delete_blog), name='delete_blog'),
    path('blog_datatableml', preprocesslangset(core_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>',preprocesslangset( core_views.search_blog), name='search_blog'), # Pending in json file
    path('loginml',preprocesslangset( user_views.login_view), name='login_view'),
    path('registerml',preprocesslangset( user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutml', preprocesslangset(user_views.logout_view), name='logout_view'),
    path('change_passwordml', preprocesslangset(user_views.change_password_view), name='change_password'),
    path('forgot_passwordml', preprocesslangset(user_views.forgot_password_view), name='forgot_password'),
    path('password_creationml/<uid>/<token>',preprocesslangset( user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listml',preprocesslangset( topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listml',preprocesslangset( user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topicml', preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionml/<slug:topic_slug>',preprocesslangset( view_topic_discussion), name="view_topic_discussion"),
    path('submit_answerml/<slug:topic_slug>',preprocesslangset( submit_answer), name='submit_answer'),
    path('upvote_answerml',preprocesslangset( upvote_answer_view), name='upvote_answer_view'),
    path('test_taskml',preprocesslangset( core_views.test_celery), name="test_task"),
    path('user_profile',preprocesslangset( user_views.user_profile_view), name='user_profile'), # Pending in json file
]   