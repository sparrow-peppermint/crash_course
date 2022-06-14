from survey_me import AnonymousSurvey

# define a question and make a survey

question = "How old are you?"

my_survey = AnonymousSurvey(question)

# show the question and store responses to the question

my_survey.show_question()
print("Enter q at any time to quit")

while True:
    response = input("Enter age: ")
    if response == "q":
        break
    my_survey.store_response(response)

my_survey.show_results()



