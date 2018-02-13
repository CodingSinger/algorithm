
#coding=utf-8


#这道题给我们了一个image数组当做x,y分布的带颜色的图像，不同的数字代表不同的颜色，给了我们一个起始点坐标，还有一个新的颜色，让我们把起始点的颜色以及其相邻(上下左右相邻,不包括对角线)的同样的颜色都换成新的颜色。

#因此我们可以用深度遍历，上下左右一直遍历到底，将相同颜色的图像换成新颜色的

class Solution:
    def helper(self, image, sr, sc, newColor):

        if image[sr][sc] == newColor:
            return image

        oldColor = image[sr][sc]
        self.DFS(image,sr,sc,newColor,oldColor)
        return image



    def DFS(self,image,x,y,newColor,oldColor):


        if x>=len(image) or y >=len(image[0]) or x<0 or y <0 or oldColor!=image[x][y]: #记住需要比较oldColor和该图像的颜色是否一致 不一致不需要变化

            return


        if  image[x][y] != newColor:
            image[x][y] = newColor


        self.DFS(image,x+1,y,newColor,oldColor)
        self.DFS(image,x,y+1,newColor,oldColor)
        self.DFS(image,x-1,y,newColor,oldColor)
        self.DFS(image,x,y-1,newColor,oldColor)


s = Solution()
print(s.helper([[0,0,0],[0,0,0]],0,0,2))
