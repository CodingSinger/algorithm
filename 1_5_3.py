

class FT:
    def __init__(self,n):

        self.id = [i for i in range(n)]
        self.sz = [i for i in range(n)]

    def find(self,index):

        while index != self.id[index]:
            index = self.id[index]
        return index

    def union(self,p,q):


        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        if self.sz[rootp] > self.sz[rootq]:
            self.id[rootq] = rootp
            self.sz[rootp] +=self.sz[rootq]

        else:
            self.id[rootp] = rootq
            self.sz[rootq] +=self.sz[rootp]

    def connect(self,p,q):
            return self.find(p) == self.find(q)



if __name__ == '__main__':
    f = FT(10)
    f.union(1,5)
    print f.connect(1,5)
    print f.connect(1,2)
    f.union(2,5)
    print f.connect(1,2)



