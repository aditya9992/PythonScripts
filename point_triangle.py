# Program to find if a point is within the triangle or not

import math

def point_triangle(point, coord):
     areaTriangle = math.fabs((coord[0][0]*(coord[1][1]-coord[2][1]) + coord[1][0]*(coord[2][1]-coord[0][1]) + coord[2][0]*(coord[0][1]-coord[1][1]))/2)
     
     area1 =  math.fabs((point[0]*(coord[1][1]-coord[2][1]) + coord[1][0]*(coord[2][1]-point[1]) + coord[2][0]*(point[1]-coord[1][1]))/2)
     
     area2 = math.fabs((coord[0][0]*(point[1]-coord[2][1]) + point[0]*(coord[2][1]-coord[0][1]) + coord[2][0]*(coord[0][1]-point[1]))/2)
     
     area3 = math.fabs((coord[0][0]*(coord[1][1]-point[1]) + coord[1][0]*(point[1]-coord[0][1]) + point[0]*(coord[0][1]-coord[1][1]))/2)
     
     if (area1 + area2 + area3 == areaTriangle):
        return True  
     else:
        return False