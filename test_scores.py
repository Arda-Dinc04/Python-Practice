#! /usr/bin/usr python3

print("The Test Scores Program" + "\n""\nEnter 3 test scores")     # Title, skip 2 lines, and Enter 3...
# add the equal sign divider below Enter 3...
x = "="
y = 26
product = x * y
print(str(product))

# Get values from user
totalScore = 0
totalScore += int(input("Enter test score: "))
totalScore += int(input("Enter test score: "))
totalScore += int(input("Enter test score: "))

# Calculate the Avg
avgScore = round(totalScore / 3 )

#  display total and avg

print("=" * 26 )
print("Total Score: ", totalScore)
print("Average Score", avgScore)