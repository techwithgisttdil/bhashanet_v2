# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset



Translation_urlpatterns_gujarati = [
    path('ઘર', preprocesslangset(core_views.home), name='home'),
    path('ગોપનીયતાનીતિ', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('નિયમોઅનેશરત', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('યુએભારતપ્રોગ્રામ', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('IDNCCTLDgu', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('શ્રેષ્ઠવ્યવહાર', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('ઇએઆઈ', preprocesslangset(core_views.EAI), name='EAI'),
    path('યુએ', preprocesslangset(core_views.UA), name='UA'),
    path('સાધનો',preprocesslangset( core_views.tools), name='tools'),
    path('યુનિકોડ_પનીકોડ_જનરેટર', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('યુનિકોડ_ફોન્ટ્સ', preprocesslangset(core_views.unicode_fonts), name='unicode_fonts'),
    path('લિવ્યંતરણ', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('સ્ક્રિપ્ટ_શોધ', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('ડોમેન_માન્યકર્તા', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('ઇમેઇલ_માન્યકર્તા',preprocesslangset( core_views.email_validator), name='email_validator'),
    path('પ્રતિસાદ', preprocesslangset(core_views.feedback), name='feedback'),
    path('તૈયારથઈ',preprocesslangset( core_views.becomeuaready), name='becomeuaready'),
    path('FAQSgu',preprocesslangset( core_views.FAQs), name='FAQs'),
    path('દસ્તાવેજપૃષ્ઠ',preprocesslangset( core_views.documentPage), name='documentPage'),
    path('દસ્તાવેજડેટા',preprocesslangset( core_views.documentData), name='documentData'),
    path('આધાર', preprocesslangset(core_views.support), name='support'),
    path('શોધ_પરિણામો', preprocesslangset(core_views.search_results), name='search_results'),
    path('હુંડીએન_વેબસાઇટ્સ/<int:id>',preprocesslangset( core_views.idn_websites), name='idn_websites'),
    path('ઘટના',preprocesslangset( core_views.event), name='event'),
    path('ગેલેરી',preprocesslangset( core_views.gallery), name='gallery'),
    path('ભાષા_શોધ',preprocesslangset( core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardgu',preprocesslangset( core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_tech_pagegu',preprocesslangset( core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pagegu',preprocesslangset( core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documentgu',preprocesslangset( core_views.sop_document), name='sop_document'), 
    path('tld_validatorgu', preprocesslangset(core_views.tld_validator), name='tld_validator'),
    path('ડેશબોર્ડ',preprocesslangset( core_views.dashboard), name='dashboard'),
    path('બ્લોગ', preprocesslangset(core_views.blogs), name='blogs'),
    # path('શ્રેણીપસંદકરી/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('બ્લોગ/<str:id>', preprocesslangset(core_views.blogs), name='blogs'),
    path('બ્લોગસિંગલ/<str:id>',preprocesslangset( core_views.blog), name='blog'),
    path('test_supportgu',preprocesslangset( core_views.test_support), name='test_support'),
    path('idn_websites_requestgu',preprocesslangset( core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_bloggu',preprocesslangset( user_views.add_blog), name='add_blog'),
    path('edit_bloggu/<str:id>', preprocesslangset(user_views.edit_blog), name='edit_blog'),
    path('delete_bloggu/<str:id>',preprocesslangset( user_views.delete_blog), name='delete_blog'),
    path('blog_datatablegu',preprocesslangset( user_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>',preprocesslangset( user_views.search_blog), name='search_blog'), # Pending in json file
    path('logingu', preprocesslangset(user_views.login_view), name='login_view'),
    path('registergu',preprocesslangset( user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutgu', preprocesslangset(user_views.logout_view), name='logout_view'),
    path('change_passwordgu', preprocesslangset(user_views.change_password_view), name='change_password'),
    path('forgot_passwordgu',preprocesslangset( user_views.forgot_password_view), name='forgot_password'),
    path('password_creationgu/<uid>/<token>',preprocesslangset( user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listgu',preprocesslangset( topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listgu', preprocesslangset(user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topicgu', preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussiongu/<slug:topic_slug>',preprocesslangset( view_topic_discussion), name="view_topic_discussion"),
    path('submit_answergu/<slug:topic_slug>', preprocesslangset(submit_answer), name='submit_answer'),
    path('upvote_answergu', preprocesslangset(upvote_answer_view), name='upvote_answer_view'),
    path('test_taskgu',preprocesslangset( core_views.test_celery), name="test_task"),
    path('user_profile',preprocesslangset( user_views.user_profile_view), name='user_profile'), # Pending in json file
]   