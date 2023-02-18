# i have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse('home')

def analyze(request):
    # get the text
    rawText=request.POST.get('text','default')

    rempun = request.POST.get('rempun','off')
    remspace = request.POST.get('remspace','off')
    capfirst = request.POST.get('capfirst','off')
    remnewline = request.POST.get('remnewline','off')
    upcase = request.POST.get('upcase','off')

    params = {"purpose":"", "analyzed_text":rawText}

    if(rempun=='on'):
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzedText = ""
        for char in rawText:
            if char not in punctuations:
                analyzedText+=char
        params["purpose"]+='Removed Punctuations, '
        params["analyzed_text"]=analyzedText
        rawText=analyzedText
    if(remspace=='on'):
        analyzedText = ""
        for char in rawText:
            if char != ' ':
                analyzedText+=char
        params["purpose"]+='Removed spaces, '
        params["analyzed_text"]=analyzedText
        rawText=analyzedText
    if(remnewline=='on'):
        analyzedText = ""
        for char in rawText:
            if char != '\n' and char!='\r':
                analyzedText+=char 
        params["purpose"]+='Removed new line, '
        params["analyzed_text"]=analyzedText
        rawText=analyzedText
    if(capfirst=='on'):
        analyzedText = ""
        for index, char in enumerate(rawText):
            if (index==0):
                analyzedText+=char.upper()
            elif (rawText[index-1]==" "):
                analyzedText+=char.upper()
            else:
                analyzedText+=char
        params["purpose"]+='Capitalized first character, '
        params["analyzed_text"]=analyzedText
        rawText=analyzedText
    if(upcase=='on'):
        analyzedText = ""
        for char in rawText:
            analyzedText+=char.upper()
        params["purpose"]+='Converted to upper case, '
        params["analyzed_text"]=analyzedText
        rawText=analyzedText
    return render(request, 'analyze.html', params)