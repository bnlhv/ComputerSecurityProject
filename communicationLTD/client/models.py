from django.db import models
from django.db.models import CharField


class Client(models.Model):
    class DataPackageOptions(models.TextChoices):
        _2GB = "2GB"
        _5GB = "5GB"
        _10GB = "10GB"
        _50GB = "50GB"
        _100GB = "100GB"

    full_name = models.CharField(max_length=50,
                                 default="default_name",
                                 null=True)
    email = models.EmailField(max_length=50,
                              null=True)
    data_package = models.CharField(max_length=5,
                                    choices=DataPackageOptions.choices,
                                    default=DataPackageOptions._2GB)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> CharField:
        return self.full_name


class Sectors(models.Model):
    name = models.CharField(max_length=50,
                            default="default_sector",
                            null=True)
