from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(RequestTable)
admin.site.register(ReviewTable)
admin.site.register(OrderTable)
admin.site.register(CartTable)
