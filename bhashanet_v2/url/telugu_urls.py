# ----ADDED BY SHWETA PATIL ----
from django.urls import path
from core_app import views as core_views
from admin_app import views as user_views
from discussion_forum_app.views import *
from core_app.decorator import preprocesslangset


Translation_urlpatterns_telugu = [
    path('ఇల్లు', preprocesslangset(core_views.home), name='home'),
    path('గోప్యతావిధానం', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('నిబంధనలుమరియుషరతులు',preprocesslangset( core_views.termsandconditions), name='termsandconditions'),
    path('UAఇండియాప్రోగ్రామ్',preprocesslangset( core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('ఐడిఎన్సిసిటిఎల్డి', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('ఉత్తమపద్ధతులు', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('ఇఎI', preprocesslangset(core_views.EAI), name='EAI'),
    path('సార్వత్రిక_అంగీకారం', preprocesslangset(core_views.UA), name='UA'),
    path('సాధనం', preprocesslangset(core_views.tools), name='tools'),
    path('యూనికోడ్_పునికోడ్_జనరేటర్', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('యూనికోడ్_ఫాంట్',preprocesslangset( core_views.unicode_fonts), name='unicode_fonts'),
    path('లిప్యంతరీకరణ',preprocesslangset( core_views.transliteration), name='transliteration'),
    path('స్క్రిప్ట్_డిటెక్షన్', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('డొమైన్_వెరిఫైయర్', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('ఇమెయిల్_వెరిఫైయర్', preprocesslangset(core_views.email_validator), name='email_validator'),
    path('అభిప్రాయం', preprocesslangset(core_views.feedback), name='feedback'),
    path('యూరేడీఅవుతుంది',preprocesslangset( core_views.becomeuaready), name='becomeuaready'),
    path('అడగడానికిప్రశ్నలు',preprocesslangset( core_views.FAQs), name='FAQs'),
    path('డాక్యుమెంట్_పేజీ',preprocesslangset( core_views.documentPage), name='documentPage'),
    path('డాక్యుమెంట్డేటా', preprocesslangset(core_views.documentData), name='documentData'),
    path('సహాయం', preprocesslangset(core_views.support), name='support'),
    path('శోధనఫలితాలు',preprocesslangset( core_views.search_results), name='search_results'),
    path('idn_వెబ్‌సైట్‌లు/<int:id>', preprocesslangset(core_views.idn_websites), name='idn_websites'),
    path('సంఘటన', preprocesslangset(core_views.event), name='event'),
    path('గ్యాలరీ', preprocesslangset(core_views.gallery), name='gallery'),
    path('భాష_గుర్తింపు',preprocesslangset( core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboardte', preprocesslangset(core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_టెక్_పేజీ', preprocesslangset(core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_డాక్యుమెంట్_పేజీ',preprocesslangset( core_views.sop_document_page), name='sop_document_page'), 
    path('sop_పత్రం', preprocesslangset(core_views.sop_document), name='sop_document'), 
    path('tld_వాలిడేటర్', preprocesslangset(core_views.tld_validator), name='tld_validator'),
    path('డాష్బోర్డ్', preprocesslangset(core_views.dashboard), name='dashboard'),
    path('బ్లాగు', preprocesslangset(core_views.blogs), name='blogs'),
    # path('వర్గంఎంపికచేయబడింది/<str:id>', core_views.cat_selected, name='cat_selected'),
    path('బ్లాగు/<str:id>', preprocesslangset(core_views.blogs), name='blogs'),
    path('బ్లాగ్సింగిల్/<str:id>', preprocesslangset(core_views.blog), name='blog'),
    path('test_supportte',preprocesslangset( core_views.test_support), name='test_support'),
    path('idn_websites_requestte',preprocesslangset( core_views.idn_websites_request_AJAX), name='idn_websites_request_AJAX'),
    path('add_blogte',preprocesslangset( core_views.add_blog), name='add_blog'),
    path('edit_blogte/<str:id>', preprocesslangset(core_views.edit_blog), name='edit_blog'),
    path('delete_blogte/<str:id>', preprocesslangset(core_views.delete_blog), name='delete_blog'),
    path('blog_datatablete', preprocesslangset(core_views.admin_blog_datatable), name='admin_blog_datatable'),
    path('search_blog/<str:id>',preprocesslangset( core_views.search_blog), name='search_blog'), # Pending in json file
    path('loginte',preprocesslangset( user_views.login_view), name='login_view'),
    path('registerte', preprocesslangset(user_views.register_view), name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logoutte',preprocesslangset( user_views.logout_view), name='logout_view'),
    path('change_passwordte',preprocesslangset( user_views.change_password_view), name='change_password'),
    path('forgot_passwordte',preprocesslangset( user_views.forgot_password_view), name='forgot_password'),
    path('password_creationte/<uid>/<token>',preprocesslangset( user_views.password_creation_view), name='password_creation'),
    path('discussion_forum_topic_listte', preprocesslangset(topic_list), name="topic_list"),
    path('discussion_forum_user_topic_listte',preprocesslangset( user_topic_list), name="user_topic_list"),
    path('discussion_forum_add_topicte', preprocesslangset(add_topic), name="add_topic"),
    path('discussion_forum_view_topic_discussionte/<slug:topic_slug>',preprocesslangset( view_topic_discussion), name="view_topic_discussion"),
    path('submit_answerte/<slug:topic_slug>',preprocesslangset( submit_answer), name='submit_answer'),
    path('upvote_answerte', preprocesslangset(upvote_answer_view), name='upvote_answer_view'),
    path('test_taskte', preprocesslangset(core_views.test_celery), name="test_task"),
    path('user_profile',preprocesslangset( user_views.user_profile_view), name='user_profile'), # Pending in json file
]   