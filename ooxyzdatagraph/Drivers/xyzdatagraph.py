# Copyright Paul Lu, 2023
import matplotlib.pyplot as xyzplt
import matplotlib.cm as cm
from xydata import *

class XYZDatagraph(XYData):
    def __init__(self,name=""):
        super().__init__(name)
        self.__z = []
        return

    def __str__(self):
        s = "XYZData: " + self.name()
        return s

    def __repr__(self):
        super().__repr__(self)
        return s

    def dumplist(self):
        l=[]
        for i in range(len(self.__z)):
            l.append([self.__x[i],
                   self.__y[i],
                   self.__z[i]])
        return(l)

    def dump(self):
        for i in range(len(self.__z)):
            print([self.__x[i],
                   self.__y[i],
                   self.__z[i]])
        return print(f"Print: {self.dumplist()}")

    def swapxy(self):
        ty=self.y()
        tx=self.x()
        self.x(ty)
        self.y(tx)
       

    def swapxz(self):
        tz=self.z()
        tx=self.x()
        self.x(tz)
        self.z(tx)

    def swapyz(self):
        ty=self.y()
        tz=self.z()
        self.z(ty)
        self.y(tz)
        
    def z(self,data=[]):
        # HINT: Borrow idea from Lecture 14 worksheet, polymorphism
        if len(data) == 0:
            return(self.__z)
        elif type(data) is list:
            self.__z = data.copy()
            assert self.__z is not data, "Not copied"
            return(len(data))
        assert False, "Should not be here: z"
        return None

    # Expects list of 3-element [x,y,z] lists
    def xyz(self,data=[]):
        # HINT: Borrow idea from Lecture 14 worksheet, polymorphism
        als=[]
        if len(data) == 0:
            tx,ty,tz=self.x(),self.y(),self.z()
            for i in range(len(tz)):
                als.append([tx[i],
                             ty[i],
                              tz[i]])
                return als
        else:
            tx,ty,tz=[],[],[]
            for i in data:
                tx.append(i[0])
                ty.append(i[1])
                tz.append(i[2])
            self.x(tx)
            self.y(ty)
            self.z(tz)


    def plot3dpng(self):
        fig = xyzplt.figure()
        ax = fig.add_subplot(projection='3d')

        sc = ax.scatter(self.x(), self.y(), self.z(), c=self.z(), cmap=cm.turbo)
        fig.colorbar(sc, pad=0.2)

        ax.set_xlabel('Fingerprint Size (bytes)')
        ax.set_ylabel('Min Chunk Size (bytes)')
        ax.set_zlabel('Deduplication Ratio')
        ax.set_title('Deduplication Ratio vs.\nFingerprint Size and Min Chunk Size')
        xyzplt.savefig(self.name() + ".png")

         
        return
