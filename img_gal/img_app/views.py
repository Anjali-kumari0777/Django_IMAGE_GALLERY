from django.shortcuts import render
from .models import *
from .form import ImgForm

def Image_view(request):
    if request.method=='POST':
        form=ImgForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=ImgForm()
    imag=Imagemodel.objects.all()
    return render (request,'img_app/form.html',{'form':form,'imag':imag})

