from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)  # Tên trường
    location = models.CharField(max_length=255)  # Địa chỉ
    contact_email = models.EmailField(blank=True, null=True)  # Email liên hệ
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # Số điện thoại liên hệ

    def __str__(self):
        return self.name


class Program(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='programs')
    name = models.CharField(max_length=255)  # Tên ngành học
    description = models.TextField(blank=True, null=True)  # Mô tả ngành học
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)  # Học phí
    duration = models.IntegerField()  # Thời gian học (năm)
    admission_requirements = models.TextField(blank=True, null=True)  # Yêu cầu đầu vào
    scholarships = models.TextField(blank=True, null=True)  # Học bổng có sẵn
    career_opportunities = models.TextField(blank=True, null=True)  # Cơ hội nghề nghiệp sau khi tốt nghiệp
    language_of_instruction = models.CharField(max_length=50, default='Vietnamese')  # Ngôn ngữ giảng dạy
    intake_period = models.CharField(max_length=50, blank=True, null=True)  # Kỳ tuyển sinh
    application_process = models.TextField(blank=True, null=True)  # Quy trình ứng tuyển
    
    def __str__(self):
        return f"{self.name} - {self.university.name}"


class FAQ(models.Model):
    question = models.CharField(max_length=255)  # Câu hỏi thường gặp
    answer = models.TextField()  # Câu trả lời
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='faqs', blank=True, null=True)

    def __str__(self):
        return self.question
