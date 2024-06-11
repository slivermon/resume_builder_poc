from django.db import models
from accounts.models import CustomUser


class Timeline_Event(models.Model):
    '''Base event details share among all timeline events'''
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event_add_datetime = models.DateTimeField("datetime event added to timeline")
    timeline_start_date = models.DateField("start date")
    timeline_end_date = models.DateField("end date", null=True)
    
    # org_type is one of: company, education
    org_type = models.CharField(max_length=20)

    org_name = models.CharField(max_length=50)
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{user_id}: {org_name}, {role_name}, {org_type}, {timeline_start_date}"

    def get_events(self, user_id):
        return self.objects.filter(user_id)
    
    def is_ended(self):
        '''Return bool of timeline_end_date; True means event has ended/completed'''
        return Timeline_Event.timeline_end_date


class Timeline_Event_Detail(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timeline_event_id = models.ForeignKey(Timeline_Event, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000, null=True, blank=True)
    degree = models.CharField(max_length=20, null=True, blank=True)
    # TODO: Implement order for content
    # display_rank = models.CharField(max_length=5)

    def __str__(self):
        return f"{user_id}: {timeline_event_id}, {content}, {degree}"

    def get_event_detail(self, user_id):
        return self.objects.filter(user_id)

    # TODO: Implement rank changing to allow user ordering of details
    # def rank_change(self, lower_detail_id, upper_detail_id):
    #     pass