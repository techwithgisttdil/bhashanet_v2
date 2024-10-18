# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset



Translation_urlpatterns_boro = [
    path('नआव', preprocesslangset(core_views.home), name='home'),
    path('privacypolicybrx', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('termsandconditionsbrx', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('uaindiaprogrammebrx', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('IDNCCTLDbrx', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('bestpracticesbrx', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('EAIbrx', preprocesslangset(core_views.EAI), name='EAI'),
    path('UAbrx', preprocesslangset(core_views.UA), name='UA'),
    path('toolsbrx', preprocesslangset(core_views.tools), name='tools'),
    path('unicode_punycode_generatorbrx', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('unicode_fontsbrx', preprocesslangset(core_views.unicode_fonts), name='unicode_fonts'),
    path('transliterationbrx', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('script_detectionbrx', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('domain_validatorbrx', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('email_validatorbrx', preprocesslangset(core_views.email_validator), name='email_validator'),
    path('feedbackbrx', preprocesslangset(core_views.feedback), name='feedback'),
    path('becomeuareadybrx', preprocesslangset(core_views.becomeuaready), name='becomeuaready'),
    path('FAQSbrx', preprocesslangset(core_views.FAQs), name='FAQs'),
    path('documentPagebrx', preprocesslangset(core_views.documentPage), name='documentPage'),
    path('documentDatabrx', preprocesslangset(core_views.documentData), name='documentData'),
    path('supportbrx', preprocesslangset(core_views.support), name='support'),
    path('search_resultsbrx', preprocesslangset(core_views.search_results), name='search_results'),
    path('idn_websitesbrx/<int:id>', preprocesslangset(core_views.idn_websites), name='idn_websites'),
    path('eventbrx', preprocesslangset(core_views.event), name='event'),
    path('gallerybrx', preprocesslangset(core_views.gallery), name='gallery'),
    path('language_detectionbrx', preprocesslangset(core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardbrx', preprocesslangset(core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_tech_pagebrx', preprocesslangset(core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pagebrx', preprocesslangset(core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documentbrx', preprocesslangset(core_views.sop_document), name='sop_document'), 
    path('tld_validatorbrx', preprocesslangset(core_views.tld_validator), name='tld_validator'),
    path('dashboardbrx', preprocesslangset(core_views.dashboard), name='dashboard'),
    path('blogsbrx', preprocesslangset(core_views.blogs), name='blogs'),
    # path('cat_selectedbrx/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('blogsbrx/<str:id>', preprocesslangset(core_views.blogs), name='blogs'),
    path('blogbrx/<str:id>', preprocesslangset(core_views.blog), name='blog'),
    path('test_supportboro', preprocesslangset(core_views.test_support), name='test_support'),
    path('idn_websites_requestbrx', preprocesslangset(core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_blogbrx', preprocesslangset(core_views.add_blog), name='add_blog'),
    path('edit_blogbrx/<str:id>', preprocesslangset(core_views.edit_blog), name='edit_blog'),
    path('delete_blogbrx/<str:id>', preprocesslangset(core_views.delete_blog), name='delete_blog'),
    path('blog_datatablebrx', preprocesslangset(core_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>', preprocesslangset(core_views.search_blog), name='search_blog'), # Pending in json file
    path('loginbrx', preprocesslangset(user_views.login_view), name='login_view'),
    path('registerbrx', preprocesslangset(user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutbrx', preprocesslangset(user_views.logout_view), name='logout_view'),
    path('change_passwordbrx', preprocesslangset(user_views.change_password_view), name='change_password'),
    path('forgot_passwordbrx', preprocesslangset(user_views.forgot_password_view), name='forgot_password'),
    path('password_creationbrx/<uid>/<token>', preprocesslangset(user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listbrx', preprocesslangset(topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listbrx', preprocesslangset(user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topicbrx', preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionbrx/<slug:topic_slug>', preprocesslangset(view_topic_discussion), name="view_topic_discussion"),
    path('submit_answerbrx/<slug:topic_slug>', preprocesslangset(submit_answer), name='submit_answer'),
    path('upvote_answerbrx', preprocesslangset(upvote_answer_view), name='upvote_answer_view'),
    path('test_taskbrx', preprocesslangset(core_views.test_celery), name="test_task"),
    path('user_profile', preprocesslangset(user_views.user_profile_view), name='user_profile'), # Pending in json file
]   