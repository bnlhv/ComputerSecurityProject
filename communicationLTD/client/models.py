from django.db import models
from django.db.models import CharField


class Sectors(models.Model):
    name = models.CharField(max_length=50,
                            default="default_sector",
                            null=True)

    def __str__(self) -> CharField:
        return self.name


class Client(models.Model):
    PACKAGES = (
        ("2GB", "2GB"),
        ("5GB", "5GB"),
        ("10GB", "10GB"),
        ("50GB", "50GB"),
        ("100GB", "100GB"),
    )
    full_name = models.CharField(max_length=50,
                                 default="default_name",
                                 null=True)
    email = models.EmailField(max_length=50,
                              null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    data_package = models.CharField(max_length=5,
                                    null=True,
                                    choices=PACKAGES)
    sectors = models.ManyToManyField(Sectors, related_name="sectors")

    def __str__(self) -> CharField:
        return self.full_name
