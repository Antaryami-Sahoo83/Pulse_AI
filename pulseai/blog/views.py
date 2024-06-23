from django.shortcuts import render, HttpResponse # type: ignore

# Create your views here.
def index(request):
      # return HttpResponse("Hello World!!!")
      return render(request,'blog/index.html')