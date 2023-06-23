from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todo = Todo.objects.all()

    if request.method == 'POST':
        task = Todo(title=request.POST['title'], date=request.POST['date'])
        print(task)
        task.save()
        return redirect('/')

    return render(request, 'index.html', {'todos':todo},)

def manage(request,pk):
    todo = Todo.objects.get(id=pk)

    if(request.method=="POST"):
        todo.title = request.POST['title']
        todo.date = request.POST['date']
        todo.save()
        return redirect('/')
    
    return render(request, 'manage.html', {'todos':todo})

def done(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')
