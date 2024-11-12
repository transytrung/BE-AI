from django.urls import path
from . import views

urlpatterns = [
    # University endpoints
    path('universities/', views.university_list_create, name='university-list-create'),  # GET: Danh sách trường, POST: Thêm trường mới
    path('universities/<int:pk>/', views.university_detail, name='university-detail'),   # GET, PUT, DELETE: Chi tiết trường theo ID

    # Program endpoints
    path('programs/', views.program_list_create, name='program-list-create'),            # GET: Danh sách chương trình, POST: Thêm chương trình mới
    path('programs/<int:pk>/', views.program_detail, name='program-detail'),             # GET, PUT, DELETE: Chi tiết chương trình theo ID

    # FAQ endpoints
    path('faqs/', views.faq_list_create, name='faq-list-create'),                        # GET: Danh sách câu hỏi, POST: Thêm câu hỏi mới
    path('faqs/<int:pk>/', views.faq_detail, name='faq-detail'),                         # GET, PUT, DELETE: Chi tiết câu hỏi theo ID

    # Chatbot endpoint
    path('chatbot/', views.chatbot_view, name='chatbot'),                                # POST: Nhận yêu cầu từ người dùng, trả lời tư vấn
]
