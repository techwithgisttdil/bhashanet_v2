from django.db import models
from django.core.validators import FileExtensionValidator
from .validate import *
from django.core.validators import MaxValueValidator, MinValueValidator

# ---------------------------------------------------------------------------------------------------

class Article(models.Model):
    Article_Title=models.TextField()
    Article_Alias=models.TextField()
    Article_Title_Description=models.TextField()
    Article_Title_icon=models.ImageField(upload_to='core_app/Article/icon/', blank=True, null=True,
                                            validators=[validate_image,
                                                        FileExtensionValidator(
                                                            allowed_extensions=["jpg", "png",
                                                                                "JPEG", "svg"])],
                                            help_text='Maximum file size allowed is 5Mb')
    Article_Title_Image1=models.ImageField(upload_to='core_app/Article/icon/', blank=True, null=True,
                                            validators=[validate_image,
                                                        FileExtensionValidator(
                                                            allowed_extensions=["jpg", "png",
                                                                                "JPEG", "svg"])],
                                            help_text='Maximum file size allowed is 5Mb')
    Article_Title_Image2=models.ImageField(upload_to='core_app/Article/icon/', blank=True, null=True,
                                            validators=[validate_image,
                                                        FileExtensionValidator(
                                                            allowed_extensions=["jpg", "png",
                                                                                "JPEG", "svg"])],
                                            help_text='Maximum file size allowed is 5Mb')
    Article_Upload_Doc1=models.FileField(upload_to='core_app/Article/upload_doc/', blank=True, null=True)
    Article_Upload_Doc2=models.FileField(upload_to='core_app/Article/upload_doc/', blank=True, null=True)
    Article_Upload_Doc3=models.FileField(upload_to='core_app/Article/upload_doc/', blank=True, null=True)
    Article_Upload_Doc4=models.FileField(upload_to='core_app/Article/upload_doc/', blank=True, null=True)
    Article_Upload_Doc5=models.FileField(upload_to='core_app/Article/upload_doc/', blank=True, null=True)
    Article_Subtitle1=models.CharField(max_length=500, blank=True, null=True)
    Article_Subtitle2=models.CharField(max_length=500, blank=True, null=True)
    Article_Subtitle3=models.CharField(max_length=500, blank=True, null=True)
    Article_Subtitle4=models.CharField(max_length=500, blank=True, null=True)
    Article_Subtitle5=models.CharField(max_length=500, blank=True, null=True)
    Article_Description1=models.TextField(blank=True, null=True)
    Article_Description2=models.TextField(blank=True, null=True)
    Article_Description3=models.TextField(blank=True, null=True)
    Article_Description4=models.TextField(blank=True, null=True)
    Article_Description5=models.TextField(blank=True, null=True)
    Article_Internalink1=models.CharField(max_length=500, blank=True, null=True)
    Article_Internalink2=models.CharField(max_length=500, blank=True, null=True)
    Article_Internalink3=models.CharField(max_length=500, blank=True, null=True)
    Article_Internalink4=models.CharField(max_length=500, blank=True, null=True)
    Article_Internalink5=models.CharField(max_length=500, blank=True, null=True)
    Article_Externalink1=models.CharField(max_length=500, blank=True, null=True)
    Article_Externalink2=models.CharField(max_length=500, blank=True, null=True)
    Article_Externalink3=models.CharField(max_length=500, blank=True, null=True)
    Article_Externalink4=models.CharField(max_length=500, blank=True, null=True)
    Article_Externalink5=models.CharField(max_length=500, blank=True, null=True)
    Article_Image1=models.ImageField(upload_to='core_app/Article/image/', blank=True, validators=[validate_image,
                                                                                                FileExtensionValidator(
                                                                                                    allowed_extensions=[
                                                                                                        "jpg", "png",
                                                                                                        "JPEG",
                                                                                                        "svg"])],
                                        help_text='Maximum file size allowed is 5Mb')
    Article_Image2=models.ImageField(upload_to='core_app/Article/image/', blank=True, validators=[validate_image,
                                                                                                FileExtensionValidator(
                                                                                                    allowed_extensions=[
                                                                                                        "jpg", "png",
                                                                                                        "JPEG",
                                                                                                        "svg"])],
                                        help_text='Maximum file size allowed is 5Mb')
    Article_Image3=models.ImageField(upload_to='core_app/Article/image/', blank=True, validators=[validate_image,
                                                                                                FileExtensionValidator(
                                                                                                    allowed_extensions=[
                                                                                                        "jpg", "png",
                                                                                                        "JPEG",
                                                                                                        "svg"])],
                                        help_text='Maximum file size allowed is 5Mb')
    Article_Image4=models.ImageField(upload_to='core_app/Article/image/', blank=True, validators=[validate_image,
                                                                                                FileExtensionValidator(
                                                                                                    allowed_extensions=[
                                                                                                        "jpg", "png",
                                                                                                        "JPEG",
                                                                                                        "svg"])],
                                        help_text='Maximum file size allowed is 5Mb')
    Article_Image5=models.ImageField(upload_to='core_app/Article/image/', blank=True, validators=[validate_image,
                                                                                                FileExtensionValidator(
                                                                                                    allowed_extensions=[
                                                                                                        "jpg", "png",
                                                                                                        "JPEG",
                                                                                                        "svg"])],
                                        help_text='Maximum file size allowed is 5Mb')

    Article_video=models.FileField(upload_to='core_app/Article/videos_uploaded/', null=True, blank=True,
                                    validators=[FileExtensionValidator(
                                        allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    Article_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    Article_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)
    Article_CreatedDate=models.DateField(auto_now_add=True)
    Article_UpdatedDate=models.DateField(auto_now=True, )
    Article_PublishStatus=models.CharField(
        max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default="Unpublished")

    def __str__(self):
        return self.Article_Title + " - ID : {}".format(self.id) or ''

    class Meta:
        db_table = 'ARTICLE'
        verbose_name_plural = "Single Page Article "

# ---------------------------------------------------------------------------------------------------

class TermsAndConditions(models.Model):
    
    TermsAndConditions_title=models.CharField(max_length=100, blank=True, null=True)
    TermsAndConditions_title_desc=models.TextField(max_length=5000, blank=True, null=True)
    TermsAndConditions_subtitle1=models.CharField(max_length=100, blank=True, null=True)
    TermsAndConditions_desc1=models.TextField(max_length=5000, blank=True, null=True)
    TermsAndConditions_document1=models.FileField(upload_to='core_app/terms_and_conditions/documents', null=True,
                                                    blank=True,
                                                    validators=[FileExtensionValidator(
                                                        allowed_extensions=['doc', 'docx', 'pdf'])])
    TermsAndConditions_subtitle2=models.CharField(max_length=100, blank=True, null=True)
    TermsAndConditions_desc2=models.TextField(max_length=5000, blank=True, null=True)
    TermsAndConditions_document2=models.FileField(upload_to='core_app/terms_and_conditions/documents', null=True,
                                                    blank=True,
                                                    validators=[FileExtensionValidator(
                                                        allowed_extensions=['doc', 'docx', 'pdf'])])
    TermsAndConditions_subtitle3=models.CharField(max_length=100, blank=True, null=True)
    TermsAndConditions_desc3=models.TextField(max_length=5000, blank=True, null=True)
    TermsAndConditions_document3=models.FileField(upload_to='core_app/terms_and_conditions/documents', null=True,
                                                    blank=True,
                                                    validators=[FileExtensionValidator(
                                                        allowed_extensions=['doc', 'docx', 'pdf'])])
    TermsAndConditions_subtitle4=models.CharField(max_length=100, blank=True, null=True)
    TermsAndConditions_desc4=models.TextField(max_length=5000, blank=True, null=True)
    TermsAndConditions_document4=models.FileField(upload_to='core_app/terms_and_conditions/documents', null=True,
                                                    blank=True,
                                                    validators=[FileExtensionValidator(
                                                        allowed_extensions=['doc', 'docx', 'pdf'])])
    TermsAndConditions_subtitle5=models.CharField(max_length=100, blank=True, null=True)
    TermsAndConditions_desc5=models.TextField(max_length=5000, blank=True, null=True)
    TermsAndConditions_document5=models.FileField(upload_to='core_app/terms_and_conditions/documents', null=True,
                                                    blank=True,
                                                    validators=[FileExtensionValidator(
                                                        allowed_extensions=['doc', 'docx', 'pdf'])])
    TermsAndConditions_image=models.ImageField(upload_to='core_app/terms_and_conditions/img', blank=True, null=True,
                                                validators=[validate_image, FileExtensionValidator(
                                                    allowed_extensions=["jpg", "png", "JPEG", 'svg'])],
                                                help_text='Maximum file size allowed is 5Mb')
    TermsAndConditions_url=models.CharField(max_length=500, blank=True, null=True)
    TermsAndConditions_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    TermsAndConditions_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)
    TermsAndConditions_PublishStatus=models.CharField(
        max_length=30, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default='Unpublished')
    TermsAndConditions_CreationDate=models.DateField(auto_now_add=True)
    TermsAndConditions_LastUpdateDate=models.DateField(auto_now=True)

    class Meta:
        db_table = 'TERMS_AND_CONDITIONS'
        verbose_name_plural = "Terms and Conditions"

    def __str__(self):
        return self.TermsAndConditions_title or ''

# ---------------------------------------------------------------------------------------------------

class FeedbackCategory(models.Model):
    FeedbackCategory_Name = models.CharField(max_length=300)
    FeedbackCategory_CreationDate=models.DateField(auto_now_add=True)
    FeedbackCategory_LastUpdateDate=models.DateField(auto_now=True, blank=True, null=True)


    def __str__(self):
        return self.FeedbackCategory_Name or ''
    
    class Meta:
        db_table = 'FeedbackCategory'
        verbose_name_plural = "Feedback Categories"

# ---------------------------------------------------------------------------------------------------

class UserFeedbackData(models.Model):
    Feedback_FirstName = models.CharField(max_length=30)
    Feedback_Email = models.CharField(max_length=300, blank=False)
    Feedback_Related_To = models.ForeignKey(FeedbackCategory,on_delete=models.CASCADE)
    Feedback_Message = models.TextField(max_length=500)
    Feedback_Submission_Date = models.DateField(
        auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.Feedback_FirstName or ''
    

    class Meta:
        db_table = 'UserFeedbackData'
        verbose_name_plural = "User Feedback Data"

# ---------------------------------------------------------------------------------------------------

class LimitCheck(models.Model):
    Email = models.CharField(max_length=300, blank=False)
    Generation_Time = models.DateField(auto_now=True)
    Counter = models.IntegerField(blank=False, null=True, validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])

    def __str__(self):
        return self.Email

    class Meta:
        db_table = "LimitCheck"
        verbose_name_plural = "LimitCheck"

# ---------------------------------------------------------------------------------------------------

class DomainSyntax(models.Model):
    Domain_Name = models.CharField(max_length=253)

    def __str__(self):
        return self.Domain_Name or ''

    class Meta:
        db_table = 'DOMAIN SYNTAX'
        verbose_name_plural = "DOMAIN SYNTAX"

# ---------------------------------------------------------------------------------------------------
    
class EmailSyntax(models.Model):
    Email_Address = models.CharField(max_length=350)

    def __str__(self):
        return self.Email_Address or ''

    class Meta:
        db_table = 'EMAIL SYNTAX'
        verbose_name_plural = "EMAIL SYNTAX"

# ---------------------------------------------------------------------------------------------------

class BestPractices(models.Model):
    
    BestPractices_title=models.CharField(max_length=100, blank=True, null=True)
    BestPractices_title_desc=models.TextField(max_length=1000, blank=True, null=True)
    BestPractices_title_image=models.ImageField(upload_to='core_app/best_practices/img', blank=True, null=True,
                                                validators=[validate_image, FileExtensionValidator(
                                                    allowed_extensions=["jpg", "png", "JPEG", 'svg'])],
                                                help_text='Maximum file size allowed is 5Mb')
    BestPractices_subtitle1=models.CharField(max_length=100, blank=True, null=True)
    BestPractices_desc1=models.TextField(max_length=1000, blank=True, null=True)
    BestPractices_image1=models.ImageField(upload_to='core_app/best_practices/img', blank=True, null=True,
                                            validators=[validate_image, FileExtensionValidator(
                                                allowed_extensions=["jpg", "png", "JPEG", 'svg'])],
                                            help_text='Maximum file size allowed is 5Mb')
    BestPractices_internalURL1=models.CharField(max_length=500, blank=True, null=True)
    BestPractices_externalURL1=models.CharField(max_length=500, blank=True, null=True)
    BestPractices_subtitle2=models.CharField(max_length=100, blank=True, null=True)
    BestPractices_desc2=models.TextField(max_length=1000, blank=True, null=True)
    BestPractices_image2=models.ImageField(upload_to='core_app/best_practices/img', blank=True, null=True,
                                            validators=[validate_image, FileExtensionValidator(
                                                allowed_extensions=["jpg", "png", "JPEG", 'svg'])],
                                            help_text='Maximum file size allowed is 5Mb')
    BestPractices_internalURL2=models.CharField(max_length=500, blank=True, null=True)
    BestPractices_externalURL2=models.CharField(max_length=500, blank=True, null=True)
    BestPractices_subtitle3=models.CharField(max_length=100, blank=True, null=True)
    BestPractices_desc3=models.TextField(max_length=1000, blank=True, null=True)
    BestPractices_image3=models.ImageField(upload_to='core_app/best_practices/img', blank=True, null=True,
                                            validators=[validate_image, FileExtensionValidator(
                                                allowed_extensions=["jpg", "png", "JPEG", 'svg'])],
                                            help_text='Maximum file size allowed is 5Mb')
    BestPractices_internalURL3=models.CharField(max_length=500, blank=True, null=True)
    BestPractices_externalURL3=models.CharField(max_length=500, blank=True, null=True)
    BestPractices_subtitle4=models.CharField(max_length=100, blank=True, null=True)
    BestPractices_desc4=models.TextField(max_length=1000, blank=True, null=True)
    BestPractices_image4=models.ImageField(upload_to='core_app/best_practices/img', blank=True, null=True,
                                            validators=[validate_image, FileExtensionValidator(
                                                allowed_extensions=["jpg", "png", "JPEG", 'svg'])],
                                            help_text='Maximum file size allowed is 5Mb')
    BestPractices_internalURL4=models.CharField(max_length=500, blank=True, null=True)
    BestPractices_externalURL4=models.CharField(max_length=500, blank=True, null=True)
    BestPractices_subtitle5=models.CharField(max_length=100, blank=True, null=True)
    BestPractices_desc5=models.TextField(max_length=1000, blank=True, null=True)
    BestPractices_image5=models.ImageField(upload_to='core_app/best_practices/img', blank=True, null=True,
                                            validators=[validate_image, FileExtensionValidator(
                                                allowed_extensions=["jpg", "png", "JPEG", 'svg'])],
                                            help_text='Maximum file size allowed is 5Mb')
    BestPractices_internalURL5=models.CharField(max_length=500, blank=True, null=True)
    BestPractices_externalURL5=models.CharField(max_length=500, blank=True, null=True)
    BestPractices_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    BestPractices_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)
    BestPractices_PublishStatus=models.CharField(
        max_length=30, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default='Unpublished')
    BestPractices_CreationDate=models.DateField(auto_now_add=True)
    BestPractices_LastUpdateDate=models.DateField(auto_now=True)
    

    class Meta:
        db_table = 'BEST PRACTICES'
        verbose_name_plural = "Best Practices"

    def __str__(self):
        return self.BestPractices_title or ''
    
    def clean(self):
        super().clean()
        
        # Validate BestPractices_image1
        if self.BestPractices_image1:
            print("Present Here ....")
            validate_image(self.BestPractices_image1)
            extension = self.BestPractices_image1.name.split('.')[-1].lower()
            if extension not in ['jpg', 'png', 'jpeg', 'svg']:
                raise ValidationError('Invalid file extension for image1.')

# ---------------------------------------------------------------------------------------------

class Announcements(models.Model):

    Announcement_Title=models.TextField(blank=True, null=True)
    Announcement_Description=models.TextField(blank=True, null=True)
    Announcement_Description1=models.TextField(blank=True, null=True)
    Announcement_PublishStatus=models.CharField(
        max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default="Unpublished")
    Announcement_Image=models.ImageField(upload_to='core_app/Announcement/', blank=True, validators=[validate_image,
                                                                                                    FileExtensionValidator(
                                                                                                        allowed_extensions=[
                                                                                                            "jpg",
                                                                                                            "png",
                                                                                                            "JPEG",
                                                                                                            "svg"])],
                                            help_text='Maximum file size allowed is 5Mb')
    Announcement_InternalURL=models.CharField(max_length=500, blank=True, null=True)
    Announcement_ExternalURL=models.CharField(max_length=500, blank=True, null=True)
    Announcement_CreatedDate=models.DateField(auto_now_add=True,blank=True, null=True)
    Announcement_UpdatedDate=models.DateField(auto_now=True, blank=True, null=True)
    Announcement_Author=models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.Announcement_Title or ''

    class Meta:
        db_table = 'ANNOUNCEMENTS'
        verbose_name_plural = "Announcements"

# ---------------------------------------------------------------------------------------------

class Testimonials(models.Model):
    
    Testimonials_Title=models.TextField()
    Testimonials_Description=models.TextField()
    Testimonials_Description1=models.TextField(blank=True, null=True)
    Testimonials_PublishStatus=models.CharField(
        max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default="Unpublished")
    Testimonials_Image=models.ImageField(upload_to='core_app/Testimonials/', blank=True, validators=[validate_image,
                                                                                                    FileExtensionValidator(
                                                                                                        allowed_extensions=[
                                                                                                            "jpg",
                                                                                                            "png",
                                                                                                            "JPEG",
                                                                                                            "svg"])],
                                            help_text='Maximum file size allowed is 5Mb')
    Testimonials_InternalURL=models.CharField(max_length=500, blank=True, null=True)
    Testimonials_ExternalURL=models.CharField(max_length=500, blank=True, null=True)
    Testimonials_CreatedDate=models.DateField(auto_now_add=True)
    Testimonials_UpdatedDate=models.DateField(auto_now=True, blank=True, null=True)
    Testimonials_Author=models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.Testimonials_Title or ''

    class Meta:
        db_table = 'TESTIMONIALS'
        verbose_name_plural = "Testimonials"

# ------------------------------------------------------------------------------------------------

class Objectives(models.Model):
    
    Objectives_Name=models.CharField(max_length=800)
    Objectives_Description=models.TextField()
    Objectives_CreationDate=models.DateField(auto_now_add=True)
    Objectives_LastUpdatedDate=models.DateField(auto_now=True)
    Objectives_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    Objectives_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)
    Objectives_PublishedStatus=models.CharField(
        max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default="Unpublished")
    Objectives_Slug=models.SlugField(max_length=255, blank=True, null=True)
    Objectives_Thumbnail=models.ImageField(
        upload_to="core_app/Objectives/Thumbnail", validators=[validate_image,
                                                            FileExtensionValidator(
                                                                allowed_extensions=["jpg", "png", "JPEG", "svg"])],
        help_text='Maximum file size allowed is 5Mb',
        height_field=None, width_field=None, max_length=None, null=True, blank=True)

    class Meta:
        db_table = 'OBJECTIVE'
        verbose_name_plural = "Objectives"

    def __str__(self):
        return self.Objectives_Name or ''

# ------------------------------------------------------------------------------------------------

class DocumentCategory(models.Model):
    
    DocumentCategory_Name=models.CharField(max_length=500)
    DocumentCategory_Status=models.BooleanField(default=False)
    DocumentCategory_CreationDate=models.DateField(auto_now_add=True)
    DocumentCategory_LastUpdatedDate=models.DateField(auto_now=True)
    DocumentCategory_PublishedStatus=models.CharField(
        max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default="Unpublished")
    DocumentCategory_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    DocumentCategory_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'DOCUMENT_CATEGORY'
        verbose_name_plural = "Document Category"

    def __str__(self):
        return self.DocumentCategory_Name or ''

# ------------------------------------------------------------------------------------------------

class Document(models.Model):
    
    Document_Name=models.CharField(max_length=800)
    Document_Description=models.TextField()
    Document_CreationDate=models.DateField(auto_now_add=True)
    Document_LastUpdatedDate=models.DateField(auto_now=True)
    Document_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    Document_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)
    Document_CategoryType=models.ForeignKey(
        DocumentCategory, on_delete=models.CASCADE)
    Document_LanguageType=models.CharField(max_length=500)
    Document_PublishedStatus=models.CharField(
        max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default="Unpublished")
    Document_Slug=models.SlugField(max_length=255, blank=True, null=True)
    Document_Thumbnail=models.ImageField(
        upload_to="core_app/Document/Thumbnail", validators=[validate_image,
                                                            FileExtensionValidator(
                                                                allowed_extensions=["jpg", "png", "JPEG", "svg"])],
        help_text='Maximum file size allowed is 5Mb',
        height_field=None, width_field=None, max_length=None, null=True, blank=True)
    Document_DocumentFile=models.FileField(upload_to="core_app/Document/DocumentFile",
                                            validators=[
                                                FileExtensionValidator(['pdf', 'zip', 'csv', 'xls', 'ppt', 'html'])],
                                            null=True, blank=True)
    Document_FileSize=models.CharField(max_length=30)
    Document_Count=models.IntegerField()
    Document_Type=models.CharField(max_length=30)
    DocumentUASG_url=models.CharField(max_length=500, blank=True, null=True)


    class Meta:
        db_table = 'DOCUMENT'
        verbose_name_plural = "Document"

    def __str__(self):
        return self.Document_Name or ''

    def get_slug_splited(self):
        return self.Document_Slug.split('-')

# ------------------------------------------------------------------------------------------------

class FaqCategory(models.Model):
    
    FaqCategory_Name=models.CharField(max_length=300, blank=False)
    FaqCategory_CreationDate=models.DateField(auto_now_add=True)
    FaqCategory_LastUpdateDate=models.DateField(
        auto_now=True, blank=True, null=True)
    FaqCategory_Author=models.CharField(
        max_length=100, blank=True, null=True)
    FaqCategory_PublishStatus=models.CharField(
        max_length=20, choices=[('Published', 'Published'), ('Unpublished', 'Unpublished')], default="Unpublished")
    

    def __str__(self):
        return self.FaqCategory_Name or ''

    class Meta:
        db_table = 'FAQS_CATEGORY'
        verbose_name_plural = "FAQ's Category"

# ------------------------------------------------------------------------------------------------

class Faqs(models.Model):
    
    Faqs_Ques=models.TextField()
    Faqs_Ans=models.TextField()
    Faqs_CreationDate=models.DateField(auto_now_add=True)
    Faqs_LastUpdateDate=models.DateField(
        auto_now=True, blank=True, null=True)
    Faqs_PublishStatus=models.CharField(
        max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default="Unpublished")
    Faqs_Category=models.ForeignKey(FaqCategory, on_delete=models.CASCADE)
    Faqs_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    Faqs_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Faqs_Ques or ''

    class Meta:
        db_table = 'FAQS'
        verbose_name_plural = "Frequently Asked Questions"

# ------------------------------------------------------------------------------------------------

class PrivacyPolicy(models.Model):
    
    PrivacyPolicy_title=models.CharField(max_length=100, blank=True, null=True)
    PrivacyPolicy_title_desc=models.TextField(max_length=2000, blank=True, null=True)
    PrivacyPolicy_subtitle1=models.CharField(max_length=100, blank=True, null=True)
    PrivacyPolicy_desc1=models.TextField(max_length=1000, blank=True, null=True)
    PrivacyPolicy_subtitle2=models.CharField(max_length=100, blank=True, null=True)
    PrivacyPolicy_desc2=models.TextField(max_length=1000, blank=True, null=True)
    PrivacyPolicy_subtitle3=models.CharField(max_length=100, blank=True, null=True)
    PrivacyPolicy_desc3=models.TextField(max_length=1000, blank=True, null=True)
    PrivacyPolicy_subtitle4=models.CharField(max_length=100, blank=True, null=True)
    PrivacyPolicy_desc4=models.TextField(max_length=1000, blank=True, null=True)
    PrivacyPolicy_subtitle5=models.CharField(max_length=100, blank=True, null=True)
    PrivacyPolicy_desc5=models.TextField(max_length=1000, blank=True, null=True)
    PrivacyPolicy_image=models.ImageField(upload_to='core_app/privacy_policy/img', blank=True, null=True,
                                            validators=[validate_image, FileExtensionValidator(
                                                allowed_extensions=["jpg", "png", "JPEG", 'svg'])],
                                            help_text='Maximum file size allowed is 5Mb')
    PrivacyPolicy_url=models.CharField(max_length=500, blank=True, null=True)
    PrivacyPolicy_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    PrivacyPolicy_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)
    PrivacyPolicy_PublishStatus=models.CharField(
        max_length=30, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default='Unpublished')
    PrivacyPolicy_CreationDate=models.DateField(auto_now_add=True)
    PrivacyPolicy_LastUpdateDate=models.DateField(auto_now=True)
    

    class Meta:
        db_table = 'PRIVACY_POLICY'
        verbose_name_plural = "Privacy Policies"

    def __str__(self):
        return self.PrivacyPolicy_title or ''

# ------------------------------------------------------------------------------------------------

class Subscriber(models.Model):
    
    Subscriber_Email=models.CharField(max_length=200)
    Subscriber_Subscription_Status=models.CharField(max_length=20, choices=[("Subscribed", "Subscribed"),
                                                                            ("Unsubscribed", "Unsubscribed")],
                                                    default="Subscribed")
    Subscriber_Subscription_Date=models.DateField(auto_now_add=True)
    

    class Meta:
        db_table = 'SUBSCRIBER'
        verbose_name_plural = "List of Subscribers"

    def __str__(self):
        return self.Subscriber_Email or ''

# ------------------------------------------------------------------------------------------------

class UAIndiaProgramme(models.Model):
    
    UAIndiaProgramme_Title=models.TextField(blank=True, null=True)
    UAIndiaProgramme_Title_Description=models.TextField(blank=True, null=True)
    UAIndiaProgramme_Title_Image=models.ImageField(upload_to='core_app/UAIndiaProgramme/image/', blank=True, null=True,
                                                    validators=[validate_image,
                                                                FileExtensionValidator(
                                                                    allowed_extensions=["jpg", "png",
                                                                                        "JPEG"])],
                                                    help_text='Maximum file size allowed is 5Mb')
    UAIndiaProgramme_Subtitle1=models.TextField(blank=True, null=True)
    UAIndiaProgramme_Description1=models.TextField(blank=True, null=True)
    UAIndiaProgramme_Image1=models.ImageField(upload_to='core_app/UAIndiaProgramme/image/', blank=True, null=True,
                                                validators=[validate_image,
                                                            FileExtensionValidator(
                                                                allowed_extensions=["jpg", "png",
                                                                                    "JPEG"])],
                                                help_text='Maximum file size allowed is 5Mb')
    UAIndiaProgramme_Subtitle2=models.TextField(blank=True, null=True)
    UAIndiaProgramme_Description2=models.TextField(blank=True, null=True)
    UAIndiaProgramme_Image2=models.ImageField(upload_to='core_app/UAIndiaProgramme/image/', blank=True, null=True,
                                                validators=[validate_image,
                                                            FileExtensionValidator(
                                                                allowed_extensions=["jpg", "png",
                                                                                    "JPEG"])],
                                                help_text='Maximum file size allowed is 5Mb')
    UAIndiaProgramme_Subtitle3=models.TextField(blank=True, null=True)
    UAIndiaProgramme_Description3=models.TextField(blank=True, null=True)
    UAIndiaProgramme_Image3=models.ImageField(upload_to='core_app/UAIndiaProgramme/image/', blank=True, null=True,
                                                validators=[validate_image,
                                                            FileExtensionValidator(
                                                                allowed_extensions=["jpg", "png",
                                                                                    "JPEG"])],
                                                help_text='Maximum file size allowed is 5Mb')
    UAIndiaProgramme_Subtitle4=models.TextField(blank=True, null=True)
    UAIndiaProgramme_Description4=models.TextField(blank=True, null=True)
    UAIndiaProgramme_Image4=models.ImageField(upload_to='core_app/UAIndiaProgramme/image/', blank=True, null=True,
                                                validators=[validate_image,
                                                            FileExtensionValidator(
                                                                allowed_extensions=["jpg", "png",
                                                                                    "JPEG"])],
                                                help_text='Maximum file size allowed is 5Mb')
    UAIndiaProgramme_Subtitle5=models.TextField(blank=True, null=True)
    UAIndiaProgramme_Description5=models.TextField(blank=True, null=True)
    UAIndiaProgramme_Image5=models.ImageField(upload_to='core_app/UAIndiaProgramme/image/', blank=True, null=True,
                                                validators=[validate_image,
                                                            FileExtensionValidator(
                                                                allowed_extensions=["jpg", "png",
                                                                                    "JPEG"])],
                                                help_text='Maximum file size allowed is 5Mb')

    UAIndiaProgramme_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    UAIndiaProgramme_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)
    UAIndiaProgramme_CreatedDate=models.DateField(auto_now_add=True)
    UAIndiaProgramme_UpdatedDate=models.DateField(auto_now=True, )
    UAIndiaProgramme_PublishStatus=models.CharField(
        max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default="Unpublished")
    

    class Meta:
        db_table = 'UA_INDIA_PROGRAMME'
        verbose_name_plural = "UA India Programme"

    def __str__(self):
        return self.UAIndiaProgramme_Title or ''

# ------------------------------------------------------------------------------------------------

class IDNLanguages(models.Model):
    
    IDNLanguages_IDN_Domain=models.CharField(max_length=100, blank=True, null=True)
    IDNLanguages_Script=models.CharField(max_length=100, blank=True, null=True)
    IDNLanguages_Policies_Document=models.FileField(upload_to="core_app/Document/IDNLanguages_Policies_Document",
                                                    validators=[
                                                        FileExtensionValidator(
                                                            ['pdf', 'zip', 'csv', 'xls', 'ppt', 'html'])],
                                                    null=True, blank=True)
    Language_Supported=models.CharField(max_length=300, blank=True, null=True)
    IDNLanguages_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    IDNLanguages_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)
    IDNLanguages_CreatedDate=models.DateField(auto_now_add=True)
    IDNLanguages_UpdatedDate=models.DateField(auto_now=True, )
    IDNLanguages_PublishStatus=models.CharField(
        max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default="Unpublished")

    class Meta:
        db_table = 'IDN_LANGUAGES'
        verbose_name_plural = "List of IDN Languages"

    def __str__(self):
        return self.IDNLanguages_IDN_Domain or ''

# ------------------------------------------------------------------------------------------------

class IDNccTLDs(models.Model):
    
    IDNccTLDs_Title=models.CharField(max_length=500, blank=True, null=True)
    IDNccTLDs_Description=models.TextField(blank=True, null=True)
    IDNccTLDs_Image1=models.ImageField(upload_to='core_app/IDNccTLDs/image/', blank=True, null=True,
                                        validators=[validate_image,
                                                    FileExtensionValidator(
                                                        allowed_extensions=["jpg", "png",
                                                                            "JPEG"])],
                                        help_text='Maximum file size allowed is 5Mb')
    IDNccTLDs_Image2=models.ImageField(upload_to='core_app/IDNccTLDs/image/', blank=True, null=True,
                                        validators=[validate_image,
                                                    FileExtensionValidator(
                                                        allowed_extensions=["jpg", "png",
                                                                            "JPEG"])],
                                        help_text='Maximum file size allowed is 5Mb')
    IDNccTLDs_Image3=models.ImageField(upload_to='core_app/IDNccTLDs/image/', blank=True, null=True,
                                        validators=[validate_image,
                                                    FileExtensionValidator(
                                                        allowed_extensions=["jpg", "png",
                                                                            "JPEG"])],
                                        help_text='Maximum file size allowed is 5Mb')
    IDNccTLDs_Image4=models.ImageField(upload_to='core_app/IDNccTLDs/image/', blank=True, null=True,
                                        validators=[validate_image,
                                                    FileExtensionValidator(
                                                        allowed_extensions=["jpg", "png",
                                                                            "JPEG"])],
                                        help_text='Maximum file size allowed is 5Mb')
    IDNLanguages_Subtitle1=models.TextField(blank=True, null=True)
    IDNLanguages_Description1=models.TextField(blank=True, null=True)
    IDNLanguages_Subtitle2=models.TextField(blank=True, null=True)
    IDNLanguages_Description2=models.TextField(blank=True, null=True)
    IDNLanguages_Subtitle3=models.TextField(blank=True, null=True)
    IDNLanguages_Description3=models.TextField(blank=True, null=True)
    IDNLanguages_Subtitle4=models.TextField(blank=True, null=True)
    IDNLanguages_Description4=models.TextField(blank=True, null=True)
    IDNLanguages_link1=models.CharField(max_length=500, blank=True, null=True)
    IDNLanguages_link2=models.CharField(max_length=500, blank=True, null=True)
    IDNLanguages_link3=models.CharField(max_length=500, blank=True, null=True)
    IDNLanguages_link4=models.CharField(max_length=500, blank=True, null=True)

    IDNccTLDs_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    IDNccTLDs_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)
    IDNccTLDs_CreatedDate=models.DateField(auto_now_add=True)
    IDNccTLDs_UpdatedDate=models.DateField(auto_now=True)
    IDNccTLDs_PublishStatus=models.CharField(
        max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default="Unpublished")
    

    class Meta:
        db_table = 'IDNccTLDs'
        verbose_name_plural = "IDN Country Code TLD Page "

    def __str__(self):
        return self.IDNccTLDs_Title or ''

# ------------------------------------------------------------------------------------------------

class Tools(models.Model):
    
    Tools_Name=models.CharField(max_length=100)
    Tools_Description=models.TextField(
        max_length=1000, blank=True, null=True)
    Tools_InternalURL=models.CharField(max_length=500, blank=True, null=True)
    Tools_ExternalURL=models.CharField(max_length=500, blank=True, null=True)
    Tools_ThumbnailImage=models.FileField(
        upload_to='core_app/tools/thunbnail_img/', blank=True, null=True)
    Tools_Image=models.ImageField(upload_to='core_app/tools/img', blank=True, null=True,
                                    validators=[validate_image, FileExtensionValidator(
                                        allowed_extensions=["jpg", "png", "JPEG", 'svg'])],
                                    help_text='Maximum file size allowed is 5Mb')
    Tools_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    Tools_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)
    Tools_PublishStatus=models.CharField(
        max_length=30, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default='Unpublished')
    Tools_CreationDate=models.DateField(auto_now_add=True)
    Tools_LastUpdateDate=models.DateField(auto_now=True)
    

    class Meta:
        db_table = 'TOOLS'
        verbose_name_plural = "List of All Tools"
        ordering = ['-id']

    def __str__(self):
        return self.Tools_Name or ''

# ------------------------------------------------------------------------------------------------

class EmailAddressInternationalization(models.Model):
    
    EmailAddressInternationalization_title=models.CharField(max_length=100, blank=True, null=True)
    EmailAddressInternationalization_title_desc=models.TextField(max_length=1000, blank=True, null=True)
    EmailAddressInternationalization_title_image=models.ImageField(
        upload_to='core_app/EmailAddressInternationalization/img', blank=True,
        null=True, validators=[validate_image,
                                FileExtensionValidator(
                                    allowed_extensions=[
                                        "jpg", "png",
                                        "JPEG", 'svg'])],
        help_text='Maximum file size allowed is 5Mb')
    EmailAddressInternationalization_subtitle1=models.CharField(max_length=100, blank=True, null=True)
    EmailAddressInternationalization_desc1=models.TextField(max_length=1000, blank=True, null=True)
    EmailAddressInternationalization_image1=models.ImageField(upload_to='core_app/EmailAddressInternationalization/img',
                                                                blank=True,
                                                                null=True,
                                                                validators=[validate_image, FileExtensionValidator(
                                                                    allowed_extensions=["jpg", "png", "JPEG",
                                                                                        'svg'])],
                                                                help_text='Maximum file size allowed is 5Mb')
    EmailAddressInternationalization_internalURL1=models.CharField(max_length=500, blank=True, null=True)
    EmailAddressInternationalization_externalURL1=models.CharField(max_length=500, blank=True, null=True)
    EmailAddressInternationalization_subtitle2=models.CharField(max_length=100, blank=True, null=True)
    EmailAddressInternationalization_desc2=models.TextField(max_length=1000, blank=True, null=True)
    EmailAddressInternationalization_image2=models.ImageField(upload_to='core_app/EmailAddressInternationalization/img',
                                                                blank=True,
                                                                null=True,
                                                                validators=[validate_image, FileExtensionValidator(
                                                                    allowed_extensions=["jpg", "png", "JPEG",
                                                                                        'svg'])],
                                                                help_text='Maximum file size allowed is 5Mb')
    EmailAddressInternationalization_internalURL2=models.CharField(max_length=500, blank=True, null=True)
    EmailAddressInternationalization_externalURL2=models.CharField(max_length=500, blank=True, null=True)
    EmailAddressInternationalization_subtitle3=models.CharField(max_length=100, blank=True, null=True)
    EmailAddressInternationalization_desc3=models.TextField(max_length=1000, blank=True, null=True)
    EmailAddressInternationalization_image3=models.ImageField(upload_to='core_app/EmailAddressInternationalization/img',
                                                                blank=True,
                                                                null=True,
                                                                validators=[validate_image, FileExtensionValidator(
                                                                    allowed_extensions=["jpg", "png", "JPEG",
                                                                                        'svg'])],
                                                                help_text='Maximum file size allowed is 5Mb')
    EmailAddressInternationalization_internalURL3=models.CharField(max_length=500, blank=True, null=True)
    EmailAddressInternationalization_externalURL3=models.CharField(max_length=500, blank=True, null=True)
    EmailAddressInternationalization_subtitle4=models.CharField(max_length=100, blank=True, null=True)
    EmailAddressInternationalization_desc4=models.TextField(max_length=1000, blank=True, null=True)
    EmailAddressInternationalization_image4=models.ImageField(upload_to='core_app/EmailAddressInternationalization/img',
                                                                blank=True,
                                                                null=True,
                                                                validators=[validate_image, FileExtensionValidator(
                                                                    allowed_extensions=["jpg", "png", "JPEG",
                                                                                        'svg'])],
                                                                help_text='Maximum file size allowed is 5Mb')
    EmailAddressInternationalization_internalURL4=models.CharField(max_length=500, blank=True, null=True)
    EmailAddressInternationalization_externalURL4=models.CharField(max_length=500, blank=True, null=True)
    EmailAddressInternationalization_subtitle5=models.CharField(max_length=100, blank=True, null=True)
    EmailAddressInternationalization_desc5=models.TextField(max_length=1000, blank=True, null=True)
    EmailAddressInternationalization_image5=models.ImageField(upload_to='core_app/EmailAddressInternationalization/img',
                                                                blank=True,
                                                                null=True,
                                                                validators=[validate_image, FileExtensionValidator(
                                                                    allowed_extensions=["jpg", "png", "JPEG",
                                                                                        'svg'])],
                                                                help_text='Maximum file size allowed is 5Mb')
    EmailAddressInternationalization_internalURL5=models.CharField(max_length=500, blank=True, null=True)
    EmailAddressInternationalization_externalURL5=models.CharField(max_length=500, blank=True, null=True)
    EmailAddressInternationalization_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    EmailAddressInternationalization_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)
    EmailAddressInternationalization_PublishStatus=models.CharField(
        max_length=30, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default='Unpublished')
    EmailAddressInternationalization_CreationDate=models.DateField(auto_now_add=True)
    EmailAddressInternationalization_LastUpdateDate=models.DateField(auto_now=True)


    class Meta:
        db_table = 'EMAIL_ADDRESS_INTERNATIONALIZATION'
        verbose_name_plural = "Email Address Internationalization"

    def __str__(self):
        return self.EmailAddressInternationalization_title or ''

# ------------------------------------------------------------------------------------------------

class UniversalAcceptance(models.Model):
    
    UniversalAcceptance_title=models.CharField(max_length=100)
    UniversalAcceptance_title_desc=models.TextField(max_length=1000, blank=True, null=True)
    UniversalAcceptance_subtitle1=models.CharField(max_length=100, blank=True, null=True)
    UniversalAcceptance_desc1=models.TextField(max_length=1000, blank=True, null=True)
    UniversalAcceptance_subtitle2=models.CharField(max_length=100, blank=True, null=True)
    UniversalAcceptance_desc2=models.TextField(max_length=1000, blank=True, null=True)
    UniversalAcceptance_subtitle3=models.CharField(max_length=100, blank=True, null=True)
    UniversalAcceptance_desc3=models.TextField(max_length=1000, blank=True, null=True)
    UniversalAcceptance_subtitle4=models.CharField(max_length=100, blank=True, null=True)
    UniversalAcceptance_desc4=models.TextField(max_length=1000, blank=True, null=True)
    UniversalAcceptance_subtitle5=models.CharField(max_length=100, blank=True, null=True)
    UniversalAcceptance_desc5=models.TextField(max_length=1000, blank=True, null=True)
    UniversalAcceptance_image1=models.FileField(upload_to='core_app/privacy_policy/img', blank=True, null=True,
                                                validators=[validate_image, FileExtensionValidator(
                                                    allowed_extensions=["jpg", "png", "JPEG", 'svg', 'webp'])],
                                                help_text='Maximum file size allowed is 5Mb')
    UniversalAcceptance_image2=models.FileField(upload_to='core_app/privacy_policy/img', blank=True, null=True,
                                                validators=[validate_image, FileExtensionValidator(
                                                    allowed_extensions=["jpg", "png", "JPEG", 'svg', 'webp'])],
                                                help_text='Maximum file size allowed is 5Mb')
    UniversalAcceptance_image3=models.FileField(upload_to='core_app/privacy_policy/img', blank=True, null=True,
                                                validators=[validate_image, FileExtensionValidator(
                                                    allowed_extensions=["jpg", "png", "JPEG", 'svg', 'webp'])],
                                                help_text='Maximum file size allowed is 5Mb')
    UniversalAcceptance_url=models.CharField(max_length=500, blank=True, null=True)
    UniversalAcceptance_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    UniversalAcceptance_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)
    UniversalAcceptance_PublishStatus=models.CharField(
        max_length=30, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default='Unpublished')
    UniversalAcceptance_CreationDate=models.DateField(auto_now_add=True)
    UniversalAcceptance_LastUpdateDate=models.DateField(auto_now=True)


    class Meta:
        db_table = 'UNIVERSAL_ACCEPTANCE'
        verbose_name_plural = "Universal Acceptance"

    def __str__(self):
        return self.UniversalAcceptance_title or ''

# ------------------------------------------------------------------------------------------------

class GenericList(models.Model):
    
    GenericList_Category_Name=models.CharField(max_length=500, blank=True, null=True)
    GenericList_Title_Name=models.TextField(blank=True, null=True)
    GenericList_Title_Description=models.TextField(blank=True, null=True)
    GenericList_Value1=models.TextField(blank=True, null=True)
    GenericList_Value2=models.TextField(blank=True, null=True)
    GenericList_Value3=models.TextField(blank=True, null=True)
    GenericList_Value4=models.TextField(blank=True, null=True)
    GenericList_Value5=models.TextField(blank=True, null=True)
    GenericList_Value6=models.TextField(blank=True, null=True)
    GenericList_Value7=models.TextField(blank=True, null=True)
    GenericList_Value8=models.TextField(blank=True, null=True)
    GenericList_Value9=models.TextField(blank=True, null=True)
    GenericList_Value10=models.TextField(blank=True, null=True)
    GenericList_CreationDate=models.DateField(auto_now_add=True)
    GenericList_LastUpdatedDate=models.DateField(auto_now=True)
    GenericList_PublishedStatus=models.CharField(
        max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")], default="Unpublished")
    GenericList_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    GenericList_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        db_table = 'GENERIC_LIST'
        verbose_name_plural = "Generic List"

    def __str__(self):
        return "{} - ID : {}".format(self.GenericList_Title_Name, self.id) or ''

    # ------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------

class Stackholder(models.Model):
    
    Stackholder_image=models.FileField(upload_to='core_app/Stackholder/img', blank=True, null=True,
                                        validators=[validate_image, FileExtensionValidator(
                                            allowed_extensions=["jpg", "png", "JPEG", 'svg', 'webp'])],
                                        help_text='Maximum file size allowed is 5Mb')
    Stackholder_image_title=models.CharField(max_length=500, blank=True, null=True)
    Stackholder_url=models.CharField(max_length=500, blank=True, null=True)

    Stackholder_CreationDate=models.DateField(auto_now_add=True)
    Stackholder_LastUpdatedDate=models.DateField(auto_now=True)
    Stackholder_PublishedStatus=models.CharField(
        max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")],
        default="Unpublished")
    Stackholder_Content_Author=models.CharField(max_length=100, blank=True, null=True)
    Stackholder_Content_Modifier=models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        db_table = 'STACKHOLDER'
        verbose_name_plural = "Stackholders"

    def __str__(self):
        return self.Stackholder_url or ''

# ---------------------------------------------------------------------------------------------------

class DocumentCategoryWithoutTrans(models.Model):
    DocumentCategory_Name = models.CharField(max_length=500)
    DocumentCategory_Status = models.BooleanField(default=False)
    DocumentCategory_CreationDate = models.DateField(auto_now_add=True)
    DocumentCategory_LastUpdatedDate = models.DateField(auto_now=True)
    DocumentCategory_PublishStatus = (
        ('Published', 'PUBLISHED'), ('Unpublished', 'UNPUBLISHED'))
    DocumentCategory_PublishedStatus = models.CharField(
        max_length=20, choices=DocumentCategory_PublishStatus, default="Unpublished")
    DocumentCategory_Author = models.CharField(
        max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Document Category Without Translation"
        ordering = ['DocumentCategory_Name']

    def __str__(self):
        return self.DocumentCategory_Name or ''

# ---------------------------------------------------------------------------------------------------

class DocumentWithoutTrans(models.Model):
    Document_Name = models.CharField(max_length=800)
    Document_Description = models.TextField()
    Document_CreationDate = models.DateField(auto_now_add=True)
    Document_LastUpdatedDate = models.DateField(auto_now=True)
    Document_Author = models.CharField(max_length=200, null=True, blank=True)
    Document_CategoryType = models.ForeignKey(
        DocumentCategoryWithoutTrans, on_delete=models.CASCADE)
    Document_LanguageType = models.CharField(max_length=500)
    Document_Status = (('Published', 'PUBLISHED'),
                       ('Unpublished', 'UNPUBLISHED'))
    Document_PublishedStatus = models.CharField(
        max_length=20, choices=Document_Status, default="Unpublished")
    Document_Slug = models.SlugField(max_length=255, blank=True, null=True)
    Document_Thumbnail = models.ImageField(
        upload_to="core_app/Document/Thumbnail", validators=[validate_image,
                                                         FileExtensionValidator(
                                                             allowed_extensions=["jpg", "png", "JPEG", "svg"])],
        help_text='Maximum file size allowed is 5Mb',
        height_field=None, width_field=None, max_length=None, null=True, blank=True)
    Document_DocumentFile = models.FileField(upload_to="core_app/Document/DocumentFile",
                                             validators=[
                                                 FileExtensionValidator(['pdf', 'zip', 'csv', 'xls', 'ppt', 'html'])],
                                             null=True, blank=True)
    Document_FileSize = models.CharField(max_length=30)
    Document_Count = models.IntegerField()
    Document_Type = models.CharField(max_length=30)
    DocumentUASGTrans_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Document Without Translation"
        ordering = ['Document_Name']

    def __str__(self):
        return self.Document_Name or ''

    def get_slug_splited(self):
        return self.Document_Slug.split('-')

    # ---------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------

class TestimonialsMessages(models.Model):

    TestimonialsMessages_PersonName=models.TextField(blank=True, null=True)
    TestimonialsMessages_PersonDesignation=models.TextField(blank=True, null=True)
    TestimonialsMessages_Title=models.TextField(blank=True, null=True)
    TestimonialsMessages_Description=models.TextField(blank=True, null=True)
    TestimonialsMessages_Description1=models.TextField(blank=True, null=True)
    TestimonialsMessages_PublishStatus=models.CharField(
        max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")],
        default="Unpublished")
    TestimonialsMessages_Image=models.ImageField(upload_to='core_app/TestimonialsMessages/', blank=True,
                                                    validators=[validate_image,
                                                                FileExtensionValidator(
                                                                    allowed_extensions=[
                                                                        "jpg",
                                                                        "png",
                                                                        "JPEG",
                                                                        "svg"])],
                                                    help_text='Maximum file size allowed is 5Mb')
    TestimonialsMessages_InternalURL=models.CharField(max_length=500, blank=True, null=True)
    TestimonialsMessages_ExternalURL=models.CharField(max_length=500, blank=True, null=True)
    TestimonialsMessages_CreatedDate=models.DateField(auto_now_add=True)
    TestimonialsMessages_UpdatedDate=models.DateField(auto_now=True, blank=True, null=True)
    TestimonialsMessages_Author=models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.TestimonialsMessages_PersonName or ''

    class Meta:
        db_table = 'TESTIMONIALS_MESSAGES'
        verbose_name_plural = "Testimonials Messages "

# ------------------------------------------------------------------------------------------------

class IDNReadyWebsitesCategory(models.Model):
    IDNReadyWebsites_Category_Name = models.CharField(max_length=100)
    IDNReadyWebsites_Category_Creation_Date = models.DateField(auto_now_add=True)
    IDNReadyWebsites_Category_Last_Updated_Date = models.DateField(auto_now=True)
    IDNReadyWebsites_Category_Publish_Status = models.CharField(max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")],
            default="Unpublished")
    
    class Meta:
        db_table = 'IDN_WEBSITES_CATEGORY'
        verbose_name_plural = "List of IDN Ready Websites Category"

    def __str__(self):
        return self.IDNReadyWebsites_Category_Name or ''

# ---------------------------------------------------------------------------------------------------

class IDNReadyWebsitesLanguages(models.Model):
    IDNReadyWebsites_Language_Name = models.CharField(max_length=100)
    IDNReadyWebsites_Language_Creation_Date = models.DateField(auto_now_add=True)
    IDNReadyWebsites_Language_Last_Updated_Date = models.DateField(auto_now=True)
    IDNReadyWebsites_Language_Publish_Status = models.CharField(max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")],
            default="Unpublished")
    
    class Meta:
        db_table = 'IDN_WEBSITES_LANGUAGES'
        verbose_name_plural = "List of IDN Ready Websites Languages"

    def __str__(self):
        return self.IDNReadyWebsites_Language_Name or ''
    
# ---------------------------------------------------------------------------------------------------

class IDNReadyWebsites(models.Model):
    IDNReadyWebsites_Title = models.CharField(max_length=100)
    IDNReadyWebsites_Category = models.ManyToManyField(IDNReadyWebsitesCategory)
    IDNReadyWebsites_Logo = models.ImageField(upload_to='core_app/Idn_websites/', blank=True,
                                                     validators=[validate_image,
                                                                 FileExtensionValidator(
                                                                     allowed_extensions=[
                                                                         "jpg",
                                                                         "png",
                                                                         "JPEG",
                                                                         "svg"])],
                                                     help_text='Maximum file size allowed is 5Mb')
    IDNReadyWebsites_Creation_Date = models.DateField(auto_now_add=True)
    IDNReadyWebsites_Last_Updated_Date = models.DateField(auto_now=True)
    IDNReadyWebsites_Publish_Status = models.CharField(max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")],
            default="Unpublished")
    
    class Meta:
        db_table = 'IDN_WEBSITES'
        verbose_name_plural = "List of IDN Ready Websites"

    def __str__(self):
        return self.IDNReadyWebsites_Title or ''
    
# ---------------------------------------------------------------------------------------------------

class IDNReadyWebsitesLangugeURLMapping(models.Model):
    IDNReadyWebsites = models.ForeignKey(IDNReadyWebsites, on_delete=models.CASCADE)
    IDNReadyWebsites_lang = models.ForeignKey(IDNReadyWebsitesLanguages, on_delete=models.CASCADE)
    IDNReadyWebsites_url = models.CharField(max_length=500)
    IDNReadyWebsites_LangURLMapping_Creation_Date = models.DateField(auto_now_add=True)
    IDNReadyWebsites_LangURLMapping_Last_Updated_Date = models.DateField(auto_now=True)
    IDNReadyWebsites_LangURLMapping_Publish_Status = models.CharField(max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")],
            default="Unpublished")
    
    class Meta:
        db_table = 'IDN_WEBSITES_LANGUAGE_URL_MAPPING'
        verbose_name_plural = "List of IDN Ready Websites Language Url Mapping"

    def __str__(self):
        return self.IDNReadyWebsites_url or ''

# ---------------------------------------------------------------------------------------------------

class GalleryHeadings(models.Model):
    Gallery_heading = models.CharField(max_length=500)
    Gallery_heading_Creation_Date = models.DateField(auto_now_add=True)
    Gallery_heading_Last_Updated_Date = models.DateField(auto_now=True)
    Gallery_heading_Publish_Status = models.CharField(max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")],
            default="Unpublished")
    
    class Meta:
        db_table = 'Gallery_Headings'
        verbose_name_plural = "Gallery Video Headings"

    def __str__(self):
        return self.Gallery_heading or ''
    
# ---------------------------------------------------------------------------------------------------

class GalleryVideos(models.Model):
    Gallery_Heading = models.ForeignKey(GalleryHeadings, on_delete=models.CASCADE)
    Gallery_Video_Label = models.CharField(max_length=500)
    Gallery_Video_Link = models.CharField(max_length=500)
    Gallery_Video_Creation_Date = models.DateField(auto_now_add=True)
    Gallery_Video_Last_Updated_Date = models.DateField(auto_now=True)
    Gallery_Video_Publish_Status = models.CharField(max_length=20, choices=[("Published", "Published"), ("Unpublished", "Unpublished")],
            default="Unpublished")
    
    class Meta:
        db_table = 'Gallery_Videos'
        verbose_name_plural = "Gallery Videos"

    def __str__(self):
        return self.Gallery_Video_Label or ''

# ---------------------------------------------------------------------------------------------------

class SOPTechnologyCategory(models.Model):
    SOPTechnologyCategory_Name = models.CharField(max_length=500)
    SOPTechnologyCategory_Status = models.BooleanField(default=False)
    SOPTechnologyCategory_CreationDate = models.DateField(auto_now_add=True)
    SOPTechnologyCategory_LastUpdatedDate = models.DateField(auto_now=True)
    SOPTechnologyCategory_PublishStatus = (
        ('Published', 'PUBLISHED'), ('Unpublished', 'UNPUBLISHED'))
    SOPTechnologyCategory_PublishedStatus = models.CharField(
        max_length=20, choices=SOPTechnologyCategory_PublishStatus, default="Unpublished")
    SOPTechnologyCategory_Author = models.CharField(
        max_length=500, blank=True, null=True)
    SOPTechnologyCategory_Thumbnail = models.ImageField(
        upload_to="core_app/SOPTechnologyCategory/Thumbnail", validators=[validate_image,
                                                         FileExtensionValidator(
                                                             allowed_extensions=["jpg", "png", "JPEG", "svg"])],
        help_text='Maximum file size allowed is 5Mb',
        height_field=None, width_field=None, max_length=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = "SOP Technology Category"
        ordering = ['SOPTechnologyCategory_Name']

    def __str__(self):
        return self.SOPTechnologyCategory_Name

# ---------------------------------------------------------------------------------------------------

class SOPTechnologyDocument(models.Model):
    SOPTechnologyDocument_Name = models.CharField(max_length=800)
    SOPTechnologyDocument_Description = models.TextField()
    SOPTechnologyDocument_CreationDate = models.DateField(auto_now_add=True)
    SOPTechnologyDocument_LastUpdatedDate = models.DateField(auto_now=True)
    SOPTechnologyDocument_LastUpdatedSOPDate = models.DateField()
    SOPTechnologyDocument_Author = models.CharField(max_length=200, null=True, blank=True)
    SOPTechnologyDocument_CategoryType = models.ForeignKey(
        SOPTechnologyCategory, on_delete=models.CASCADE)
    SOPTechnologyDocument_LanguageType = models.CharField(max_length=500,null=True, blank=True)
    SOPTechnologyDocument_Status = (('Published', 'PUBLISHED'),
                       ('Unpublished', 'UNPUBLISHED'))
    SOPTechnologyDocument_PublishedStatus = models.CharField(
        max_length=20, choices=SOPTechnologyDocument_Status, default="Unpublished")
    SOPTechnologyDocument_Slug = models.SlugField(max_length=255, blank=True, null=True)
    SOPTechnologyDocument_Thumbnail = models.ImageField(
        upload_to="core_app/SOPTechnologyDocument/Thumbnail", validators=[validate_image,
                                                         FileExtensionValidator(
                                                             allowed_extensions=["jpg", "png", "JPEG", "svg"])],
        help_text='Maximum file size allowed is 5Mb',
        height_field=None, width_field=None, max_length=None, null=True, blank=True)
    SOPTechnologyDocument_DocumentFile = models.FileField(upload_to="core_app/SOPTechnologyDocument/DocumentFile",
                                             validators=[FileExtensionValidator(['pdf', 'zip', 'csv', 'xls', 'ppt', 'html'])], null=True, blank=True)
    SOPTechnologyDocument_FileSize = models.CharField(max_length=30,null=True, blank=True)
    SOPTechnologyDocument_Count = models.IntegerField(null=True, blank=True)
    SOPTechnologyDocument_Type = models.CharField(max_length=30,null=True, blank=True)
    SOPTechnologyDocument_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = "SOP Technology Document"
        ordering = ['SOPTechnologyDocument_Name']

    def __str__(self):
        return self.SOPTechnologyDocument_Name

    def get_slug_splited(self):
        return self.SOPTechnologyDocument_Slug.split('-')    

# ---------------------------------------------------------------------------------------------------

class SOPDownloadCounter(models.Model):
    SOPTechnologyDocument_Obj = models.ForeignKey(SOPTechnologyDocument, on_delete=models.CASCADE)
    DownloadCounter = models.IntegerField()

    class Meta:
        verbose_name_plural = "SOP Download Counter"
        # ordering = ['SOPTechnologyDocument_Name']

    def __str__(self):
        return self.SOPTechnologyDocument_Obj.SOPTechnologyDocument_Name


# ---------------------------------------------------------------------------------------------------

class IDNRequestForUserWebsitesCategories(models.Model):
    IDN_category_name =models.CharField(max_length=255, blank=True, null=True,unique=True)
    website_Status = (('Active', 'Active'), ('Inactive', 'Inactive'))
    website_status = models.CharField(max_length=20, choices=website_Status, default="Active")
    
    
    IDN_category_creation_date = models.DateField(auto_now_add=True)
    IDN_category_last_updated_date = models.DateField(auto_now=True)
    

    class Meta:
        verbose_name = "IDN Request For User Websites Categories"
        verbose_name_plural = "IDN Request For User Websites Categories"

    def __str__(self):
        return self.IDN_category_name

# ---------------------------------------------------------------------------------------------------

class IDNRequestForUserWebsites(models.Model):
    submitter_name = models.CharField(max_length=100)
    IDN_Email = models.CharField(max_length=500)
    IDN_Category = models.ForeignKey(IDNRequestForUserWebsitesCategories, verbose_name="Category", on_delete=models.DO_NOTHING)
    IDN_English_Domain=models.CharField(max_length=255,unique=True)
    IDN_URLS = models.JSONField()
    need_assistance = models.BooleanField(blank=True, null=True, default=False)
    assist_langs = models.CharField(max_length=500, blank=True, null=True)
    assist_remark = models.CharField(max_length=500, blank=True, null=True)
    
    IDN_Created_Date = models.DateField(auto_now_add=True)
    IDN_Last_Updated_Date = models.DateField(auto_now=True)
    IDN_Approve_Choices = (('APPROVED', 'APPROVED'), ('NOT-APPROVED', 'NOT-APPROVED'))
    IDN_Approve_Category = models.CharField(max_length=20, choices=IDN_Approve_Choices, default="NOT-APPROVED", blank=True, null=True)
   
    class Meta:
        verbose_name = "IDN Request For User Websites"
        verbose_name_plural = "IDN Request For User Websites"

    def __str__(self):
        return self.IDN_Email
    
# ---------------------------------------------------------------------------------------------------

class OTP_For_IDNRequestForUserWebsites(models.Model):
    OTP_Email = models.CharField(max_length=500, blank=True, null=True)
    OTP_Value = models.IntegerField()
    OTP_Entered_Count = models.IntegerField()
    OTP_Status = models.BooleanField(default=False, blank=True, null=True)
    OTP_Created_Date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "OTP FOR IDN Request For User Websites"
        verbose_name_plural = "OTP FOR IDN Request For User Websites"

    def __str__(self):
        return self.OTP_Email
    
# ---------------------------------------------------------------------------------------------------
