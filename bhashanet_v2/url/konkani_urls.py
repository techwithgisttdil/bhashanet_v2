# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset

# -----ADDED BY SHWETA PATIL -------
Translation_urlpatterns_konkani = [
    path('होमकोंकणी', preprocesslangset(core_views.home), name='home'),
    path('privacypolicykok', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('termsandconditionskok', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('uaindiaprogrammekok', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('IDNCCTLDkok', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('bestpracticeskok', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('EAIkok', preprocesslangset(core_views.EAI), name='EAI'),
    path('UAkok', preprocesslangset(core_views.UA), name='UA'),
    path('toolskok', preprocesslangset(core_views.tools), name='tools'),
    path('unicode_punycode_generatorkok', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('unicode_fontskok', preprocesslangset(core_views.unicode_fonts), name='unicode_fonts'),
    path('transliterationkok', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('script_detectionkok', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('domain_validatorkok', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('email_validatorkok', preprocesslangset(core_views.email_validator), name='email_validator'),
    path('feedbackkok', preprocesslangset(core_views.feedback), name='feedback'),
    path('becomeuareadykok', preprocesslangset(core_views.becomeuaready), name='becomeuaready'),
    path('FAQSkok', preprocesslangset(core_views.FAQs), name='FAQs'),
    path('documentPagekok', preprocesslangset(core_views.documentPage), name='documentPage'),
    path('documentDatakok', preprocesslangset(core_views.documentData), name='documentData'),
    path('supportkok', preprocesslangset(core_views.support), name='support'),
    path('search_resultskok', preprocesslangset(core_views.search_results), name='search_results'),
    path('idn_websiteskok/<int:id>', preprocesslangset(core_views.idn_websites), name='idn_websites'),
    path('eventkok', preprocesslangset(core_views.event), name='event'),
    path('gallerykok', preprocesslangset(core_views.gallery), name='gallery'),
    path('language_detectionkok', preprocesslangset(core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardkok', preprocesslangset(core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_tech_pagekok', preprocesslangset(core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pagekok', preprocesslangset(core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documentkok', preprocesslangset(core_views.sop_document), name='sop_document'), 
    path('tld_validatorkok', preprocesslangset(core_views.tld_validator), name='tld_validator'),
    path('dashboardkok', preprocesslangset(core_views.dashboard), name='dashboard'),
    path('blogskok', preprocesslangset(core_views.blogs), name='blogs'),
    # path('cat_selectedkok/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('blogskok/<str:id>', preprocesslangset(core_views.blogs), name='blogs'),
    path('blogkok/<str:id>', preprocesslangset(core_views.blog), name='blog'),
    path('test_supportkok', preprocesslangset(core_views.test_support), name='test_support'),
    path('idn_websites_requestkok', preprocesslangset(core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_blogkok', preprocesslangset(user_views.add_blog), name='add_blog'),
    path('edit_blogkok/<str:id>', preprocesslangset(user_views.edit_blog), name='edit_blog'),
    path('delete_blogkok/<str:id>', preprocesslangset(user_views.delete_blog), name='delete_blog'),
    path('blog_datatablekok', preprocesslangset(user_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>', preprocesslangset(user_views.search_blog), name='search_blog'), # Pending in json file
    path('loginkok', preprocesslangset(user_views.login_view), name='login_view'),
    path('registerkok', preprocesslangset(user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutkok', preprocesslangset(user_views.logout_view), name='logout_view'),
    path('change_passwordkok', preprocesslangset(user_views.change_password_view), name='change_password'),
    path('forgot_passwordkok', preprocesslangset(user_views.forgot_password_view), name='forgot_password'),
    path('password_creationkok/<uid>/<token>', preprocesslangset(user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listkok', preprocesslangset(topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listkok', preprocesslangset(user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topickok', preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionkok/<slug:topic_slug>', preprocesslangset(view_topic_discussion), name="view_topic_discussion"),
    path('submit_answerkok/<slug:topic_slug>', preprocesslangset(submit_answer), name='submit_answer'),
    path('upvote_answerkok', preprocesslangset(upvote_answer_view), name='upvote_answer_view'),
    path('user_profile', preprocesslangset(user_views.user_profile_view), name='user_profile'), # Pending in json file
]   
