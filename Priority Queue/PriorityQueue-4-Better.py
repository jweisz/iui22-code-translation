class priority_queue:
    """
    Python  code  to  implement  a  priority - queue  using  an
    ArrayList - based  implementation  of  a  binary  heap

    This class  can  be  parameterized  for  any  element  class  that  supports  the  Comparable
        interface  on  itself

    A  priority  queue  allows  one  to  store  comparable  elements
    and  remove  them  in  the  order  defined  by  the  comparator
    This  implementation  will  remove  the  highest  priority  items  first
    Insertion  and  removal  are  O ( log  n )  operations  in  terms  of  the  number  of  items  in  the  queue
    """

    def __init__(self):
        self.heap = []

    def insert(self, item):
        """insert  an  item  into  the  priority  queue
        item  -  to  be  inserted
        """
        index = len(self.heap)
        self.heap.append(item)
        while index > 0:
            parent_index = (index - 1) // 2
            parent = self.heap[parent_index]
            if parent < item:
                self.heap[parentIndex] = item
                self.heap[index] = parent
                index = parent_index
            else:
                break

    def remove(self):
        """ Remove the highest priority item """
        if len(self.heap) == 0:
            return None
        index = len(self.heap) - 1
        element = self.heap[0]
        self.heap[0] = self.heap[index]
        self.heap[index] = element
        self._heapify(self.heap)
        return element

    def size(self):
        """ Get  the  number  of  items  in  the  priority  queue """
        return len(self.heap())

    def peek(self):
        """ Return  the  next  element  to  be  returned  by  remove  without  removing  it  from  the  priority  queue """
        if not self.heap.empty():
            return self.heap.get(0)
        else:
            return None

    def is_empty(self):
        """Is  the  Priority  queue  empty ?
        : return :  True  if  and  only  if  the  priority  queue  is  empty"""
        return self.heap.empty()

    def enumerate(self):
        """ Provide  all  the  results  in  the  priority  queue  in  order """
        saved_heap = [self.heap]
        results = []
        while not self.heap:
            results.append(self.remove())
        self.heap = saved_heap
        return results

    def addAll(self, seq):
        """ Add  the  elements  of  a  collection  to  the  priority  queue """
        for element in seq:
            self.insert(element)

    def _heapify(self, x):
        """ Transform list into a heap , in - place , in O ( len ( x ) ) time . """
        n = len(x)
        #  Transform  bottom - up .  The  largest  index  there 's  any  point  to  looking  at
        #  is  the  largest  with  a  child  index  in - range ,  so  must  have  2 * i  +  1  <  n ,
        #  or  i  <  ( n - 1 ) / 2 .  If  n  is  even  =  2 * j ,  this  is  ( 2 * j - 1 ) / 2  =  j - 1/2  so
        #  j - 1  is  the  largest ,  which  is  n / /2  -  1 .  If  n  is  odd  =  2 * j + 1 ,  this  is
        #  ( 2 * j + 1-1 ) / 2  =  j  so  j - 1  is  the  largest ,  and  that 's  again  n / /2-1 .
        for i in reversed(range(n // 2)):
            _siftup(x, i)
