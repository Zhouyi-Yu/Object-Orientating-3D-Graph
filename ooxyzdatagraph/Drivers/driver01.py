from xyzdatagraph import *

# Only text output
def main():
    s = XYZDatagraph("Output/driver01")
    print(s)
    s.x([1,2,3,4])
    s.y([2,4,6,8])
    s.z([4,8,12,16])
    print("x:")
    print(s.x())
    print("y:")
    print(s.y())
    print("z:")
    print(s.z())

    l = [
          [ 5,8,1.2 ],
          [ 5,16,2.1 ],
          [ 5,32,3.1 ],
          [ 5,64,4.1 ],
          [ 5,128,5.1 ],
          [ 5,256,6.1 ],
          [ 5,512,7.1 ],
          [ 5,1024,8.1 ]
        ]

    print("dump:")
    s.dump()

    s.xyz(l)
    print("dump xyz:")
    s.dump()

    print("*** swapxz:")
    s.swapxz()
    print("dump:")
    s.dump()
    print("Print:", s.xyz())

    print("*** swapxy:")
    s.swapxy()
    print("dump:")
    s.dump()
    print("Print:", s.xyz())

    print("*** swapyz:")
    s.swapyz()
    print("dump:")
    s.dump()
    print("Print:", s.xyz())

    print(s.name())

if __name__ == "__main__":
    main()
