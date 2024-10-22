# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset



Translation_urlpatterns_dogri = [
    path('होमडोगरी', preprocesslangset(core_views.home), name='home'),
    path('privacypolicydoi', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('termsandconditionsdoi', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('uaindiaprogrammedoi', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('IDNCCTLDdoi', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('bestpracticesdoi', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('EAIdoi', preprocesslangset(core_views.EAI), name='EAI'),
    path('UAdoi', preprocesslangset(core_views.UA), name='UA'),
    path('toolsdoi', preprocesslangset(core_views.tools), name='tools'),
    path('unicode_punycode_generatordoi', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('unicode_fontsdoi', preprocesslangset(core_views.unicode_fonts), name='unicode_fonts'),
    path('transliterationdoi', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('script_detectiondoi', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('domain_validatordoi', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('email_validatordoi', preprocesslangset(core_views.email_validator), name='email_validator'),
    path('feedbackdoi', preprocesslangset(core_views.feedback), name='feedback'),
    path('becomeuareadydoi', preprocesslangset(core_views.becomeuaready), name='becomeuaready'),
    path('FAQSdoi', preprocesslangset(core_views.FAQs), name='FAQs'),
    path('documentPagedoi', preprocesslangset(core_views.documentPage), name='documentPage'),
    path('documentDatadoi', preprocesslangset(core_views.documentData), name='documentData'),
    path('supportdoi', preprocesslangset(core_views.support), name='support'),
    path('search_resultsdoi', preprocesslangset(core_views.search_results), name='search_results'),
    path('idn_websitesdoi/<int:id>', preprocesslangset(core_views.idn_websites), name='idn_websites'),
    path('eventdoi', preprocesslangset(core_views.event), name='event'),
    path('gallerydoi', preprocesslangset(core_views.gallery), name='gallery'),
    path('language_detectiondoi', preprocesslangset(core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboarddoi', preprocesslangset(core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_tech_pagedoi', preprocesslangset(core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pagedoi', preprocesslangset(core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documentdoi', preprocesslangset(core_views.sop_document), name='sop_document'), 
    path('tld_validatordoi', preprocesslangset(core_views.tld_validator), name='tld_validator'),
    path('dashboarddoi', preprocesslangset(core_views.dashboard), name='dashboard'),
    path('blogsdoi', preprocesslangset(core_views.blogs), name='blogs'),
    # path('cat_selecteddoi/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('blogsdoi/<str:id>', preprocesslangset(core_views.blogs), name='blogs'),
    path('blogdoi/<str:id>', preprocesslangset(core_views.blog), name='blog'),
    path('test_supportdoi', preprocesslangset(core_views.test_support), name='test_support'),
    path('idn_websites_requestdoi', preprocesslangset(core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_blogdoi', preprocesslangset(user_views.add_blog), name='add_blog'),
    path('edit_blogdoi/<str:id>', preprocesslangset(user_views.edit_blog), name='edit_blog'),
    path('delete_blogdoi/<str:id>', preprocesslangset(user_views.delete_blog), name='delete_blog'),
    path('blog_datatabledoi', preprocesslangset(user_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>', preprocesslangset(user_views.search_blog), name='search_blog'), # Pending in json file
    path('logindoi', preprocesslangset(user_views.login_view), name='login_view'),
    path('registerdoi', preprocesslangset(user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutdoi', preprocesslangset(user_views.logout_view), name='logout_view'),
    path('change_passworddoi', preprocesslangset(user_views.change_password_view), name='change_password'),
    path('forgot_passworddoi', preprocesslangset(user_views.forgot_password_view), name='forgot_password'),
    path('password_creationdoi/<uid>/<token>',preprocesslangset( user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listdoi', preprocesslangset(topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listdoi', preprocesslangset(user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topicdoi',preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussiondoi/<slug:topic_slug>', preprocesslangset(view_topic_discussion), name="view_topic_discussion"),
    path('submit_answerdoi/<slug:topic_slug>', preprocesslangset(submit_answer), name='submit_answer'),
    path('upvote_answerdoi',preprocesslangset( upvote_answer_view), name='upvote_answer_view'),
    path('test_taskdoi',preprocesslangset( core_views.test_celery), name="test_task"),
    path('user_profile', preprocesslangset(user_views.user_profile_view), name='user_profile'), # Pending in json file
]   
