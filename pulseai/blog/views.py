from django.shortcuts import render, HttpResponse # type: ignore

# Create your views here.
def index(request):
      # return HttpResponse("Hello World!!!")
      return render(request,'blog/index.html')

def about(request):
      # return HttpResponse("<h1>About Us</h1>")
      return render(request,'blog/about.html')


def contact(request):
      mobile=8926194183
      email="er.antaryami@gmail.com"
      a=10
      b=10
      languages=['C','C++','Java','Python']
      blog={
            "titile":"Blog Title",
            "auhor":"John",
            "content":"Blog details"
      }
      students=[
            {"roll":1,"name":"sibu","cgpa":9.2},
            {"roll":2,"name":"lipu","cgpa":8.7},
            
      ]
      context={
            "mob":mobile,
            "email":email,
            "a":a,
            "b":b,
            "languages":languages,
            'blog':blog,
            'students':students,
      }
      return render(request,'blog/contact.html',context)