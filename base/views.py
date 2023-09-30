from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Patient, Ward
from .forms import PatientForm
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')
        

    context = {}
    return render(request, 'base/login.html', context) 

def registrationPage(request):
    context = {}
    return render(request, 'base/register.html', context)


def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def patientList(request):
    # q = request.GET.get('q') if request.GET.get('q') != None else '' 
    # filteredPatients = Patient.objects.filter(name__icontains=q)

    # existing_entries =  Patient.objects.filter(created__isnull=True).exists()

    # if existing_entries:
    #     Patient.objects.filter(created__isnull=True).updated(created=timezone.now())

    patients = Patient.objects.all().order_by('created')
    context = {'patients':patients}
    return render(request, 'base/patient_list.html', context)


def registerPatient(request):
    form = PatientForm()
    if request.method == 'POST':

        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')

    context = {'form': form}
    return render(request, 'base/patient_form.html', context)


def editPatient(request, pk):
    patient = Patient.objects.get(patient_id = pk)
    form = PatientForm(instance = patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance = patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    context = {'form': form}
    return render(request, 'base/patient_form.html', context)

def deletePatient(request, pk):
    patient = Patient.objects.get(patient_id = pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')

    return render(request, 'base/delete.html', {'obj': patient})


def wardList(request):
    wards = Ward.objects.all().order_by('ward_id')
    context = {'wards':wards}
    return render(request, 'base/wards.html', context)



