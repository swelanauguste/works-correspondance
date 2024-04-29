from django.db import models
from users.models import User
from django.urls import reverse

class Outgoing(models.Model):
    date_typed = models.DateField(blank=True, null=True)
    out_date = models.DateField(blank=True, null=True, verbose_name="outgoing date")
    out_from = models.CharField(max_length=100, verbose_name="from")
    to = models.CharField(max_length=100, verbose_name="to")
    subject = models.CharField(max_length=255)
    cc = models.CharField(max_length=100, null=True, blank=True)
    hand = models.BooleanField(default=False, verbose_name="hand delivery")
    r_mail = models.BooleanField(default=False, verbose_name="regular mail")
    notes = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="outgoing/files/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="outgoing_created_by",
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="outgoing_updated_by",
    )

    class Meta:
        ordering = ["-out_date"]

    def get_absolute_url(self):
        return reverse("outgoing-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"({self.pk}) {self.subject}"
