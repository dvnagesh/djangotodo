from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils import timezone
from .models import Todo
from .forms import TodoForm

def todo_list(request):
	todos = Todo.objects.filter(published_date__lte=timezone.now()).order_by('due_date')
	return render(request, 'todoapp/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	return render(request, 'todoapp/todo_detail.html', {'todo': todo})

def todo_new(request):
	form = TodoForm()
	return render(request, 'todoapp/todo_edit.html', {'form': form})
