import time
def chat(): #Defining/Creating the chat function
  print("Hey Guys! I am Gameo your personal assistant")
  time.sleep(1) # Gives a pause for 1 second
  name = input("What is your name: ")
  print("That's a really good name")
  time.sleep(1)
  age = int(input("So "+name+", How old are you right now? "))
  print("Wow! Well I'm just 1 day old as I was created yesterday by class coding")
  time.sleep(3)
  interest = input("By the way, what do you do in your free time? ")
  print("That's cool! Usually I play video games")
  time.sleep(2)
  question = input("Do you want to know which games do I play (Yes/No)? ")
  if question == "Yes": # if else condition
    print("Great, so I play FIFA and Minecraft. These games are very fun to play")
    time.sleep(2)
    question2 = input("Which games do you play? ")
    print("Thats cool!")
    time.sleep(1)
    print("Anyways, it was great talking to you",name+". Let's catch up again soon. Good-bye!")
  else:
    print("Aw, well fine. Let's catch-up later whenever you want to talk",name+". Good-bye!")


