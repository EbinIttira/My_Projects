from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from .models import ToDotb
from .forms import ToDoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

def addtask(request):
    task=ToDotb.objects.all()
    if request.method == 'POST':
        task=request.POST.get('task')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        tasks=ToDotb(task=task,priority=priority,date=date)
        tasks.save()
        return redirect('/')
    return render(request,'Home.html',{'tasks':task})

def delete(request,id):
    task=ToDotb.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=ToDotb.objects.get(id=id)
    form=ToDoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'tasks':task})

class TaskListview(ListView):
    model=ToDotb
    template_name = 'Home.html'
    context_object_name = 'tasks'

class TaskDetailview(DetailView):
    model=ToDotb
    template_name ='details.html'
    context_object_name = 'task'

class TaskUpdateview(UpdateView):
    model=ToDotb
    template_name ='edit.html'
    context_object_name = 'task'
    fields=('task','priority','date')
    def get_success_url(self):
        return reverse_lazy('ToDoapp:detailview',kwargs={'pk':self.object.id})

class TaskDeleteview(DeleteView):
    model=ToDotb
    template_name ='delete.html'
    success_url = reverse_lazy('ToDoapp:listview')





