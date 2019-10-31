#LAB X
#Due Date: 04/07/2019, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:             
#
########################################

class MaxHeapPriorityQueue:
    ### Copy and paste your code from LAB 12 here
    def __init__(self):
        self.heap=[]
        self.size = 0

    def __len__(self):
        return len(self.heap)-1


    def parent(self,index):
        if  (index > 1 and index <= self.size):
            return self.heap[(index//2-1)]
        else:
            return None
        

    def leftChild(self,index):
        if (index >=1 and index*2 <= self.size):
            return self.heap[index*2]

        else: 
            return None


    def rightChild(self,index):
        if (index>= 1 and ((index*2)+1)<= self.size):
            return self.heap[(index*2+1)]
        else:
            return None
 

    def swap(self, index1, index2):
        self.heap[index1-1], self.heap[index2-1] = self.heap[index2-1], self.heap[index1-1]
        
    def max_heapUp(self,n):
        parent = (n)//2-1
        if parent <= 1:
            return
        elif self.heap[parent] < self.heap[n]:
            self.swap(n,parent)
            self.max_heapUp(parent)

    def insert(self,x):
        self.size = self.size+1
        self.heap.append(x)
        self.max_heapUp(len(self.heap)-1)


    def max_heapify(self, n):
        left = n *2 
        right = n*2+1
        large = n
        if len(self.heap) > left and self.heap[large] <self.heap[left]:
            large = left
        if len(self.heap) > right and self.heap[large] < self.heap[right]:
            large = right
        if large != n:
            self.swap(n, large)
            self.max_heapify(large)





    def deleteMax(self):
        if len(self.heap) >2:
            self.swap(1, len(self.heap)-1)
            max1 = self.heap[1]
            self.max_heapify(1)
        elif len(self.heap) == 2:
            max1 = self.heap.max_heapify()
        else: 
            max1 = False
        self.size = self.size-1
        return max1
 
        #write your code here

def heapSort(numList):
    '''
       >>> heapSort([9,7,4,1,2,4,8,7,0,-1])
       [-1, 0, 1, 2, 4, 4, 7, 7, 8, 9]
    '''
	sort_heap = MaxHeapPriorityQueue()
    #write your code here
    out = []
    n = len(numList)
    for i in range(n,-1,-1):
    	sort_heap.insert(numList[i])
    for i in range(n-1, 0, -1):
    	out.append(sort_heap[i])
