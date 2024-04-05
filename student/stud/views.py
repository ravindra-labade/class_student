from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.views import View


class create_view(View):
    def get(self, request):
        form = StudentForm()
        context = {'form': form}
        return render(request, 'stud/create.html', context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
        context = {'form': form}
        return render(request, 'stud/create.html', context)


class show_view(View):
    def get(self, request):
        students = Student.objects.all()
        context = {'students': students}
        return render(request, 'stud/show.html', context)


class update_view(View):
    def get(self, request, pk):
        obj = Student.objects.get(id=pk)
        form = StudentForm(instance=obj)
        context = {'form': form}
        return render(request, 'stud/create.html', context)

    def post(self, request, pk):
        obj = Student.objects.get(id=pk)
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')

class delete_view(View):
    def get(self, request, pk):
        return render(request, 'stud/confirm.html')

    def post(self, pk):
        obj = Student.objects.get(id=pk)
        obj.delete()
        return redirect('show_url')