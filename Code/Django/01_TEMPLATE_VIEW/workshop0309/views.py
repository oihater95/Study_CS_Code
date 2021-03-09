from django.shortcuts import render

def dinner(request, menu, people):
    context = {
        'people': people,
        'menu': menu,
    }
    return render(request, 'workshop0309/dinner.html',context)
