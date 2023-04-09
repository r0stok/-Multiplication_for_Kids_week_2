from random import randint

correct = 0
wrong = 0
questions = 0

for num in range(10):
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    num_3 = num_1 * num_2
    questions += 1
    print("Question", questions, ":", num_1, "x", num_2, "?")
    answer = int(input("Student Answer: "))

    if answer == num_1 * num_2:
        print("Answer: ", num_1 * num_2, "Status: Correct")
        correct += 1

    else:
        print("Answer: ", num_1 * num_2, " Status: Wrong")

if correct >= 7:
    print("Test passed")
else:
    print("Test failed try again!!!")

print("The number of points received are", correct, "out of", questions)
