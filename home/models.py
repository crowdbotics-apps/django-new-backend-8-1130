from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    r2 = models.BigIntegerField(null=True, blank=True,)
    r3 = models.BigIntegerField(null=True, blank=True,)
    r4 = models.ForeignKey(
        "home.HomePage",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="customtext_r4",
    )
    r5 = models.OneToOneField(
        "home.HomePage1",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="customtext_r5",
    )
    r6 = models.ManyToManyField(
        "home.NursingInstruction", null=True, blank=True, related_name="customtext_r6",
    )

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
    r2 = models.BigIntegerField(null=True, blank=True,)
    r3 = models.BigIntegerField(null=True, blank=True,)

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
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="homepage1_r1",
    )


class NursingInstruction(models.Model):
    "Generated Model"
    name = models.CharField(max_length=255,)
    key_word = models.CharField(blank=True, max_length=255,)
    r3 = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="nursinginstruction_r3",
    )


class R1x(models.Model):
    "Generated Model"
    r1 = models.ForeignKey(
        "home.CustomText", on_delete=models.CASCADE, related_name="r1x_r1",
    )
    r2 = models.BigIntegerField()
    r3 = models.BigIntegerField()
    r4 = models.OneToOneField(
        "home.NursingInstruction", on_delete=models.CASCADE, related_name="r1x_r4",
    )
    r5 = models.ManyToManyField("home.HomePage", related_name="r1x_r5",)


class R2d2(models.Model):
    "Generated Model"
    r1 = models.ForeignKey(
        "home.HomePage", on_delete=models.CASCADE, related_name="r2d2_r1",
    )
    r2 = models.OneToOneField(
        "home.CustomText", on_delete=models.CASCADE, related_name="r2d2_r2",
    )
    r3 = models.ManyToManyField("home.HomePage1", related_name="r2d2_r3",)


class RX2(models.Model):
    "Generated Model"
    r1 = models.CharField(max_length=23,)
    r2 = models.DecimalField(max_digits=31, decimal_places=11,)
    r3 = models.ForeignKey(
        "home.CustomText",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="rx2_r3",
    )
    r4 = models.OneToOneField(
        "home.Ghh",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="rx2_r4",
    )
    r5 = models.ManyToManyField(
        "home.HomePage", blank=True, null=True, related_name="rx2_r5",
    )


class RX3(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()
    r2 = models.BigIntegerField(null=True, blank=True,)
    r3 = models.DecimalField(null=True, blank=True, max_digits=30, decimal_places=10,)
    r4 = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="rx3_r4",
    )
    r41 = models.OneToOneField(
        "home.R1x",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="rx3_r41",
    )
    r5 = models.ManyToManyField(
        "home.R2d2", null=True, blank=True, related_name="rx3_r5",
    )


class Ghh(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()
    r2 = models.ManyToManyField("home.RX3", related_name="ghh_r2",)
