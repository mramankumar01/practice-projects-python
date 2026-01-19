# Kaun Banega Crorepati

questions = [["Who is the CEO of Tesla?", "Elon Musk", "Jeff Bezos", "Bill Gates", "Steve Jobs", 1],
             ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
             ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", 2],
             ["What is the largest mammal in the world?", "Elephant", "Blue Whale", "Giraffe", "Great White Shark", 2],
             ["Who wrote 'Romeo and Juliet'?", "Mark Twain", "Charles Dickens", "William Shakespeare", "Jane Austen", 3],
             ["Who is Shah Rukh Khan?", "Cricketer", "Actor", "Politician", "Scientist", 2],
             ["Who painted the Mona Lisa?", "Vincent Van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3],
             ["What is the smallest prime number?", "0", "1", "2", "3", 3],
             ["Which ocean is the largest?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],
             ["What is the chemical symbol for gold?", "Au", "Ag", "Gd", "Go", 1],
             ["What is the fastest land animal?", "Cheetah", "Lion", "Tiger", "Ostrich", 1],
             ["What is the smallest country in the world?", "Monaco", "Vatican City", "Nauru", "San Marino", 2],
             ["Who discovered penicillin?", "Marie Curie", "Alexander Fleming", "Louis Pasteur", "Isaac Newton", 2],
             ["What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Platinum", 3],
             ["Which planet has the most moons?", "Earth", "Mars", "Jupiter", "Saturn", 3]]


i = 0

prizes = [1000, 3000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000, 3000000, 5000000, 10000000, 30000000, 50000000]

for question in questions:
    print(f"Q. {question[0]}")
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    answer = int(input("Enter your answer : "))

    #  Check the answer
    if(answer == question[5]):
        print("Correct answer!")
        print(f"You have won Rs. {prizes[i]}")
        i += 1
    else:
        print("Wrong answer! You lost the game.")
        print("Better luck next time.")
        break

