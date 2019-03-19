from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo


def home(request):
    ttodos = request.user.todo_set.filter(completed=True).all().order_by('-id')
    ftodos = request.user.todo_set.filter(completed=False).all().order_by('-id')
    return render(request, 'todos/home.html', {
        "ttodos": ttodos,
        "ftodos": ftodos
    })


def create(request):
    content = request.POST.get('content')
    user_id = request.user.id
    Todo.objects.create(content=content, user_id=user_id)
    return redirect('todos:home')


def check(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = False if todo.completed else True
    todo.save()
    return redirect('todos:home')


def delete(request, todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()
    return redirect('todos:home')
