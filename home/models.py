from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    r2 = models.BigIntegerField(blank=True, null=True,)
    r3 = models.BigIntegerField(blank=True, null=True,)

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class HomePage1(models.Model):
    "Generated Model"
    body = models.TextField()
    r1 = models.ForeignKey(
        "home.HomePage",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="homepage1_r1",
    )


class NursingInstruction(models.Model):
    "Generated Model"
    name = models.CharField(max_length=255,)
    key_word = models.CharField(blank=True, max_length=255,)
    r3 = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="nursinginstruction_r3",
    )
