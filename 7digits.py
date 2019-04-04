'''
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7]
'''

class Solution:
	def convertToBase7(self, num: int) -> str:
		r = []
		re = ''
		if num < 0:
			re += '-'
			num = -num

		num = abs(num)

		while 1:
			r.append(num % 7)
			num = num // 7
			if num == 0:
				break
		for i in r[::-1]:
			re += str(i)

		return re


if __name__ == '__main__':
	sol = Solution()
	print(sol.convertToBase7(0))
