from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

def index(request):
    reservations = Reservation.objects.all()
    context = { 'reservations': reservations }
    return render(request, 'board/index.html', context)


def detail(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    context = { 'reservation': reservation }
    return render(request, 'board/detail.html', context)


def new(request):
    # index -> a tag new -> views.new GET -> new.html -> views.new POST(create)
    if request.method == 'GET':
        form = ReservationForm()
        context = { 'form': form }
        return render(request, 'board/new.html', context)
    
    # create(new에서 받은 데이터(POST)담기)
    elif request.method == 'POST':
        form = ReservationForm(request.POST)
        # 유효성 검사
        if form.is_valid():  # form 조건 만족하는지, max_length등
            reservation = form.save()
            return redirect('detail', reservation.pk)
        # 유효성 검사 False 다시 전송
        context = { 'form': form }
        return render(request, 'board/new.html', context)


def edit(request, pk):
    # detail -> views.edit GET -> edit.html -> views.edit POST(update) -> detail
    reservation = Reservation.objects.get(id=pk)
    if request.method == 'GET':
        form = ReservationForm(instance=reservation)
        context = { 'form': form }
        return render(request, 'board/edit.html', context)

    elif request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)  # instance 안쓰면 새로 생성
        # 유효성 검사
        if form.is_valid():
            reservation = form.save()
            return redirect('detail', reservation.pk)
        # 유효성 검사 False
        context = { 'form': form }
        return render(request, 'board/edit.html', context)



def delete(request, pk):
    reservation = Reservation.objects.get(id=pk)

    if request.method == 'POST':
        reservation.delete()

    return redirect('index')

