## Run app
1. Create and activate virtual environment (Python >= 3.6)
2. `pip install -r requirements.txt`
3. `python manage.py runserver`

## How to fullfill database?
1. Put `.csv` file with books into `books_for_import` dir (e.g. `ksiazki.csv`)
2. Put `.csv` file with opinions into `books_for_import` dir (e.g. `opinie.csv`) 
3. Run `python manage.py import_books ksiazki.csv` - for import all books into database 
4. Run `python manage.py import_opinions opinie.csv` - for import all opinions into database 

## Usage
http://127.0.0.1:8000/api/books - List of all books \
http://127.0.0.1:8000/api/books?title=abc - Shows all books with `abc` sentence in title \
http://127.0.0.1:8000/api/books?pk=1 - Shows book with id `1` (contains all opinions) 

All results are limited to 20 records
