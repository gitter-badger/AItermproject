from django.contrib import admin
from polls.models import *
from django.contrib.auth.models import User

class ActivityInline(admin.StackedInline):
    model = Activity
    extra = 1

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Comment',          {'fields': ['comment']}),
        ('Date information', {'fields': ['pub_date','deadline_date'], 'classes': ['collapse']}),

    ]
    list_display = ('title', 'comment' ,'pub_date', 'deadline_date')
    list_filter = ['pub_date']
    list_filter = ['deadline_date']
    search_fields = ['title']
    inlines = [ActivityInline]

class DayInline(admin.StackedInline):
    model = Day
    extra = 1

class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title','poll']}),
        ('Description',      {'fields': ['description']}),
        ('Time duration',    {'fields': ['time_duration_hours']}),

    ]
    list_display = ('title','poll' ,'description' ,'time_duration_hours')
    list_filter = ['poll']
    inlines = [DayInline]

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Poll, PollAdmin)