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
        data = Subject_MOdel_Class(title=title, subject=subject, pdf_document=pdf_document, date=date, discription=discription)
        data.save()
        sucess_message = 'Successfully saved ' + title
        messages.info(request, sucess_message)
        err_message = 'Err to save. try again. ' + title
        messages.info(request, err_message)
    else:
        fm = Sub_Input()
    return render(request, 'Home/Home.html', {'fm':fm})

def AllSub(request):
    data = Subject_MOdel_Class.objects.all()
    Alls = 'bg-sky-500'
    return render(request, 'Home/subjects.html', {'data': data, 'Alls': Alls})
def Physics(request):
    data = Subject_MOdel_Class.objects.filter(subject='physics')
    phy = 'bg-sky-500'
    return render(request, 'Home/subjects.html', {'data': data, 'phy': phy})
def Mathematics_1(request):
    data = Subject_MOdel_Class.objects.filter(subject='mathematic_1')
    math = 'bg-sky-500'
    return render(request, 'Home/subjects.html', {'data': data, 'math': math})
def BME(request):
    data = Subject_MOdel_Class.objects.filter(subject='bme')
    bme = 'bg-sky-500'
    return render(request, 'Home/subjects.html', {'data': data, 'bme': bme})
def ES(request):
    data = Subject_MOdel_Class.objects.filter(subject='es')
    es = 'bg-sky-500'
    return render(request, 'Home/subjects.html', {'data': data, 'es': es})
def Other(request):
    data = Subject_MOdel_Class.objects.filter(subject='other')
    other = 'bg-sky-500'
    return render(request, 'Home/subjects.html', {'data': data, 'other': other})