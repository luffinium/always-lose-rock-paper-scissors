looping = True
while looping:
    print (
        "Rock , Paper , Scissors , Shoot!"
        )
    player = input()
    ai = ["Rock", "Paper", "Scissors"]
    validChoice = True
    if player == "Rock" :
        ai = "Paper"
    elif player =="Paper" :
        ai = "Scissors"
    elif player =="Scissors" :
        ai = "Rock"
    else:
        validChoice = False
    if validChoice:
        print (ai, "beats", player, "you lose.")
    else:
        print ("Rock, Paper, or Scissors.")