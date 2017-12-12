#Peter and Michael - Purple Mayonaise
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team Dio' # Only 10 chars displayed.
strategy_name = 'ZA WURDO'
strategy_description = 'Anaylze their_history for patterns and counter them'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. g
    '''
    if len(my_history) == 0 or 1:
        return 'b'
    if their_history[-1] == their_history[-3]: #cbc/bcb counter
        if their_history[-1] == 'c':
            return 'b'
        if their_history[-1] == 'b':
            return 'c'
    if their_history[-1] == their_history[-4]: #cbb/bcc counter
        if their_history[-1] == 'c':
            return 'b'
        if their_history[-1] == 'b':
            return 'c'
    if their_history[-1] == their_history[-5]: #cccb/bbbc counter
        if their_history[-1] == 'b':
            return 'c'
        if their_history[-1] == 'c':
            return 'b'
    if their_history[-1] and their_history[-4] == 'c': #ccccc to c
        if their_history[-2] and their_history[-3] == 'c':
            return 'c'
    if their_history[-1] and their_history[-2] == 'c': #cc to b
        return 'b'
    if their_history[-1] and their_history[-2] == 'b': #bb to b
        return 'b'
    if their_history[-1] != their_history[-2]: #cb/bc
        if their_history[-1] == 'b':
            return 'c'
        if their_history[-1] == 'c':
            return 'b'
        
    
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
