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

class Commend(BaseCommand):

    def add_arguments(self, parser):
        # This is the input -> file name
        parser.add_argument(
            'file_name',
            type=str,
            help='This txt file that contains the journal titles'
            ) 
    def handle(self, *args: Any, **options: Any):
        file_name = options['file_name']
        with open(f'{file_name}.txt') as file:
            for row in file:
               title = row 
               author= generate_author_name()
               category = generate_category()
               publish_date = generate_publish_date()
               views = generate_views()
               reviewed = generate_is_reviewed()

               print(title,author ,category,publish_date,views,reviewed)