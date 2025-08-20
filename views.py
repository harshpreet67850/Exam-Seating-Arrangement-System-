# Create your views here.
from django.shortcuts import render  # Ensure Django is installed: pip install django


def home(request):
    return render(request, "home.html")
import csv
from django.http import HttpResponse  # Ensure Django is installed: pip install django
from .models import ExamSeating

def export_exam_seating_csv(_request):
    # Response setup
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exam_seating.csv"'

    writer = csv.writer(response)
    # Header Row
    writer.writerow(['Roll Number', 'Student Name', 'Branch', 'Semester', 'Room Number', 'Seat Number'])

    # Fetching data from ExamSeating + related Student & Classroom
    exam_seatings = ExamSeating.objects.select_related('student', 'classroom').all()
    for es in exam_seatings:
        writer.writerow([
            es.student.roll_number,
            es.student.name,
            es.student.branch,
            es.student.semester,
            es.classroom.room_number,
            es.seat_number,
        ])

    return response
