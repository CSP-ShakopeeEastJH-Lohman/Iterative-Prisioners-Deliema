####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
#Description, we collude when they coolude but betray after a few colludes, and we brtray a lot

team_name = 'Lance & Thomas Black Unicorn' # Only 10 chars displayed.
strategy_name = 'Winner'
strategy_description = 'WE collude when they coolude but betray after a few colludes, and we betray a lot'
'
    
def move(my_history,their_history, my_score, their_score):
    if my_history == 0:
        return 'c'
    if my_history == 99:
        return 'b'
    if their_history[-1] and their_history[-2]=='b':
        return 'b'
    if their_history [-1] and their_history [-2] and their_history [-3] and their_history [-4] and their_history [-5] == 'c':
        return 'b'
    if their_history[-1] and their_history[-2] and their_history[-3] == 'c':
        return 'b'
    if their_history[-1] and my_history[-1] == 'c':
        return 'c'
    if my_history == 199:
        return 'b'
    if their_history > 0:
        return 'b' 
    
    
    
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.