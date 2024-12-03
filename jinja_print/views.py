from django.shortcuts import render

# Create your views here.

def jinja_print(request):
    D={'NAME':'SAI','AGE':23}
    return render(request,'jinja_print.html',context=D)