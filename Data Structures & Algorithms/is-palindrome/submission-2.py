class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_list = []


        non_alpha = "! `¬|\,./;'#[]<>?:@~{}-=£$%^&*()_+"
        for char in s:
            if char.isalnum():
                alpha_list.append(char.lower())
        
        alpha_list = "".join(alpha_list)
        alpha_list.strip()

        left = 0
        right = len(alpha_list) - 1

        print(alpha_list)
        while left <= right:
            if alpha_list[left] == alpha_list[right]:
                print(alpha_list[left], alpha_list[right])
                left +=1
                right -=1
            else:
                print(alpha_list[left], alpha_list[right])
                return False
        return True