from django.db import models
from django.contrib.auth.models import User

__all__ = [
    'Lab',
    'LabParameter',
    'LabType',
    'LabTypeMetaparameter',
    'SSHKey',
    'StaffRegistration',
    'StudentRegistration',
    'User',
]

class SSHKey(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=128)
    fingerprint = models.CharField(max_length=48)
    public_key = models.TextField()

class Lab(models.Model):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    maximum_students = models.IntegerField()
    start_date = models.DateTimeField()
    lab_type = models.ForeignKey('LabType')
    
class LabType(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128, unique=True)
    display_name = models.CharField(max_length=128)
    implementation_class = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.display_name

class LabTypeMetaparameter(models.Model):
    types = (
        ('INT', 'Integer'),
        ('STR', 'String'),
        ('BOOL', 'Boolean'),
    )
    lab_type = models.ForeignKey(LabType, related_name='metaparameters')
    name = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    parameter_type = models.CharField(max_length=16, choices=types)

    def __str__(self):
        return "%s.%s" % (self.lab_type.name, self.name)

class LabParameter(models.Model):
    # Parent cannot be named check because of Djangos ORM wanting to map the
    # `Lab` model to a `check()` method to this object when mapping
    # its relationships.
    parent = models.ForeignKey(Lab, related_name='parameters')
    meta = models.ForeignKey(LabTypeMetaparameter, related_name='+')
    updated_at = models.DateTimeField(auto_now=True)
    value = models.TextField()

    @property
    def name(self):
        return self.meta.name

    # TODO LabParameter.parent's ForeignKey def can accept limit_choices_to
    # but we don't have any context to correctly limit the choices.  If we
    # have access to self, this is what we'd want:
    #
    # def parent_limiter(self):
    #     return LabTypeMetaparameter.objects.filter(check_type_id=parent.check_type.id)

    def __str__(self):
        return str(self.name)

class StaffRegistration(models.Model):
    user = models.ForeignKey(User)
    lab = models.ForeignKey(Lab)

class StudentRegistration(models.Model):
    status_codes = (
        ('active', 'Active'),
        ('complete', 'Complete'),
        ('new', 'New'),
        ('waitlist', 'Wait list'),
        ('withdrawn', 'Withdrawn'),
    )

    user = models.ForeignKey(User)
    lab = models.ForeignKey(Lab)
    registration_date = models.DateTimeField()
    status = models.CharField(choices=status_codes, max_length=128, default='new')

