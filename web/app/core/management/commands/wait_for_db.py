"""
Django command to WAIT for DB availability.
"""
import time

from psycopg2 import OperationalError as Psycopg2OperError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to WAIT for DB."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('\nWating for DB...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OperError, OperationalError):
                self.stdout.write('DB unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
