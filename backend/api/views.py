from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .models import Program
from .serializers import ProgramSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    View API DRF for Program
    """
    serializer = ProgramSerializer(data=request.data)
    if serializer.is_valid():
        # Optionally save the instance if needed
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)
# @api_view(['POST'])
# def chatbot_view(request):
#     """
#     Chatbot endpoint to handle user queries.
#     """
#     user_question = request.data.get("question", "")
#     if not user_question:
#         return Response({"error": "Question field is required."}, status=400)

#     # Placeholder for chatbot response logic
#     # You can integrate an AI model or use simple rule-based logic here
#     response = process_chatbot_response(user_question)
    
#     return Response({"question": user_question, "answer": response})

# def process_chatbot_response(question):
#     faq = FAQ.objects.filter(question__icontains=question).first()
#     if faq:
#         return faq.answer
#     return "Xin lỗi, tôi không tìm thấy câu trả lời cho câu hỏi này."

class UpdateProgramFromAPI(api_view):
    def post(self, request, *args, **kwargs):
        # Lấy dữ liệu từ API bên ngoài
        external_data = request.get('https://external-source.com/api/programs').json()

        # Lặp qua các dữ liệu nhận được và cập nhật vào cơ sở dữ liệu của bạn
        for data in external_data:
            program, created = Program.objects.update_or_create(
                name=data['name'],
                defaults={
                    'tuition_fee': data['tuition_fee'],
                    'duration': data['duration'],
                    'language_of_instruction': data['language_of_instruction'],
                }
            )
            if created:
                print(f'Chương trình mới: {data["name"]}')
            else:
                print(f'Chương trình đã được cập nhật: {data["name"]}')
        
        # Trả về phản hồi thành công
        return Response({"message": "Cập nhật thành công"})
