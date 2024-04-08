from django.contrib import admin

from .models import BugReport, FeatureRequest


@admin.action(description='Mark selected New')
def make_new(modeladmin, request, queryset):
    queryset.update(status='New')


@admin.action(description='Mark selected In_progress')
def make_in_progress(modeladmin, request, queryset):
    queryset.update(status='In_progress')


@admin.action(description='Mark selected Completed')
def make_completed(modeladmin, request, queryset):
    queryset.update(status='Completed')


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'update_at')
    list_filter = ('title', 'project', 'task', 'status', 'priority')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'update_at')
    fieldsets = (
        ("Описание", {'fields': ('title', 'description')}),
        ("Уточнение", {'fields': ('project', 'task', 'status', 'priority')}),
        ("Служебное", {'fields': ('created_at', 'update_at')})
    )

    actions = [make_new, make_in_progress, make_completed]


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'update_at')
    list_filter = ('title', 'project', 'task', 'status', 'priority')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'update_at')
    fieldsets = (
        ("Описание", {'fields': ('title', 'description')}),
        ("Уточнение", {'fields': ('project', 'task', 'status', 'priority')}),
        ("Служебное", {'fields': ('created_at', 'update_at')})
    )
