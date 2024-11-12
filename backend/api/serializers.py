from rest_framework import serializers
from .models import University, Program, FAQ

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'location', 'contact_email', 'phone_number']

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'university', 'name', 'tuition_fee', 'duration', 'language_of_instruction']

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'program']
