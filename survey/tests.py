from django.contrib.auth.models import User
from django.test import TestCase

from survey.models import Answer, Question


class QuestionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345789")
        self.user2 = User.objects.create_user(username="testuser2", password="12345789")
        self.user3 = User.objects.create_user(username="testuser3", password="12345789")
        self.user4 = User.objects.create_user(username="testuser4", password="12345789")
        self.client.login(username="testuser", password="12345789")
        Question.objects.create(
            author=self.user, title="TestQuestion", description="TestDescription"
        )
        Question.objects.create(
            author=self.user2, title="TestQuestion2", description="TestDescription2"
        )
        Question.objects.create(
            author=self.user3, title="TestQuestion3", description="TestDescription3"
        )
        Question.objects.create(
            author=self.user4, title="TestQuestion4", description="TestDescription4"
        )

    def test_creation_quetions(self):
        """Questions were created with descriptions"""
        question1 = Question.objects.get(title="TestQuestion")
        question2 = Question.objects.get(title="TestQuestion2")
        question3 = Question.objects.get(title="TestQuestion3")
        question4 = Question.objects.get(title="TestQuestion4")
        self.assertEqual(question1.description, "TestDescription")
        self.assertEqual(question2.description, "TestDescription2")
        self.assertEqual(question3.description, "TestDescription3")
        self.assertEqual(question4.description, "TestDescription4")

    def test_quetions_initial_ranking(self):
        """Questions were created with descriptions"""
        question1 = Question.objects.get(title="TestQuestion")
        question2 = Question.objects.get(title="TestQuestion2")
        question3 = Question.objects.get(title="TestQuestion3")
        question4 = Question.objects.get(title="TestQuestion4")
        self.assertEqual(question1.ranking, 10)
        self.assertEqual(question2.ranking, 10)
        self.assertEqual(question3.ranking, 10)
        self.assertEqual(question4.ranking, 10)

    def test_verify_question_ranking(self):
        """Question should have a ranking of 32. Initial 10 point for being
        within 24 hours"""
        question1 = Question.objects.get(title="TestQuestion")
        Answer.objects.update_or_create(
            author=self.user,
            question=question1,
            defaults={"value": 3},
        )  # +10 points answer question Regular
        Answer.objects.update_or_create(
            author=self.user2,
            question=question1,
            defaults={"like": 1},
        )  # -3 dislike
        Answer.objects.update_or_create(
            author=self.user3,
            question=question1,
            defaults={"like": 2},
        )  # +5 like
        Answer.objects.update_or_create(
            author=self.user4,
            question=question1,
            defaults={"value": 5},
        )  # 10 answer question Very High
        self.assertEqual(question1.ranking, 32)
