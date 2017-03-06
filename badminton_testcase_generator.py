# @author = SRvSaha
# Description : The test cases generation code for Badminton Match of 21 pts.
# Timestamp : 2.05 PM 06-Mar-2017

t1score = 21
t2score = 0
# Cases when Team 1 win
while t2score <= 19:
    print(t1score, t2score)
    t2score += 1

t1score = 0
t2score = 21
# Cases when Team 2 win
while t1score <= 19:
    print(t1score, t2score)
    t1score += 1

# Cases of Deuce and then Team 2 wins
t1score = 20
t2score = 20

while t1score <= 28:
    print(t1score, t2score + 2)
    t1score += 1
    t2score += 1

# Cases of Deuce and then Team 1 wins
t1score = 20
t2score = 20

while t2score <= 28:
    print(t1score+2, t2score)
    t1score += 1
    t2score += 1

# Corner Case : When a Team scores 30 first, he wins. Here Team 2 wins
t1score = 29
t2score = 30
print(t1score, t2score)

# Corner Case : When a Team scores 30 first, he wins. Here Team 1 wins
t1score = 30
t2score = 29
print(t1score, t2score)

# Cases of Deuce when difference of point is 1 => No Winner
t1score = 20
t2score = 20

while t2score <= 28:
    t1score += 1
    print(t1score, t2score)
    t2score += 1

t1score = 20
t2score = 20

while t1score <= 28:
    t2score += 1
    print(t1score, t2score)
    t1score += 1
