# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CybersportDislike(models.Model):
    id = models.BigAutoField(primary_key=True)
    rating = models.ForeignKey('CybersportRating', models.DO_NOTHING)
    user = models.ForeignKey('CybersportUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Cybersport_dislike'
        unique_together = (('user', 'rating'),)


class CybersportLike(models.Model):
    id = models.BigAutoField(primary_key=True)
    rating = models.ForeignKey('CybersportRating', models.DO_NOTHING)
    user = models.ForeignKey('CybersportUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Cybersport_like'
        unique_together = (('user', 'rating'),)


class CybersportRating(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Cybersport_rating'


class CybersportUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    rating = models.OneToOneField(CybersportRating, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cybersport_user'


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'category'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Category(name='{self.name}')"


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=5000)
    created_at = models.DateTimeField()
    author = models.ForeignKey(CybersportUser, models.DO_NOTHING, blank=True, null=True)
    new = models.ForeignKey('New', models.DO_NOTHING)
    rating = models.OneToOneField(CybersportRating, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class NewManager(models.Manager):
    def create(self, *args, **kwargs):
        if 'rating' not in kwargs:
            kwargs['rating'] = CybersportRating.objects.create()
        return super(NewManager, self).create(*args, **kwargs)


class New(models.Model):
    objects = NewManager()

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=5000)
    slug = models.CharField(max_length=300)
    date = models.DateTimeField()
    image_url = models.CharField(max_length=300)
    is_published = models.BooleanField()
    author = models.ForeignKey(CybersportUser, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    rating = models.OneToOneField(CybersportRating, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new'

    def __repr__(self):
        return f"New(title='{self.title}')"
