from django.shortcuts import render
from django.http import HttpResponse
from formsapp.forms import StudentForm

# Create your views here.
def demo(request):
	return HttpResponse('I am from Formsapp')
def reg(request):
	if request.method == 'POST':
		form=StudentForm(request.POST)
		form.save()
		return HttpResponse('Data inserted using forms....')
	form = StudentForm()
	return render(request,'Formsapp/reg.html',{'form':form})