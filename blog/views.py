from django.shortcuts import render
from .models import Post

# dummy data
posts = [
    {
        'author':'RobbyG',
        'title': "Garry's Mod",
        'content':'First post content',
        'date_posted':'June 18, 2020',
        'grade': 'A'
    },
    {
        'author':'RobbyG',
        'title':'Our Newest Site',
        'content':'First post content',
        'date_posted':'June 18, 2020',
        'grade': 'B',
    },
]

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})
 