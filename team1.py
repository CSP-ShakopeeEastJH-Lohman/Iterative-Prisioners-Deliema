#Makayla the best around town

team_name = 'makayla'
strategy_name = 'coolio'
strategy_description = 'Tit for tat, check for repetitive patterns.'  
    
def move(my_history, their_history, my_score, their_score):
    '''basic start'''
    if len(my_history) < 3:
        return 'c'
        
    '''checking for very repetitive patterns'''
    if their_history[-1: -4] == 'b':
        return 'b'
    if their_history[-1: -4] == 'c':
        return 'b'
        
    '''general strat'''
    '''tit for tat
     once an opponent defects, the tit for tat player immediately responds by defecting on the next move'''
    if their_history[-1] == 'b':
        return 'b'
    if their_history[-1] == 'c':
        return 'c'
        
    '''tit for two tats
    if their_history[-1] and their_history[-2] == 'b':
        return 'b'
    if their_history[-1] and their_history[-2] == 'c':
        return 'c'
    '''
    
    '''score plans'''
    if their_score > 0:
        if their_history[-1] == their_history[-3]:
            if their_history[-1] == 'c':
                return 'b'
            elif their_history[-1] == 'b':
                return 'c'
        if their_history[-1] == 'c':
            return 'b'
        elif their_history[-1] == 'b':
            return 'c'
        if their_history[-1] == their_history[-5]:
            if their_history[-1] == 'b':
                return 'c'
            if their_history[-1] == 'c':
                return 'b'
    if my_score < 0:
        return 'b'