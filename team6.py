#Bennett blue cat
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Bennett' # Only 10 chars displayed.
strategy_name = 'Defensive Preservation'
strategy_description = 'Picks pattern and decides'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)== 0:
        return 'c'
    if len(my_history) < 2 and their_history[-1]== 'c':
        return'c'
    if their_history[-1]== 'b':
        return 'b'
    if their_history[-2] == 'c' and their_history[-1]=='c':
        return 'c'
    if their_history[-2] == 'b' and their_history[-1]=='b':
        return 'b'
    if their_history[-2] == 'c' and their_history[-1]=='b':
        return 'c'
    if their_history[-1]=='b':
        return 'b'
    if len(my_history) ==199:
        return 'b'
    if their_history[-1:-4]==['c','c','c','c']:
        return 'c'
    if their_history[-1:-4]==['b','b','b','b']:
        return 'b'
    if their_history[-1:-4]==['c','b','c','b']:
        return 'c'
    if their_history[-1:-4]==['c','c','b','b']:
        return 'b'
    if their_history[-1:-4]==['b','b','c','c']:
        return 'b'
    else:
        return'b'



