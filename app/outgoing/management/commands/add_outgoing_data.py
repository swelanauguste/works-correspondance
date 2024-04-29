# import_data_excel.py
from datetime import datetime

import pandas as pd
from django.core.management.base import BaseCommand

from ...models import Outgoing  # Update with your app name


class Command(BaseCommand):
    help = "Import data from Excel file to Outgoing model"
    # Incoming.objects.all().delete()

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to the Excel file")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        df = pd.read_excel(file_path)

        # for index, row in df.head(5).iterrows():
        for index, row in df.iterrows():

            date_typed = row.get("TYPED")
            if isinstance(date_typed, datetime):
                date_typed_obj = date_typed
            elif date_typed and isinstance(date_typed, str):
                date_typed_obj = datetime.strptime(date_typed, "%d-%b-%y")
            else:
                date_typed_obj = None

            out_date = row.get("out_date")
            if isinstance(out_date, datetime):
                out_date_obj = out_date
            elif out_date and isinstance(out_date, str):
                out_date_obj = datetime.strptime(out_date, "%d-%b-%y")
            else:
                out_date_obj = None

            outgoing, created = Outgoing.objects.get_or_create(
                out_date=out_date_obj,
                date_typed=date_typed_obj,
                out_from=row.get("FROM"),
                to=row.get("TO"),
                subject=row.get("SUBJECT"),
                cc=row.get("CC"),
                hand=row.get("hand"),  # Directly assign action as CharField
                r_mail=row.get("mail"),
                # Add other fields as necessary
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added {outgoing}"))
            else:
                self.stdout.write(self.style.WARNING(f"{outgoing} already exists"))

        self.stdout.write(self.style.SUCCESS("Data imported successfully"))
