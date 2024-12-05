from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    # return HttpResponse("<h1>Hello i am a django server</h1>")

    people = [
        {'name': 'Aryan', 'age': 22},
        {'name': 'Meera', 'age': 24},
        {'name': 'Vikram', 'age': 18},
        {'name': 'Nisha', 'age': 21},
        {'name': 'Rohan', 'age': 15},
        {'name': 'Priya', 'age': 10},
        {'name': 'Kabir', 'age': 23},
        {'name': 'Simran', 'age': 17},
        {'name': 'Aarav', 'age': 19}
    ]

    return render(request, "index.html", context={'peoples' : people, 'page':"Home"})

def about(request):
    return render(request, "about.html", context={'page':"About"})

def contact(request):
    return render(request, "contact.html", context={'page':"Contact"})

def success_page(request):
    # print("*" * 10 )
    return HttpResponse("<h1>Hey this is a success page</h1>")