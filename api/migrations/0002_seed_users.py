from django.db import migrations
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
import random

def create_seed_data(apps, schema_editor):
    User = get_user_model()
    Loan = apps.get_model('api', 'Loan')
    Document = apps.get_model('api', 'Document')

    # Function to create a random user
    def create_random_user(role):
        username = get_random_string(length=7)
        user = User.objects.create_user(
            username=username,
            email=f'{username}@example.com',
            password='defaultpassword',
            role=role,
            phone_number='1234567890',
            address='123 Main St, Anytown, USA'
        )
        return user

    # Create multiple lenders and borrowers
    lenders = [create_random_user('lender') for _ in range(10)]
    borrowers = [create_random_user('borrower') for _ in range(10)] 

    # Function to create a random loan
    def create_random_loan(borrower, lender):
        loan = Loan.objects.create(
            amount=random.randint(50000, 500000),
            interest_rate=random.choice([3.5, 4.0, 4.5, 5.0, 5.5]),
            start_date='2024-01-01',
            due_date='2029-01-01',
            borrower_id=borrower.id,
            lender_id=lender.id,
            criteria={'max_loan_to_value_ratio': random.choice([70, 75, 80, 85]), 'min_credit_score': random.choice([650, 680, 700, 720])}
        )
        return loan

    # Create loans for each pair of lenders and borrowers
    loans = [create_random_loan(random.choice(borrowers), random.choice(lenders)) for _ in range(20)]

    # Function to create a random document
    def create_random_document(loan):
        document = Document.objects.create(
            document_type=random.choice(['Mortgage Agreement', 'Occupancy Permit', 'Title']),
            document_url=f'http://example.com/doc/{get_random_string(length=12)}.pdf',
            description='A document related to financial transaction.',
            loan_id=loan.id
        )
        return document

    # Create documents for each loan
    documents = [create_random_document(loan) for loan in loans]

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_seed_data),
    ]