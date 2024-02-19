class Solution(object):
    def mostFrequentPrime(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        prime_number_count = {} #key: prime number, value = frequency
        
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        
        row, col = len(mat), len(mat[0])
        
        def is_prime(number):
            if number < 2:
                return False
            # when I use number/2 instead of number ** 0.5, time limit exceed error happens
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    return False
            return True
        
        def travel_path(i, j, dx, dy):
            curr_x, curr_y = i, j
            number = 0
            curr_number = ""
            while 0<= curr_x < row and 0 <= curr_y < col:
                curr_number += str(mat[curr_x][curr_y])
                curr_number_int = int(curr_number)
                # number = number * 10 + mat[curr_x][curr_y]
                if len(curr_number) == 1 or curr_number_int == 10:
                    curr_x = curr_x + dx
                    curr_y = curr_y + dy
                    continue
                if is_prime(curr_number_int):
                    print(curr_number_int)
                    prime_number_count[curr_number_int] = prime_number_count.get(curr_number_int, 0) + 1
                curr_x = curr_x + dx
                curr_y = curr_y + dy
                # if is_prime(number) and number > 10:
                #     prime_number_count[number] = prime_number_count.get(number, 0) + 1
                # curr_x = curr_x + dx
                # curr_y = curr_y + dy
                
        for i in range(row):
            for j in range(col):
                for dx, dy in directions:
                    travel_path(i, j, dx, dy)
            
        
        if not len(prime_number_count): return -1
        
        res = 0
        most_frequency = 0
        
        for key, value in prime_number_count.items():
            if value > most_frequency:
                res = key
                most_frequency = value
            if value == most_frequency and key > res:
                res = key
                
        return res
            
                
        
        
