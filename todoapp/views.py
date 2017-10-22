from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from .models import Todo

def todo_list(request):
	todos = Todo.objects.filter(published_date__lte=timezone.now()).order_by('due_date')
	return render(request, 'todoapp/todo_list.html', {'todos': todos})