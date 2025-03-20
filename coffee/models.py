from django.db import models
from django.contrib.auth.models import User
import uuid 


class Coffee(models.Model):
    image = models.ImageField(upload_to="static/coffee_images/")
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.IntegerField()

    def __str__(self):
        return self.name
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # coffee_id = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, 
        choices=[("pending", "Pending"), ("completed", "Completed"), ("canceled", "Canceled")], 
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for order creation


    def total_price(self):
        return sum(item.subtotal() for item in self.items.all())

    # def __str__(self):
    #     return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.quantity * self.coffee.cost

    # def __str__(self):
    #     return f"{self.quantity} x {self.coffee.name}"