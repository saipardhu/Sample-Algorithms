import sys
import os
def rec(rolls, dice):
    # rolls_original = rolls + 1
    if rolls == 1:
        return float(3.50)
    else:
        expected_prev_val = rec(rolls-1, dice)
        large_set =[]
        small_set = []
        # large_set = [x for x in dice if x > expected_prev_val]
        for throw in dice:
            if throw > expected_prev_val:
                large_set.append(throw)
        # small_set = [x for x in dice if x <= expected_prev_val]
        for throw in dice:
            if throw <= expected_prev_val:
                small_set.append(throw)
        print ("Roll " + str(rolls))
        # print "Rolls_original" + str(rolls_original)
        # expected_new_val = ((len(large_set)/len(fair_dice)) * (sum(large_set)/len(large_set))) + ((len(small_set)/len(fair_dice)) * (sum(small_set)/len(large_set)))
        expected_new_val = ((float(len(large_set))/len(dice)) * (float(sum(large_set))/len(large_set))) + ((float(len(small_set))/len(dice)) * float(expected_prev_val))
        return expected_new_val

def die_game_fair_value(rolls):
    dice = [1,2,3,4,5,6]
    expected_new_val = rec(rolls, dice)
    return int(float(expected_new_val) * 10000)

print (die_game_fair_value(25))