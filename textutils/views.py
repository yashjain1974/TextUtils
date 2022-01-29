# I have created this file -Yash jain
from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter




def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse("<h1>Hello world<h1>")

def analyze(request):
    #Get the text
    djtext=request.POST.get('text','default')
    punc=request.POST.get('puncremove','off')
    upper_case=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    params={}
    #Analyze the text
    analyzed=djtext
    if(punc=="on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        djtext=analyzed

    if upper_case == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed

    if spaceremover=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        djtext=analyzed

    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char

    if(punc!="on" and upper_case != "on" and spaceremover!="on" and newlineremover!="on"):
        params = {"purpose": "Analyzed text", "Analyzed_text": analyzed,
                  "CaharacterCount": characterCont(request, analyzed)}
        return render(request, "analyze.html", params)

    params = {"purpose": "Analyzed text", "Analyzed_text": analyzed, "CaharacterCount": characterCont(request,analyzed)}
    return render(request, "analyze.html", params)
def characterCont(request,analyzed):
    return Counter(analyzed)
