from django.shortcuts import render

posts = [
    {
        "author": "Mrityunjay",
        "title": "Getting Started with Django",
        "content": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. In this post, we'll explore the basics of setting up a Django project from scratch.",
        "date_posted": "June 1, 2026"
    },
    {
        "author": "Rohan Sharma",
        "title": "Understanding Django Models",
        "content": "Models are the single, definitive source of information about your data. In this post, we'll dive deep into Django models, fields, and how to interact with the database using Django's ORM.",
        "date_posted": "June 2, 2026"
    },
    {
        "author": "Priya Verma",
        "title": "Django Templates Explained",
        "content": "Django's template engine provides a powerful mini-language for defining the HTML of your application. Learn how to use template tags, filters, and inheritance to build clean UIs.",
        "date_posted": "June 3, 2026"
    },
    {
        "author": "Amit Khanna",
        "title": "User Authentication in Django",
        "content": "Django comes with a built-in authentication system. In this post, we'll cover login, logout, registration, and protecting views with the login_required decorator.",
        "date_posted": "June 4, 2026"
    },
    {
        "author": "Sneha Gupta",
        "title": "Working with Django Forms",
        "content": "Forms are an essential part of any web application. Django provides a powerful forms library that handles rendering, validation, and processing of form data with minimal code.",
        "date_posted": "June 5, 2026"
    },
    {
        "author": "Mrityunjay",
        "title": "Django URL Routing",
        "content": "URL routing in Django is handled by URLconfs. In this post we'll explore how to map URLs to views using path(), include(), and named URL patterns for cleaner templates.",
        "date_posted": "June 6, 2026"
    },
]

# Create your views here.
def home(request):
    context = {
        "posts": posts
    }
    return render(request,"blog/home.html",context)

def about(request):
    return render(request,"blog/about.html")