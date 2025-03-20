from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('user_details', views.user_details, name='user_details'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('coffee', views.coffee, name='coffee'),
    path('orders', views.orders, name='orders'),
    path('history', views.history, name='history'),
    # path('book/<int:id>', views.book, name='book'),
    # path('booking_confirm/<int:id>', views.booking_confirm, name='booking_confirm'),
    # path('delete_bookings/<int:id>', views.delete_bookings, name='delete_bookings'),
    # path('update_bookings/<int:id>', views.update_bookings, name='update_bookings'),
    # path('order_history', views.order_history, name='order_history'),
]