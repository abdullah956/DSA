from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newcolor: int) -> List[List[int]]:
        if image[sr][sc] == newcolor: #if color is already same just return
            return image
        self.fill(image, sr, sc, image[sr][sc],newcolor) 
        return image
    def fill(self, image, sr, sc,  currentcolor, newcolor) :
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]): #return out of bounds
            return
        if currentcolor != image[sr][sc]:  #if the color does not match the starting color return 
            return
        image[sr][sc] = newcolor # if color is same as starting change it
        self.fill(image, sr-1, sc, currentcolor, newcolor) #row column 
        self.fill(image, sr+1, sc, currentcolor, newcolor) #row down
        self.fill(image, sr, sc-1, currentcolor, newcolor) #column left
        self.fill(image, sr, sc+1, currentcolor, newcolor) #column right
        