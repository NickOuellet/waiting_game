import time
import random
import math as m

def waiting_game():
    goal = random.randrange(2,5,1)
    print("You're goal is %d seconds" % goal)

    input("---Press Enter when you are ready to start the game---")
    init_time = time.time()
    user_input = input("...press enter after %d seconds have passed ..." % goal)
    final_time = time.time()
    elapsed_time = final_time - init_time
    print("You're time was %.3f seconds" % elapsed_time)
    score = abs(elapsed_time - goal)
    if elapsed_time > goal:
        print("(You were %.3f seconds too slow)" % score)
    if elapsed_time < goal:
        print("(You were %.3f seconds too fast)" % score)
    if elapsed_time == goal:
        print("Wow! You were spot on! Nice job.")
        print("(You're elapsed time was %.2f seconds)" % elapsed_time)
    return score
waiting_game()
