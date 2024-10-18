# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset

Translation_urlpatterns_bengali = [
    path('বাড়ি', preprocesslangset(core_views.home), name='home'),
    path('গোপনীয়তানীতি', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('শর্তাবলী', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('ইউএআইইন্ডিয়াপ্রোগ্রাম', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('আইডিএনসিটিএলডি', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('ভালোঅভ্যাস', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('আসো', preprocesslangset(core_views.EAI), name='EAI'),
    path('সর্বজনীনগ্রহণযোগ্যতা', preprocesslangset(core_views.UA), name='UA'),
    path('যন্ত্রপাতি', preprocesslangset(core_views.tools), name='tools'),
    path('ইউনিকোডপুনিককোডজেনারেটর', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('ইউনিকোডফন্ট', preprocesslangset(core_views.unicode_fonts), name='unicode_fonts'),
    path('ট্রান্সলিটারেশন', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('স্ক্রিপ্টআবিষ্কার', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('ডোমেইনচেকার', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('ইমেইলভ্যালিডেটর', preprocesslangset(core_views.email_validator), name='email_validator'),
    path('প্রতিক্রিয়া', preprocesslangset(core_views.feedback), name='feedback'),
    path('প্রস্তুতহতেহবে', preprocesslangset(core_views.becomeuaready), name='becomeuaready'),
    path('প্রশ্নজিজ্ঞাসা', preprocesslangset(core_views.FAQs), name='FAQs'),
    path('নথিপাতা', preprocesslangset(core_views.documentPage), name='documentPage'),
    path('নথিডেটা', preprocesslangset(core_views.documentData), name='documentData'),
    path('সমর্থন', preprocesslangset(core_views.support), name='support'),
    path('অনুসন্ধানফলাফল', preprocesslangset(core_views.search_results), name='search_results'),
    path('আইডিএন_ওয়েবসাইট/<int:id>', preprocesslangset(core_views.idn_websites), name='idn_websites'),
    path('ঘটনা', preprocesslangset(core_views.event), name='event'),
    path('গ্যালারি',preprocesslangset( core_views.gallery), name='gallery'),
    path('language_detectionbn', preprocesslangset(core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardbn', preprocesslangset(core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_tech_pagebn', preprocesslangset(core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_pagebn', preprocesslangset(core_views.sop_document_page), name='sop_document_page'), 
    path('sop_documentbn', preprocesslangset(core_views.sop_document), name='sop_document'), 
    path('tld_validatorbn', preprocesslangset(core_views.tld_validator), name='tld_validator'),
    path('ড্যাশবোর্ড', preprocesslangset(core_views.dashboard), name='dashboard'),
    path('ব্লগ', preprocesslangset(core_views.blogs), name='blogs'),
    # path('বিভাগনির্বাচিত/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('ব্লগ/<str:id>', preprocesslangset(core_views.blogs), name='blogs'),
    path('ব্লগএকক/<str:id>', preprocesslangset(core_views.blog), name='blog'),
    path('test_supportbn', preprocesslangset(core_views.test_support), name='test_support'),
    path('idn_websites_requestbn', preprocesslangset(core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_blogbn', preprocesslangset(core_views.add_blog), name='add_blog'),
    path('edit_blogbn/<str:id>',preprocesslangset( core_views.edit_blog), name='edit_blog'),
    path('delete_blogbn/<str:id>', preprocesslangset(core_views.delete_blog), name='delete_blog'),
    path('blog_datatablebn', preprocesslangset(core_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>',preprocesslangset( core_views.search_blog), name='search_blog'), # Pending in json file
    path('loginbn', preprocesslangset(user_views.login_view), name='login_view'),
    path('registerbn', preprocesslangset(user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutbn', preprocesslangset(user_views.logout_view), name='logout_view'),
    path('change_passwordbn', preprocesslangset(user_views.change_password_view), name='change_password'),
    path('forgot_passwordbn', preprocesslangset(user_views.forgot_password_view), name='forgot_password'),
    path('password_creationbn/<uid>/<token>', preprocesslangset(user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listbn', preprocesslangset(topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listbn', preprocesslangset(user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topicbn', preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionbn/<slug:topic_slug>', preprocesslangset(view_topic_discussion), name="view_topic_discussion"),
    path('submit_answerbn/<slug:topic_slug>', preprocesslangset(submit_answer), name='submit_answer'),
    path('upvote_answerbn', preprocesslangset(upvote_answer_view), name='upvote_answer_view'),
    path('test_taskbn', preprocesslangset(core_views.test_celery), name="test_task"),
    path('user_profile', preprocesslangset(user_views.user_profile_view), name='user_profile'), # Pending in json file
]   