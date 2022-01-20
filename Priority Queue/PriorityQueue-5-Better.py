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
        while index:
            parent_index = (index - 1) // 2
            parent = self.heap[parent_index]
            if parent < item:
                self.heap[parent_index] = item
                self.heap[index] = parent
                index = parent_index
            else:
                break

    def remove(self):
        """ Remove ▁ the ▁ highest ▁ priority ▁ item """
        if len(self.heap) == 0:
            return None
        index = len(self.heap) - 1
        element = self.heap[0]
        self.heap[:index] = self.heap[index + 1 :]
        self.heap.pop(index)
        self._heapify(self.heap)
        return element

    def size(self):
        """ Get  the  number  of  items  in  the  priority  queue """
        return len(self.heap[0])

    def peek(self):
        """ Return  the  next  element  to  be  returned  by  remove  without  removing  it  from  the  priority  queue """
        if not self.heap:
            return None
        else:
            return self.heap.pop()

    def empty(self):
        """Is  the  Priority  queue  empty ?
        : return :  True  if  and  only  if  the  priority  queue  is  empty"""
        return len(self.heap) == 0

    def enumerate(self):
        """ Provide  all  the  results  in  the  priority  queue  in  order """
        saved_heap = copy.deepcopy(self.heap)
        results = []
        while not self.heap:
            results.append(self.remove())
        self.heap = saved_heap
        return results

    def addAll(self, seq):
        """ Add  the  elements  of  a  collection  to  the  priority  queue """
        for element in seq:
            self.insert(element)

    def _heapify(self, index, size):
        """Restore  a  section  of  the  heap  to  maintain  heap  properties
        index  -  the  point  in  the  heap  to  work  on
        If  the  indicated  point  does  not  have  the  proper  relation  to  its  descendants ,
        their  values  are  swapped  and  the  descendant  is  then  processed  recursively"""
        if size > 0:
            leftIndex = (index * 2) + 1
            rightIndex = (index * 2) + 2
            parent = self.heap[index]
            maxIndex = index
            if leftIndex < size and self.heap[leftIndex] > parent:
                maxIndex = leftIndex
            if rightIndex < size and self.heap[rightIndex] > self.heap[leftIndex]:
                maxIndex = rightIndex
            if maxIndex != index:
                #  swap  them  and  recurse  on  the  subtree  rooted  at  min _ index  heap [ index ]
                self.heap[index] = self.heap[maxIndex]
                self.heap[maxIndex] = parent
                self._heapify(maxIndex, size)
