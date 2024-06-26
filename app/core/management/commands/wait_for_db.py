"""Django command to wait for the database to be available """
import time

from typing import Any

from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args: Any, **options: Any):
        """Entrypoint for command"""
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (OperationalError, Psycopg2OpError):
                self.stdout.write("Database unavaiable, \
                                  waiting for 1 second ...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database avaiable!!!"))
