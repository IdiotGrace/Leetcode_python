'''
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
给出两个整数 x 和 y，计算它们之间的汉明距离。
注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。
'''
	
class Solution:
    def hanmingDistance(self, x, y):
    	"""
		:type x: int
		:type y: int
		:rtype: int
		"""
        string = bin(x ^ y)
        count = 0
        for s in string:
            if s == "1":
                count += 1
        return count

if __name__ == '__main__':
	sol = Solution()
	print(sol.hanmingDistance(1, 4))
