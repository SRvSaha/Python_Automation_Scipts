# @author : SRvSaha
# Description : Automated Updation of score & winner decider for Badminton,
#               Shaurya'17
# Timestamp : 11.49 AM 06-Mar-2017

match_id = int(input("Enter the current Match ID: "))
t2score = t1score = 0
if match_id <= 6:
    while(t1score <= 20 and t2score <= 20):
        entered = int(input("Enter 1 if t1 won the point and 2 if t2 : "))
        if entered == 1:
            t1score += 1
        else:
            t2score += 1

        ###############
        ##  TESTING  ##
        ###############
        # For Manual Testing
        # t1score = int(input("Team 1 score : "))
        # t2score = int(input("Team 2 score: "))
        print("Team 1 score ", t1score)
        print("Team 2 score ", t2score)
        if t1score == 15 and t2score <= 13:
            print("Winner : Team 1")
            break
        elif t2score == 15 and t1score <= 13:
            print("Winner : Team 2")
            break
        elif t1score >= 14 and t2score >= 14:
            if t1score == 20 and t2score < 20:
                print("Winner : Team 1")
                break
            elif t2score == 20 and t1score < 20:
                print("Winner : Team 2")
                break
            else:
                if t1score - t2score == 2:
                    print("Winner Team 1")
                    break
                elif t2score - t1score == 2:
                    print("Winner Team 2")
                    break
else:
    while(t1score <= 30 and t2score <= 30):
        entered = int(input("Enter 1 if t1 won the point and 2 if t2 : "))
        if entered == 1:
            t1score += 1
        else:
            t2score += 1

        ###############
        ##  TESTING  ##
        ###############
        # For manual testing
        # t1score = int(input("Team 1 score : "))
        # t2score = int(input("Team 2 score: "))
        # For Automated TESTING
        # t1score, t2score = tuple(map(int, input().strip().split()))
        print("Team 1 score ", t1score)
        print("Team 2 score ", t2score)
        if t1score == 21 and t2score <= 19:
            print("Winner : Team 1")
            break
        elif t2score == 21 and t1score <= 19:
            print("Winner : Team 2")
            break
        elif t1score >= 20 and t2score >= 20:
            if t1score == 30 and t2score < 30:
                print("Winner : Team 1")
                break
            elif t2score == 30 and t1score < 30:
                print("Winner : Team 2")
                break
            else:
                if t1score - t2score == 2:
                    print("Winner Team 1")
                    break
                elif t2score - t1score == 2:
                    print("Winner Team 2")
                    break
