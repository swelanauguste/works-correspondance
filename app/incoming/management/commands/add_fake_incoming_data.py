import random
from datetime import datetime

from django.core.management.base import BaseCommand
from faker import Faker
from users.models import User

from ...models import Action, Incoming


class Command(BaseCommand):
    help = "Adds fake incoming correspondence to the database."

    def add_arguments(self, parser):
        parser.add_argument(
            "number",
            type=int,
            help="Number of fake incoming correspondences to create.",
        )

    def handle(self, *args, **options):
        number = options["number"]
        fake = Faker()
        actions = list(Action.objects.all())
        users = list(User.objects.all())

        if not actions:
            self.stdout.write(
                self.style.ERROR("No actions found. Please add some actions first.")
            )
            return

        if not users:
            self.stdout.write(
                self.style.ERROR("No users found. Please add some users first.")
            )
            return

        for _ in range(number):
            incoming = Incoming.objects.create(
                subject=fake.sentence(),
                received=fake.date_between(start_date="-1y", end_date="today"),
                dated=fake.date_between(start_date="-2y", end_date="-1y"),
                rfrom=fake.company(),
                to=fake.company(),
                cc=fake.company() if random.choice([True, False]) else "",
                action=random.choice(actions),
                forward=fake.name() if random.choice([True, False]) else "",
                notes=fake.text(),
                created_at=fake.date_time_between(start_date="-1y", end_date="now"),
                updated_at=fake.date_time_between(start_date="-1y", end_date="now"),
                created_by=random.choice(users),
                updated_by=random.choice(users),
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully added fake incoming correspondence: {incoming}"
                )
            )
