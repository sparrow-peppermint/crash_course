import unittest
from survey_me import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = "What languages do you speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", "Spanish", "French"]

    def test_single_response(self):
        """test that a single response is stored correctly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_three_responses(self):
        """test that three individual responses are stored correctly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == "__main__":
    unittest.main()

