# import_data_excel.py
from datetime import datetime

import pandas as pd
from django.core.management.base import BaseCommand

from ...models import Incoming  # Update with your app name


class Command(BaseCommand):
    help = "Import data from Excel file to Incoming model"
    Incoming.objects.all().delete()

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to the Excel file")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        df = pd.read_excel(file_path)

        # for index, row in df.head(5).iterrows():
        for index, row in df.iterrows():

            lettdate = row.get("LETTDATE")

            if isinstance(lettdate, datetime):
                lettdate_obj = lettdate
            elif lettdate and isinstance(lettdate, str):
                lettdate_obj = datetime.strptime(lettdate, "%d-%b-%y")
            else:
                lettdate_obj = None

            date = row.get("DATE")

            if isinstance(date, datetime):
                date_obj = date
            elif date and isinstance(date, str):
                date_obj = datetime.strptime(date, "%d-%b-%y")
            else:
                date_obj = None

            date_received = row.get("DATE RECEIVED")

            if isinstance(date_received, datetime):
                date_received_obj = date_received
            elif date_received and isinstance(date_received, str):
                date_received_obj = datetime.strptime(date_received, "%d-%b-%y")
            else:
                date_received_obj = None

            incoming, created = Incoming.objects.get_or_create(
                subject=row.get("SUBJECT"),
                received=date_received_obj,
                dated=lettdate_obj,
                rfrom=row.get("FROM"),
                to=row.get("TO_WHOM"),
                action=row.get("ACTION"),  # Directly assign action as CharField
                forward=row.get("FORWARD"),
                date=date_obj,
                # Add other fields as necessary
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added {incoming}"))
            else:
                self.stdout.write(self.style.WARNING(f"{incoming} already exists"))

        self.stdout.write(self.style.SUCCESS("Data imported successfully"))
