""" Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
Example: Given digit string as'2' the fucntions must return [a,b,c]. Given digit string as '23, it must return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]"""
class Solution:
    def letterCombinations(self, digits):
        res = []
        if (digits == ""):
            return res
        #Storing the mapped letter for the digits in dictionary
        nums = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'],
                "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}
        res = nums[digits[0]]
        return self.combs(nums, digits, 1, res)

    #combs returns the combination of two digits
    def combs(self,nums,digits,index,res):
        #if the value of index is same as the length of input, it returns the array of current stored combinations
        if (index == len(digits)):
            return res
        temp = nums[digits[index]] #temporary array to store the next incoming dictionary value of array letters
        new_res = []  #stores the new combination of letters
        for elem1 in res:
            for elem2 in temp:
                new_res.append(elem1 + elem2)
        return self.combs(nums, digits, index + 1, new_res) #incrementing the index bring the next digit in the string and new_res uses the latest combination as input for creating the combination with the new index digit

if __name__=='__main__':
    sol = Solution()
    a= sol.letterCombinations('23')
    print(a)




