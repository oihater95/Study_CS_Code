from django.shortcuts import render, redirect
from .models import Student  # Student Model 사용하려면 반드시 import해야함

# Read(조회)
def index(request):
    students = Student.objects.all()  # 위에서 import했기 때문에 사용 가능
    context = {
        'students': students,
    }
    return render(request, 'orm_practice/index.html', context)


def detail(request, pk):
    student = Student.objects.get(id=pk)  # pk=pk로 써도 가능
    context = {
        'student': student
    }
    return render(request, 'orm_practice/detail.html', context)


# Create(생성)
def new(request):  # 정보 받기
    return render(request, 'orm_practice/new.html')


def create(request):  # 받은 정보를 토대로 생성
    student = Student()
    student.name = request.GET.get('name')
    student.age = request.GET.get('age')
    student.major = request.GET.get('major')
    student.intro = request.GET.get('intro')
    student.save()

    # create => index 로 보내기, pass쓰면 안됨 pass는 응답이 없음
    # redirect(RAW URL / urls.py의 name)
    return redirect('detail', pk=student.pk)  # 'index' = /practice/, 'detail'은 넘겨줄 인자 필요
