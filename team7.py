####
#Description, we collude when they coolude but betray after a few colludes, and we brtray a lot

team_name = 'Lance & Thomas Black Unicorn' # Only 10 chars displayed.
strategy_name = 'collude and betray when pattern is present'
strategy_description = 'WE collude when they collude but betray after a few colludes, and we betray a lot'

    
def move(my_history,their_history, my_score, their_score):
    if my_history == 0:
        return 'c'
    if my_history == 99:
        return 'b'
    if their_history[-1] == 'b' and their_history[-2] =='b':
        return 'b'
    if their_history [-1] == 'c' and their_history [-2] == 'c' and their_history [-3] == 'c':
        return 'c'
    if their_history[-1] == 'c' and my_history[-1] == 'c':
        return 'c'
    if my_history == 199:
        return 'b'
    if their_score > 0:
        return 'b' 
    else:
        return 'c'
    
    
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