from django.db import models

class d_type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.type_name}"


class book_type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    photo = models.ImageField()
    def __str__(self):
        return f"{self.name}"

class book_books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    photo = models.ImageField()
    def __str__(self):
        return f"{self.name}"
    
class book_novel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    photo = models.ImageField()
    def __str__(self):
        return f"{self.name}"
    
class book_manga(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    photo = models.ImageField()
    def __str__(self):
        return f"{self.name}"
    
class BookType(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  photo = models.ImageField()
  def __str__(self):
    return f"{self.name}"