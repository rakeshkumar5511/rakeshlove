from django.db import models


class Route(models.Model):
    route_name = models.CharField(max_length=100)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)

    def __str__(self):
        return self.route_name


class Bus(models.Model):
    bus_number = models.CharField(max_length=50)
    driver_name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    assigned_route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.bus_number


class BusLocation(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    speed = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bus.bus_number} - {self.latitude}, {self.longitude}"


class PassengerCount(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    current_count = models.PositiveIntegerField()
    in_count = models.PositiveIntegerField(default=0)
    out_count = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bus.bus_number} - {self.current_count} passengers"