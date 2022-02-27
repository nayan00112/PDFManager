from django.shortcuts import render
from .forms import Sub_Input
from .models import Subject_MOdel_Class
from django.contrib import messages

# Create your views here.
def Index(request):
    return render(request, 'Home/index.html')

def Home(request):

    if request.method == 'POST':
        fm = Sub_Input(request.POST)
        title = request.POST['title']
        subject = request.POST['subject']
        pdf_document = request.FILES['pdf_document']
        date = request.POST['date']
        discription = request.POST['discription']
        userhid = request.user.username
        data = Subject_MOdel_Class(title=title, subject=subject, pdf_document=pdf_document, date=date, discription=discription, userhid=userhid)
        data.save()
        sucess_message = 'Successfully saved ' + title
        messages.info(request, sucess_message)
    else:
        fm = Sub_Input()
    return render(request, 'Home/Home.html', {'fm':fm})

def AllSub(request):
    data = Subject_MOdel_Class.objects.filter(userhid=request.user.username)
    Alls = 'bg-sky-500'
    return render(request, 'Home/subjects.html', {'data': data, 'Alls': Alls})
def Physics(request):
    data = Subject_MOdel_Class.objects.filter(subject='physics', userhid=request.user.username)
    phy = 'bg-sky-500'
    return render(request, 'Home/subjects.html', {'data': data, 'phy': phy})
def Mathematics_1(request):
    data = Subject_MOdel_Class.objects.filter(subject='mathematic_1', userhid=request.user.username)
    math = 'bg-sky-500'
    return render(request, 'Home/subjects.html', {'data': data, 'math': math})
def BME(request):
    data = Subject_MOdel_Class.objects.filter(subject='bme', userhid=request.user.username)
    bme = 'bg-sky-500'
    return render(request, 'Home/subjects.html', {'data': data, 'bme': bme})
def ES(request):
    data = Subject_MOdel_Class.objects.filter(subject='es', userhid=request.user.username)
    es = 'bg-sky-500'
    return render(request, 'Home/subjects.html', {'data': data, 'es': es})
def Other(request):
    data = Subject_MOdel_Class.objects.filter(subject='other', userhid=request.user.username)
    other = 'bg-sky-500'
    return render(request, 'Home/subjects.html', {'data': data, 'other': other})