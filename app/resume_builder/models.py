from django.db import models
from accounts.models import CustomUser


class Timeline_Event(models.Model):
    '''Base event details share among all timeline events'''
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        db_column="user_id",
    )
    event_add_datetime = models.DateTimeField(null=True)
    timeline_start_date = models.DateField("start date")
    timeline_end_date = models.DateField("end date", null=True, blank=True)
    
    # org_type is one of: company, education
    org_type = models.CharField(max_length=20)

    org_name = models.CharField("company", max_length=50)
    role_name = models.CharField("role", max_length=50)

    def __str__(self):        
        return f"pk: {self.pk}, org: {self.org_name}"

    def get_events(self, user_id):
        return self.objects.filter(user_id)
    
    def is_ended(self):
        '''
        Return bool of timeline_end_date; 
        True means event has ended/completed
        '''
        return Timeline_Event.timeline_end_date


class Timeline_Event_Detail(models.Model):
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="event_details",
        db_column="user_id",
    )
    timeline_event_id = models.ForeignKey(
        Timeline_Event,
        on_delete=models.CASCADE,
        db_column="timeline_event_id",
    )
    content = models.CharField(max_length=1000, null=True, blank=True)    

    def __str__(self):        
        return f"{self.pk}"

    def get_event_detail(self, user_id):
        return self.objects.filter(user_id)
