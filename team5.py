#Chloe & Josh
#     move: A function that returns 'c' or 'b'

team_name = 'Chloe and Josh' 
strategy_name = 'Betrayal at last.'
strategy_description = 'If our opponent colludes every time we do as well except for the last round where we return betray.'
    
def move(my_history, their_history, my_score, their_score): 
    if len(my_history) < 3:
        return 'c'
        if their_history[-1] == 'c' and their_history[-2] == 'c':
            return 'c'
    if len(their_history) > 5:
        return 'c'
    else:
        if their_history[-1] == 'b'or their_history[-2] == 'b':
            return 'b'
        elif their_score > 0 and their_history[-1] == 'b' or 'c':
            return 'b'
        else:
            return 'c'
        if their_history[-199] == 'c':
            return 'b'
            
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
