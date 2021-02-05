from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.db import migrations
# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)
 

class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    interests = models.ManyToManyField(Subject, related_name='interested_students')

    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers \
            .filter(answer__question__quiz=quiz) \
            .values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions

    def __str__(self):
        return self.user.username


class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)


class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')

# class Courses(models.Model):
#     # name = models.CharField(max_length=100, blank=False)
#     # description = models.TextField(blank=False)
#     Bachelors_in_Computer_Science = 'BCompSc'
#     Business_School = 'Business'
#     Engineering_School ='Engineering'
#     Health_Science = 'Medicine'
#     Course_choices = [
#         (Bachelors_in_Computer_Science,'BCompSc'),
#         (Business_School,'Business'),
#         (Engineering_School,'Engineering'),
#         (Health_Science,'Medicine'),
#     ]
#     Course_choices = models.CharField(
#         max_length=15,
#         choices=Course_choices,
#         default=Health_Science,
#     )
#     # courses = models.ForeignKey(Courses,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.courses
    
    

    
    
    
# class Tutor(models.Model):
#     # name = models.CharField(max_length = 100)
#     # image = CloudinaryField('image')
#     # accolades=models.CharField(max_length=255)
#     bio = models.CharField(max_length=255,default=None)
#     # email = models.TextField(blank=True)
#     courses = models.ForeignKey(Courses,default=None,on_delete=models.CASCADE)
#     # user = models.ManyToManyField(User)
    
#     def __str__(self):
#         return self.bio
    
#     def save_tutor(self):
#         self.save()
        
#     def delete_tutor(self):
#         self.delete()
        
#     @classmethod
#     def update_bio(cls,id,bio):
#         update_profile = cls.objects.filter(id = id).update(bio =bio)
#         return update_profile
    
#     @classmethod
#     def get_all_profiles(cls):
#         students = Students.objects.all()
#         return students
    
#     @classmethod
#     def search_user(cls,user):
#         return cls.objects.filter(user__username__icontains = user).all()
    
    
#     class Meta:
#         verbose_name_plural = "Tutors"
    
    
