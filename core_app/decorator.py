import environ
env = environ.Env()
environ.Env.read_env()
import json
from django.http import HttpResponseRedirect
import urllib.parse
from django.conf import settings

# -----ADDED BY SHWETA PATIL -------
def preprocesslangset(view_func):
    def wrapper(request, *args, **kwargs):
        print("requested path ------------------",request.build_absolute_uri())
        maindomain = request.build_absolute_uri().split('/')[2]
        print("requested path ------------------",request.build_absolute_uri().split('/')[4:])
        try:
            parameter1=request.build_absolute_uri().split('/')[4]
        except:
            parameter1=''
        try:
            parameter2=request.build_absolute_uri().split('/')[5]
        except:
            parameter2=''

        try:
            parameter3=request.build_absolute_uri().split('/')[6]
        except:
            parameter3=''
        
        requested_domain_withoutport=maindomain.split(':')[0]
        finalpath='/'+request.build_absolute_uri().split('/')[3].split('?')[0]
        pathdecode=urllib.parse.unquote(finalpath)
        domain_lang=''
        path_lang=''
        return_path=''
        print("Inside decorator================",requested_domain_withoutport)
        with open(env('LANGUAGE_DOMAINS'), 'r',encoding="utf8") as j:
            dom = json.loads(j.read())
            print("hello data")
        for data in range(len(dom)):
            for key,value in dom[data].items():
                filterdomain1=value.split('/')[2]
                filterdomain2=filterdomain1.split(':')[0]
                if requested_domain_withoutport == filterdomain2 :
                    print("domain match",requested_domain_withoutport,filterdomain2)
                    domain_lang=key
                    return_domain=value
                    print("Inside decorator",requested_domain_withoutport,key)
        with open(env('LANGUAGE_PATHS'), 'r',encoding="utf8") as j:
            path = json.loads(j.read())
        for data in range(len(path)):
            for key,value in path[data].items():
                if pathdecode == value :
                    print("0-0-0-0--",key,value)
                    return_path = path[data][domain_lang]
                    print("0-0-0-0--",return_path)
                    path_lang=key
        if path_lang==domain_lang:
            return view_func(request, *args, **kwargs)
        else:
            if parameter1:
                if parameter2:
                    if parameter3:
                        print("insidse1",return_domain+return_path+'/'+parameter1+'/'+parameter2+'/'+parameter3)
                        response = HttpResponseRedirect(return_domain+return_path+'/'+parameter1+'/'+parameter2+'/'+parameter3)
                    else:
                        print("insidse2",return_domain+return_path+'/'+parameter1+'/'+parameter2,pathdecode)
                        response = HttpResponseRedirect(return_domain+return_path+'/'+parameter1+'/'+parameter2)
                else:
                    print("insidse3",return_domain+return_path+'/'+parameter1)
                    response = HttpResponseRedirect(return_domain+return_path+'/'+parameter1)
            else:
                print("insidse4",return_domain+return_path)
                response = HttpResponseRedirect(return_domain+return_path)
            return response
    return wrapper