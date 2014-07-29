
from django.shortcuts import redirect
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
from .forms import PostsForm

def index(request):

    if request.method == "POST":
        #POST : auto data encoding, GLOBAL SERVICE
        #PUT : low memory, object delete, NOT AVAILABLE FOR GLOBAL SERVICE
        #SERVICE
        print request.POST
        m = PostsForm(request.POST) #save
        post_obj = m.save()
        obj = m.save()
        print obj
        return redirect("/blog/")
        # save
   # else:
        #GET
        #first request or ....
    #    return render(request,"base.html",
    #        {})


    print "hello world"
    pform = PostsForm()
    print pform.as_p()
    print "hello world"
    return render(request,"base.html",
        {"hello":"helloworld",
         "form" : pform} )

#    return HttpResponse("sdfsdaf")
