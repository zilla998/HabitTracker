from django.contrib import admin

from api.models import Habit, HabitRecord


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    fields = ('id', 'user', 'title', 'description', 'period', 'start_date', 'is_active')


@admin.register(HabitRecord)
class HabitRecordAdmin(admin.ModelAdmin):
    fields = ('habit', 'date', 'done')