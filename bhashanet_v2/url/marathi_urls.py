# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset



Translation_urlpatterns_marathi = [
    path('मुख्यपान', preprocesslangset(core_views.home), name='home'),
    path('गोपनीयताधोरण', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('नियमआणिअटी', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('यूएइंडियाकार्यक्रम', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('आईडीएनसीसीटीएलडी', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('चांगलासराव', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('ईए_आई', preprocesslangset(core_views.EAI), name='EAI'),
    path('सार्वत्रिक_स्वीकृती', preprocesslangset(core_views.UA), name='UA'),
    path('साधने', preprocesslangset(core_views.tools), name='tools'),
    path('यूनिकोडपुनीकोड​जनरेटर',preprocesslangset( core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('यूनि_कोड_फोंट',preprocesslangset( core_views.unicode_fonts), name='unicode_fonts'),
    path('लिप्यं_तरण', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('स्क्रिप्ट_डिटेक्शन', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('डोमेनसत्यापनकर्ता', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('ईमेलसत्यापनकर्ता', preprocesslangset(core_views.email_validator), name='email_validator'),
    path('अभिप्राय', preprocesslangset(core_views.feedback), name='feedback'),
    path('तयारझाले', preprocesslangset(core_views.becomeuaready), name='becomeuaready'),
    path('विचारण्यासाठीप्रश्न', preprocesslangset(core_views.FAQs), name='FAQs'),
    path('दस्तऐवजपृष्ठ', preprocesslangset(core_views.documentPage), name='documentPage'),
    path('दस्तऐवजडेटा',preprocesslangset( core_views.documentData), name='documentData'),
    path('समर्थन', preprocesslangset(core_views.support), name='support'),
    path('शोध_परिणाम',preprocesslangset( core_views.search_results), name='search_results'),
    path('आयडीएन_वेबसाइट्स/<int:id>',preprocesslangset( core_views.idn_websites), name='idn_websites'),
    path('क्रार्यक्रम', preprocesslangset(core_views.event), name='event'),
    path('गॅलरी', preprocesslangset(core_views.gallery), name='gallery'),
    path('language_detectionmr',preprocesslangset( core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardmr', preprocesslangset(core_views.cdac_keyboard), name='cdac_keyboard'),
    path('sop_tech_pagemr',preprocesslangset( core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pagemr',preprocesslangset( core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documentmr',preprocesslangset( core_views.sop_document), name='sop_document'), 
    path('tld_validatormr',preprocesslangset( core_views.tld_validator), name='tld_validator'),
    path('डॅशबोर्ड',preprocesslangset( core_views.dashboard), name='dashboard'),
    path('ब्लॉगमराठी',preprocesslangset( core_views.blogs), name='blogs'),
    # path('श्रेणीचयनित/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('ब्लॉगमराठी/<str:id>', preprocesslangset(core_views.blogs), name='blogs'),
    path('ब्लॉगसिंगल/<str:id>', preprocesslangset(core_views.blog), name='blog'),
    path('add_blogmr', preprocesslangset(user_views.add_blog), name='add_blog'),
    path('edit_blogmr/<str:id>',preprocesslangset( user_views.edit_blog), name='edit_blog'),
    path('delete_blogmr/<str:id>',preprocesslangset( user_views.delete_blog), name='delete_blog'),
    path('blog_datatablemr', preprocesslangset(user_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blogmr/<str:id>',preprocesslangset( user_views.search_blog), name='search_blog'),
    path('loginmr', preprocesslangset(user_views.login_view), name='login_view'),
    path('registermr', preprocesslangset(user_views.register_view), name='register_view'),
    path('logoutmr', preprocesslangset(user_views.logout_view), name='logout_view'),
    path('change_passwordmr', preprocesslangset(user_views.change_password_view), name='change_password'),
    path('forgot_passwordmr', preprocesslangset(user_views.forgot_password_view), name='forgot_password'),
    path('password_creationmr/<uid>/<token>',preprocesslangset( user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listmr',preprocesslangset( topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listmr',preprocesslangset( user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topicmr',preprocesslangset( add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionmr/<slug:topic_slug>',preprocesslangset( view_topic_discussion), name="view_topic_discussion"),
    path('submit_answermr/<slug:topic_slug>', preprocesslangset(submit_answer), name='submit_answer'),
    path('upvote_answermr', preprocesslangset(upvote_answer_view), name='upvote_answer_view'),
    path('test_taskmr', preprocesslangset(core_views.test_celery), name="test_task"),
    path('user_profilemr',preprocesslangset( user_views.user_profile_view), name='user_profile'),
    path('admindashboardmr',preprocesslangset( core_views.admindashboard), name='admindashboard'),
    path('idn_websites_requestmr',preprocesslangset( core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'), 
 
]
