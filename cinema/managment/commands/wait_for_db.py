from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("waiting db to be ready...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                self.stdout.write(self.style.SUCCESS("db available"))
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
