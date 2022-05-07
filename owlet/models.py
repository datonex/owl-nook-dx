# from django.db import models
# from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


# class UserProfile(models.Model):
#     profile = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="owlnook_user"
#     )
#     avatar_image = CloudinaryField("image", default="avatar")
#     biography = models.TextField(verbose_name="biography", max_length=200, blank=True)
