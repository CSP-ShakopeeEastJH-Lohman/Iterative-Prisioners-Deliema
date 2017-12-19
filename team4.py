team_name = 'Max_Dom' # Only 10 chars displayed.
strategy_name = 'play the player'
strategy_description = 'We play the player not the game'
    
def move(my_history, their_history, my_score, their_score):
    
    if my_history == []:
        return 'c'
    
    if their_history [-1] == 'b':
        if their_history [-2] == 'b':
            return 'b'
            
    if their_history [-1] == 'b':
        return 'c'
        
    if their_score > my_score:
        return 'c'
        
    if my_history [-1] == 'c':
        if my_history [-2] == 'c':
            if their_history [-1] == 'b':
                if their_history [-2] == 'b':
                    return 'b'
                    
    if their_score > my_score:
        if their_history [-1] == 'b':
            return 'b'
            
    else: 
        return 'c'

my_history = []
their_history = [] 
my_score = 0
their_score = 0
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
