from rest_framework import generics
from ..models import User

from rest_framework import serializers, permissions
from ..models import Document, Loan

class DocumentSerializer(serializers.ModelSerializer):
    loan = serializers.PrimaryKeyRelatedField(queryset=Loan.objects.all(), required=False)

    class Meta:
        model = Document
        permission_classes = [permissions.IsAuthenticated]
        fields = ['id', 'document_type', 'document_url', 'description', 'loan']

class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        # Optional: Customize the creation of Document instances here if needed
        serializer.save()

class DocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer