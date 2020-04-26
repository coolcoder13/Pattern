for i in range(1,6):
    print("* "*i,end='')
    print("  "*(10-i*2),end='')
    print("* "*i)
for i in range(5,0,-1):
    print("* "*i,end='')
    print("  "*(10-i*2),end='')
    print("* "*i)

'''
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
'''