from django.contrib import admin
from .models import *

class LabParameterInline(admin.TabularInline):
    model = LabParameter

class LabAdmin(admin.ModelAdmin):
    inlines = [
        LabParameterInline,
    ]

class LabTypeMetaparameterInline(admin.TabularInline):
    model = LabTypeMetaparameter

class LabTypeAdmin(admin.ModelAdmin):
    inlines = [
        LabTypeMetaparameterInline,
    ]

admin.site.register(Lab, LabAdmin)
admin.site.register(LabParameter)
admin.site.register(LabType, LabTypeAdmin)
admin.site.register(LabTypeMetaparameter)
admin.site.register(SSHKey)
admin.site.register(StaffRegistration)
admin.site.register(StudentRegistration)


