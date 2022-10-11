from django.shortcuts import render
from django.shortcuts import redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages


def index(request):
    data = Task.objects.all()
    params = {
        'data': data,
    }
    return render(request, 'task/index.html', params)

def create(request):
    params = {
        'form': TaskForm(),
    }
    if (request.method == 'POST'):
        title = request.POST['title']
        body = request.POST['body']
        task = Task(title=title, body=body)
        task.save()
        messages.add_message(request, messages.SUCCESS, "Task created succesfully")    # 追加
        return redirect(to='/task')
    return render(request, 'task/create.html', params)


def detail(request, task_id):
	task = Task.objects.get(id=task_id)
	params = {
            'id': task_id,
        	'obj': task,
        }
	return render(request, 'task/detail.html', params)


def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if (request.method == 'POST'):
        task.title = request.POST['title']
        task.body = request.POST['body']
        task.save()
        return redirect(to='/task')
    else:
        form = TaskForm(initial={
            'title': task.title,
            'body': task.body,
        })
        params = {
            'task': task,
            'form': form,
        }
        return render(request, 'task/edit.html', params)

def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if (request.method == 'POST'):
        task.delete()
        return redirect(to='/task')
    else:
        params = {
            'id': task_id,
            'obj': task,
        }
        return render(request, 'task/delete.html', params)
