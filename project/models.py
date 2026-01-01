from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Count, F, Sum, Q
from django.db.models.signals import post_save
from django.dispatch import receiver

# python manage.py makemigrations project
# python manage.py makemigrations
# python manage.py migrate


class ProfileManager(models.Manager):
    def popular_users(self, num):
        return self.order_by('-rating', 'user__date_joined')[:num]
    
    def update_rating(self):
        profiles = self.annotate(total_score=Sum('answervote__score') + Sum('questionvote__score'))
        for profile in profiles:
            profile.rating = profile.total_score or 0
        self.bulk_update(profiles, ['rating'])
 
 
class Profile(models.Model):
    objects = ProfileManager()

    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE
        )
    nickname = models.CharField(
        max_length=256,
        default='lame_user',
        blank=False,
        )
    avatar = models.ImageField(
        blank=True,
        default='default_avatar.jpeg',  
        upload_to='avatars/%Y/%m/%d/',
    )

    def __str__(self):
        return self.user.username

    def absolute_url(self):
        return f"/profile/{self.pk}/"
    
    class Meta:
        db_table = 'profile'
        ordering = ['-user']
    
'''
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance,
            nickname=nickname,
            avatar=avatar,)
        instance.profile.save()
'''
    