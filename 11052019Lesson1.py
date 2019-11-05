#一般设计程序的过程：
#1.始于自己模糊的理解。在此步，收集可能需要的概念与细节；
#2.提炼自己的理解，形成对问题的描述
#3.变换成可以代码化的对象
#4.可运行的代码

#德州扑克程序设计 讲解
#def poker(hands):
#    "Return the best hand: poker([hand,...]) => hand"
#    return max()# max is a function that takes a list as input and returns the highest ranking one.
print(max([3, 4, 5, 0]), max([3, 4, -5, 0], key=abs))

# -----------
# User Instructions
# 
# 1st
# Modify the poker() function to return the best hand 
# according to the hand_rank() function. Since we have
# not yet written hand_rank(), clicking RUN won't do 
# anything, but clicking SUBMIT will let you know if you
# have gotten the problem right. 
#

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return(max(hands, key=hand_rank))#enter your code here. Your return should call max()

#def hand_rank(hand):
#    return None # we will be changing this later.

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    # Your code here.
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result


def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    
    ranks = ['--23456789TJQKA'.index(r) for r, s in cards]
    ranks.sort(reverse=True)
    return ranks

print(card_ranks(['AC', '3D', '4S', 'KH']))#should output [14, 13, 4, 3]

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))# your code here
    elif flush(hand):                              # flush
        return (5, ranks)# your code here
    elif straight(ranks):                          # straight
        return (4, max(ranks))# your code here
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)# your code here
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)# your code here
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)# your code here
    else:                                          # high card
        return (0, ranks)# your code here



# 2nd
# Modify the test() function to include two new test cases:
# 1) four of a kind (fk) vs. full house (fh) returns fk.
# 2) full house (fh) vs. full house (fh) returns fh.
def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    # Your code here.
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    "Return True if all the cards have the same suit."
    # Your code here.
    suits = [s for r, s in hand]
    return len(set(suits)) == 1

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Your code here.
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    # Your code here.
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # => ['6C', '7C', '8C', '9C', 'TC'] # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return 'tests pass'
    # Add 2 new assert statements here. The first 
    # should check that when fk plays fh, fk 
    # is the winner. The second should confirm that
    # fh playing against fh returns fh.
    
print(test())

# 3rd
# Modify the test() function to include two new test cases:
# 1) A single hand.
# 2) 100 hands.


# 4th
# Modify the test() function to include three new test cases.
# These should assert that hand_rank gives the appropriate
# output for the given straight flush, four of a kind, and
# full house.
#
# For example, calling hand_rank on sf should output (8, 10)

# 5th
# Modify the hand_rank function so that it returns the
# correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair,
# pair, and high card hands. 
# 
# Do this by completing each return statement below.
#
# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens 
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function 
#                  returns their corresponding ranks as a 
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks 
#                  in a hand (where the order goes from
#                  highest to lowest rank). 

# 6th
# Modify the test() function to include three new test cases.
# These should assert that card_ranks gives the appropriate
# output for the given straight flush, four of a kind, and
# full house.
#
# For example, calling card_ranks on sf should output  
# [10, 9, 8, 7, 6]
#

# 7th
# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10, 
# 'J' to 11, etc...


# 8th
# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.

# 9th
# Define a function, kind(n, ranks).

# 10th
# Define a function, two_pair(ranks).

# 11st
# Write a function, allmax(iterable, key=None), that returns
# a list of all items equal to the max of the iterable, 
# according to the function specified by key. 


# Write a function, deal(numhands, n=5, deck), that 
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]
    # Your code here.