from django.db import models


class Announcement(models.Model):
    """An announcement to broadcast to the community."""

    title = models.CharField(max_length=128)
    description = models.TextField()
    expires_at = models.DateTimeField(db_index=True)

    class Meta:
        ordering = ["-expires_at"]

    def __str__(self):
        return self.title
