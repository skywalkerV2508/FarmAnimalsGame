
"""
import random

class Solution:
    def isScramble(self, s1: str, s2: str):

        def first_process(s1):
            string_length = len(s1)
            random_index = random.randint(1, string_length + 1)
            first_part = (s1[:random_index])
            second_part = (s1[random_index:])
            return first_part, second_part

        def second_process(s1, s2):
            def swap(s1, s2):
                s1, s2 = s2, s1
                return s1, s2
            
            if random.randint(0, 1) == 0:
                return swap(s1, s2)
            else:
                return s1, s2
        
        def third_process(s1, s2):
            s3 = s1 + s2
            s3 = s3.replace(' ', '')
            print(s3)
            return s3
        i = 0 
        while True:
            i += 1
            first_part, second_part = first_process(s1)
            print(first_part, second_part)
            first_part2, second_part2 = second_process(first_part, second_part)
            print(first_part2, second_part2)
            first_part3, second_part3 = first_process(first_part2)
            first_part4, second_part4 = first_process(second_part2)
            print(first_part3, second_part3)
            print(first_part4, second_part4)
            first_part5 = first_part3 + " " + first_part4
            second_part5 = second_part3 + " " + second_part4
            first_part6, second_part6 = second_process(first_part5, second_part5)
            print(first_part6, second_part6)
            res = third_process(first_part6, second_part6)
            if res == s2:
                break
            if i == 100:
                break
"""
import random

class Solution:
    def isScramble(self, s1: str, s2: str):

        def first_process(s1):
            string_length = len(s1)
            random_index = 2
            first_part = (s1[:random_index])
            second_part = (s1[random_index:])
            return first_part, second_part

        def second_process(s1, s2):
            def swap(s1, s2):
                s1, s2 = s2, s1
                return s1, s2
            
            if random.randint(0, 1) == 0:
                return swap(s1, s2)
            else:
                return s1, s2
        
        def third_process(s1, s2):
            s3 = s1 + s2
            s3 = s3.replace(' ', '')
            print(s3)
            return s3
        i = 0 
        while True:
            i += 1
            first_part, second_part = first_process(s1)
            print(first_part, second_part)
            first_part2, second_part2 = second_process(first_part, second_part)
            print(first_part2, second_part2)
            first_part3, second_part3 = first_process(first_part2)
            first_part4, second_part4 = first_process(second_part2)
            print(first_part3, second_part3)
            print(first_part4, second_part4)
            first_part5 = first_part3 + " " + first_part4
            second_part5 = second_part3 + " " + second_part4
            first_part6, second_part6 = second_process(first_part5, second_part5)
            print(first_part6, second_part6)
            res = third_process(first_part6, second_part6)
            if res == s2:
                break
            if i == 100:
                break












c = Solution()
c.isScramble("great", "rgeat")