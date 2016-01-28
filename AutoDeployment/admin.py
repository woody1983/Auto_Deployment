from django.contrib import admin
from AutoDeployment.models import Deploy

class DeployAdmin(admin.ModelAdmin):
    #fields = ('name','email')
    list_display = ('RFC_Number','RFC_STATUS', 'Modify_Time','Deploy_Date','Deploy_Server','Change_Type') # list
    search_fields = ('RFC_Number',)
    #inlines = [TagInline] #Inline
    fieldsets = (
        ['Main',{
            'fields':('RFC_Number','RFC_STATUS', 'Deploy_Date','Deploy_Server','RFC_SQL'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('Change_Type',),
        }]
    )

admin.site.register(Deploy, DeployAdmin)
#from AutoDeployment import Test

# Register your models here.

#admin.site.register(Test)
