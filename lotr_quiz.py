print("Welcome, brave soul, to the lands of Middle-Earth!")

playing = input("Do you wish to join the Fellowship and embark on a perilous journey to destroy the One Ring? ").strip().lower()

if playing != "yes":
    quit()

print("Very well, you have been chosen. But first, answer these questions to prove your worth!")
score = 0

# Question 1: Gandalf’s Challenge
answer = input("Gandalf asks: 'What is the air speed velocity of an unladen swallow?' ").strip().lower()
if answer == "what do you mean? an african or european swallow":
    print("Correct! Gandalf chuckles, pleased by your knowledge.")
    score += 1
else:
    print("Incorrect. Gandalf raises an eyebrow.")

# Question 2: Gollum’s Riddle
answer = input("Gollum asks: 'This thing all things devours: birds, beasts, trees, flowers; Gnaws iron, bites steel; Grinds hard stones to meal; Slays king, ruins town, and beats high mountain down. What is it?' ").strip().lower()
if answer == "time":
    print("Correct! Gollum gives a twisted grin, impressed by your answer.")
    score += 1
else:
    print("Incorrect. Gollum hisses angrily.")

# Question 3: Legolas’ Question
answer = input("Legolas asks: 'What is the sound of a bowstring pulled tight, and arrows in the air?' ").strip().lower()
if answer == "the whisper of the wind":
    print("Correct! Legolas nods silently, satisfied with your answer.")
    score += 1
else:
    print("Incorrect. Legolas raises his bow, clearly not impressed.")

# Question 4: The Elven Question
answer = input("Galadriel, Lady of Lothlórien, asks: 'In the darkness of the world, what light gives us hope?' ").strip().lower()
if answer == "the light of the stars" or answer == "hope":
    print("Correct! Galadriel smiles, and the light around her seems brighter.")
    score += 1
else:
    print("Incorrect. Galadriel gazes at you with a sad look in her eyes.")

# End of Quiz
print(f"You answered {score} out of 4 questions correctly!")
print(f"Your score: {round((score / 4) * 100, 2)}%")
