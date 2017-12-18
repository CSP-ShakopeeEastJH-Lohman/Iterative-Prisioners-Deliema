#Raj Test Panda Silver
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Raj' # Only 10 chars displayed.
strategy_name = 'Collude, if Betrayed then betray'
strategy_description = 'If they vetray, btray everysingle time. If they dont, collude'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
        return 'c'
    if len(my_history) == 199:
        return 'b'
    if my_history[-1] == 'b':
       return 'b' 
    if len(my_history) < 2 and their_history[-1] == 'c':
        return 'c'
    if their_history[-2] == 'c' and their_history[-1] == 'c':
        return 'c'
        my_score += 1100
    if their_history[-1] == 'b':
        return 'b'
    if len(my_history) == 199:
        return 'b'

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.