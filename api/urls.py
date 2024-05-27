from django.urls import path
from .views.user import UserListCreateView, UserDetailView
from .views.loan import LoanListCreateView, LoanDetailView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('loans/', LoanListCreateView.as_view(), name='loan-list'),
    path('loans/<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
]