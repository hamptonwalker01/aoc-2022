l = open("day2.txt", "r").readlines()
lines = [_.strip() for _ in l]

# A & X - Rock
# B & Y = Paper
# C & Z = Scissors
score = 0
for line in lines:
  opp, me = line.split(" ")
  if opp == "A" and me == "X":
    score += 3
  elif opp == "A" and me == "Y":
    score += 4
  elif opp == "A" and me == "Z":
    score += 8
  elif opp == "B" and me == "X":
    score += 1
  elif opp == "B" and me == "Y":
    score += 5
  elif opp == "B" and me == "Z":
    score += 9
  elif opp == "C" and me == "X":
    score += 2
  elif opp == "C" and me == "Y":
    score += 6
  elif opp == "C" and me == "Z":
    score += 7

print(score)