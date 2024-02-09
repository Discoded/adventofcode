# https://adventofcode.com/2023/day/7
import re
import math

global theFile
def main():
    try: 
        # Open file containing the words separated by a line

        theFile = open("./day7.txt")
        #theFile = open("./day7-practice.txt")
              
    except:
        print("NO FILE")

    iterable = iter(theFile)
    reg_ex = "(\\w+) (\\d+)"
    card_sets = []
    
    # Handle input
    for line in theFile:
        result = re.findall(reg_ex, line)
        card_set = result.pop()
        card_sets.append((card_set[0], int(card_set[1])))

    #  Create a dictionary of the values of the cards
    all_cards = "AKQT98765432J"
    card_values = {}
    card_value = len(all_cards)
    for card in all_cards:
        card_values[card] = card_value
        card_value -= 1
    print(card_values)

    # Determine rank
    same_card_count = 0
    pair = []
    pair_count = 0
    j_count = 0
    hands_by_rank = [[] for x in range(0, 7)]

    for hand_bid in card_sets:
        print("Hand: ", hand_bid)
        for i, card in enumerate(hand_bid[0]):
            if(card == 'J'):
                    j_count += 1
            #print(i)
            for next_card in hand_bid[0][i+1:]:
                if i == 4:
                    break
                #print(i, card, next_card)
                
                if (card == next_card):
                    same_card_count += 1
                    pair.append(card+next_card)

        

        if pair != []:
            pair_count = find_count(pair)

        
        print("same_card_count", same_card_count)
        print("pair_count: ", pair_count)
        print("j_count: ", j_count)
        print("pair: ", pair)
        

        if(same_card_count == 1):
            
            rank = 1
            
            if(j_count) == 0:
                print("One pair")
            elif j_count == 1:
                print("One pair to Three of a kind")
                rank = 3
            # ABCJJ one pair -> 3OAK
            elif j_count == 2:
                rank = 3
                print("One pair to Three of a kind")
            else:
                raise Exception("One Pair error")
            hands_by_rank[rank].append(hand_bid)
        elif(same_card_count == 2):
            
            rank = 2
            if j_count == 0:
                rank = 2
                print("Two pair")
            elif j_count == 1:
                rank = 4
                print("Two pair to Full house")
            elif j_count == 2:
                rank = 5
                print("Two pair to Four of a kind")
            else:
                raise Exception("Two Pair error")
            hands_by_rank[rank].append(hand_bid)
            
        elif same_card_count == 4 and pair_count == 3:
            rank = 4
            if j_count == 2:
                rank = 6
                print("Full house to Five of a kind")
            else:
                print("Full house")
            hands_by_rank[rank].append(hand_bid)
        elif same_card_count == 6:
            rank = 5
            if j_count == 1:
                rank = 6
                print("Four of a kind to Five of a kind")
            else:
                print("Four of a kind")
            hands_by_rank[rank].append(hand_bid)
        elif same_card_count == 3:
            rank = 3
            if j_count == 1:
                rank = 4
                print("Three of a kind to Four of a kind")
            elif j_count == 3:
                if pair_count == 1:
                    rank = 6
                    print("Three of a kind to Five of a kind")
                else:
                    rank = 5
                    print("Three of a kind to Four of a kind")
            else:
                print("Three of a kind")
            hands_by_rank[rank].append(hand_bid)
        elif same_card_count == 10:
            rank = 6
            print("Five of a kind ")
            hands_by_rank[6].append(hand_bid)
        else:
            rank = 0
            if j_count == 1:
                print("High card to one pair")
                rank = 1
            else:
                print("High card")
            hands_by_rank[rank].append(hand_bid)
        print()

        same_card_count = 0
        pair = []
        pair_count = 0
        j_count = 0

    #[print(x) for x in hands_by_rank]

    iterable = iter(hands_by_rank)
    out = next(iterable)
    ranked_hands = []
    labels = ["High card: ", "One pair:  ", "Two pair:  ", "THREE:     ", "FullHouse: ", "FOUR:      ", "FIVE:   "]
    i = 0
    while True:
        try:
            if out:
                out.sort(key=lambda e: (card_values[e[0][0]], card_values[e[0][1]], card_values[e[0][2]], card_values[e[0][3]], card_values[e[0][4]]))
                
                
                for hand in out:
                    ranked_hands.append(hand)
            print(labels[i], out)
            i+=1
            out = next(iterable)
        except:
            break
    
    
    print("Ranked hands: ", ranked_hands)

    total_winnings = 0

    for i, hand in enumerate(ranked_hands):
        total_winnings += (i+1)*hand[1]
    print("total_winnings: ", total_winnings)


def find_count(theArray: list):
    if not theArray:
        return 0
    count = 0
    first = theArray[0]
    for elem in theArray[1:]:
        if(elem == first):
            count += 1


    return count + find_count(theArray[1:])

"""Given a hand, determine the type
"""
def determine_type(theHand: str):
    if not theHand:
        return []
    pair = []
    i = 0
    card0 = theHand[0]
    for card in theHand[1:]:
        if(card0 == card):
            pair.append(card + card0)
        print(i, card0, card)
        i+=1
    

    return pair + determine_type(theHand[1:])




main()
