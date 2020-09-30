#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:41:48 2020

@author: marekdziergas
"""


import random
bankroll = 1.8
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
ratio = 0


while wager<bankroll and rolls < 1000000:
    roll = random.uniform(0, 99.99)
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
        win_streak +=1
        wins +=1
        loss_streak = 0
    if win_streak > longest_win_streak:
        longest_win_streak = win_streak                
        
ratio = wins/losses
print("Bust")
print ('Rolls:', rolls)
print ('Bankroll:', bankroll)
print ('Longest loss streak:', longest_loss_streak)
print ('Longest win streak', longest_win_streak)
print ('Wins to Losses:', ratio)
