def ff(n):
    s=n+1
    for i in range(n-1):
        print(' '*i,i+1,' '*s,i+1,' '*i)
        s-=2
    j=4
    print(' '*j,j,' '*s,' '*j)
    s=n-3
    for i in range(n-1,0,-1):
        print(' '*(i-1),i,' '*s,i,' '*(i+1))
        s+=2
        
ff(4)

'''
 1       1 
  2     2  
   3   3   
     4      
   3   3     
  2     2    
 1       1   
'''