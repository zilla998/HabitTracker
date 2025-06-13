from django.contrib.auth.models import User
from django.db import models


class Habit(models.Model):
    choices_period = [
        ('daily', 'Ежедневная'),
        ('weekly', 'Еженедельная'),
        ('monthly', 'Ежемесячная'),
        ('yearly', 'Ежегодная'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(verbose_name="Название привычки")
    description = models.CharField(blank=True, null=True, verbose_name="Описание (необяз.)")
    period = models.CharField(choices=choices_period, verbose_name="Периодичность")
    start_date = models.DateField(verbose_name="Дата начала")
    is_active = models.BooleanField(verbose_name="Активна/неактивна", default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"{self.title} ({self.period})"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"


class HabitRecord(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, verbose_name="Привычка")
    date = models.DateField(verbose_name="Дата")
    done = models.BooleanField(verbose_name="Выполнено (да/нет)", default=False)
    comment = models.CharField(blank=True, null=True, verbose_name="Комментарий (необяз.)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ['-date']
