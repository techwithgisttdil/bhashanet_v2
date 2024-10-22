# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset


Translation_urlpatterns_kannada = [
    path('ಮುಖಪುಟ', preprocesslangset(core_views.home), name='home'),
    path('ಗೌಪ್ಯತಾನೀತಿ', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('ನಿಯಮಗಳುಮತ್ತುಷರತ್ತುಗಳು', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('ಯುಇಂಡಿಯಾಪ್ರೋಗ್ರಾಂ', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('ಐಡಿಎನಸೀಟಿಎಲಡಿ', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('ಒಳ್ಳೆಯಅಭ್ಯಾಸಗಳು',preprocesslangset( core_views.bestpractices), name='bestpractices'),
    path('ಇಎಬನ್ನಿಇ',preprocesslangset( core_views.EAI), name='EAI'),
    path('ಸಾರ್ವತ್ರಿಕಸ್ವೀಕಾರ', preprocesslangset(core_views.UA), name='UA'),
    path('ಉಪಕರಣಗಳು', preprocesslangset(core_views.tools), name='tools'),
    path('ಯುನಿಕೋಡ್_ಪುನಿಕೋಡ್_ಜನರೇಟರ್', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('ಯುನಿಕೋಡ್ಫಾಂಟ್', preprocesslangset(core_views.unicode_fonts), name='unicode_fonts'),
    path('ಲಿಪ್ಯಂತರಣ', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('ಸ್ಕ್ರಿಪ್ಟ್_ಪತ್ತೆ', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('ಡೊಮೇನ್ಪರಿಶೀಲಕ', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('ಇಮೇಲ್_ವ್ಯಾಲಿಡೇಟರ್', preprocesslangset(core_views.email_validator), name='email_validator'),
    path('ಪ್ರತಿಕ್ರಿಯೆ',preprocesslangset( core_views.feedback), name='feedback'),
    path('ಸಿದ್ಧನಾಗುತ್ತಾನೆ', preprocesslangset(core_views.becomeuaready), name='becomeuaready'),
    path('ಕೇಳಲುಪ್ರಶ್ನೆಗಳು', preprocesslangset(core_views.FAQs), name='FAQs'),
    path('ಡಾಕ್ಯುಮೆಂಟ್‌ಪುಟ', preprocesslangset(core_views.documentPage), name='documentPage'),
    path('ಡಾಕ್ಯುಮೆಂಟ್ಡೇಟಾ', preprocesslangset(core_views.documentData), name='documentData'),
    path('ಬೆಂಬಲ', preprocesslangset(core_views.support), name='support'),
    path('ಹುಡುಕಾಟಫಲಿತಾಂಶಗಳು', preprocesslangset(core_views.search_results), name='search_results'),
    path('ಐಡಿಎನ್_ವೆಬ್‌ಸೈಟ್‌ಗಳು/<int:id>', preprocesslangset(core_views.idn_websites), name='idn_websites'),
    path('ಈವೆಂಟ್', preprocesslangset(core_views.event), name='event'),
    path('ಗ್ಯಾಲರಿ', preprocesslangset(core_views.gallery), name='gallery'),
    path('language_detectionkn', preprocesslangset(core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardkn',preprocesslangset( core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_tech_pagekn', preprocesslangset(core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pagekn',preprocesslangset( core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documentkn',preprocesslangset( core_views.sop_document), name='sop_document'), 
    path('tld_validatorkn', preprocesslangset(core_views.tld_validator), name='tld_validator'),
    path('ಡ್ಯಾಶ್ಬೋರ್ಡ್', preprocesslangset(core_views.dashboard), name='dashboard'),
    path('ಬ್ಲಾಗ್',preprocesslangset( core_views.blogs), name='blogs'),
    # path('ವರ್ಗವನ್ನುಆಯ್ಕೆಮಾಡಲಾಗಿದೆ/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('ಬ್ಲಾಗ್/<str:id>', preprocesslangset(core_views.blogs), name='blogs'),
    path('ಬ್ಲಾಗ್ಸಿಂಗಲ್/<str:id>', preprocesslangset(core_views.blog), name='blog'),
    path('test_supportkn',preprocesslangset( core_views.test_support), name='test_support'),
    path('idn_websites_requestkn', preprocesslangset(core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_blogkn', preprocesslangset(user_views.add_blog), name='add_blog'),
    path('edit_blogkn/<str:id>', preprocesslangset(user_views.edit_blog), name='edit_blog'),
    path('delete_blogkn/<str:id>', preprocesslangset(user_views.delete_blog), name='delete_blog'),
    path('blog_datatablekn', preprocesslangset(user_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>',preprocesslangset( user_views.search_blog), name='search_blog'), # Pending in json file
    path('loginkn',preprocesslangset( user_views.login_view), name='login_view'),
    path('registerkn', preprocesslangset(user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutkn',preprocesslangset( user_views.logout_view), name='logout_view'),
    path('change_passwordkn', preprocesslangset(user_views.change_password_view), name='change_password'),
    path('forgot_passwordkn', preprocesslangset(user_views.forgot_password_view), name='forgot_password'),
    path('password_creationkn/<uid>/<token>', preprocesslangset(user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listkn',preprocesslangset( topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listkn', preprocesslangset(user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topickn', preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionkn/<slug:topic_slug>',preprocesslangset( view_topic_discussion), name="view_topic_discussion"),
    path('submit_answerkn/<slug:topic_slug>', preprocesslangset(submit_answer), name='submit_answer'),
    path('upvote_answerkn', preprocesslangset(upvote_answer_view), name='upvote_answer_view'),
    path('test_taskkn', preprocesslangset(core_views.test_celery), name="test_task"),
    path('user_profile',preprocesslangset( user_views.user_profile_view), name='user_profile'), # Pending in json file
]   
