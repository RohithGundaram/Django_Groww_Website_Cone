from django.shortcuts import render

# Create your views here.
def LandingPage(request):
    return render(request,'LandingPage.html')

def Home(request):
    return render(request, 'Dashboard_index.html')