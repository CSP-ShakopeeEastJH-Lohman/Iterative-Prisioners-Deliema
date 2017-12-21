team_name = 'Max_Dom' # Only 10 chars displayed.
strategy_name = 'physolmololgy'
strategy_description = 'We read the other players mind'
    
def move(my_history, their_history, my_score, their_score):
    
    if len(my_history) < 2:
        return 'c'
    
    if their_history [-1] == 'b':
        if their_history [-2] == 'b':
            return 'b'
          
    if len(my_history) > 197:
        return 'b'
          
    if their_history [-1] == 'c':
        if their_history [-2] == 'c':
            return 'c'
            
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

