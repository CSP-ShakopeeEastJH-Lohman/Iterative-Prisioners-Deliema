#Seth & Devin
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Devin & Seth' # Only 10 chars displayed.
strategy_name = '''
Collude all the time unless betrayed in the first ten rounds then'
betray the rest of the game but if they collude the whole time we will betray on round 200
'''
strategy_description = 'Betray if ever betray and betray at the end  '
    

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.

def move(my_history, their_history, my_score, their_score):
    if len(my_history) < 3:
        return 'c'
    if their_history[0] == 'c' and their_history[1] == 'c' and their_history[2] == 'c':
        if len(their_history) == 198:
            return 'b'
        else:
            return 'c'   
    if 'b' in their_history[0:10]: 
        return 'b'
    else:
        return 'c'
        
   