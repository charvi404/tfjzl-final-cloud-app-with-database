from django.shortcuts import render, get_object_or_404
from .models import Course, Submission, Choice, Enrollment


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollment = Enrollment.objects.get(user=request.user, course=course)

    selected_choices = request.POST.getlist('choice')
    submission = Submission.objects.create(enrollment=enrollment)

    for choice_id in selected_choices:
        choice = Choice.objects.get(pk=choice_id)
        submission.choices.add(choice)

    return show_exam_result(request, course.id, submission.id)


def show_exam_result(request, course_id, submission_id):
    submission = Submission.objects.get(pk=submission_id)

    total = submission.choices.count()
    correct = 0

    for choice in submission.choices.all():
        if choice.is_correct:
            correct += 1

    score = (correct / total) * 100 if total > 0 else 0

    return render(request, 'onlinecourse/exam_result.html', {
        'score': score,
        'total': total,
        'correct': correct
    })
