lines = open("day3.txt").readlines()

# Initialize dictionary of priorities
d = {}
priority = 1
# lower case priorities: 1-26
for char in range(ord('a'), ord('z') + 1):
  d[char] = priority
  priority += 1
# upper case priorities: 27-52
for char in range(ord('A'), ord('Z') + 1):
  d[char] = priority
  priority += 1

# Part 1 solution
sum1 = 0
for idx, line in enumerate(lines):
  l = line.strip()
  midpoint = int(len(l)/2)
  # split string into 2 parts, loop over first and try to find match in second string
  # update sum of priorities and then break out of this loop to continue to the next line
  for char in l[0:midpoint]:
    if char in l[midpoint:]:
        sum1 += d[ord(char)]
        break

# Solution to second question
sum2 = 0
for idx, line in enumerate(lines[0::3]):
  # create group of 3 lines, sort by smallest length
  grp = sorted([line.strip(), lines[idx*3 + 1].strip(), lines[idx*3 + 2].strip()], key=len)
  # loop over smallest string
  for char in grp[0]:  
    # try to match character in both other strings
    # once match is found, udpate sum and continue to next group of lines
    if char in grp[1] and char in grp[2]:
      sum2 += d[ord(char)]
      break

print(f"Part 1 answer: {sum1}\nPart 2 answer: {sum2}")