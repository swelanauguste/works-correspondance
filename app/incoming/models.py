from django.db import models
from django.urls import reverse
from users.models import User


class Action(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Incoming(models.Model):
    subject = models.CharField(max_length=100)
    received = models.DateField(blank=True, null=True)
    dated = models.DateField(blank=True, null=True)
    rfrom = models.CharField(max_length=100, verbose_name="from")
    to = models.CharField(max_length=100, null=True, blank=True)
    cc = models.CharField(max_length=100, null=True, blank=True)
    action = models.ForeignKey(
        Action,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="incoming_action",
    )
    forward = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="incoming_created_by",
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="incoming_updated_by",
    )
    
    class Meta:
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("incoming-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"({self.pk}) {self.subject}"
