from ast import And
from django.shortcuts import render
from django.http import HttpResponse
from . import util
import markdown2
    



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request,title):
    return render(request, "encyclopedia/title.html", {
        "content": markdown2.markdown(util.get_entry(title)), "title":title
    }
    )  

def search(request):
    if request.method == "GET":
        form=request.GET['q']
        f=util.substring(form) 
        if type(f) is str:
          return render(request, "encyclopedia/title.html", {
             "content":markdown2.markdown (util.get_entry(f)), "title":f

             }
             )
        elif type(f) is list:
            return render(request, "encyclopedia/search.html", {
             "searchlist":f})
        
        else:
            return render(request, "encyclopedia/search.html", {
             "searchlist":'error'})

def new(request):
    return render(request, "encyclopedia/new.html",{'v':'F'})
       
     
def create(request):                             
  if request.method == "POST":
    
     title=request.POST['title']
     content=request.POST['newentry']
     res=request.POST['flag']
     f=util.substring(title) 
    
     if type(f) is str and res=='F':
           return render(request, "encyclopedia/error.html")
     else:
        util.save_entry(title,content)
        return render(request, "encyclopedia/index.html",{
        "entries": util.list_entries()
    })
   
''' else:
    return HttpResponse(request, 'fail')  type(f) is str  
'''
def edit(request):
    f=request.POST['edit']
    return render(request, "encyclopedia/new.html",
    {'title':f, 'content':util.get_entry(f), 'v':'T'})
 

def random(request):
    title=util.randompage()
    return render(request, "encyclopedia/title.html", {
        "content": markdown2.markdown(util.get_entry(title)), "title":title
    }
    )
