from django.contrib import admin
from TestModel.models import Test,Contact,Tag

class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    #fields = ('name','email')
    list_display = ('name','age', 'email') # list
    search_fields = ('name',)
    inlines = [TagInline] #Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
admin.site.register([Tag])

# Register your models here.
