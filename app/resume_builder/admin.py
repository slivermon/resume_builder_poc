from django.contrib import admin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Timeline_Event, Timeline_Event_Detail

class UserTimelineAdmin(admin.ModelAdmin):
    pass


admin.site.register(Timeline_Event)
admin.site.register(Timeline_Event_Detail)
