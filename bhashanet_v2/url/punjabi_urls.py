# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset


Translation_urlpatterns_punjabi = [
    path('ਘਰ', preprocesslangset(core_views.home), name='home'),
    path('ਪਰਾਈਵੇਟਨੀਤੀ', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('ਨਿਬੰਧਨਅਤੇਸ਼ਰਤਾਂ', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('ਯੂਏਭਾਰਤਪ੍ਰੋਗਰਾਮ', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('IDNCCTLDPa', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('ਵਧੀਆਅਭਿਆਸ', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('ਈਏਆਈ', preprocesslangset(core_views.EAI), name='EAI'),
    path('ਯੂਏ', preprocesslangset(core_views.UA), name='UA'),
    path('ਸੰਦ', preprocesslangset(core_views.tools), name='tools'),
    path('ਯੂਨੀਕੋਡ_ਪਨੀਕੋਡ_ਜਨਰੇਟਰ', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('ਯੂਨੀਕੋਡ_ਫੌਂਟ', preprocesslangset(core_views.unicode_fonts), name='unicode_fonts'),
    path('ਲਿਪੀਅੰਤਰਨ', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('ਸਕ੍ਰਿਪਟ_ਖੋਜ', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('ਡੋਮੇਨ_ਪ੍ਰਮਾਣਕeTE', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('ਈਮੇਲ_ਪ੍ਰਮਾਣਕ',preprocesslangset( core_views.email_validator), name='email_validator'),
    path('ਸੁਝਾਅ', preprocesslangset(core_views.feedback), name='feedback'),
    path('ਤਿਆਰਹੋਗਿਆ',preprocesslangset( core_views.becomeuaready), name='becomeuaready'),
    path('FAQSPa', preprocesslangset(core_views.FAQs), name='FAQs'),
    path('ਦਸਤਾਵੇਜ਼ਪੰਨਾ',preprocesslangset( core_views.documentPage), name='documentPage'),
    path('ਦਸਤਾਵੇਜ਼ਡੇਟਾ', preprocesslangset(core_views.documentData), name='documentData'),
    path('ਸਮਰਥਨ', preprocesslangset(core_views.support), name='support'),
    path('ਖੋਜ_ਨਤੀਜੇ', preprocesslangset(core_views.search_results), name='search_results'),
    path('ਆਈਡੀਐਨਵੈੱਬਸਾਈਟਾਂ/<int:id>', preprocesslangset(core_views.idn_websites), name='idn_websites'),
    path('ਘਟਨਾ', preprocesslangset(core_views.event), name='event'),
    path('ਗੈਲਰੀ', preprocesslangset(core_views.gallery), name='gallery'),
    path('ਭਾਸ਼ਾ_ਦੀ_ਖੋਜ', preprocesslangset(core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardpa',preprocesslangset( core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_tech_pagepa',preprocesslangset( core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pagepa',preprocesslangset( core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documentpa', preprocesslangset(core_views.sop_document), name='sop_document'), 
    path('tld_validatorpa', preprocesslangset(core_views.tld_validator), name='tld_validator'),
    path('ਡੈਸ਼ਬੋਰਡ',preprocesslangset( core_views.dashboard), name='dashboard'),
    path('ਬਲੌਗ',preprocesslangset( core_views.blogs), name='blogs'),
    # path('ਸ਼੍ਰੇਣੀਚੁਣੀਗਈਹੈ/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('ਬਲੌਗ/<str:id>',preprocesslangset( core_views.blogs), name='blogs'),
    path('ਬਲੌਗਸਿੰਗਲ/<str:id>', preprocesslangset(core_views.blog), name='blog'),
    path('test_supportpa',preprocesslangset( core_views.test_support), name='test_support'),
    path('idn_websites_requestpa',preprocesslangset( core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_blogpa', preprocesslangset(core_views.add_blog), name='add_blog'),
    path('edit_blogpa/<str:id>',preprocesslangset( core_views.edit_blog), name='edit_blog'),
    path('delete_blogpa/<str:id>', preprocesslangset(core_views.delete_blog), name='delete_blog'),
    path('blog_datatablepa', preprocesslangset(core_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>',preprocesslangset( core_views.search_blog), name='search_blog'), # Pending in json file
    path('loginpa', preprocesslangset(user_views.login_view), name='login_view'),
    path('registerpa', preprocesslangset(user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutpa',preprocesslangset( user_views.logout_view), name='logout_view'),
    path('change_passwordpa',preprocesslangset( user_views.change_password_view), name='change_password'),
    path('forgot_passwordpa',preprocesslangset( user_views.forgot_password_view), name='forgot_password'),
    path('password_creationpa/<uid>/<token>',preprocesslangset( user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listpa',preprocesslangset( topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listpa',preprocesslangset( user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topicpa', preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionpa/<slug:topic_slug>',preprocesslangset( view_topic_discussion), name="view_topic_discussion"),
    path('submit_answerpa/<slug:topic_slug>', preprocesslangset(submit_answer), name='submit_answer'),
    path('upvote_answerpa',preprocesslangset( upvote_answer_view), name='upvote_answer_view'),
    path('test_taskpa', preprocesslangset(core_views.test_celery), name="test_task"),
    path('user_profile',preprocesslangset( user_views.user_profile_view), name='user_profile'), # Pending in json file
]   