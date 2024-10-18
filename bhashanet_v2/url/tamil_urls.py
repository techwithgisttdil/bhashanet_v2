# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset



Translation_urlpatterns_tamil = [
    path('வீடு', preprocesslangset(core_views.home), name='home'),
    path('தனியுரிமைக்கொள்கை', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('விதிமுறைகள்மற்றும்நிபந்தனைகள்',preprocesslangset( core_views.termsandconditions), name='termsandconditions'),
    path('யுஏஇந்தியாதிட்டம்', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('ஐடிஎன்சிசிடிஎல்டி',preprocesslangset( core_views.IDNCCTLD), name='IDNCCTLD'),
    path('சிறந்தநடைமுறைகள்', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('இஎஐ', preprocesslangset(core_views.EAI), name='EAI'),
    path('உலகளாவிய_ஏற்றுக்கொள்ளுதல்', preprocesslangset(core_views.UA), name='UA'),
    path('கருவி', preprocesslangset(core_views.tools), name='tools'),
    path('யூனிகோட்_புனிகோட்_ஜெனரேட்டர்', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('யூனிகோட்எழுத்துருக்கள்', preprocesslangset(core_views.unicode_fonts), name='unicode_fonts'),
    path('ஒலிபெயர்ப்பு', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('ஸ்கிரிப்ட்_கண்டறிதல்', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('டொமைன்வேலிடேட்டர்', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('மின்னஞ்சல்_சரிபார்ப்பாளர்', preprocesslangset(core_views.email_validator), name='email_validator'),
    path('பின்னூட்டம்', preprocesslangset(core_views.feedback), name='feedback'),
    path('யூரேடிஆக',preprocesslangset( core_views.becomeuaready), name='becomeuaready'),
    path('கேட்கவேண்டியகேள்விகள்', preprocesslangset(core_views.FAQs), name='FAQs'),
    path('ஆவணம்_பக்கம்',preprocesslangset( core_views.documentPage), name='documentPage'),
    path('ஆவணதரவு', preprocesslangset(core_views.documentData), name='documentData'),
    path('உதவி',preprocesslangset( core_views.support), name='support'),
    path('தேடல்முடிவுகள்',preprocesslangset( core_views.search_results), name='search_results'),
    path('idn_இணையதளங்கள்/<int:id>',preprocesslangset( core_views.idn_websites), name='idn_websites'),
    path('நிகழ்வு', preprocesslangset(core_views.event), name='event'),
    path('காட்சியகம்', preprocesslangset(core_views.gallery), name='gallery'),
    path('மொழி_கண்டறிதல்',preprocesslangset( core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardta', preprocesslangset(core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_டெக்_பக்கம்', preprocesslangset(core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_ஆவணப்_பக்கம்',preprocesslangset( core_views.sop_document_page), name='sop_document_page'), 
    path('sop_ஆவணம்',preprocesslangset( core_views.sop_document), name='sop_document'), 
    path('tld_மதிப்பீட்டாளர்',preprocesslangset( core_views.tld_validator), name='tld_validator'),
    path('டாஷ்போர்டு', preprocesslangset(core_views.dashboard), name='dashboard'),
    path('வலைப்பதிவு',preprocesslangset( core_views.blogs), name='blogs'),
    # path('வகைதேர்ந்தெடுக்கப்பட்டது/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('வலைப்பதிவு/<str:id>',preprocesslangset( core_views.blogs), name='blogs'),
    path('வலைப்பதிவுஒற்றை/<str:id>', preprocesslangset(core_views.blog), name='blog'),
    path('உதவி',preprocesslangset( core_views.test_support), name='test_support'),
    path('idn_websites_requestta',preprocesslangset( core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_blogta',preprocesslangset( core_views.add_blog), name='add_blog'),
    path('edit_blogta/<str:id>', preprocesslangset(core_views.edit_blog), name='edit_blog'),
    path('delete_blogta/<str:id>', preprocesslangset(core_views.delete_blog), name='delete_blog'),
    path('blog_datatableta', preprocesslangset(core_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>',preprocesslangset( core_views.search_blog), name='search_blog'), # Pending in json file
    path('loginta',preprocesslangset( user_views.login_view), name='login_view'),
    path('registerta', preprocesslangset(user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutta',preprocesslangset( user_views.logout_view), name='logout_view'),
    path('change_passwordta', preprocesslangset(user_views.change_password_view), name='change_password'),
    path('forgot_passwordta', preprocesslangset(user_views.forgot_password_view), name='forgot_password'),
    path('password_creationta/<uid>/<token>',preprocesslangset( user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listta',preprocesslangset( topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listta',preprocesslangset( user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topicta', preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionta/<slug:topic_slug>',preprocesslangset( view_topic_discussion), name="view_topic_discussion"),
    path('submit_answerta/<slug:topic_slug>', preprocesslangset(submit_answer), name='submit_answer'),
    path('upvote_answerta',preprocesslangset( upvote_answer_view), name='upvote_answer_view'),
    path('test_taskta',preprocesslangset( core_views.test_celery), name="test_task"),
    path('user_profile',preprocesslangset( user_views.user_profile_view), name='user_profile'), # Pending in json file
]   