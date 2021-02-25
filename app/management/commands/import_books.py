import csv
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from app.models import Book


class Command(BaseCommand):
    help = "Reads books from indicated csv file and writes it's fields to the database - if they don't exist. Use: 'python manage.py import_books books.csv'"

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help="Indicate directory with books for convert them to database.")

    def handle(self, *args, **options):

        file = options['file']
        csv_dir = f'{settings.BASE_DIR}/books_for_import/{file}'

        with open(csv_dir, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader)
            for row in reader:
                try:
                    book_exists = Book.objects.get(isbn=row[0])
                except Book.DoesNotExist:
                    book_exists = None

                if not book_exists:
                    Book.objects.create(
                        author=row[2] if row[2] else None,
                        title=row[1] if row[1] else None,
                        type=row[3] if row[3] else None,
                        isbn=row[0] if row[0] else None,
                    )
                    print('Added new book to db.')
                else:
                    print('Book actually exists in db.')
