# I have created this file.
from django.http import HttpResponse




from django.shortcuts import render



def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text 
    djtext = request.POST.get('text', 'default')  # text we entered in textbox

    # Checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')    
    extraspaceremover = request.POST.get('extraspaceremover', 'off')    
    charcount = request.POST.get('charcount', 'off')    
    
    #print(removepunc)
    #print(djtext)
    
    # ***** analyse the text *****

    # for punctuations
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        
        params = {'purpose': 'Remove Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed

    # for uppercase
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        
        params = {'purpose': 'Changed to UpperCase', 'analyzed_text':analyzed}
        djtext = analyzed

    # for Removing new line
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":  # char!="\r" -> bcz we are using POST request
                analyzed += char
        
        params = {'purpose': 'Remove new line', 'analyzed_text':analyzed}
        djtext = analyzed

    # for Removing new line
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed += char
        
        params = {'purpose': 'Remove extra space', 'analyzed_text':analyzed}
        djtext = analyzed
    
    if charcount == "on":
        analyzed = 0
        for char in djtext:
            if char.isalpha() :
                analyzed += 1
        params = {'purpose': 'Char count', 'analyzed_text':analyzed}

    if djtext == "":
        return HttpResponse("<h3>Oops! No texted entered... Please enter some text and select the operation</h3>")

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        params = {'analyzed_text': djtext}
        return render(request, 'analyze.html', params)


    return render(request, 'analyze.html', params)


