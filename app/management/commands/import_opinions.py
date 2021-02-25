import csv
from django.shortcuts import get_object_or_404
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from django.conf import settings
from app.models import Book, Opinion


class Command(BaseCommand):
    help = "Reads opinions from indicated csv file and writes it's fields to the database - if they don't exist. Use: 'python manage.py import_opinions opinions.csv'"

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help="Indicate directory with opinions for convert them to database.")

    def handle(self, *args, **options):

        file = options['file']
        csv_dir = f'{settings.BASE_DIR}/books_for_import/{file}'

        with open(csv_dir, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader)
            for row in reader:
                try:
                    opinion_exists = Opinion.objects.get(Q(description=row[2]) & Q(isbn=int(row[0])))
                except Opinion.DoesNotExist:
                    opinion_exists = None

                if not opinion_exists:
                    book = get_object_or_404(Book, isbn=int(row[0]))
                    Opinion.objects.create(
                        book=book,
                        rate=row[1] if row[1] else None,
                        description=row[2] if row[2] else None,
                        isbn=row[0] if row[0] else None,
                    )
                    print('Added new opinion to db.')
                else:
                    print('Opinion actually exists in db.')
