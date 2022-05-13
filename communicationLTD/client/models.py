from datetime import datetime
from typing import List, Any

from django.db import models, connection
from django.db.models import CharField


def create_client_with_sqli_demonstration(full_name: str,
                                          email: str,
                                          data_package: str,
                                          sectors: List) -> Any:
    """ Bypass the ORM and execute raw sql query directly to th database """
    create_query = "INSERT INTO clients(full_name, email, date_created, " \
                   "data_package) VALUES (%s, %s, %s, %s);"
    fetch_query = "SELECT * FROM clients WHERE full_name = %s;"
    with connection.cursor() as cursor:
        cursor.execute(create_query, [full_name, email, data_package, datetime.now()])
        cursor.execute(fetch_query, [full_name])
        row = cursor.fetchall()
        print(row)

    return row


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
    sectors = models.ManyToManyField(Sectors,
                                     default=None,
                                     related_name="sectors")

    class Meta:
        db_table = "clients"

    def __str__(self) -> CharField:
        return self.full_name
