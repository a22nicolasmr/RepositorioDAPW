from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Exercise(models.Model):
    title=models.CharField(max_length=100)
    repetitions=models.IntegerField()
    weight=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="toExercise/images",null=True,unique=True)

    def __str__(self):
        return f"Title={self.title}, Repetitions={self.repetitions}, Weight={self.weight}, Date={self.date} , Category={self.category}"
    
