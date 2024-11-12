from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import University, Program, FAQ

class UniversityModelTestCase(TestCase):
    def setUp(self):
        self.university = University.objects.create(
            name="University of Transport and Communication",
            location="Hanoi",
            website = "utc.edu.vn"
        )

    def test_university_str(self):
        self.assertEqual(str(self.university), "Test University")

class ProgramModelTestCase(TestCase):
    def setUp(self):
        university = University.objects.create(
            name="Another University",
            location="Another Location"
        )
        self.program = Program.objects.create(
            university=university,
            name="Test Program",
            tuition_fee=10000,
            duration=4
        )

    def test_program_str(self):
        self.assertEqual(str(self.program), "Test Program - Another University")

class FAQModelTestCase(TestCase):
    def setUp(self):
        program = Program.objects.create(
            university=University.objects.create(name="Uni"),
            name="Sample Program",
            tuition_fee=12000,
            duration=3
        )
        self.faq = FAQ.objects.create(
            question="What is the program duration?",
            answer="3 years",
            program=program
        )

    def test_faq_str(self):
        self.assertEqual(str(self.faq), "What is the program duration?")

class UniversityAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.university_data = {
            "name": "University of Transport and Communication",
            "location": "Hanoi",
            "website": "utc.edu.vn",
            
        }
        self.response = self.client.post(
            reverse('university-list-create'), 
            self.university_data, 
            format="json"
        )

    def test_create_university(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_universities(self):
        response = self.client.get(reverse('university-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

