numberOfRows = 7  
def formatNumber(number):  
  if number<10:  
    return "  "+str(number) + " "  
  else:  
    return " " + str(number) + " "  
row = [1]  
print("  " * 7 + formatNumber(row[0]))  
row.append(1)  
print("  " * 6 + formatNumber(row[0]) + formatNumber(row[1]))  
row.append(2)  
print("  " * 5 + formatNumber(row[0]) + formatNumber(row[1]+row[0]) + formatNumber(row[1]))  
row.append(3)  
print("  " * 4 + formatNumber(row[0]) + formatNumber(row[3]) +formatNumber(row[3]) + formatNumber(row[1]))  
row.append(4)  
print("  " * 3 + formatNumber(row[0]) + formatNumber(row[4]) + formatNumber(row[4]+row[2]) +formatNumber(row[4]) + formatNumber(row[1]))  
row.append(5)  
print("  " * 2 + formatNumber(row[0]) + formatNumber(row[5]) + formatNumber(row[5]+row[5]) + formatNumber(row[5]+row[5]) +formatNumber(row[5]) + formatNumber(row[1]))  

'''

                1 
              1   1 
            1   2   1 
          1   3   3   1 
        1   4   6   4   1 
      1   5  10  10   5   1 
'''