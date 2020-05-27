from django.shortcuts import render
from django.http import HttpResponse
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
    data={'posts':posts}
    return render(request,'blog/home.html',data)

def about(request):
    return render(request,'blog/about.html',{'title':'About us'})