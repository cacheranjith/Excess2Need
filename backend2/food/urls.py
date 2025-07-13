from django.urls import path
from .views import FoodItemCreateView, FoodListView, BookingView, MyBookingsView
from .views import DonorBookingsView

urlpatterns = [
    path('upload/', FoodItemCreateView.as_view(), name='upload_food'),
    path('list/', FoodListView.as_view()),
    path('book/', BookingView.as_view()),
    path('my-bookings/', MyBookingsView.as_view()),
    path('donor/bookings/', DonorBookingsView.as_view()),
]
