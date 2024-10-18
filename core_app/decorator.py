import environ
env = environ.Env()
environ.Env.read_env()
import json
from django.http import HttpResponseRedirect
import urllib.parse
from django.conf import settings


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
                    response = HttpResponseRedirect(return_domain+return_path+'/'+parameter1+'/'+parameter2)
                else:
                    print("insidse",return_domain+return_path+'/'+parameter1)
                    response = HttpResponseRedirect(return_domain+return_path+'/'+parameter1)
            else:
                response = HttpResponseRedirect(return_domain+return_path)
            return response
    return wrapper