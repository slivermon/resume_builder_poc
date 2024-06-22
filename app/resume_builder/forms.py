from datetime import datetime
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget, Textarea
from resume_builder.models import Timeline_Event, Timeline_Event_Detail

# Create the form class using variables from the model
class TimelineForm(ModelForm):
    class Meta:
        model = Timeline_Event
        exclude = [
            "event_add_timeline",
            "user_id",
            "org_type",
        ]
        fields = [
            "org_name",
            "role_name",
            "timeline_start_date",
            "timeline_end_date",            
        ]            

        years = []
        for _ in range(datetime.now().year, 1979, -1):
            years.append(_)

        org_type_list = ["company", "education",]

        widgets = {            
            "timeline_start_date": SelectDateWidget(years=years),
            # "timeline_start_date": DateInput(attrs={'type': 'date', 'format': '%Y-%m'}),
            "timeline_end_date": SelectDateWidget(years=years),            
        }

class TimelineDetailForm(ModelForm):
    class Meta:
        model = Timeline_Event_Detail
        exclude = [
            "timeline_event_id",
            "user_id",
        ]
        fields = [
            "content",                       
        ]         

        widgets = {
            "content": Textarea(),
        }   
