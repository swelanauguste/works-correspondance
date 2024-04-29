from django.db import models
from django.urls import reverse
from users.models import User


class Incoming(models.Model):
    subject = models.CharField(max_length=255, null=True)
    received = models.DateField(blank=True, null=True)
    dated = models.DateField(blank=True, null=True)
    rfrom = models.CharField(max_length=100, verbose_name="from")
    to = models.CharField(max_length=100, null=True, blank=True)
    cc = models.CharField(max_length=100, null=True, blank=True)
    action = models.CharField(max_length=255, null=True, blank=True)
    forward = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="incoming/files/", blank=True, null=True)
    date = models.DateField(blank=True, null=True)
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
        ordering = ["-received", "subject"]

    def get_absolute_url(self):
        return reverse("incoming-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"({self.pk}) {self.subject}"
