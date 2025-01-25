#Made a game similar to Kaun Banega Crorepati (KBC)

name = input("Enter Your Name: ")

print("Welcome",name,"in Kaun Banega Crorepati (KBC)")

questions = ["What is the capital of India?","Which planet is known as the 'Red Planet'?","What is the national bird of India?","Who was the first Prime Minister of India?","What is the currency of India?","Which is the largest continent in the world by area?","Who wrote the national anthem of India, 'Jana Gana Mana'?","Which is the smallest planet in our solar system?","In Indian history, who is known as the 'Iron Man of India'?","What is the chemical symbol for water?"]

answers = ["New Delhi","Mars","Peacock","Jawaharlal Nehru","Rupee","Asia","Rabindranath Tagore","Mercury","Sardar Vallabhbhai Patel","H2O"]

index = 0
rightCount = 0

for question in questions:
  print(question)
  answer = input("Enter your answer: ")
  if(answer == answers[index]):
    print("Right Answer")
    index = index+1
    rightCount = rightCount+1
  else:
    print("Wrong Answer")
    index = index+1
    break

if(rightCount == index):
  print("You have answered all 5 questions correctly and showcased incredible knowledge and confidence!")
else:
  print("Oh no! Unfortunately, your answer was incorrect, and your journey in this competition ends here.")