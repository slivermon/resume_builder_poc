from django.contrib import admin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Timeline_Event, Timeline_Event_Detail

class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ("user_id", "timeline_start_date", "org_name", "role_name")


class TimelineEventDetailAdmin(admin.ModelAdmin):
    list_display = ("user_id", "timeline_event_id", "content")


admin.site.register(Timeline_Event, TimelineEventAdmin)
admin.site.register(Timeline_Event_Detail, TimelineEventDetailAdmin)
