from django.db import models


class Quote(models.Model):
    """Represents a quote, including the text of the quote and its author."""

    text = models.TextField(max_length=1000)
    author = models.CharField(max_length=255, db_index=True)

    class Meta:
        unique_together = (
            "text",
            "author",
        )

    def __str__(self):
        """Returns a string representation of the quote."""
        return f"{self.text} - {self.author}"
