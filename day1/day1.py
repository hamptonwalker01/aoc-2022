# open file and read all lines
lines = open("day1.txt", "r").readlines()

# max 3 values seen and temp sum variable
m = [0, 0, 0]
s = 0

# Function to compare temp sum with max 3 values
# updates max values when appropraite
def update_max(s):
  for (idx, item) in enumerate(m):
    if s > item:
      m[idx] = s
      return 0
  return 0
  
# Main loop - loop through lines and sum values
# if we encounter a newline -> try to update max values seen
for line in lines:
  if (len(line.strip()) == 0):
    s = update_max(s)
  else:
    s += int(line.strip())
# call update_max one final time
update_max(s)

print(f"\nMost weight carried by elf: {m[0]}") # Answer to question 1
print(f"Sum of top 3 weights: {sum(m)}") # Answer to question 2