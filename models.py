# Create your models here.
from django.db import models


# Student Table
class Student(models.Model):
    roll_number = models.CharField(max_length=20, unique=True)  # e.g., 23CSE101
    name = models.CharField(max_length=100)  # Student Name
    branch = models.CharField(max_length=50)  # e.g., CSE, ECE
    semester = models.IntegerField()  # e.g., 5
    seat_number = models.CharField(
        max_length=10, blank=True, null=True
    )  # Seat Allotted

    def __str__(self):
        return f"{self.roll_number} - {self.name}"


# Classroom Table
class Classroom(models.Model):
    room_number = models.CharField(max_length=10, unique=True)  # e.g., A101
    capacity = models.IntegerField()  # Number of seats

    def __str__(self):
        return f"Room {self.room_number} (Capacity: {self.capacity})"


# Exam Seating (Mapping Student → Classroom)
class ExamSeating(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)  # e.g., 12A

    def __str__(self):
        return f"{self.student.roll_number} → {self.classroom.room_number} Seat {self.seat_number}"
