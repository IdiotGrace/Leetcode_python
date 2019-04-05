'''
包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

示例 1:

输入:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
输出:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
注意:

给定矩阵中的整数范围为 [0, 255]。
矩阵的长和宽的范围均为 [1, 150]。
'''
import copy
class Solution:
	def imageSmoother(self, M):
		'''
		:type M: List[List[int]]
		:rtype: List[List[int]]
		'''
		col = len(M)
		row = len(M[0])
		N = copy.deepcopy(M)
		S = 0

		for i in range(col):
			for j in range(row):
				S += N[i][j]

		if col == 1 and row < 3:
			for j in range(row):
				M[0][j] = S//row

		elif col == 1 and row >= 3:
			M[0][0] = (N[0][0] + N[0][1])//2
			M[0][-1] = (N[0][-2] + N[0][-1])//2
			for j in range(1, row-1):
				M[0][j] = (N[0][j-1] + N[0][j] + N[0][j+1])//3

		elif col < 3 and row == 1:
			for i in range(col):
				M[i][0] = S//col

		elif col >= 3 and row == 1:
			M[0][0] = (N[0][0] + N[1][0])//2
			M[-1][0] = (N[-2][0] + N[-1][0])//2
			for i in range(1, col-1):
				M[i][0] = (N[i-1][0] + N[i][0] + N[i+1][0])//3

		else:
			for i in range(col):
				for j in range(row):
					if i > 0 and i < col-1 and j > 0 and j < row-1:
						M[i][j] = (N[i-1][j-1] + N[i-1][j] + N[i-1][j+1] + N[i][j-1] + N[i][j] + N[i][j+1] + N[i+1][j-1] + N[i+1][j] + N[i+1][j+1])//9
					elif i == 0 and j == 0:
						M[i][j] = (N[i][j+1] + N[i][j] + N[i+1][j] + N[i+1][j+1])//4
					elif i == 0 and j == row-1:
						M[i][j] = (N[i][j-1] + N[i][j] + N[i+1][j-1] + N[i+1][j])//4
					elif i == col-1 and j == 0:
						M[i][j] = (N[i-1][j] + N[i][j] + N[i-1][j+1] + N[i][j+1])//4
					elif i == col-1 and j == row-1:
						M[i][j] = (N[i][j-1] + N[i-1][j-1] + N[i-1][j] + N[i][j])//4
					elif i > 0 and i < col-1 and j == 0:
						M[i][j] = (N[i-1][j] + N[i][j] + N[i+1][j] + N[i-1][j+1] + N[i][j+1] + N[i+1][j+1])//6
					elif i > 0 and i < col-1 and j == row-1:
						M[i][j] = (N[i-1][j-1] + N[i][j-1] + N[i+1][j-1] + N[i-1][j] + N[i][j] + N[i+1][j])//6
					elif j > 0 and j < row-1 and i == 0:
						M[i][j] = (N[i][j-1] + N[i+1][j-1] + N[i][j] + N[i+1][j] + N[i][j+1] + N[i+1][j+1])//6
					elif j > 0 and j < row-1 and i == col-1:
						M[i][j] = (N[i-1][j-1] + N[i][j-1] + N[i-1][j] + N[i][j] + N[i-1][j+1] + N[i][j+1])//6
		return M


if __name__ == '__main__':
	sol = Solution()
	print(sol.imageSmoother([[1]]))





