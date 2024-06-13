from django.forms import ModelForm, inlineformset_factory
from resume_builder.models import Timeline_Event, Timeline_Event_Detail

# Create the form class using variables from the model
class TimelineForm(ModelForm):
    class Meta:
        model = Timeline_Event_Detail
        exclude = ()
        # fields = [
        #     "org_type",
        #     "org_name",
        #     "role_name",
        #     "timeline_start_date",
        #     "timeline_end_date",
        # ]

# Create a form using the model
form = inlineformset_factory(Timeline_Event, Timeline_Event_Detail, form=TimelineForm)

# Create form to edit timeline
# timeline = Timeline_Event.objects.get(user_id=session.user.id)
# form = TimelineForm(instance=timeline)