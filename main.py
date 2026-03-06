from questions import questions
from evaluator import evaluate_answer

print("AI Mock Interview Agent\n")

for question, reference_answer in questions.items():

    print("Question:", question)
    candidate_answer = input("Your Answer: ")

    score, result = evaluate_answer(reference_answer, candidate_answer)

    print("Score:", round(score,2))
    print("Evaluation:", result)
    print("----------------------------------")