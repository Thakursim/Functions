from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") #string of html code
    return render(request, "home.html", {})
	
	
def contact_view(request, *args, **kwargs): # *args, **kwargs
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs): # *args, **kwargs
    my_content = {
	  "my_text": "This is about us",
	  "my_number": 123,
	  "my_list": [123, 456, 908, 788, "Simran"]
	}
    return render(request, "about.html", my_content)

def social_view(request, *args, **kwargs): # *args, **kwargs
    return HttpResponse("<h1>Social Page</h1>") 