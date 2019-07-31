# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 08:56:03 2019

@author: HP
"""

def occurences(s,pos):
    count = 0
    for i in range(pos-1):
        if(s[i] == s[pos-1]):
            count += 1
       
    return count  

if __name__ == '__main__':
    size = int(input())  
    s = input()
    t = int(input())
    
    l = [0]*len(s)
    h = {}
    
    h[s[0]] = 1
    
    for i in range(1,len(s)):
        if s[i] in h:
            l[i] = h[s[i]]
            h[s[i]] += 1
        else:
            h[s[i]] = 1
        

    for i in range(t):
        pos = int(input())
        print(l[pos-1])