###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: llewellyndm
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import os
os.chdir('C:\\Users\\ladm1\\Documents\\Llewellyn\\Python\\MIT Course\\Part 2\\PS1')


#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cow_dict = {}
    COWS1 = open(filename, 'r')
    for line in COWS1:
        k, v = line.strip('\n').split(',')
        cow_dict[k] = int(v)
    COWS1.close()
    return cow_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    def find_cow_that_fits(c, s):
        """
        Parameters
        ----------
        c : dictionary of cows.
        s : integer representing remaining ship capacity.

        Returns
        -------
        name of heaviest cow that fits on ship, or an empty string if no such
        cow exists.
        """
        c_copy = c.copy()
        while len(c_copy) > 0:
            heaviest = max(c_copy, key=c_copy.get) #the heaviest cow
            if c_copy[heaviest] <= s: #if the heabiest cow is not too heavy for ship
                return heaviest
            else:
                del c_copy[heaviest]
        return ''
    
    cows_left = cows.copy()
    trip_list = []
    passengers = []
    capacity = limit
    while len(cows_left) > 0: #while there are cows waiting to be transported
        heaviest = find_cow_that_fits(cows_left, capacity)
        if heaviest != '': #if there is a cow that isn't too heavy
            passengers.append(heaviest)
            capacity -= cows_left[heaviest] # reduce remaining capacity
            del cows_left[heaviest] # takes the cow that has just boarded out of consideration
        else:
            trip_list.append(passengers) #send off current ship and start over with remaining cows
            passengers = []
            capacity = limit
    trip_list.append(passengers) #final ship will break out of loop without 
    # adding to trip_list, this line deals with that
    return trip_list

        
    
# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    final_partition = [0]*len(cows)
    for partition in get_partitions(cows):
        listOfWeights = [] # this will be a list of weights for each trip corresponding to each partition
        for partition_element in partition:
            totalWeight = 0
            for cow in partition_element:
                totalWeight += cows[cow]
            listOfWeights.append(totalWeight)
        if max(listOfWeights) <= limit and len(partition) <len(final_partition):#if each trip is within weight limit AND the number of trips is the smallest found so far
            final_partition = partition
    if final_partition == [0]*len(cows):
        return 'No optimal solution'
    else:
        return final_partition
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    COWS = load_cows('ps1_cow_data.txt')
    
    start = time.time()
    greedy_cow_transport(COWS)
    end = time.time()
    duration = end - start
    print('Greedy algorithm:\nMinimum number of trips =', 
          len(greedy_cow_transport(COWS)),
          '\nTime taken =', duration, 'seconds\n')
    
    start2 = time.time()
    brute_force_cow_transport(COWS)
    end2 = time.time()
    duration2 = end - start
    print('Brute force algorithm:\nMinimum number of trips =', 
          len(brute_force_cow_transport(COWS)),
          '\nTime taken =', duration2, 'seconds')

    
    
