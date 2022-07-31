from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    tasks = task.objects.all()
    form = task_form()

    if request.method == "POST":
        form = task_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    return render(request, "index.html", {"tasks":tasks,"form":form})


def update_task(request, pk):
    tasks = task.objects.get(id=pk)

    form = task_form(instance=tasks)

    if request.method == "POST":
        form = task_form(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {"form":form}

    return render(request, "update_task.html", context)

def delete_task(request, pk):
    item = task.objects.get(id=pk)
    if request.method =='POST':
        item.delete()
        return redirect("/")
    return render(request, "confirm_delete.html", {"item":item})