from django.shortcuts import render
from .models import todomodel
# Create your views here.

def todo_view(request):
    print(request.POST)
    if request.method=="POST":
        todomodel.objects.create(item=request.POST['a'])
    obj=todomodel.objects.all()
    context={'obj':obj}
    return render(request,'index.html',context)



