import random
import datetime
from django.core.management.base import BaseCommand
from core.models import Category, Journal,Author

categories = [
    'Sport',
    'Lifestyle',
    'Music',
    'Coding',
    'Travelling'
]

authors = [
    'John', 'Michael', 'Luke', 'Sally', 'Joe', 'Dude', 'Guy', 'Barbara'
]


def generate_author_name():
    index = random.randrange(0,7)
    return authors[index]

def generate_category():
    index = random.randrange(0,4)
    return categories[index]

def generate_views():
    return random.randrange(0,100)

def generate_is_reviewed():
    res = random.randrange(0,1)
    if res == 0 :
        return False
    return True

def generate_publish_date():
    year = random.randrange(2000,2030)
    month = random.randrange(1,12)
    day = random.randrange(1,28)

    return datetime.date(year,month,day)

class Command(BaseCommand):

    def add_arguments(self, parser):
        # This is the input -> file name
        parser.add_argument(
            'file_name',
            type=str,
            help='This txt file that contains the journal titles'
            ) 
    def handle(self, *args, **options):
        file_name = options['file_name']
        with open(f'{file_name}.txt') as file:
            for row in file:
               title = row 
               author_name= generate_author_name()
               category_name = generate_category()
               publish_date = generate_publish_date()
               views = generate_views()
               reviewed = generate_is_reviewed()

                # Every loop it will create the user if it's need to 
               author = Author.objects.get_or_create(
                   name= author_name
               )

               journal = Journal(
                   title=title,
                   author = Author.objects.get(name=author_name),
                   publish_date=publish_date,
                   views=views,
                   reviewed = reviewed
               )

               journal.save()

               category = Category.objects.get_or_create(
                   name= category_name
               ) 
               
               journal.categories.add(
                   Category.objects.get(name=category_name)
               )

               self.stdout.write(self.style.SUCCESS('Data Imported successfully'))

