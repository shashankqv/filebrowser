from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

import os
import spwd
import crypt
from utils import *

# Create your views here.



def index(request):
    status = login('shashank','India@123')
    print status
    status = login('shashank1','India@123')
    print status
    return render_to_response('home.html', {'name': 'Shashank',
        'message' : 'I am coming here in template'},
        context_instance=RequestContext(request))



def loggingin(request):
    status = "Not Logged In"
    statusmessage = ""

    if request.method == "POST":
        print "Hey I am post"

        username = request.POST.get('login',None)
        password = request.POST.get('password',None)
        
        
        if loginvalidate(username):
            pass
        else:
            return HttpResponse("Root Login not allowed") 

        
        if username is not None and password is not None:
            print "Hey i am present"
            status = login(username,password)
    
    data1 = path_to_dict_1_level('/home/%s/' % (username
        ))
    
    data = json.loads(data1)
    childr = parseJson(data1)
    #childr = json.loads(childr)
    
    print data
    print type(data)

    return render_to_response('filebrowse.html', {'name': data['name'],
        'children' : childr, 'type' : data['type'], 'complete' : data},
        context_instance=RequestContext(request))
    return HttpResponse(data)


def parseJson(data):
    data_in_dict = json.loads(data)
    dirlist = []
    for i in data_in_dict['children']:
        finaldata= {}
        data = i.split('/')
        filename = data[-1]
        print filename
        print i + "----" + filename
        finaldata['url'] = i
        finaldata['value'] = filename
        if os.path.isdir(i):
            finaldata['typeo'] = "dir"
        else:
            finaldata['typeo'] = "file"
        print finaldata
        if filename.startswith("."):
            finaldata['ishidden'] = True
        else:
            finaldata['ishidden'] = False
        dirlist.append(finaldata)
        print dirlist
    return dirlist