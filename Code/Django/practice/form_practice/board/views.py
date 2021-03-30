from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReservationForm
from django.views.decorators.http import require_GET, require_POST, require_http_methods

@require_GET
def index(request):
    reservations = Reservation.objects.all()
    context = { 'reservations': reservations }
    return render(request, 'board/index.html', context)


@require_http_methods(['GET', 'POST'])
def new(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect('board:detail', reservation.pk)
    
    else:
        form = ReservationForm()

    context = {
        'form': form
    }
    return render(request, 'board/new.html', context)


@require_GET
def detail(request, reservation_pk):
    reservation = get_object_or_404(Reservation, pk=reservation_pk)
    context = { 'reservation': reservation }
    return render(request, 'board/detail.html', context)


@require_http_methods(['GET', 'POST'])
def edit(request, reservation_pk):
    reservation = get_object_or_404(Reservation, id=reservation_pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            reservation = form.save()
            return redirect('board:detail', reservation_pk)

    else:
        form = ReservationForm(instance=reservation)
    context = { 'form':form }
    return render(request, 'board/edit.html', context)


@require_POST
def delete(request, reservation_pk):
    reservation = get_object_or_404(Reservation, id=reservation_pk)
    reservation.delete()
    return redirect('board:index')