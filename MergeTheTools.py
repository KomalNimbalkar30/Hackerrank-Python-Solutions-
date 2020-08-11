def merge_the_tools(s, k):
    # your code goes here
    num_subsegments = int(len(s) / k)
    #print(num_subsegments)

    for i in range(num_subsegments):
        # Subsegment string
        #print(i*k, i+1,k)
        t = s[i * k : (i + 1) * k]
        #print(t)
        
        # Subsequence string having distinct characters
        u = ""
        
        # If a character is not already in 'u', append
        for c in t:
            if c not in u:
                u += c

        # Print final converted string
        print(u)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
