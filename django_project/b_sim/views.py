from django.shortcuts import render

# Create your views here.


posts = [
    {
        'author': 'Vijay',
        'title': 'Blog1 Post',
        'content': 'First Content',
        'date_posted': 'October 1st, 2019',
    },
    {
        'author': 'Vijay Karigowdara',
        'title': 'Blog2 Post',
        'content': 'Second Content',
        'date_posted': 'October 1st, 2019',
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'b_sim/home.html',context)


def about(request):
    return render('b_sim/help.html')
