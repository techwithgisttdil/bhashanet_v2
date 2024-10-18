from urllib.parse import urlsplit
from django.conf import settings

def custom_context(request):
  maindomain = request.build_absolute_uri().split('/')[2]
  requesteddomainwithoutport=maindomain.split(':')[0]
  if requesteddomainwithoutport == "xn-----btdbc3d4hd37blpqm.xn--mgbbh1a71e" or requesteddomainwithoutport == "xn----ymcac5dzf1p7v.xn--mgbbh1a":
    print("True from context")
    return {'urdu_domain': True}
  elif requesteddomainwithoutport=="xn--uwcjna1a5bb9d4cb.xn--rvc1e0am3e":
    return {'malayalam_domain': True} 
  else:
    print("False from context")
  return {'urdu_domain': False}
  


  
  
  
  

