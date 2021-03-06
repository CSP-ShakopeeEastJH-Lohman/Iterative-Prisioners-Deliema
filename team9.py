
#Zach Owens
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Zachs team' # Only 10 chars displayed.
strategy_name = 'play what they played 2 games ago.'
strategy_description = 'The strategy is to play what they played 2 games ago.'
    
def move(my_history, their_history, my_score, their_score):
    if their_history >= 3:
        return 'c'
    if their_history[-1] and their_history[-2] and their_history[-3] == 'c':
        return 'c'
                        
    elif their_history[-1] and their_history[-2] and their_history[-3] == 'b':
        return 'b'
    else:
        if their_history[-2] == 'c':
            return 'c'
        if their_history[-2] == 'b':
            return 'b' 

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
