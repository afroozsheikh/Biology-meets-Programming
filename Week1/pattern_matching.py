# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    n = len(Genome)
    k = len(Pattern)
    for i in range(n-k+1):
        patt = Genome[i:i+k]
        if patt == Pattern:
            positions.append(i)
    
    return positions