from django.db import models

class imagedata(models.Model):
    filename = models.CharField(max_length=70, help_text="Image File Name")
    object_name = models.CharField(max_length=50, help_text="Name of the Object")
    xmin = models.IntegerField(help_text="Minimum X co-ordinate")
    ymin = models.IntegerField(help_text="Minimum Y co-ordinate")
    xmax = models.IntegerField(help_text="Maximum X co-ordinate")
    ymax = models.IntegerField(help_text="Maximum Y co-ordinate")
    timestamp = models.DateField(auto_now_add=True,help_text="Timestamp")

    def __str__(self):
        return self.filename