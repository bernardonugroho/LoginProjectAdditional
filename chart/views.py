from django.shortcuts import render

def viewbar(request):
    return render(request, 'chart/viewbar.html')

def viewbubble(request):
    return render(request, 'chart/viewbubble.html')

def viewpie(request):
    return render(request, 'chart/viewpie.html')

def viewdynamic(request):
    return render(request, 'chart/viewdynamic.html')

def viewmultiple(request):
    return render(request, 'chart/viewmultiple.html')

def viewmap(request):
    return render(request, 'chart/viewmap.html')

def viewgeo(request):
    return render(request, 'chart/viewgeo.html')