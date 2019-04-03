'''
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
'''

class Solution:
	def addBinary(self, a: str, b: str) -> str:
		end = ''
		carry = False
		while len(a) != len(b):
			if len(a) > len(b):
				b = '0' + b
			else:
				a = '0' + a
		for i in range(len(a)-1, -1, -1):
			if a[i] == '1' and b[i] == '0' and carry == False or a[i] == '0' and b[i] == '1' and carry == False:
				end = '1' + end
			elif a[i] == '1' and b[i] == '0' and carry == True or a[i] == '0' and b[i] == '1' and carry == True:
				end = '0' + end
			elif a[i] == '1' and b[i] == '1' and carry == False:
				end = '0' + end
				carry = True
			elif a[i] == '0' and b[i] == '0' and carry == False:
				end = '0' + end
			elif a[i] == '1' and b[i] == '1' and carry == True:
				end = '1' + end
			elif a[i] == '0' and b[i] == '0' and carry == True:
				end = '1' + end
				carry = False

		if carry:
			end = '1' + end

		return end

if __name__ == '__main__':
	sol = Solution()
	print(sol.addBinary('11','1'))