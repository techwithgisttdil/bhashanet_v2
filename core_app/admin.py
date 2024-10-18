from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.

@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ('id', 'Article_Title', 'Article_Title_Description',
                    'Article_Subtitle1')
    list_display_links = ('id', 'Article_Title', 'Article_Title_Description',
                          'Article_Subtitle1')
    ordering = ('id',)
    list_per_page: int = 20
    save_on_top = True


############################################################################

@admin.register(TermsAndConditions)
class AdminTermsAndConditions(admin.ModelAdmin):
    list_display = ('id', 'TermsAndConditions_title', 'TermsAndConditions_title_desc',
                    'TermsAndConditions_subtitle1', 'TermsAndConditions_desc1')
    list_display_links = ('id', 'TermsAndConditions_title', 'TermsAndConditions_title_desc',
                          'TermsAndConditions_subtitle1', 'TermsAndConditions_desc1')
    ordering = ('id',)
    list_per_page: int = 20
    save_on_top = True


############################################################################

@admin.register(BestPractices)
class AdminBestPractices(admin.ModelAdmin):
    list_display = ('id', 'BestPractices_title', 'BestPractices_title_desc',
                    'BestPractices_subtitle1', 'BestPractices_desc1')
    list_display_links = ('id', 'BestPractices_title', 'BestPractices_title_desc',
                          'BestPractices_subtitle1', 'BestPractices_desc1')
    ordering = ('id',)
    list_per_page: int = 20
    save_on_top = True


############################################################################

@admin.register(Announcements)
class AdminAnnouncements(admin.ModelAdmin):
    list_display = ('id', 'Announcement_Title', 'Announcement_Description',
                    'Announcement_Description1', 'Announcement_PublishStatus')
    list_display_links = ('id', 'Announcement_Title', 'Announcement_Description',
                          'Announcement_Description1', 'Announcement_PublishStatus')
    ordering = ('id',)
    list_per_page: int = 20
    save_on_top = True


############################################################################

@admin.register(Objectives)
class AdminObjectives(admin.ModelAdmin):
    list_display = ('id', 'Objectives_Name', 'Objectives_Description',)
    list_display_links = ('id', 'Objectives_Name', 'Objectives_Description',)
    ordering = ('id',)
    list_per_page: int = 20
    save_on_top = True


############################################################################

@admin.register(DocumentCategory)
class AdminDocumentCategory(admin.ModelAdmin):
    list_display = ('id', 'DocumentCategory_Name', 'DocumentCategory_Status', 'DocumentCategory_PublishedStatus')
    list_display_links = ('id', 'DocumentCategory_Name', 'DocumentCategory_Status', 'DocumentCategory_PublishedStatus')
    ordering = ('id',)
    list_per_page: int = 20
    save_on_top = True


############################################################################

@admin.register(FaqCategory)
class AdminFaqCategory(admin.ModelAdmin):
    list_display = ('id', 'FaqCategory_Name', 'FaqCategory_PublishStatus', 'FaqCategory_LastUpdateDate')
    list_display_links = ('id', 'FaqCategory_Name', 'FaqCategory_PublishStatus', 'FaqCategory_LastUpdateDate')
    ordering = ('id',)
    list_per_page: int = 20
    save_on_top = True


############################################################################

@admin.register(Faqs)
class AdminFaqs(admin.ModelAdmin):
    list_display = ('id', 'Faqs_Ques', 'Faqs_Ans', 'Faqs_Category', 'Faqs_PublishStatus')
    list_display_links = ('id', 'Faqs_Ques', 'Faqs_Ans', 'Faqs_Category', 'Faqs_PublishStatus')
    ordering = ('id',)
    list_per_page: int = 20
    save_on_top = True


############################################################################

@admin.register(PrivacyPolicy)
class AdminPrivacyPolicy(admin.ModelAdmin):
    list_display = (
        'id', 'PrivacyPolicy_title', 'PrivacyPolicy_title_desc', 'PrivacyPolicy_subtitle1', 'PrivacyPolicy_desc1')
    list_display_links = (
        'id', 'PrivacyPolicy_title', 'PrivacyPolicy_title_desc', 'PrivacyPolicy_subtitle1', 'PrivacyPolicy_desc1')
    ordering = ('id',)
    list_per_page: int = 20
    save_on_top = True


############################################################################

@admin.register(Subscriber)
class AdminSubscriber(admin.ModelAdmin):
    list_display = ('id', 'Subscriber_Email', 'Subscriber_Subscription_Status', 'Subscriber_Subscription_Date',)
    list_display_links = ('id', 'Subscriber_Email', 'Subscriber_Subscription_Status', 'Subscriber_Subscription_Date',)
    ordering = ('id',)
    list_per_page: int = 20
    save_on_top = True


############################################################################

@admin.register(Tools)
class AdminTools(admin.ModelAdmin):
    list_display = ('id', 'Tools_Name', 'Tools_Description', 'Tools_PublishStatus',)
    list_display_links = ('id', 'Tools_Name', 'Tools_Description', 'Tools_PublishStatus',)
    ordering = ('id',)
    list_per_page: int = 20
    save_on_top = True


############################################################################

@admin.register(TestimonialsMessages)
class AdminTestimonialsMessages(admin.ModelAdmin):
    list_display = ('id', 'TestimonialsMessages_PersonName', 'TestimonialsMessages_PersonDesignation',
                    'TestimonialsMessages_Description')
    list_display_links = ('TestimonialsMessages_PersonName', 'TestimonialsMessages_PersonDesignation')
    ordering = ('id',)
    list_per_page: int = 20


############################################################################

@admin.register(UAIndiaProgramme)
class AdminUAIndiaProgramme(admin.ModelAdmin):
    list_display = ('id', 'UAIndiaProgramme_Title', 'UAIndiaProgramme_Title_Description',
                    'UAIndiaProgramme_Subtitle1', 'UAIndiaProgramme_Description1')
    list_display_links = ('id', 'UAIndiaProgramme_Title', 'UAIndiaProgramme_Title_Description',
                          'UAIndiaProgramme_Subtitle1', 'UAIndiaProgramme_Description1')
    ordering = ('id',)
    list_per_page: int = 20


############################################################################

@admin.register(IDNLanguages)
class AdminIDNLanguages(admin.ModelAdmin):
    list_display = ('id', 'IDNLanguages_IDN_Domain', 'IDNLanguages_Script',
                    'Language_Supported', 'IDNLanguages_PublishStatus')
    list_display_links = ('id', 'IDNLanguages_IDN_Domain', 'IDNLanguages_Script',
                          'Language_Supported', 'IDNLanguages_PublishStatus')
    ordering = ('id',)
    list_per_page: int = 20


############################################################################

@admin.register(IDNccTLDs)
class AdminIDNccTLDs(admin.ModelAdmin):
    list_display = ('id', 'IDNccTLDs_Title', 'IDNccTLDs_Description',
                    'IDNLanguages_Subtitle1', 'IDNLanguages_Description1', 'IDNccTLDs_PublishStatus')
    list_display_links = ('id', 'IDNccTLDs_Title', 'IDNccTLDs_Description',
                          'IDNLanguages_Subtitle1', 'IDNLanguages_Description1', 'IDNccTLDs_PublishStatus')
    ordering = ('id',)
    list_per_page: int = 20


############################################################################

@admin.register(EmailAddressInternationalization)
class AdminEmailAddressInternationalization(admin.ModelAdmin):
    list_display = ('id', 'EmailAddressInternationalization_title', 'EmailAddressInternationalization_title_desc',
                    'EmailAddressInternationalization_PublishStatus',)
    list_display_links = ('id', 'EmailAddressInternationalization_title', 'EmailAddressInternationalization_title_desc',
                          'EmailAddressInternationalization_PublishStatus',)
    ordering = ('id',)
    list_per_page: int = 20


############################################################################

@admin.register(UniversalAcceptance)
class AdminUniversalAcceptance(admin.ModelAdmin):
    list_display = ('id', 'UniversalAcceptance_title', 'UniversalAcceptance_title_desc',
                    'UniversalAcceptance_subtitle1', 'UniversalAcceptance_desc1', 'UniversalAcceptance_PublishStatus')
    list_display_links = ('id', 'UniversalAcceptance_title', 'UniversalAcceptance_title_desc',
                          'UniversalAcceptance_subtitle1', 'UniversalAcceptance_desc1',
                          'UniversalAcceptance_PublishStatus')
    ordering = ('id',)
    list_per_page: int = 20


############################################################################

@admin.register(GenericList)
class AdminGenericList(admin.ModelAdmin):
    list_display = ('id', 'GenericList_Category_Name', 'GenericList_Title_Name',
                    'GenericList_Title_Description', 'GenericList_Value1', 'GenericList_Value2',
                    'GenericList_PublishedStatus')
    list_display_links = ('id', 'GenericList_Category_Name', 'GenericList_Title_Name',
                          'GenericList_Title_Description', 'GenericList_Value1', 'GenericList_Value2',
                          'GenericList_PublishedStatus')
    ordering = ('id',)
    list_per_page: int = 20


############################################################################

@admin.register(DocumentCategoryWithoutTrans)
class AdminDocumentCategoryWithoutTrans(admin.ModelAdmin):
    list_display = ('id', 'DocumentCategory_Name', 'DocumentCategory_Status',
                    'DocumentCategory_PublishedStatus', 'DocumentCategory_LastUpdatedDate')
    list_display_links = ('id', 'DocumentCategory_Name', 'DocumentCategory_Status',
                          'DocumentCategory_PublishedStatus', 'DocumentCategory_LastUpdatedDate')
    ordering = ('id',)
    list_per_page: int = 20


############################################################################

@admin.register(Document)
class AdminDocument(admin.ModelAdmin):
    list_display = ('id', 'Document_Name', 'Document_Description',
                    'Document_CategoryType', 'Document_PublishedStatus')
    list_display_links = ('id', 'Document_Name', 'Document_Description',
                          'Document_CategoryType', 'Document_PublishedStatus')
    ordering = ('id',)
    list_per_page: int = 20


############################################################################

@admin.register(DocumentWithoutTrans)
class AdminDocumentWithoutTrans(admin.ModelAdmin):
    list_display = ('id', 'Document_Name', 'Document_Description',
                    'Document_CategoryType', 'Document_PublishedStatus')
    list_display_links = ('id', 'Document_Name', 'Document_Description',
                          'Document_CategoryType', 'Document_PublishedStatus')
    ordering = ('id',)
    list_per_page: int = 20


############################################################################


admin.site.register(FeedbackCategory)
admin.site.register(UserFeedbackData)
admin.site.register(Testimonials)
admin.site.register(Stackholder)
admin.site.register(LimitCheck)
############################################################################

admin.site.register(IDNReadyWebsitesCategory)
admin.site.register(IDNReadyWebsitesLanguages)
admin.site.register(IDNReadyWebsites)
admin.site.register(IDNReadyWebsitesLangugeURLMapping)
############################################################################

admin.site.register(GalleryHeadings)
admin.site.register(GalleryVideos)

############################################################################

admin.site.register(SOPTechnologyCategory)
admin.site.register(SOPTechnologyDocument)

############################################################################

    


@admin.register(IDNRequestForUserWebsites)
class AdminIDNRequestForUserWebsites(admin.ModelAdmin):
    list_display = ("IDN_Email", "IDN_Category", 'IDN_English_Domain', "IDN_Created_Date", 'IDN_Approve_Category')
    list_display_links = ("IDN_Email", "IDN_Category", 'IDN_English_Domain')
    search_fields = ("IDN_Email", "IDN_Category__IDN_category_name", 'IDN_English_Domain')
    
    


admin.site.register(IDNRequestForUserWebsitesCategories)
admin.site.register(OTP_For_IDNRequestForUserWebsites)
admin.site.register(SOPDownloadCounter)