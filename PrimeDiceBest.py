#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:41:48 2020

@author: marekdziergas
"""


import random
bankroll = 1
defaultwager = 0.01
wager = 0.01
wagered = 0
rolls = 0
payout = 2
wins = 0
losses = 0
loss_streak = 0
win_streak = 0
longest_loss_streak = 0
longest_win_streak = 0

while wager<bankroll:
    roll = random.uniform(1, 100)
    rolls +=1
    if roll < 50.49:
        bankroll -= wager
        wager = wager*2
        losses +=1
        loss_streak +=1
        win_streak = 0
        if loss_streak > longest_loss_streak:
            longest_loss_streak = loss_streak
        
       
       
    else: 
        bankroll = bankroll + (wager * payout)
        wager = defaultwager
    
        wins +=1
        loss_streak = 0
       
    
print("Bust")
print (f'Rolls: {rolls}')
print (f'Bankroll: {bankroll:.8f}')
print ('Longest loss streak:', longest_loss_streak)