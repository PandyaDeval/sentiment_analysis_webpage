from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import NameForm
from . import new1
# Create your views here.
from django.template import loader, RequestContext


def index(request):
    #return render(request,'catalog/xyz.html')
    result= ''
    if request.method=='GET':
        form=NameForm(request.GET)
        if form.is_valid():
            result = form.cleaned_data['tweet']
            result=new1.predict(result)

    #template = loader.get_template('catalog/xyz.html')
    return render(request,'catalog/xyz.html',{'x':result})
