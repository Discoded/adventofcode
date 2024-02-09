def find_pair(the_hand: str):
    if len(the_hand) <= 1:
        return []
    pairs = []
    card0 = the_hand[0]
    for card in the_hand[1:]:
        if(card == card0):
            pairs.append(card + card)
        
    return pairs + find_pair(the_hand[1:])

answer = find_pair("JJJJJ") 
print(answer, len(answer))

answer = find_pair("JJJBA") 
print(answer, len(answer))

answer = find_pair("JJCBA") 
print(answer, len(answer))

answer = find_pair("23332") 
print(answer, len(answer))
answer = find_pair("22334") 
print(answer, len(answer))