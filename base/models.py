from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    patient_id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=20, blank=True, null=True)
    initials = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=1)
    address = models.CharField(max_length=30, blank=True, null=True)
    post_code = models.CharField(max_length=6, blank=True, null=True)
    admission = models.DateField(blank=True, null=True)
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    ward = models.ForeignKey('Ward', models.DO_NOTHING, blank=True, null=True)
    pat_next_kin = models.CharField(db_column='PAT_NEXT_KIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    # updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True, blank=True, null=True)

    def __str__ (self):
        return self.name

    class Meta:
        # ordering = ['-updated','-created']
        managed = False
        db_table = 'patient'

    


class Ward(models.Model):
    ward_id = models.CharField(primary_key=True, max_length=4)
    ward_name = models.CharField(max_length=25, blank=True, null=True)
    number_beds = models.IntegerField(blank=True, null=True)
    nurse_in_charge = models.CharField(max_length=20)
    ward_type = models.CharField(max_length=20, blank=True, null=True)

    def __str__ (self):
        return self.ward_id

    class Meta:
        managed = False
        db_table = 'ward'
