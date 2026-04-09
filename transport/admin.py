from django.contrib import admin
from .models import Route, Bus, BusLocation, PassengerCount

admin.site.register(Route)
admin.site.register(Bus)
admin.site.register(BusLocation)
admin.site.register(PassengerCount)