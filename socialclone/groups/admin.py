from django.contrib import admin
from . import models
# Register your models here.
class GroupMemberInline(admin.TabularInline):
    model=models.GroupMember
    
class GroupAdmin(admin.ModelAdmin):
    inlines=[GroupMemberInline]
    readonly_fields = ('member',)

admin.site.register(models.Group,GroupAdmin)