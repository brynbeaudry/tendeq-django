from rest_framework import generics
from ..models import User

from rest_framework import serializers
from ..models import Loan, User

class LoanSerializer(serializers.ModelSerializer):
    # You might want to use a nested serializer or simply display the related instance's ID or other fields.
    borrower = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='borrower'))
    lender = serializers.PrimaryKeyRelatedField(queryset=User.objects. filter(role='lender'))

    class Meta:
        model = Loan
        fields = ['id', 'amount', 'interest_rate', 'start_date', 'due_date', 'borrower', 'lender', 'criteria']
        # Optionally add extra_kwargs if you want to make any field read-only or apply other constraints

class LoanListCreateView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class LoanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer