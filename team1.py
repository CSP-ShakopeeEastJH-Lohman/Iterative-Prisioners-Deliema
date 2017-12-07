#Makayla

team_name = 'no bueno'
strategy_name = 'yah'
strategy_description = 'How does this strategy decide?'  
    
def move(my_history, their_history, my_score, their_score):
    '''basic start'''
    if len(my_history) == 0:
        return 'b'
    if len(my_history) == 1:
        return 'c'
        
    '''checks the basic c,b,c,b,c,b pattern'''
    if their_history[-1] == their_history[-3]:
        if their_history[-1] == 'c':
            return 'b'
        elif their_history[-1] == 'b':
            return 'c'
    
    '''checks the c,b,b pattern'''
    if their_history[-1] == their_history[-4]:
        if their_history[-1] == 'c':
            return 'b'
        elif their_history[-1] == 'b':
            return 'c'
    
    '''checks cccb pattern'''
    if their_history[-1] == their_history[-5]:
        if their_history[-1] == 'b':
            return 'c'
        if their_history[-1] == 'c':
            return 'b'
        
    '''basic checks'''    
    if their_history[-1] and their_history[-2] == 'c':
        return 'b'
    if their_history[-1] and their_history[-2] == 'b':
        return 'c'
    if their_history[-3] == 'b':
        return 'b'
