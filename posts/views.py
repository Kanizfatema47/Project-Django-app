from django.shortcuts import render

def posts_list(request):   #it going to receive request
    return render(request, "posts/posts_list.html")