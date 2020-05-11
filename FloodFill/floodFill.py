       def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        def fill(image,x,y,color,newColor,checked):
            checked.append([sr,sc])
            if(image[x][y]!=color or image[x][y]==newColor): 
                return image
            else:
                image[x][y]=newColor
                if(y+1<len(image[0]) and [x,y+1] not in checked): #x,y+1
                    image = fill(image,x,y+1,color,newColor,checked)
                if(y-1>=0 and [x,y-1] not in checked): #x,y-1
                    image = fill(image,x,y-1,color,newColor,checked)
                if(x+1<len(image) and [x+1,y] not in checked): #x+1,y
                    image = fill(image,x+1,y,color,newColor,checked)
                if(x-1>=0 and [x-1,y] not in checked): #x-1,y
                    image = fill(image,x-1,y,color,newColor,checked)
                return image
        checked=[]
        return fill(image,sr,sc,image[sr][sc],newColor,checked)
        
