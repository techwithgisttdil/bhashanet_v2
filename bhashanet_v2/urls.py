# ----ADDED BY SHWETA PATIL ----
from django.contrib import admin
from django.urls import path, include, re_path as url
from django.conf import settings
from django.conf.urls.static import static
from core_app import views as core_views
from admin_app import views as user_views
from django.views.static import serve
from discussion_forum_app.views import *
from django.contrib.sitemaps.views import sitemap
from core_app.sitemap import StaticSitemap
from core_app.decorator import preprocesslangset

# ----ADDED BY SHWETA PATIL ----
from .url.assamese_urls import Translation_urlpatterns_assamese
from .url.bengali_urls import Translation_urlpatterns_bengali
from .url.boro_urls import Translation_urlpatterns_boro
from .url.dogri_urls import Translation_urlpatterns_dogri
from .url.gujarati_urls import Translation_urlpatterns_gujarati
from .url.hindi_urls import Translation_urlpatterns_hindi
from .url.kannada_urls import Translation_urlpatterns_kannada
from .url.konkani_urls import Translation_urlpatterns_konkani
from .url.malayalam_urls import Translation_urlpatterns_malayalam
from .url.manipuri_urls import Translation_urlpatterns_manipuri
from .url.marathi_urls import Translation_urlpatterns_marathi
from .url.nepali_urls import Translation_urlpatterns_nepali
from .url.oriya_urls import Translation_urlpatterns_oriya
from .url.punjabi_urls import Translation_urlpatterns_punjabi
from .url.tamil_urls import Translation_urlpatterns_tamil
from .url.telugu_urls import Translation_urlpatterns_telugu
from .url.kashmiri_urls import Translation_urlpatterns_kashmiri
from .url.maithili_urls import Translation_urlpatterns_maithili
from .url.sanskrit_urls import Translation_urlpatterns_sanskrit
from .url.santali_urls import Translation_urlpatterns_santali
from .url.sindhi_urls import Translation_urlpatterns_sindhi
from .url.urdu_urls import Translation_urlpatterns_urdu


sitemaps = {
    'bhashanet_static': StaticSitemap,
}

# ----ADDED BY SHWETA PATIL ----
urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    # path('rosetta/', include('rosetta.urls')),
    path('captcha_refresh/', core_views.captcha_refresh, name='captcha_refresh'),  # added by shivam sharma
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('submit_reply_to_answer/<slug:topic_slug>/<answer_id>', submit_reply_to_answer, name='submit_reply_to_answer'),
    path('submit_reply_to_answer_2/<slug:topic_slug>/<answer_id>/<reply_id>', submit_reply_to_answer_2, name='submit_reply_to_answer_2'),
    path('SopDownloadCounter/<int:id>', core_views.SopDownloadCounter,name='SopDownloadCounter'),
    path('update_json', core_views.update_json, name="update_json"),
    path('display_table2', core_views.display_table2, name="display_table2"),
    path('idn_rediness_dashboard', core_views.idn_rediness_dashboard, name="idn_rediness_dashboard"),  
    path('bhashanet_dashboard/', include('admin_app.urls')),   
]


Translation_urlpatterns = [
    path((''), core_views.landingfunction, name='home'),
    path('home', core_views.home, name='home'),
    path('privacypolicy', preprocesslangset(core_views.privacypolicy), name='privacypolicy'),
    path('termsandconditions', preprocesslangset(core_views.termsandconditions), name='termsandconditions'),
    path('uaindiaprogramme', preprocesslangset(core_views.uaindiaprogramme), name='uaindiaprogramme'),
    path('IDNCCTLD', preprocesslangset(core_views.IDNCCTLD), name='IDNCCTLD'),
    path('bestpractices', preprocesslangset(core_views.bestpractices), name='bestpractices'),
    path('EAI', preprocesslangset(core_views.EAI), name='EAI'),
    path('UA', preprocesslangset(core_views.UA), name='UA'),
    path('tools', preprocesslangset(core_views.tools), name='tools'),
    path('unicode_punycode_generator', preprocesslangset(core_views.unicode_punycode_generator), name='unicode_punycode_generator'),
    path('unicode_fonts', preprocesslangset(core_views.unicode_fonts), name='unicode_fonts'),
    path('transliteration', preprocesslangset(core_views.transliteration), name='transliteration'),
    path('script_detection', preprocesslangset(core_views.script_detection), name='script_detection'),
    path('domain_validator', preprocesslangset(core_views.domain_validator), name='domain_validator'),
    path('email_validator', preprocesslangset(core_views.email_validator), name='email_validator'),
    path('feedback', preprocesslangset(core_views.feedback), name='feedback'),
    path('becomeuaready', preprocesslangset(core_views.becomeuaready), name='becomeuaready'),
    path('FAQS', preprocesslangset(core_views.FAQs), name='FAQs'),
    path('documentPage', preprocesslangset(core_views.documentPage), name='documentPage'),
    path('documentData', preprocesslangset(core_views.documentData), name='documentData'),
    path('support', preprocesslangset(core_views.support), name='support'),
    path('testimonial', preprocesslangset(core_views.testimonial), name='testimonial'),
    path('search_results', preprocesslangset(core_views.search_results), name='search_results'),
    path('testimonials', preprocesslangset(core_views.testimonials), name='testimonials'),
    path('idn_websites/<str:id>', preprocesslangset(core_views.idn_websites), name='idn_websites'),
    path('event', preprocesslangset(core_views.event), name='event'),
    path('gallery', preprocesslangset(core_views.gallery), name='gallery'),
    path('language_detection', preprocesslangset(core_views.language_detection), name='language_detection'), # added by tanvi patil
    path('cdac_keyboard', preprocesslangset(core_views.cdac_keyboard), name='cdac_keyboard'), # added by tanvi patil
    path('sop_tech_page', preprocesslangset(core_views.SOPTechnalogyPage), name='sop_tech_page'), 
    path('sop_document_page', preprocesslangset(core_views.sop_document_page), name='sop_document_page'), 
    path('sop_document', preprocesslangset(core_views.sop_document), name='sop_document'), 
    path('tld_validator', preprocesslangset(core_views.tld_validator), name='tld_validator'),
    path('dashboard', preprocesslangset(core_views.dashboard), name='dashboard'),
    path('admindashboard', preprocesslangset(core_views.admindashboard), name='admindashboard'),
    path('blogs', preprocesslangset(core_views.blogs), name='blogs'),
    # path('cat_selected', core_views.cat_selected, name='cat_selected'),
    path('blogs/<str:id>', preprocesslangset(preprocesslangset(core_views.blogs)), name='blogs'),
    path('blog/<str:id>', preprocesslangset(core_views.blog), name='blog'),
    path('test_support', core_views.test_support, name='test_support'),
    path('idn_websites_request', core_views.idn_websites_request_AJAX, name='idn_websites_request_AJAX'),
    path('idn_websites_request1', core_views.idn_websites_request1, name='idn_websites_request1'),
    path('add_blog', core_views.add_blog, name='add_blog'),
    path('edit_blog/<str:id>', core_views.edit_blog, name='edit_blog'),
    path('delete_blog/<str:id>', core_views.delete_blog, name='delete_blog'),
    path('blog_datatable', core_views.admin_blog_datatable, name='admin_blog_datatable'),
    path('search_blog/<str:id>', core_views.search_blog, name='search_blog'),
    path('login', user_views.login_view, name='login_view'),
    path('register', user_views.register_view, name='register_view'),
    # path('activate/<uid64>/<token>', user_views.user_activate_view, name='user_activate'),
    path('logout', user_views.logout_view, name='logout_view'),
    path('change_password', user_views.change_password_view, name='change_password'),
    path('forgot_password', user_views.forgot_password_view, name='forgot_password'),
    path('password_creation/<uid>/<token>', user_views.password_creation_view, name='password_creation'),
    path('discussion_forum_topic_list', topic_list, name="topic_list"),
    path('discussion_forum_user_topic_list', user_topic_list, name="user_topic_list"),
    path('discussion_forum_add_topic', add_topic, name="add_topic"),
    path('discussion_forum_view_topic_discussion/<slug:topic_slug>', view_topic_discussion, name="view_topic_discussion"),
    path('submit_answer/<slug:topic_slug>', submit_answer, name='submit_answer'),
    path('upvote_answer', upvote_answer_view, name='upvote_answer_view'),
    path('test_task', core_views.test_celery, name="test_task"),
    path('user_profile', user_views.user_profile_view, name='user_profile'),
    # path("<path>", core_views.RenderPageWithPathAndLang, name="RenderPageWithPathAndLang"),
    # path("<path>"+"/<uid>"+"/<token>", core_views.RenderPageWithPathAndLangIdToken, name='RenderPageWithPathAndLangIdToken'),
    # path("<path>"+"/<str:id>", core_views.RenderPageWithPathAndLangId, name="RenderPageWithPathAndLangId"),


    path('verify_user_otp/<str:email>', user_views.verify_user_otp, name='verify_user_otp'),
      
]

# ----ADDED BY SHWETA PATIL ----
urlpatterns = urlpatterns + Translation_urlpatterns + Translation_urlpatterns_hindi + Translation_urlpatterns_marathi + Translation_urlpatterns_kannada + Translation_urlpatterns_malayalam + Translation_urlpatterns_bengali + Translation_urlpatterns_manipuri + Translation_urlpatterns_gujarati + Translation_urlpatterns_punjabi + Translation_urlpatterns_telugu + Translation_urlpatterns_tamil + Translation_urlpatterns_assamese + Translation_urlpatterns_konkani + Translation_urlpatterns_nepali + Translation_urlpatterns_boro + Translation_urlpatterns_dogri + Translation_urlpatterns_oriya + Translation_urlpatterns_kashmiri +Translation_urlpatterns_maithili + Translation_urlpatterns_sanskrit + Translation_urlpatterns_santali + Translation_urlpatterns_sindhi + Translation_urlpatterns_urdu
# urlpatterns = urlpatterns + Translation_urlpatterns


# ----ADDED BY SHWETA PATIL ----
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'core_app.views.custom_page_not_found_view'
handler500 = 'core_app.views.custom_error_view'
handler403 = 'core_app.views.custom_permission_denied_view'
handler400 = 'core_app.views.custom_bad_request_view'
