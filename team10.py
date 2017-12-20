#Zach Welna test ants blue
####
# Each team's file must define four tokens:
#     team_name: CB
#     strategy_name:CALUDE 
#     strategy_description: CALUDE EVERY TIME
#     move: A function that returns 'c' or 'b'
####

team_name = 'The name the team gives to itself' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history) < 3:
        return'c'
    if their_history[-1] == 'c' and their_history[-2] == 'c':
        return 'c'
    if their_history[-1] == 'b' and their_history[-2] == 'b':
        return 'b'
    if their_history[-1] == 'b':
        return 'b'
    if their_history[-1] == 'c':
        return 'c'
    
    if their_score> 0:
        return 'b'
    if my_score > their_score:
        return'b'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
    
    
