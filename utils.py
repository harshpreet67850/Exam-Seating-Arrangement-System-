# Update the import below to match your actual model names and location.
# For example, if your models are named differently or located elsewhere, adjust accordingly.
from exam_app.models import MyStudent as Student, MyClassroom as Classroom, MyExamSeating as ExamSeating

def auto_assign_seats():
    # Get all students without seats
    # Ensure all students have up-to-date seat_number fields before filtering
    for seating in ExamSeating.objects.all():
        if hasattr(seating.student, 'seat_number'):
            seating.student.seat_number = seating.seat_number
            seating.student.save()

    students = Student.objects.filter(seat_number__isnull=True)
    # Get all students without seats
    # Ensure all students have up-to-date seat_number fields before filtering
    for seating in ExamSeating.objects.all():
        if hasattr(seating.student, 'seat_number'):
            seating.student.seat_number = seating.seat_number
            seating.student.save()

    # Check if Student model has seat_number field before filtering
    if hasattr(Student, '_meta') and any(f.name == 'seat_number' for f in Student._meta.fields):
        students = Student.objects.filter(seat_number__isnull=True)
    else:
        students = Student.objects.all()
    classrooms = Classroom.objects.all()
    for student in students:
        assigned = False
        for room in classrooms:
            if room_map[room.id] > 0:
                # Assign student
                seat_num = f"{seat_counter[room.id]}"
                ExamSeating.objects.create(
                    student=student,
                    classroom=room,
                    seat_number=seat_num
                )
                # Optionally, update the student's seat_number if the field exists
                if hasattr(student, 'seat_number'):
                    student.seat_number = seat_num
                    student.save()

                # Update counters
                seat_counter[room.id] += 1
                room_map[room.id] -= 1
                assigned = True
                break
        if not assigned:
            print(f"No available seat for {student.roll_number}")
