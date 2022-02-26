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
    else:
        fm = Sub_Input()
    return render(request, 'Home/Home.html', {'fm':fm})

def AllSub(request):
    data = Subject_MOdel_Class.objects.all()
    return render(request, 'Home/subjects.html', {'data': data})
def Physics(request):
    data = Subject_MOdel_Class.objects.filter(subject='physics')
    return render(request, 'Home/subjects.html', {'data': data})
def Mathematics_1(request):
    data = Subject_MOdel_Class.objects.filter(subject='mathematic_1')
    return render(request, 'Home/subjects.html', {'data': data})
def BME(request):
    data = Subject_MOdel_Class.objects.filter(subject='bme')
    return render(request, 'Home/subjects.html', {'data': data})
def ES(request):
    data = Subject_MOdel_Class.objects.filter(subject='es')
    return render(request, 'Home/subjects.html', {'data': data})
def Other(request):
    data = Subject_MOdel_Class.objects.filter(subject='other')
    return render(request, 'Home/subjects.html', {'data': data})