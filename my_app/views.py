from django.shortcuts import render
from learn_celery.celery import add
from celery.result import AsyncResult
from my_app.tasks import sub
# Create your views here.

## Enqueue   task using delay 
# def index(request):
#     print("result: ")
#     result1 = add.delay(10,20)
#     print("result1", result1)
#     result2 = sub.delay(60,20)
#     print("result2", result2)
#     return render(request, "myapp/home.html")

# def about(request):
#     print("result: ")
#     return render(request, "myapp/about.html")

# def contact(request):
#     print("result: ")
#     return render(request, "myapp/contact.html")

#### --------------------------------------

## Enqueue   task using delay 
# def index(request):
#     print("result: ")
#     result1 = add.apply_async(args=[10,20])
#     print("result1", result1)
#     result2 = sub.apply_async(args=[60,20])
#     print("result2", result2)
#     return render(request, "myapp/home.html")

# def about(request):
#     print("result: ")
#     return render(request, "myapp/about.html")

# def contact(request):
#     print("result: ")
#     return render(request, "myapp/contact.html")

def index(request):
    result = add.delay(10,20)
    
    return render(request, "myapp/home.html", {'result':result})

def check_result(request, task_id):
    result = AsyncResult(task_id)
    print("ready", result.ready())
    print("success", result.successful())
    print("Failed",  result.failed())
    return render(request, "myapp/result.html", {'result':result})

def about(request):
    print("result: ")
    return render(request, "myapp/about.html")

def contact(request):
    print("result: ")
    return render(request, "myapp/contact.html")

