def checkStraightLine(coordinates) -> bool:
    def check(coordinates,m=None,b=None,c=None):
        if(c==None):
            for x in coordinates:
                if(x[1]-x[0]*m!=b):
                    return False
        elif (c=='x'):
            for x in coordinates:
                if(x[0]!=m):
                    return False
        elif(c=='y'):
            for x in coordinates:
                if(x[1]!=m):
                    return False
        return True
    if (coordinates[1][1]-coordinates[0][1]==0):
        return check(coordinates,m=coordinates[1][1],c='y')
    elif (coordinates[1][0]-coordinates[0][0]==0):
        return check(coordinates,m=coordinates[1][0],c='x')
    else:
        m = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        b = coordinates[0][1]-coordinates[0][0]*m
        return check(coordinates,m=m,b=b)
   
c = [[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]
checkStraightLine(c)
