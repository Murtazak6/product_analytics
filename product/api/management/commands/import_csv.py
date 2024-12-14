import csv
from django.core.management.base import BaseCommand
from api.models import Product

class Command(BaseCommand):
    help = 'Import products from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        products = []
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    if float(row['price']) < 0 or int(row['stock']) < 0:

                        continue  # Validation: Skip invalid rows
                    products.append(Product(
                        id=row['id'],
                        name=row['name'],
                        category=row['category'],
                        price=float(row['price']),
                        stock=int(row['stock']),
                        created_at=row['created_at']
                    ))
                except (ValueError, KeyError):
                    continue  # Handle missing/invalid data gracefully
        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS('Successfully imported data'))
