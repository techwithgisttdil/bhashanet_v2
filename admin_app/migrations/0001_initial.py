# Generated by Django 5.0.4 on 2024-10-18 04:44

import ckeditor.fields
import core_app.validate
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_receipient_list', models.FileField(upload_to='receipient_list')),
                ('email_subject', models.TextField()),
                ('email_message', ckeditor.fields.RichTextField()),
                ('email_status', models.TextField()),
                ('email_sending_date', models.DateTimeField(auto_now=True)),
                ('emails_sent_count', models.IntegerField(default=0)),
                ('email_pause_threshold', models.IntegerField(default=5)),
            ],
            options={
                'verbose_name_plural': 'Bulk Email',
            },
        ),
        migrations.CreateModel(
            name='category_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('updated_On', models.DateField(default=django.utils.timezone.now)),
                ('Last_Updated_On', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'category_list',
            },
        ),
        migrations.CreateModel(
            name='language_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=25)),
                ('updated_On', models.DateField(default=django.utils.timezone.now)),
                ('Last_Updated_On', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'language_list',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role_Name', models.CharField(max_length=20)),
                ('Role_Status', models.CharField(blank=True, choices=[('Active', 'ACTIVE'), ('Inactive', 'INACTIVE')], default='Active', max_length=20, null=True)),
                ('Role_Created_Date', models.DateField(auto_now_add=True)),
                ('Role_Last_Updated_Date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'User Roles',
            },
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BlogCategory_Name', models.CharField(max_length=500)),
                ('BlogCategory_Status', models.BooleanField(default=False)),
                ('BlogCategory_CreationDate', models.DateField(auto_now_add=True)),
                ('BlogCategory_LastUpdatedDate', models.DateField(auto_now=True)),
                ('BlogCategory_PublishedStatus', models.CharField(choices=[('Published', 'PUBLISHED'), ('Unpublished', 'UNPUBLISHED')], default='Unpublished', max_length=20)),
                ('BlogCategory_Author_Char', models.CharField(blank=True, max_length=500, null=True)),
                ('BlogCategory_Author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Blog Category Category',
                'ordering': ['BlogCategory_Name'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blog_Title', models.CharField(max_length=800)),
                ('Blog_Slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('Blog_Description', models.TextField()),
                ('Blog_Body', ckeditor.fields.RichTextField()),
                ('Blog_CreationDate', models.DateField(auto_now_add=True)),
                ('Blog_LastUpdatedDate', models.DateField(auto_now=True)),
                ('Blog_Author_Char', models.CharField(blank=True, max_length=200, null=True)),
                ('Blog_PublishedStatus', models.CharField(choices=[('Published', 'PUBLISHED'), ('Unpublished', 'UNPUBLISHED')], default='Unpublished', max_length=20)),
                ('Blog_Thumbnail', models.ImageField(blank=True, null=True, upload_to='admin_app/Blog/Thumbnail', validators=[core_app.validate.validate_image, django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'JPEG', 'svg'])])),
                ('Blog_DocumentFile', models.FileField(blank=True, null=True, upload_to='admin_app/Blog/DocumentFile', validators=[django.core.validators.FileExtensionValidator(['pdf', 'zip', 'csv', 'xls', 'ppt', 'html'])])),
                ('Blog_Author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Blog_CategoryType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.blogcategory')),
            ],
            options={
                'verbose_name_plural': 'Blogs',
                'ordering': ['Blog_Title'],
            },
        ),
        migrations.CreateModel(
            name='BulkEmailAttachments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_attachment', models.FileField(blank=True, null=True, upload_to='email_attachment')),
                ('bulk_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.bulkemail')),
            ],
            options={
                'verbose_name_plural': 'Bulk Email Attachment',
            },
        ),
        migrations.CreateModel(
            name='CustomForgotPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forgot_password_token', models.CharField(max_length=100)),
                ('generation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('counter', models.IntegerField()),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Custom Forgot Password',
                'verbose_name_plural': 'Custom Forgot Password',
            },
        ),
        migrations.CreateModel(
            name='English_Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.TextField()),
                ('domain_name', models.CharField(max_length=256)),
                ('updated_On', models.DateField(default=django.utils.timezone.now)),
                ('Last_Updated_On', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.category_list')),
            ],
            options={
                'verbose_name_plural': 'English_Domain',
            },
        ),
        migrations.CreateModel(
            name='OTP_For_UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OTP_Value', models.IntegerField()),
                ('OTP_Entered_Count', models.IntegerField()),
                ('OTP_Status', models.BooleanField(blank=True, default=False, null=True)),
                ('OTP_Created_Date', models.DateTimeField(auto_now=True)),
                ('OTP_Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'OTP FOR User Registration',
                'verbose_name_plural': 'OTP FOR User Registration',
            },
        ),
        migrations.CreateModel(
            name='URL_dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDN_domain', models.CharField(max_length=255, unique=True)),
                ('ssl_configuration_status', models.TextField()),
                ('idn_domain_running_status', models.TextField()),
                ('content_language', models.TextField()),
                ('updated_On', models.DateField(default=django.utils.timezone.now)),
                ('Last_Updated_On', models.DateField(auto_now=True)),
                ('Remark', models.TextField()),
                ('English_domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.english_domain')),
                ('Language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.language_list')),
            ],
            options={
                'verbose_name_plural': 'URL_dashboard',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserProfile_name', models.CharField(max_length=100)),
                ('UserProfile_designation', models.CharField(max_length=50)),
                ('UserProfile_organization', models.CharField(max_length=50)),
                ('UserProfile_organization_logo', models.ImageField(blank=True, null=True, upload_to='user/organization_logo')),
                ('UserProfile_CreationDate', models.DateField(auto_now_add=True)),
                ('UserProfile_LastUpdatedDate', models.DateField(auto_now=True)),
                ('UserProfile_Bio', models.CharField(blank=True, max_length=500, null=True)),
                ('UserProfile_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Profile',
            },
        ),
        migrations.CreateModel(
            name='UserRoleMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role_Category_Mapping_Status', models.CharField(blank=True, choices=[('Active', 'ACTIVE'), ('Inactive', 'INACTIVE')], default='Active', max_length=20, null=True)),
                ('Role_Category_Mapping_Created_Date', models.DateField(auto_now_add=True)),
                ('Role_Category_Mapping_Last_Updated_Date', models.DateField(auto_now_add=True)),
                ('Role_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.userrole')),
                ('User_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Role Mapping',
            },
        ),
    ]