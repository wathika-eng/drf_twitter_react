# File: your_app/management/commands/populate_advocates.py
from django.core.management.base import BaseCommand
from django.db import connection, transaction
from faker import Faker
from drfapi.models import Advocate, Company

fake = Faker()


class Command(BaseCommand):
    help = "Populate Advocate and Company models with fake data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        # Clear existing data
        Advocate.objects.all().delete()
        Company.objects.all().delete()

        # Reset the primary key sequence
        with connection.cursor() as cursor:
            if connection.vendor == "postgresql":
                cursor.execute("ALTER SEQUENCE drfapi_advocate_id_seq RESTART WITH 1;")
                cursor.execute("ALTER SEQUENCE drfapi_company_id_seq RESTART WITH 1;")
            elif connection.vendor == "sqlite":
                cursor.execute(
                    "UPDATE sqlite_sequence SET seq = 0 WHERE name = 'drfapi_advocate';"
                )
                cursor.execute(
                    "UPDATE sqlite_sequence SET seq = 0 WHERE name = 'drfapi_company';"
                )
            # Add other database backends as needed

        # Create fake data
        for _ in range(5):
            company_name = fake.company()
            company_bio = (
                fake.text(max_nb_chars=40)
                if fake.boolean(chance_of_getting_true=70)
                else None
            )
            company = Company.objects.create(name=company_name, bio=company_bio)

            username = fake.user_name()
            advocate_bio = (
                fake.text(max_nb_chars=40)
                if fake.boolean(chance_of_getting_true=70)
                else None
            )
            Advocate.objects.create(
                username=username, bio=advocate_bio, company=company
            )

        self.stdout.write(self.style.SUCCESS("Successfully populated the DB!"))
