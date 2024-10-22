from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'admin_app'

urlpatterns = [
    path('', views.login_view, name="login_view"),
    path('idn_domain_forms', views.idn_domain_forms, name="idn_domain_forms"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('email_compose', views.email_compose, name="email_compose"),
    path('sent_email_view', views.sent_email_view, name="sent_email_view"),
    path('sent_email_view_detail/<int:id>', views.sent_email_view_detail, name="sent_email_view_detail"),
    path('refresh_domain_parameters/<int:id>', views.refresh_domain_parameters, name="refresh_domain_parameters"),
    path('edit_idn_domain_forms/<int:id>', views.edit_idn_domain_forms, name="edit_idn_domain_forms"),
    path('show_logs',views.show_logs,name="show_logs"),
    path('clear_logs',views.clear_logs,name="clear_logs"),
    path('show_logs_last',views.show_logs_last,name="show_logs_last"),
    path('upload_excel',views.upload_excel,name="upload_excel"),
    path('dashboard2', views.dashboard2, name="dashboard2"),
    # path('admin_login', views.admin_login, name="admin_login"),
    path('admin_logout', views.admin_logout, name='admin_logout'), 
    path('idn_domain_list',views.idn_domain_list, name='idn_domain_list'),
    path('english_domain_list',views.english_domain_list,name='english_domain_list'),
    path('update_all_domains',views.update_all_domains,name='update_all_domains'),
    path('tinymce/', include('tinymce.urls')),
    path('logout', views.logout_view, name='logout_view'),
]

