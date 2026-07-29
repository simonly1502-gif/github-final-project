from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Question, Choice, Submission

# Xử lý khi học viên bấm nút nộp bài thi
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user

    if request.method == 'POST':
        # 1. Tạo một đối tượng Submission mới cho người dùng
        submission = Submission.objects.create(user=user, course=course)
        
        # 2. Lấy danh sách các đáp án mà người dùng đã chọn từ form
        # Form gửi lên danh sách ID của các choice dưới dạng checkbox/radio
        selected_choice_ids = request.POST.getlist('choice')
        
        # 3. Lưu các choice được chọn vào submission
        for choice_id in selected_choice_ids:
            choice = get_object_or_404(Choice, pk=choice_id)
            submission.choices.add(choice)
        
        submission.save()
        
        # 4. Chuyển hướng sang trang hiển thị kết quả bài thi
        return HttpResponseRedirect(reverse('onlinecourse:show_exam_result', args=(course.id, submission.id)))

    return redirect('onlinecourse:course_details', course_id=course.id)


# Hiển thị kết quả bài thi sau khi nộp
def show_exam_result(request, course_id, submission_id):
    context = {}
    
    # Lấy thông tin khóa học và lượt nộp bài
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # Danh sách các lựa chọn mà học viên đã chọn
    selected_choices = submission.choices.all()
    
    # Tính tổng số điểm hoặc số câu trả lời đúng
    total_score = 0
    total_possible_score = 0
    
    # Duyệt qua các câu hỏi trong khóa học để tính điểm
    for question in course.question_set.all():
        total_possible_score += question.grade
        # Kiểm tra xem đáp án người dùng chọn có chính xác không
        if question.is_get_score(selected_choices):
            total_score += question.grade

    # Đưa dữ liệu vào context để truyền ra giao diện HTML
    context['course'] = course
    context['selected_ids'] = [choice.id for choice in selected_choices]
    context['total_score'] = total_score
    context['total_possible_score'] = total_possible_score
    context['submission'] = submission

    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
