"""Checklist-related models."""
from django.db import models


# Create your models here.

class Item(models.Model):
    """An item on a checklist."""
    item_text = models.CharField(max_length=200)
