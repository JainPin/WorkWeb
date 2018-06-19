from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist


from .models import OneWeb,Note
# Create your views here.

def index(request):
    latest_question_list = OneWeb.objects.order_by('-id')[:5]
    context = {
        'latest_question_list':latest_question_list,
        'count':0,
    }
    return render(request,'OneWeb/index.html',context)
    #return HttpResponse("Hellword")
def blog(request, OneWeb_id):
    blog=""
    try:
        blog = OneWeb.objects.get(id=OneWeb_id)
        pass
    except ObjectDoesNotExist as er:
        pass
    
    context = {
        'blog':blog,
    }
    return render(request,'OneWeb/blog.html',context)
    #return HttpResponse("blog")
def bNote(request):
    title = ""
    utitle= ""
    content =""
    ucontent =""
    if(request.method=="POST"):
        #get= get_object_or_404(Note)
        if(request.POST['title']!="" and request.POST['content']!=""):
            add = Note(title=request.POST['title'],content=request.POST['content'])
            add.save()
        else:
            if request.POST['title']=="" :
                title="請輸入稱呼"
            else:
                utitle=request.POST['title']
            if request.POST['content']=="" :
                content = "請輸入內容"
            else:
                ucontent = request.POST['content']
    note_list = Note.objects.order_by('-id')[:5]
    context = {
        'note_list':note_list,
        'title':title,
        'content':content,
        'utitle':utitle,
        'ucontent':ucontent,
    }

    if(note_list != None):
        return render(request,'OneWeb/note.html',context)
    else:
        return render(request,'OneWeb/note.html')
        pass
        #return HttpResponse("Note")
