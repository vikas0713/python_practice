team1_count = 0
team2_count = 0
a, b, c = input("enter the elements for team1:").split()
print("enter the first element of team1", a)
print("enter the first element of team1", b)
print("enter the first element of team1", c)
d, e, f = input("enter the elements for team2:").split()
print("enter the first element of team2", d)
print("enter the first element of team2", e)
print("enter the first element of team2", f)

if a > d:
    team1_count += 1
else:
    team2_count += 1

if b > e:
    team1_count += 1
else:
    team2_count += 1
if c > f:
    team1_count += 1
else:
    team2_count += 1
print("score of the team1 is", team1_count)
print("score of team2 is", team2_count)










