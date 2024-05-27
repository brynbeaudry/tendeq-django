from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Custom user model manager
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.create_user(
            username, email, password, **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom user model
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=50)  # Roles like 'lender', 'broker', 'borrower', 
    password_hash = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'user'  # Explicitly set table name


def default_criteria():
    return {'max_loan_to_value_ratio': 80, 'min_credit_score': 680}

# Loan model
class Loan(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    due_date = models.DateField()
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrower_loans')
    lender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lender_loans')
    # 'max_loan_to_value_ratio': 80, 'min_credit_score': 680}
    criteria = models.JSONField(default=default_criteria)  # Add the JSONField for storing criteria

    class Meta:
        db_table = 'loan'  # Explicitly set table name
    
    def __str__(self):
        return f'{self.loan_type} Loan #{self.id}'

# Document model for managing legal documents related to properties and loans
class Document(models.Model):
    document_type = models.CharField(max_length=50)  # E.g., 'Mortgage Agreement', 'Occupancy Permit', 'Title'
    document_url = models.TextField()
    description = models.TextField(blank=True, null=True)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='documents', null=True, blank=True)

    class Meta:
        db_table = 'document'  # Explicitly set table name
    
    def __str__(self):
        return f'{self.document_type} Document #{self.id}'

