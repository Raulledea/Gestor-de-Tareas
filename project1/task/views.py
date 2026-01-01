from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        
        form = TaskForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        
        form = TaskForm()
    
        completed_tasks = Task.objects.filter(realized=True)
        incomplete_tasks = Task.objects.filter(realized=False)
         
        return render(request, 'task/index.html', {
            'form': form,
            'completed_tasks': completed_tasks,
            'incomplete_tasks': incomplete_tasks
        })
        
        
def task_view(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'task/task_view.html',{'task':task})

