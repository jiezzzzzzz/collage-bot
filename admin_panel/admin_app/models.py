from django.db import models


class Theme(models.Model):
    theme_name = models.CharField(max_length=200)
    text = models.TextField(
        verbose_name='explanatory text'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='receiving time'
    )

    class Meta:
        verbose_name = 'theme'
