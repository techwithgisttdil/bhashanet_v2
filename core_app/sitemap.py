from django.contrib.sitemaps import Sitemap
from bhashanet_v2 import urls
from django.urls import reverse
from .models import IDNReadyWebsites
from admin_app.models import BlogCategory, Blog
import math

class StaticSitemap(Sitemap):
     priority = 0.8
     changefreq = 'weekly'
    #  i18n = True
     # The below method returns all urls defined in urls.py file
     def items(self):
        mylist = [ ]
        for url in urls.Translation_urlpatterns:
            if url.name != 'RenderPageWithPathAndLang' and url.name != 'RenderPageWithPathAndLangId' and url.name != 'user_activate' and url.name != 'password_creation':
                if url.name == "idn_websites":
                    count = IDNReadyWebsites.objects.all().count()
                    number_of_pages = math.ceil(count/5)
                    for i in range(1,number_of_pages+1):
                        mylist.append(f"{url.name} {i}")
                elif url.name == "cat_selected":
                    count = BlogCategory.objects.all().count()
                    number_of_pages = math.ceil(count/5)
                    for i in range(1,number_of_pages+1):
                        mylist.append(f"{url.name} {i}")
                elif url.name == "blog":
                    count = Blog.objects.all().count()
                    number_of_pages = math.ceil(count/5)
                    for i in range(1,number_of_pages+1):
                        mylist.append(f"{url.name} {i}")
                elif url.name == "edit_blog":
                    count = Blog.objects.all().count()
                    number_of_pages = math.ceil(count/5)
                    for i in range(1,number_of_pages+1):
                        mylist.append(f"{url.name} {i}")
                else:
                    mylist.append(url.name)
        print("mylist ",mylist)
        return mylist
     
     def location(self, item):
         print("inside location ",item)
         if item.split()[0] == "idn_websites":
            # print("item ", item.split())
            return reverse(item.split()[0], kwargs={'id': item.split()[1]})
         elif item.split()[0] == "cat_selected":
            return reverse(item.split()[0], kwargs={'id': item.split()[1]})
         elif item.split()[0] == "blog":
            return reverse(item.split()[0], kwargs={'id': item.split()[1]})
         elif item.split()[0] == "edit_blog":
            return reverse(item.split()[0], kwargs={'id': item.split()[1]})
         return reverse(item)
