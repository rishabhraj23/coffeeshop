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
    # path('add_coffee', views.add_coffee, name='add_coffee'),
    path('coffee_form_add_update/', views.coffee_form_add_update, name='add_coffee'),
    path('coffee_form_add_update/<int:id>', views.coffee_form_add_update, name='coffee_form_add_update'),
    path('delete_coffee/<int:id>', views.delete_coffee, name='delete_coffee'),
    path("place_order", views.place_order, name="place_order"),
    path("cancel_order/<int:id>", views.cancel_order, name="cancel_order"),

]