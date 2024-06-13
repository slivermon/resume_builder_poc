from datetime import datetime
from django.forms import ModelForm
from django.forms.widgets import ChoiceWidget, SelectDateWidget
from resume_builder.models import Timeline_Event

# Create the form class using variables from the model
class TimelineForm(ModelForm):
    class Meta:
        model = Timeline_Event
        # exclude = ()
        fields = [
            "org_type",
            "org_name",
            "role_name",
            "timeline_start_date",
            "timeline_end_date",
        ]

        
        years = []
        for _ in range(datetime.now().year, 1979, -1):
            years.append(_)

        widgets = {
            "timeline_start_date": SelectDateWidget(years=years),
            "timeline_end_date": SelectDateWidget(years=years),
            # "org_type": ChoiceWidget(
            #     allow_multiple_selected=False,
            #     choice=["company", "education"],
            # ),
        }
