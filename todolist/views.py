from django.http import HttpResponseRedirect
from django.shortcuts import render


class Todo:

    def __init__(self, description, isCompleted):
        self.title = description
        self.completed = isCompleted


def todolist(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            title = request.POST.get('title')
            Todo.objects.create(title=title)

    todolist = Todo.objects.all()
    return render(request, 'todolist.html', locals())


def delete(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    todo.delete()
    return HttpResponseRedirect('/')


def complete(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    todo.completed = True
    todo.save()
    return HttpResponseRedirect('/')