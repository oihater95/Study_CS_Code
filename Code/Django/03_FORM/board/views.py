from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Reservation
from .forms import ReservationForm

@require_http_methods(['GET', 'POST'])  # GET, POST 요청에만 응답, 다른 요청방식은 Bad Request 
def new(request):  
    if request.method == 'POST':
        form = ReservationForm(request.POST)  # POST 데이터 담음
        if form.is_valid():
            reservation = form.save()
            return redirect('board:detail', reservation.pk)  # redirect(app_name:urls, pk)

    elif request.method == 'GET':
        form = ReservationForm()
    
    # GET요청이거나 유효성 검사 통과하지 못했다면 여기로
    context = { 'form': form }
    return render(request, 'board/form.html', context)


@require_GET  # GET 요청만 응답, 나머지는 Bad Request
def index(request):
    reservations = Reservation.objects.order_by('-pk')  # pk 역순으로 가져오기
    context = { 'reservations': reservations }
    return render(request, 'board/index.html', context)


@require_GET  # GET 요청만 응답, 나머지는 Bad Request
def detail(request, reservation_pk):  # urls.py에서 reservation_pk로 받음
    reservation = get_object_or_404(Reservation, pk=reservation_pk)
    context = { 'reservation': reservation }
    return render(request, 'board/detail.html', context)


@require_http_methods(['GET', 'POST'])  # GET, POST 요청만 응답, 나머지는 bad request
def edit(request, reservation_pk):
    reservation = get_object_or_404(Reservation, pk=reservation_pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)  # POST 데이터 담음, instance = 기존 데이터
        if form.is_valid():
            reservation = form.save()
            return redirect('board:detail', reservation.pk)  # redirect(app_name:urls, pk)
    
    # GET 요청 => 사용자한테
    elif request.method == 'GET':
        form = ReservationForm(instance=reservation)
    
    # GET요청이거나 유효성 검사 통과하지 못했다면 여기로
    context = { 'form': form }
    return render(request, 'board/form.html', context)


@require_POST  # POST 요청만 응답, 나머지는 bad request
def delete(request, reservation_pk):
    reservation = get_object_or_404(Reservation, pk=reservation_pk)
    reservation.delete()
    return redirect('board:index')
