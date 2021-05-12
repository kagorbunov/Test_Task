from django.contrib import admin

from .models import step, priority, todo


admin.site.register(step)
admin.site.register(priority)
admin.site.register(todo)
