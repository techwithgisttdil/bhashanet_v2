# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset


Translation_urlpatterns_hindi = [
    path('होम', preprocesslangset(core_views.home) , name='home'),
    path('गोपनीयतानीति', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('नियमएवंशर्तें', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('यूए_इंडिया_कार्यक्रम', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('आईडीएन_सीसीटीएलडी', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('सर्वोत्तम_प्रथाएं', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('ईएआई', preprocesslangset(core_views.EAI), name='EAI'),
    path('सार्वभौमिक_स्वीकृति', preprocesslangset(core_views.UA), name='UA'),
    path('औजार', preprocesslangset(core_views.tools), name='tools'),
    path('यूनिकोड_पुनीकोड_​​जनरेटर', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('यूनिकोड_फोंट', preprocesslangset(core_views.unicode_fonts), name='unicode_fonts'),
    path('लिप्यंतरण', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('स्क्रिप्ट_का_पता_लगाने', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('डोमेन_सत्यापनकर्ता', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('ईमेल_सत्यापनकर्ता', preprocesslangset(core_views.email_validator), name='email_validator'),
    path('प्रतिक्रिया', preprocesslangset(core_views.feedback), name='feedback'),
    path('यूएरेडीबनें', preprocesslangset(core_views.becomeuaready), name='becomeuaready'),
    path('पूछेजानेवालेप्रश्न', preprocesslangset(core_views.FAQs), name='FAQs'),
    path('दस्तावेज़_पृष्ठ', preprocesslangset(core_views.documentPage), name='documentPage'),
    path('दस्तावेज़डेटा', preprocesslangset(core_views.documentData), name='documentData'),
    path('सहायता', preprocesslangset(core_views.support), name='support'),
    path('खोज_के_परिणाम', preprocesslangset(core_views.search_results), name='search_results'),
    path('आईडीएन_वेबसाइटों/<int:id>', preprocesslangset(core_views.idn_websites), name='idn_websites'),
    path('आयोजन', preprocesslangset(core_views.event), name='event'),
    path('गेलरी', preprocesslangset(core_views.gallery), name='gallery'),
    path('language_detectionhi', preprocesslangset(core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardhi', preprocesslangset(core_views.cdac_keyboard), name='cdac_keyboard'),
    path('sop_tech_pagehi', preprocesslangset(core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pagehi', preprocesslangset(core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documenthi', preprocesslangset(core_views.sop_document), name='sop_document'), 
    path('tld_validatorhi', preprocesslangset(core_views.tld_validator), name='tld_validator'),
    path('डैशबोर्ड', preprocesslangset(core_views.dashboard), name='dashboard'),
    path('ब्लॉगस', preprocesslangset(core_views.blogs), name='blogs'),
    # path('वर्गीकृत', core_views.cat_selected, name='cat_selected'),
    path('ब्लॉगस/<str:id>', preprocesslangset(core_views.blogs), name='blogs'),
    path('ब्लॉगएकल/<str:id>', preprocesslangset(core_views.blog), name='blog'),
    path('test_supporthi', preprocesslangset(core_views.test_support), name='test_support'),
    path('idn_websites_requesthi', preprocesslangset(core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_bloghi', preprocesslangset(user_views.add_blog), name='add_blog'),
    path('edit_bloghi/<str:id>', preprocesslangset(user_views.edit_blog), name='edit_blog'),
    path('delete_bloghi/<str:id>', preprocesslangset(user_views.delete_blog), name='delete_blog'),
    path('blog_datatablehi', preprocesslangset(user_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>', preprocesslangset(user_views.search_blog), name='search_blog'), # Pending in json file
    path('loginhi', preprocesslangset(user_views.login_view), name='login_view'),
    path('registerhi', preprocesslangset(user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logouthi', preprocesslangset(user_views.logout_view), name='logout_view'),
    path('change_passwordhi', preprocesslangset(user_views.change_password_view), name='change_password'),
    path('forgot_passwordhi', preprocesslangset(user_views.forgot_password_view), name='forgot_password'),
    path('password_creationhi/<uid>/<token>', preprocesslangset(user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listhi', preprocesslangset(topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listhi', preprocesslangset(user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topichi', preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionhi/<slug:topic_slug>', preprocesslangset(view_topic_discussion), name="view_topic_discussion"),
    path('submit_answerhi/<slug:topic_slug>', preprocesslangset(submit_answer), name='submit_answer'),
    path('upvote_answerhi', preprocesslangset(upvote_answer_view), name='upvote_answer_view'),
    path('test_taskhi', preprocesslangset(core_views.test_celery), name="test_task"),
    path('user_profile', preprocesslangset(user_views.user_profile_view), name='user_profile'), # Pending in json file
]
