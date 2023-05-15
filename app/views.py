from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView
# Create your views here.
from app.forms import *



def fbv_string(request):
    return HttpResponse('This is function base view string')


class cbv_string(View):
    def get(self,request):
        return HttpResponse('This is Class based views string')


def fbv_html(request):
    return render(request,'fbv_html.html')


class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')

def fbv_form(request):
    Sfo=Student_Form()
    d={'Sfo':Sfo}
    if request.method=='POST':
        Sfd=Student_Form(request.POST)
        if Sfd.is_valid():
            Sfd.save()
            return HttpResponse('Data is insertted successfully')
    return render(request,'fbv_form.html',d)


class cbv_form(View):
    def get(self,request):
        cbvo=Student_Form()
        d={'cbvo':cbvo}
        return render(request,'cbv_form.html',d)

    def post(self,request):
        if request.method=='POST':
            Cbvd=Student_Form(request.POST)
            if Cbvd.is_valid():
                Cbvd.save()
        return HttpResponse('Data insertted successfully')