from django.shortcuts import render, get_object_or_404
from .models import Blog

def main(request):
    return render(request, "main.html")

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, "blogwaro.html", {"blogs": blogs})

# ✅ FIX THIS FUNCTION:
def main_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'main-blog.html', {'blog': blog})
def search_blogs(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '').strip()
        blogs = Blog.objects.filter(title__icontains=searched)
        return render(request, 'search_blogs.html', {'searched': searched, 'blogs': blogs})
    else:
        return render(request, 'search_blogs.html', {'searched': '', 'blogs': []})




    

# Create your views here.
