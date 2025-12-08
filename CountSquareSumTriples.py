def countTriples(n):
        """
        :type n: int
        :rtype: int
        """
       
        count = 0
        for c in range(1, n+1):
            a = 1
            b = c - 1
            target = c * c
            while a < b:
                
                s = a * a + b * b
                if s == target:
                    count += 2  
                    a += 1
                    b -= 1
                elif s < target:
                    a += 1
                else:
                    b -= 1
        return count
    
print(countTriples(5))