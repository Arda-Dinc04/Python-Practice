#! /usr/bin/usr python3

# Can use single of double qoutes
name = "Arda"
occupation = 'Student'
tenure = 6
location = "highschool"

results = " \" " + name + "\"  is a " + occupation + \
    " at " + location + \
    " \n and has been for over \' " + \
      str(tenure) + "\' years "


print(results)