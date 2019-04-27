def minAddToMakeValid(S):
// Input: "())"
// Output: 1
     count = 0
     stack = []
        
     for b in S:
        if b == ')':
            if len(stack)>0 and stack[len(stack)-1] == '(':
                del stack[len(stack)-1]
            else:
                count = count +1
        else:
            stack.append('(')
        for c in stack:
            count +=1
        return count
