from django.db import models
# from django.utils import timezone
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.timezone import now
from core_app.validate import *

# Create your models here.
#########################################################################################

class category_list(models.Model):
    category_name = models.CharField(max_length=100)
    updated_On = models.DateField(default=now)
    Last_Updated_On = models.DateField(auto_now=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "category_list"

#########################################################################################

class English_Domain(models.Model):
    department_name = models.TextField()
    domain_name = models.CharField(max_length=256)
    category = models.ForeignKey(category_list, on_delete=models.CASCADE)
    updated_On = models.DateField(default=now)
    Last_Updated_On = models.DateField(auto_now=True)

    def __str__(self):
        return self.domain_name

    class Meta:
        verbose_name_plural = "English_Domain"

#########################################################################################

class language_list(models.Model):
    language_name = models.CharField(max_length=25)
    updated_On = models.DateField(default=now)
    Last_Updated_On = models.DateField(auto_now=True)

    def __str__(self):
        return self.language_name

    class Meta:
        verbose_name_plural = "language_list"

#########################################################################################
# FOR instant display in status table 
class URL_dashboard(models.Model):
    English_domain = models.ForeignKey(English_Domain, on_delete=models.CASCADE)
    Language = models.ForeignKey(language_list, on_delete=models.CASCADE)
    IDN_domain = models.CharField(max_length=255, unique=True) # Changes done by Shweta From TextField to CharField for unique data
    ssl_configuration_status = models.TextField()
    idn_domain_running_status = models.TextField()
    content_language = models.TextField()
    updated_On = models.DateField(default=now)
    Last_Updated_On = models.DateField(auto_now=True)
    Remark = models.TextField()

    def __str__(self):
        return self.IDN_domain

    class Meta:
        verbose_name_plural = "URL_dashboard"
        
#########################################################################################

class BulkEmail(models.Model):
    email_receipient_list = models.FileField(upload_to="receipient_list")
    email_subject = models.TextField()
    email_message = RichTextField()
    email_status = models.TextField()
    email_sending_date = models.DateTimeField(auto_now=True)
    emails_sent_count = models.IntegerField(default=0)   
    email_pause_threshold = models.IntegerField(default=5)
    
    def __str__(self):
        return self.email_subject

    class Meta:
        verbose_name_plural = "Bulk Email"

#########################################################################################

class BulkEmailAttachments(models.Model):
    email_attachment = models.FileField(upload_to="email_attachment", null=True,blank=True)
    bulk_email = models.ForeignKey(BulkEmail, on_delete=models.CASCADE)

    def __str__(self):
        return self.email_attachment.name

    class Meta:
        verbose_name_plural = "Bulk Email Attachment"



# ---------------------------------------------------------------------------------------------------

class BlogCategory(models.Model):
    BlogCategory_Name = models.CharField(max_length=500)
    BlogCategory_Status = models.BooleanField(default=False)
    BlogCategory_CreationDate = models.DateField(auto_now_add=True)
    BlogCategory_LastUpdatedDate = models.DateField(auto_now=True)
    BlogCategory_PublishStatus = (
        ('Published', 'PUBLISHED'), ('Unpublished', 'UNPUBLISHED'))
    BlogCategory_PublishedStatus = models.CharField(
        max_length=20, choices=BlogCategory_PublishStatus, default="Unpublished")
    BlogCategory_Author_Char= models.CharField(
        max_length=500, blank=True, null=True)
    BlogCategory_Author= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    


    
    class Meta:
        verbose_name_plural = "Blog Category Category"
        ordering = ['BlogCategory_Name']

    def __str__(self):
        return self.BlogCategory_Name
    
# ---------------------------------------------------------------------------------------------------

class Blog(models.Model):
    Blog_Title = models.CharField(max_length=800)
    Blog_Slug = models.SlugField(max_length=255, blank=True, null=True)
    Blog_Description = models.TextField()
    Blog_Body = RichTextField()
    Blog_CreationDate = models.DateField(auto_now_add=True)
    Blog_LastUpdatedDate = models.DateField(auto_now=True)
    Blog_Author_Char = models.CharField(max_length=200, null=True, blank=True)
    Blog_CategoryType = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    Blog_Status = (('Published', 'PUBLISHED'),
                       ('Unpublished', 'UNPUBLISHED'))
    Blog_PublishedStatus = models.CharField(
        max_length=20, choices=Blog_Status, default="Unpublished")
    Blog_Thumbnail = models.ImageField(
        upload_to="admin_app/Blog/Thumbnail", validators=[validate_image,
                                                         FileExtensionValidator(
                                                             allowed_extensions=["jpg", "png", "JPEG", "svg"])],
        
        height_field=None, width_field=None, max_length=None, null=True, blank=True)
    Blog_DocumentFile = models.FileField(upload_to="admin_app/Blog/DocumentFile",
                                             validators=[FileExtensionValidator(['pdf', 'zip', 'csv', 'xls', 'ppt', 'html'])], null=True, blank=True)
    Blog_Author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Blogs"
        ordering = ['Blog_Title']

    def save(self, *args, **kwargs):
        self.Blog_Slug=''
        super(Blog, self).save(*args, **kwargs)
        if self.Blog_Slug:
            self.Blog_Slug = slugify(self.Blog_Title + self.Blog_Slug)
        else:
            self.Blog_Slug = slugify(self.Blog_Title )
        super(Blog, self).save(*args, **kwargs)

    def get_slug_splited(self):
        return self.Blog_Slug.split('-')

    def __str__(self):
        return self.Blog_Title
    
# ---------------------------------------------------------------------------------------------------

class UserProfile(models.Model):
    UserProfile_user = models.ForeignKey(User, on_delete=models.CASCADE)
    UserProfile_name = models.CharField(max_length=100)
    UserProfile_designation = models.CharField(max_length=50)
    UserProfile_organization = models.CharField(max_length=50)
    UserProfile_organization_logo = models.ImageField(upload_to="user/organization_logo", height_field=None, width_field=None,max_length=None, null=True, blank=True)
    UserProfile_CreationDate = models.DateField(auto_now_add=True)
    UserProfile_LastUpdatedDate = models.DateField(auto_now=True)
    UserProfile_Bio= models.CharField(max_length=500,null=True, blank=True)

    
  
    class Meta:
        verbose_name_plural = "User Profile"

    def __str__(self):
        return self.UserProfile_user.username
        
# ---------------------------------------------------------------------------------------------------

class UserRole(models.Model):
    Role_Name = models.CharField(max_length=20)
    Role_Status_Choices = (
        ('Active', 'ACTIVE'), ('Inactive', 'INACTIVE'))
    Role_Status = models.CharField(
        max_length=20, choices=Role_Status_Choices, default="Active", blank=True, null=True)
    Role_Created_Date = models.DateField(auto_now_add=True)
    Role_Last_Updated_Date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "User Roles"

    def __str__(self):
        return self.Role_Name
    
# ---------------------------------------------------------------------------------------------------

class UserRoleMapping(models.Model):
    User_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Role_Id = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    Role_Mapping_Choices = (
        ('Active', 'ACTIVE'), ('Inactive', 'INACTIVE'))
    
    Role_Category_Mapping_Status = models.CharField(
        max_length=20, choices=Role_Mapping_Choices, default="Active", blank=True, null=True)
    Role_Category_Mapping_Created_Date = models.DateField(auto_now_add=True)
    Role_Category_Mapping_Last_Updated_Date = models.DateField(
        auto_now_add=True)

    class Meta:
        verbose_name_plural = "User Role Mapping"

    def __str__(self):
        return self.User_Id.username
    
# ---------------------------------------------------------------------------------------------------


    
class CustomForgotPassword(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    forgot_password_token = models.CharField(max_length=100, blank=False)
    generation_time = models.DateTimeField(default=now)
    counter = models.IntegerField(blank=False)

    class Meta:
        verbose_name = "Custom Forgot Password"
        verbose_name_plural = "Custom Forgot Password"

    def __str__(self):
        return self.email.email
    
# ---------------------------------------------------------------------------------------------------


class OTP_For_UserRegistration(models.Model):
    OTP_Email = models.ForeignKey(User,on_delete=models.CASCADE)
    OTP_Value = models.IntegerField()
    OTP_Entered_Count = models.IntegerField()
    OTP_Status = models.BooleanField(default=False, blank=True, null=True)
    OTP_Created_Date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "OTP FOR User Registration"
        verbose_name_plural = "OTP FOR User Registration"

    def __str__(self):
        return str(self.OTP_Email)+'For User'