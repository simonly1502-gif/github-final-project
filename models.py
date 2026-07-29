from django.db import models

class Question(models.Model):
    # Cần thêm 2 trường này:
    course = models.ForeignKey('Course', on_delete=models.CASCADE)  # Trường course
    grade = models.IntegerField()                                  # Trường grade
    
    # Các trường khác bạn đã làm...

class Choice(models.Model):
    # Cần thêm trường này:
    is_correct = models.BooleanField(default=False)               # Trường is_correct
    
    # Các trường khác bạn đã làm...

class Submission(models.Model):
    # Cần thêm 2 trường này:
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE) # Trường enrollment
    choices = models.ManyToManyField(Choice)                              # Trường choices
    
    # Các trường khác bạn đã làm...
