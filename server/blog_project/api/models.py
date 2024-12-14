from .utils import upload_image_to_cloudinary  # Import the function
# from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
import hashlib
import uuid

class CustomUser(AbstractUser):
    id = models.CharField(max_length= 64,primary_key= True ,editable= False)
    occupation = models.CharField(max_length=100, blank=True)
    
    def save (self, *args, **kwargs):
        if not self.id:   #generate only for new user
            random_value = str(uuid.uuid4())   #generate a random uuid
            unique_string = f"{self.username}{random_value}"
            self.id =hashlib.sha256(unique_string.encode()).hexdigest() #hash the combination
        super().save(*args, **kwargs) #save the instance

    def __str__(self):
        return self.username


# class Blog(models.Model):
#     CATEGORY_CHOICES = [
#         ('Technology', 'Technology'),
#         ('Health', 'Health'),
#         ('Education', 'Education'),
#         ('Lifestyle', 'Lifestyle'),
#         ('Business', 'Business'),
#         ('Travel', 'Travel'),
#     ]

#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs'
#     )
#     category = models.CharField(
#         max_length=50,
#         choices=CATEGORY_CHOICES,
#         default='Technology',  # Set a default category
#     )
#     date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title



# class Blog(models.Model):
#     CATEGORY_CHOICES = [
#         ('Technology', 'Technology'),
#         ('Health', 'Health'),
#         ('Education', 'Education'),
#         ('Lifestyle', 'Lifestyle'),
#         ('Business', 'Business'),
#         ('Travel', 'Travel'),
#     ]

#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     image = CloudinaryField('image', blank=True, null=True)  # Use CloudinaryField
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs'
#     )
#     category = models.CharField(
#         max_length=50,
#         choices=CATEGORY_CHOICES,
#         default='Technology',  # Set a default category
#     )
#     date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title


# from django.db import models
# from django.conf import settings

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('Technology', 'Technology'),
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Lifestyle', 'Lifestyle'),
        ('Business', 'Business'),
        ('Travel', 'Travel'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # ImageField for uploading
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs'
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Technology',  # Set a default category
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Override the save method to upload the image to Cloudinary."""
        if self.image:
            self.image = upload_image_to_cloudinary(self.image)  # Update image field with Cloudinary URL
        super().save(*args, **kwargs)  # Call the parent save method



class Comment(models.Model):
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments'
    )
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments'
    )

    def __str__(self):
        return f"Comment by {self.username} on {self.blog}"
