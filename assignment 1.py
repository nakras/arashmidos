import random

questions_list = ["who is your favorite actor/actress?", "what is your favorite color?", "what is your favorite food?"]
answers_list = ["hmm... awesome!", "good choice", "okay cool "]
for i in range(3):
    input(questions_list[i])
    print(random.choice(answers_list))