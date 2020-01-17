from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .forms import TodoForm
from .models import Todo

def index(request):
    mytodo = Todo.objects.order_by('id')
    form = TodoForm()
    context = { 'mytodo': mytodo, 'form':form }
    return render(request, 'app/index.html', context)

def index2(request, pk):
    todo = Todo.objects.get(pk=pk)
    form = TodoForm()
    context = { 'todo': todo, 'form': form }
    return render(request, 'app/index2.html', context)


@require_POST
def addNewTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        my_new_todo = Todo(text = request.POST['text'])
        my_new_todo.save()

    return redirect('index')

@require_POST
def updateTodo(request, pk):
    form = TodoForm(request.POST)
    if form.is_valid():
        Todo.objects.filter(pk=pk).update(text = request.POST['text'])

    return redirect('index')

def completeTodo(request,pk):
    mytodo = Todo.objects.get(pk=pk)
    mytodo.complete = True  # .complete comes from models!
    mytodo.save()  # don't forget to save it

    return redirect('index')


def deleteTodo(request,pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('index')



def resetTodo(request):
    Todo.objects.filter().delete()
    return redirect('index')