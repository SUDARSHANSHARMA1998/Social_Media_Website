from django.shortcuts import render
from .models import Post
posts=[
    {
        'author':'Sud',
        'title':'Post 1',
        'content':'First post of the day',
        'date_posted':'16th Aug'
    },
    {
        'author':'Radhika',
        'title':'Post 2',
        'content':'Second post of the day',
        'date_posted':'17th Aug'
    },


]
# Create your views here.
def home(request):
    data={'posts':Post.objects.all()}
    return render(request,'blog/home.html',data)

def about(request):
    return render(request,'blog/about.html',{'title':'About us'})