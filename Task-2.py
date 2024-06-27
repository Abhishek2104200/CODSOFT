import math
from copy import deepcopy
import numpy as np



x="X"
o="O"
EMPTY =None
def intial_state():
    return [[EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY]]
def get_diagnol(board):
    return[[board[0][0],board[1][1],board[2][2]],
           [board[0][2],board[1][1],board[2][0]]]

def get_columns(board):
    columns=[]
    for i in range(3):
        columns.append([row[i] for row in board])
    
    return columns

def three_in_a_row(row):
    return True if row.count(row[0]) == 3 else False

def player(board):
    count_x=0
    count_o=0
    for i in board:
        for j in i:
            if(j=='X'):
                count_x=count_x+1
            if(j=="O"):
                count_o=count_o+1
    return o if count_x>count_o else x


def actions(board):
    action=set()
    for i,row in enumerate(board):
        for j,vall in enumerate(row):
            if(vall==EMPTY):
                action.add((i,j))
    return action

def result(board,action):
     i,j=action
     if(board[i][j]!=EMPTY):
         raise Exception("Invalid move")
     next_move=player(board)
     deep_board=deepcopy(board)
     deep_board[i][j]=next_move
     return deep_board

def winner(board):
    rows=board+get_diagnol(board)+get_columns(board)
    for row in rows:
        current_player=row[0]
        if current_player is not None and three_in_a_row(row):
            return current_player
    return None

def terminal(board):
    xx=winner(board)
    if(xx is not None):
        return True
    if(all(all(j!=EMPTY for j in i)for i in board)):
        return True
    return False


def utility(board):
    xx==winner(board)
    if(xx == x):
        return 1
    elif(xx == o):
        return -1
    else:
        return 0
    

def max_alpha_beta_pruning(board,alpha,beta):
    if(terminal(board)==True):
        return utility(board),None
    vall=float("-inf")
    best=None
    for action in action(board):
        min_val=min_alpha_beta_pruning(result(board,action),alpha,beta)[0]
        if(min_val>vall):
            best=action
            vall=min_val
        alpha=max(alpha,vall)
        if(beta<=alpha):
            break
    return vall,best

def min_alpha_beta_pruning(board,alpha,beta):
    if(terminal(board)==True):
        return utility(board),None
    vall=float("inf")
    best=None
    for action in actions(board):
        max_val=max_alpha_beta_pruning(result(board,action),alpha,beta)[0]
        if(max_val < vall):
            best=action
            vall=max_val
        beta=min(beta,vall)
        if(beta <= alpha):
            break
    return vall,best


def minimax(board):
    if terminal(board):
        return None
    if(player(board)==x):
        return max_alpha_beta_pruning(board,float("-inf"),float("inf"))[1]
    elif(player(board)==o):
        return min_alpha_beta_pruning(board,float("-inf"),float("inf"))[1]
    else:
        raise Exception("Error in calculating Optimal Move")





