from django.db import models

class SurveyResponse(models.Model):
    gender = models.CharField(max_length=20)
    age_group = models.CharField(max_length=20)
    occupation = models.CharField(max_length=50)

    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    trip_purpose = models.CharField(max_length=50)
    transport_mode = models.CharField(max_length=50)

    travel_time = models.CharField(max_length=50)
    travel_cost = models.CharField(max_length=50)

    safety_level = models.CharField(max_length=50)

    experienced_harassment = models.CharField(max_length=10)
    harassment_type = models.CharField(max_length=50, blank=True)

    unsafe_time = models.CharField(max_length=50)
    unsafe_location = models.CharField(max_length=100)

    recommendation = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.gender} - {self.transport_mode}"