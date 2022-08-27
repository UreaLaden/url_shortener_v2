from django.shortcuts import render, HttpResponse,redirect
from django.http import Http404,HttpResponseNotFound
from .models import urlModel
import string,random
from django.views.decorators.csrf import csrf_exempt,csrf_protect

# Create your views here.
def home(request):
    return render(request,'home.html')

def make_short_url(request):
    if request.method == "POST":
        key = string.ascii_letters + '123456789~!@#$%^&*'
        original_url = request.POST['original_url']
        short_url = "".join(random.sample(key,6))
        obj = urlModel.objects.create(original_url=original_url,short_url=short_url)
        short_url = "http://localhost:8000/" + short_url
        context = {'original_url':original_url,'short_url':short_url}
        return render(request,'urlcreated.html',context)

def redirect_url(request,short_url):
    try:
        obj = urlModel.objects.get(short_url=short_url)
        obj.count += 1
        obj.save()
        return redirect(obj.original_url)
    except urlModel.DoesNotExist:
        return HttpResponse("Page not found. Double check your url")