#Riley & Aidan Test Pygmy-Marmoset Ratatoskr EmeraldGreen Black
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Ratatoskr!' # Only 10 chars displayed.
strategy_name = 'We cOPy You BEcause We ARe MEEan'
strategy_description = 'Copycatten in a boxen with a flock of moosen'
    
def move(my_history, their_history, my_score, their_score):
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

    if len(my_history) == 0:
        return 'c'

    elif len(their_history) == 199:
        return 'b'
        
    if my_history[-1] == 'c' and my_history[-2] == 'b' and my_history[-3] == 'c' and my_history[-4] == 'b':
        return 'c'
    
    elif their_history[-1] == 'c':
            return 'c'

    elif their_history[-1] == 'b':
        return 'b'
