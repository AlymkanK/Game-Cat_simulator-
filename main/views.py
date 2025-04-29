from django.http import HttpResponseRedirect
from django.shortcuts import render
from .cat import Cat

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        Cat.name = request.POST.get('name')
        return HttpResponseRedirect('/cat_stats/')

def cat_stats(request):
    if request.method == 'GET':
        context = {
            'name': Cat.name,
            'age': Cat.age,
            'happiness': Cat.happiness,
            'satiety': Cat.satiety,
            'image': Cat.image
        }
        return render(request, 'cat_stats.html', context)
    else:
        action = request.POST.get('action')
        if action == 'play':
            Cat.play()
        elif action == 'feed':
            Cat.feed()
        else:
            Cat.sleep()
        return HttpResponseRedirect('/cat_stats/')
