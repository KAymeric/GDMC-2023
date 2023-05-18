"""Define the Edge object"""

import math
import numpy
from Geometry.Vertice import Vertice


class Edge:
    x,y,z = 0,0,0
    angle = 0
    _nextEdge = None
    _previousEdge = None
    _nextVertice = None
    _previousVertice = None
    
    def __init__(self,x:int,y:int,z:int):
        self.x,self.y,self.z = x,y,z
        self._nextVertice = Vertice(self.GetPositionInTuple(),(0,0,0))
        self._previousVertice = Vertice((0,0,0),self.GetPositionInTuple())
        
    def SetNextEdge(self,_nextEdge):
        self._nextEdge = _nextEdge
        self._nextVertice.SetEnd(_nextEdge. GetPositionInTuple())
        self.CalAngle()
        
    def SetPreviousEdge(self,_previousEdge):
        self._previousEdge = _previousEdge
        self._previousVertice.SetOrigin(_previousEdge.GetPositionInTuple())
        self.CalAngle()
        
    def GetPositionInTuple(self):
        return (self.x,self.y,self.z)
    
    def CalAngle(self):
        if self._nextEdge != None and self._previousEdge != None:            
            v1 = (self._previousEdge.x - self.x, self._previousEdge.y - self.y, self._previousEdge.z - self.z)
            v2 = (self._nextEdge.x - self.x, self._nextEdge.y - self.y, self._nextEdge.z - self.z)

            magnitude_v1 = math.sqrt(v1[0]**2 + v1[1]**2 + v1[2]**2)
            magnitude_v2 = math.sqrt(v2[0]**2 + v2[1]**2 + v2[2]**2)

            dot_product = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

            angle_radians = math.acos(dot_product / (magnitude_v1 * magnitude_v2))

            self.angle = math.degrees(angle_radians)