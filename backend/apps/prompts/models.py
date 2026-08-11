from django.contrib.auth.models import User
from django.db import models


class Prompt(models.Model):
    CATEGORY_CHOICES = [
        ("coding", "Coding"),
        ("learning", "Learning"),
        ("writing", "Writing"),
        ("research", "Research"),
        ("career", "Career"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="prompts",
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="other",
    )
    tool = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title