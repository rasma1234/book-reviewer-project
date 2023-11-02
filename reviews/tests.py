
from django.test import TestCase
from .models import Book, Review
from django.urls import reverse

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.book = Book.objects.create(title='Sample Book', author='Asma Rahimi')
        cls.review = Review.objects.create(book=cls.book, review_text="it is reviewed", rating=5)

    def test_content(self):
        self.assertEqual(self.book.title, 'Sample Book')
        self.assertEqual(self.book.author, 'Asma Rahimi')
        self.assertEqual(self.review.book, self.book)
        self.assertEqual(self.review.review_text, 'it is reviewed')

    def test_api_list_view(self):
        response = self.client.get(reverse("book_list"))
        response1 = self.client.get(reverse("review_list"))
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(Review.objects.count(), 1)
        self.assertContains(response1, self.review.review_text)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)

    def test_api_detail_view(self):
        response = self.client.get(reverse("book_detail", kwargs={"pk":self.book.id}))
        response1 = self.client.get(reverse("review_detail", kwargs={"pk":self.review.id}))
        self.assertEqual(response1.status_code, 200)
        self.assertContains(response1, "it is reviewed")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Asma Rahimi")
    