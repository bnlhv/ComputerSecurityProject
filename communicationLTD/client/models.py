from django.db import models
from django.db.models import CharField


class DataPackage(models.Model):
    class DataPackageOptions(models.TextChoices):
        _2GB = "2GB"
        _5GB = "5GB"
        _10GB = "10GB"
        _50GB = "50GB"
        _100GB = "100GB"

    package_size = models.CharField(max_length=5,
                                    choices=DataPackageOptions.choices,
                                    default=DataPackageOptions._2GB)


class Sectors(models.Model):
    name = models.CharField(max_length=50,
                            default="default_sector",
                            null=True)


class Client(models.Model):
    full_name = models.CharField(max_length=50,
                                 default="default_name",
                                 null=True)
    email = models.EmailField(max_length=50,
                              null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    data_package = models.ForeignKey(DataPackage, null=True, on_delete=models.SET_NULL)
    sectors = models.ManyToManyField(Sectors)

    def __str__(self) -> CharField:
        return self.full_name
