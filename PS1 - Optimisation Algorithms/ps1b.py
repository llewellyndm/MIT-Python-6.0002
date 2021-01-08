###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
# =============================================================================
#     This solution was adapted from Github user tuthang02's solution:
#     https://github.com/tuthang102/MIT-6.0002-Intro-to-Computational-Thinking-and-Data-Science/blob/master/PS1/ps1b.py
# =============================================================================
    min_eggs = target_weight #minimum number of eggs will be at most the target weight
    
    if target_weight in egg_weights:        
        memo[target_weight] = 1
        return 1
    
    try:
        if memo[target_weight] > 0:
            return memo[target_weight]
    
    except:
        
        for w in [x for x in egg_weights if x <= target_weight]:            
            #now we take an egg of a certain weight, w, and then consider the minimum
            #number of eggs we can take if we want target_weight - w.
            #We do this for each weight in egg_weights
            number_of_eggs = 1 + dp_make_weight(egg_weights, target_weight - w)
            
            if number_of_eggs < min_eggs:
                #if we come across a combination of weights that is less than our 
                #calculated minimum so far, then we set that as the minimum
                min_eggs = number_of_eggs
                memo[target_weight] = min_eggs
                
        return min_eggs
            
    
    

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()