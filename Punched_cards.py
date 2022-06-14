T = int(input())
import numpy as np


for t in range(1,T+1):
    print('Case #'+str(t)+':')
    
    x,y = map(int,input().split(' '))
    
    for i in range(0,int(x*2+1)):
        for j in range(0,int(y*2+1)):
            
            if i == 0 and j == 0:
                print('.',end='')
            
            elif (i == 0 and j == 1): 
                print('.',end='')
                
            elif (j == 0 and i ==1):
                print('.',end='')
            
            elif (i%2 == 0 and j%2 !=0):
                print('-',end='')
            
            elif (i%2 !=0 and j%2 == 0):
                print('|',end='')
                
            elif (i%2 == 0 and j%2 == 0):
                print('+',end='')
                
            elif (i%2 != 0 and j%2 !=0):
                print('.',end='')
        
        print('')
