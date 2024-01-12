from django.shortcuts import render

from django.http import HttpResponse


def main(request):
    return render(request,'main.html')
def index(request):
    return render(request,'index.html')
def yes_page(request):
    return render(request, 'yes.html')