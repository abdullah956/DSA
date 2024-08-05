from typing import List
from unittest import result


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        results=[]
        rows = len(img)
        print("number of rows :",rows)
        cols = len(img[0])
        print("number of columns  :",cols)

        for r,row in  enumerate(img):
            print("first for loop :")
            print("index of row : ",r,"value at index of row: ",row)

            results.append([])
            print("after appending empty list in results : ",results)

            for c,column in enumerate(row):
                print("second for loop :")
                print("index of column",c,"value at index of column: ",column)

                s=0
                print("sum : ",s)

                count=0

                for dx in range(-1,2) :
                    print("third for loop :")
                    print("value of dx :",dx)

                    for dy  in range(-1,2) :
                        print("forth for loop :")
                        print("value of dy:",dy)

                        print("outside if : r+dx :",r+dx," rows :",rows," c+dy :",c+dy,"cols :",cols)

                        if r+dx>=0 and r+dx<rows and c+dy>=0 and c+dy<cols :
                            print("inside if : r+dx :",r+dx," rows :",rows," c+dy :",c+dy,"cols :",cols)

                            s += img[r+dx][c+dy]

                            print("img in if :",img[r+dx][c+dy])

                            print("sum in if :",s)

                            count+=1
                            print("count in if :",count)
                
                print("avg : ",s//count)
                results[-1].append(s//count)     
                print("results : ",results)
        return results
img = [[100,200,100],[200,50,200],[100,200,100]]
s=Solution()
print("output : ",s.imageSmoother(img))