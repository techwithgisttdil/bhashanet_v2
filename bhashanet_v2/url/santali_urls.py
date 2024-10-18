# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset



Translation_urlpatterns_santali = [
    path('ᱚᱲᱟᱜ', preprocesslangset(core_views.home), name='home'),
    path('privacypolicysat', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('termsandconditionssat', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('uaindiaprogrammesat',preprocesslangset( core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('IDNCCTLDsat', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('bestpracticessat',preprocesslangset( core_views.bestpractices), name='bestpractices'),
    path('EAIsat', preprocesslangset(core_views.EAI), name='EAI'),
    path('UAsat', preprocesslangset(core_views.UA), name='UA'),
    path('toolssat',preprocesslangset( core_views.tools), name='tools'),
    path('unicode_punycode_generatorsat', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('unicode_fontssat', preprocesslangset(core_views.unicode_fonts), name='unicode_fonts'),
    path('transliterationsat', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('script_detectionsat',preprocesslangset( core_views.script_detection), name='script_detection'),
    path('domain_validatorsat', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('email_validatorsat', preprocesslangset(core_views.email_validator), name='email_validator'),
    path('feedbacksat', preprocesslangset(core_views.feedback), name='feedback'),
    path('becomeuareadysat',preprocesslangset( core_views.becomeuaready), name='becomeuaready'),
    path('FAQSsat', preprocesslangset(core_views.FAQs), name='FAQs'),
    path('documentPagesat', preprocesslangset(core_views.documentPage), name='documentPage'),
    path('documentDatasat',preprocesslangset( core_views.documentData), name='documentData'),
    path('supportsat', preprocesslangset(core_views.support), name='support'),
    path('search_resultssat',preprocesslangset( core_views.search_results), name='search_results'),
    path('idn_websitessat/<int:id>',preprocesslangset( core_views.idn_websites), name='idn_websites'),
    path('eventsat',preprocesslangset( core_views.event), name='event'),
    path('gallerysat', preprocesslangset(core_views.gallery), name='gallery'),
    path('language_detectionsat',preprocesslangset( core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardsat',preprocesslangset( core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_tech_pagesat',preprocesslangset( core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pagesat', preprocesslangset(core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documentsat', preprocesslangset(core_views.sop_document), name='sop_document'), 
    path('tld_validatorsat',preprocesslangset( core_views.tld_validator), name='tld_validator'),
    path('dashboardsat', preprocesslangset(core_views.dashboard), name='dashboard'),
    path('blogssat', preprocesslangset(core_views.blogs), name='blogs'),
    # path('cat_selectedsat/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('blogssat/<str:id>',preprocesslangset( core_views.blogs), name='blogs'),
    path('blogsat/<str:id>',preprocesslangset( core_views.blog), name='blog'),
    path('test_supportboro', preprocesslangset(core_views.test_support), name='test_support'),
    path('idn_websites_requestsat',preprocesslangset( core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_blogsat', preprocesslangset(core_views.add_blog), name='add_blog'),
    path('edit_blogsat/<str:id>', preprocesslangset(core_views.edit_blog), name='edit_blog'),
    path('delete_blogsat/<str:id>',preprocesslangset( core_views.delete_blog), name='delete_blog'),
    path('blog_datatablesat', preprocesslangset(core_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>',preprocesslangset( core_views.search_blog), name='search_blog'), # Pending in json file
    path('loginsat',preprocesslangset( user_views.login_view), name='login_view'),
    path('registersat', preprocesslangset(user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutsat',preprocesslangset( user_views.logout_view), name='logout_view'),
    path('change_passwordsat',preprocesslangset( user_views.change_password_view), name='change_password'),
    path('forgot_passwordsat',preprocesslangset( user_views.forgot_password_view), name='forgot_password'),
    path('password_creationsat/<uid>/<token>',preprocesslangset( user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listsat',preprocesslangset( topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listsat', preprocesslangset(user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topicsat', preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionsat/<slug:topic_slug>',preprocesslangset( view_topic_discussion), name="view_topic_discussion"),
    path('submit_answersat/<slug:topic_slug>',preprocesslangset( submit_answer), name='submit_answer'),
    path('upvote_answersat',preprocesslangset( upvote_answer_view), name='upvote_answer_view'),
    path('test_tasksat',preprocesslangset( core_views.test_celery), name="test_task"),
    path('user_profile', preprocesslangset(user_views.user_profile_view), name='user_profile'), # Pending in json file
]   