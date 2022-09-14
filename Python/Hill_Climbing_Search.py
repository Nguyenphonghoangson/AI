import queue
import os
from traceback import print_tb
from Node import Node
def ID():
    graph =[]
    with open('InputFile1.txt') as f:
        l=f.readline()
        s=l.strip().split(',')[0]
        e=l.strip().split(',')[1]
        while True:
            l = f.readline()
            if not l:
                break
            graph.append(Node(l.strip().split(',')[0],l.strip().split(',')[1],int(l.strip().split(',')[2])))
    return graph,s,e
def ED(v,g,vt,stack,l1):
    PV(v)
    PN(g)
    PVT(vt)
    DSL1(l1)
    PIVS(stack)
def DSL1(l1):
    with open('Out_HillClimbingSearch.txt', 'a') as f:
        while l1:
            x=l1.pop()
            f.write(x.vertex+str(x.weight))
        f.write('\t\t\t\t\t')
def PV(v):
    with open('Out_HillClimbingSearch.txt', 'a') as f:
        print(v.vertex+str(v.weight))
        f.write(v.vertex+str(v.weight))
        f.write('\t\t\t\t\t')
        f.close()
def PN(g):
    with open('Out_HillClimbingSearch.txt', 'a') as f:
        if g:
            for neighbor in g:
                f.write(neighbor)
            f.write('\t\t\t\t\t')
        else: f.write('\t\t\t\t\t')
        f.close()
def PVT(vt):
    with open('Out_HillClimbingSearch.txt', 'a') as f:
        for v in vt:
            f.write(v)
        f.write('\t\t\t\t')
        f.close()
def PIVS(stack):
    list=[]
    while stack.qsize():
        v=stack.get()                                        
        list.append(v)
    with open('Out_HillClimbingSearch.txt', 'a') as f:
        for v in list:
            f.write(v.vertex+str(v.weight))
        f.write('\n')
        f.close()
    while list:
        stack.put(list.pop())
def SD(st):
    print(st)
    list,e=[],st.pop()
    list.append(e)
    while st:
        v=st.pop()
        l=Vertex(v).neighbor.split();
        if l:
            if  e in l:
                e=v
                list.append(e);
    with open('Out_HillClimbingSearch.txt', 'a') as f:
        f.write("Direction =>")
        for i in range(len(list)-1,-1,-1):
            f.write('->'+list[i])
def Vertex(x):
    n=Node(x)
    for i in range(0,len(graph)):
            if x is graph[i].vertex:
                n = graph[i]
    return n
def getWeight(e):
      return e.weight
def HCS():
    vt,stack,st,list,l1=[],queue.LifoQueue(),[],[],[];
    stack.put(Vertex(s))
    while stack:
        v=stack.get()
        st.append(v.vertex)
        if v.vertex  not in vt:
            vt.append(v.vertex)
        g=v.neighbor.split(); 
        if v.vertex==Vertex(e).vertex: 
            ED(v,g,vt,stack,l1)
            break
        if g:
            for neighbor in g:
                if neighbor not in vt:
                    vt.append(neighbor)   
                    list.append(Vertex(neighbor))
            list.sort(key=getWeight)
            while list:
                x=list.pop()
                l1.append(x)
                stack.put(x)  
        ED(v,g,vt,stack,l1) 
    SD(st);
if __name__ == '__main__':
        os.remove('Out_HillClimbingSearch.txt')
        graph,s,e =ID()
        with open('Out_HillClimbingSearch.txt', 'a') as f:
            f.write('TT\t\t\t\tTrang Thai Ke\t\t\tDanh sach Q\t\t\t\tDanh sach L1\t\t\t\tDanh sach L\n')
            f.close()
        HCS()
