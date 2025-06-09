from django.core.management.base import BaseCommand
from django.core.management import call_command
import os


class Command(BaseCommand):
    help = 'Load production data from fixture'

    def handle(self, *args, **options):
        fixture_file = 'production_data.json'

        if os.path.exists(fixture_file):
            self.stdout.write('Loading production data...')
            try:
                call_command('loaddata', fixture_file)
                self.stdout.write(
                    self.style.SUCCESS('Production data loaded successfully!')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error loading data: {e}')
                )
        else:
            self.stdout.write(
                self.style.WARNING('No production data file found')
            )
