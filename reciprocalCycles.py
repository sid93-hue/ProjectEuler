"""Problem 26"""

from collections import defaultdict
from eulerlib.operations import get_list_of_digits

num_digits = 1000

def longest_subsequence_size(input_list):
    if(len(input_list) > num_digits) : raise Exception ("size of input list = ", len(input_list), "and num_digits =", num_digits)
    
    dp = defaultdict(dict)
    max_length = 0
    
    for j in range(0, len(input_list)):
        for i in range(0, len(input_list)):
            #print("i = ", i, " & j = ", j)
            if(i == j) : 
                dp[i][j] = 0
            elif(i == 0) :  
                if(input_list[0] == input_list[j]):
                    dp[i][j] = 1
                    if(max_length < dp[i][j]) : max_length = dp[i][j]
                else:
                    dp[i][j] = 0
            elif(j == 0) :  
                if(input_list[0] == input_list[i]):
                    dp[i][j] = 1
                    if(max_length < dp[i][j]) : max_length = dp[i][j]
                else:
                    dp[i][j] = 0
            elif(input_list[i] == input_list[j]):
                dp[i][j] = dp[i-1][j-1] + 1
                if(max_length < dp[i][j]) : max_length = dp[i][j]
            else :
                dp[i][j] = 0
            
            #print("dp[", i, "][", j, "] = ", dp[i][j])
            
    return max_length

def get_length_of_recurring_cycle(n):
    
    output_list = []
    numerator = 1
    
    while(len(output_list) < num_digits):
        numerator = numerator * 10
        digit = int(numerator/n)
        output_list.append(numerator)
        if(numerator > n) : numerator = (numerator) - (n * digit)
    
    print(output_list)
    #return output_list
    
    output_list.reverse()
    last_numerator = output_list[0]
    
    for i in range(1, len(output_list)):
        if(output_list[i] == last_numerator):
            break
    
    print("length of recurring sequence of ", n, " = ", i)
    
    return i
        
def main():
    
    answer = 0
    computed_length = 0
    max_length = 0
    
    
    for i in range (2, 1000):
        print("Iteration = ", i)
        computed_length = get_length_of_recurring_cycle(i)
        if(computed_length > max_length) : 
            max_length = computed_length
            answer = i
    
    print("Max_length = ", max_length)
    print("Answer = ", answer)
    print("output_list = ", get_list_of_digits(answer))
    

main()
#n = 7
#print(get_list_of_digits(n))
#print(get_length_of_recurring_cycle(n))
        
        
    