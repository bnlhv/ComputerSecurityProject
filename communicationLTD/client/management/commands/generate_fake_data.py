import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'communicationLTD.settings')

import django

django.setup()

from django.core.management import BaseCommand
from faker import Faker
from faker.providers import BaseProvider

from communicationLTD.client import models


class DataPackageProvider(BaseProvider):
    def data_package(self) -> str:
        return self.random_element(models.Client.PACKAGES)


class Command(BaseCommand):
    help = "run this for population"

    def handle(self, *args, **options):
        """ Handle population of data """
        fake = Faker()
        fake.seed(0)
        for i in range(5):
            sector = models.Sectors.objects.create(name=fake.company())
            client = models.Client.objsects.create(
                full_name=fake.name(),
                email=fake.ascii_email(),
                date_created=fake.date_object(),
                data_package=DataPackageProvider.data_package(),
                sectors=sector
            )
            self.stdout.write(self.style.SUCCESS(f"Created {client}"))
