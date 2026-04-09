from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bus, BusLocation, PassengerCount
from .forms import BusLocationForm, PassengerCountForm


def dashboard(request):
    buses = Bus.objects.all()
    selected_bus = None
    latest_location = None
    latest_passenger = None

    bus_id = request.GET.get('bus')

    if bus_id:
        selected_bus = Bus.objects.filter(id=bus_id).first()

        if selected_bus:
            latest_location = BusLocation.objects.filter(bus=selected_bus).order_by('-timestamp').first()
            latest_passenger = PassengerCount.objects.filter(bus=selected_bus).order_by('-timestamp').first()

    context = {
        'buses': buses,
        'selected_bus': selected_bus,
        'latest_location': latest_location,
        'latest_passenger': latest_passenger,
    }

    return render(request, 'dashboard.html', context)


def update_location(request):
    if request.method == 'POST':
        form = BusLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BusLocationForm()

    return render(request, 'update_location.html', {'form': form})


def update_passenger(request):
    if request.method == 'POST':
        form = PassengerCountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PassengerCountForm()

    return render(request, 'update_passenger.html', {'form': form})


def driver_tracking(request):
    buses = Bus.objects.all()
    return render(request, 'driver_tracking.html', {'buses': buses})


def auto_save_location(request):
    if request.method == 'POST':
        bus_id = request.POST.get('bus')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        speed = request.POST.get('speed', 0)

        bus = Bus.objects.filter(id=bus_id).first()

        if bus and latitude and longitude:
            try:
                BusLocation.objects.create(
                    bus=bus,
                    latitude=float(latitude),
                    longitude=float(longitude),
                    speed=float(speed) if speed else 0
                )
                return HttpResponse("Location Saved")
            except Exception as e:
                return HttpResponse(f"Error: {str(e)}")

    return HttpResponse("Failed")