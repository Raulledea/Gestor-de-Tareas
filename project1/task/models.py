from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    realized = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Si se marca como realizada y no tenía fecha de completado
        if self.realized and self.completed_at is None:
            self.completed_at = timezone.now()

        # Si se desmarca como realizada, limpiamos la fecha
        if not self.realized:
            self.completed_at = None

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
