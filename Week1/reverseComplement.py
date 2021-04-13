def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern


# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    # your code here
    str_tmp = ''
    for char in Pattern:
        str_tmp = char + str_tmp
    return str_tmp


## second solution
# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    # your code here
    str_tmp = ''
    ls = [i for i in Pattern]
    ls.reverse()
    str_tmp = ''.join([i for i in ls])
    
    return str_tmp


# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
def Complement(Pattern):
    # your code here
    dic = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    ls = [dic[i] for i in Pattern]
    str_tmp = ''.join([i for i in ls])
    return str_tmp 
