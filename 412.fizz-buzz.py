#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#


# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        :type n:int
        "rtype: List[str]
        """
        # answer list
        ans = []

        # Ordered dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = collections.OrderedDict([(3, "Fizz"), (5, "Buzz")])

        for i in range(1, n+1):
            num_ans_str = ""
            for key in fizz_buzz_dict.keys():

                # If the num is divisible by key,
                # then add the corresponding string mapping
                # to current num_ans_str
                if i % key == 0:
                    num_ans_str += fizz_buzz_dict[key]

            if not num_ans_str:
                num_ans_str = str(i)

            ans.append(num_ans_str)

        return ans
# @lc code=end
