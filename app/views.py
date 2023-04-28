from django.shortcuts import render

def home(request):

    return render(request, "pages/index.html")


def contact(request):

    return render(request, 'pages/contact.html')

def about_page(request):

    return render(request, 'pages/about.html')

def blog_view(request):

    return render(request, "pages/blogs.html")
