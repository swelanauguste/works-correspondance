from django.db import models

class Outgoing(models.Model):
    subject = models.CharField(max_length=100)
    sent = models.DateField(blank=True, null=True)
    dated = models.DateField(blank=True, null=True)
    rfrom = models.CharField(max_length=100, verbose_name="from")
    to = models.CharField(max_length=100, null=True, blank=True)
    cc = models.CharField(max_length=100, null=True, blank=True)
    action = models.ForeignKey(
        Action,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="outgoing_action",
    )
    forward = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(blank=True)
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
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("outgoing-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"({self.pk}) {self.subject}"
