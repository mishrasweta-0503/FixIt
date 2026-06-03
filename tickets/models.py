from django.db import models
from django.contrib.auth.models import User

# Creating the User profile(tenant/staff)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #a user is linked to only a single profile
    is_tenant = models.BooleanField(default=True)
    is_staff_member = models.BooleanField(default=False)

class Ticket(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    status = models.CharField(max_length=255, default="Open")
    priority = models.CharField(max_length=30, default="Medium")
    created_at = models.DateTimeField(auto_now_add=True) #auto populates on creation
    image = models.ImageField(upload_to='ticket_pics/', blank=True, null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE) #a user can create multiple tickets