class Point:

    def __init__(self,x,y,z=None):

        self.x=x
        self.y=y
        self.z=z

    def toString(self):

        if self.z==None:
            print("P(%.2f , %.2f)"%(self.x,self.y))
        else:
            print("P(%.2f , %.2f , %.2f)"%(self.x,self.y,self.z))

Point1=Point(1,2)
Point1.toString()

Point2=Point(1,2,-3)
Point2.toString()
