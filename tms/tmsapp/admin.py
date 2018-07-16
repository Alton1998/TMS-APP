from django.contrib import admin
from .models import trafficAtD,trafficAtC,trafficAtB,trafficAtA
# Register your models here.
#registring models in django administration 
admin.site.register(trafficAtA)
admin.site.register(trafficAtB)
admin.site.register(trafficAtC)
admin.site.register(trafficAtD)
