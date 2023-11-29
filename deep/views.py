from django.shortcuts import render,HttpResponse ,redirect

# Create your views here.
# Create your views here.
def index(request):
    return render(request, 'index.html')

def tryout(request):
    return render(request, 'tryout.html')