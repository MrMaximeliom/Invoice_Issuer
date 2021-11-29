from django.contrib import admin
from .models import Country,State,City
# Register Country,City and State data models to admin dashboard
admin.site.register(Country)
admin.site.register(City)
admin.site.register(State)