class priority_queue:
    """
    Python  code  to  implement  a  priority - queue  using  an
    ArrayList - based  implementation  of  a  binary  heap

    This  class  can  be  parameterized  for  any  element  class  that  supports  the  Comparable
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
        index = self.heap.index(item)
        self.heap.insert(index, item)
        while index > 0:
            parent_index = (index - 1) // 2
            parent = self.heap.pop()
            if parent < item:
                self.heap.insert(parent_index, item)
                self.heap.insert(index, parent)
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
        self.heap.pop(index)
        self._heapify(0, self.heap)
        return element

    def size(self):
        """ Get  the  number  of  items  in  the  priority  queue """
        return len(self.heap())

    def peek(self):
        """ Return  the  next  element  to  be  returned  by  remove  without  removing  it  from  the  priority  queue """
        if not self.heap.empty():
            return self.heap.pop()
        else:
            return None

    def empty(self):
        """Is  the  Priority  queue  empty ?
        : return :  True  if  and  only  if  the  priority  queue  is  empty"""
        return self.heap.empty()

    def enumerate(self):
        """ Provide  all  the  results  in  the  priority  queue  in  order """
        saved_heap = copy.deepcopy(self.heap)
        results = []
        while not self.heap.empty():
            results.append(self.remove())
        self.heap = saved_heap
        return [x for x in results if x["priority "] == 0]

    def addAll(self, collection):
        """ Add  the  elements  of  a  collection  to  the  priority  queue """
        for element in collection:
            self.insert(element)
        return collection

    def _heapify(self, index, size):
        """Restore  a  section  of  the  heap  to  maintain  heap  properties
        index  -  the  point  in  the  heap  to  work  on
        If  the  indicated  point  does  not  have  the  proper  relation  to  its  descendants ,
        their  values  are  swapped  and  the  descendant  is  then  processed  recursively"""

        if self.heap:
            left_index = (index * 2) + 1
            right_index = (index * 2) + 2
            parent = self.heap.pop(index)
            max_index = heap.index[parent]
            if left_index < left_index and self.heap[left_index] > parent:
                max_index = left_index
            if right_index < right_index and self.heap[right_index] > parent:
                max_index = right_index
            if max_index != left_index:
                #  swap  them  and  recurse  on  the  subtree  rooted  at  min _ index  heap [ index ]
                self.heap[left_index] = self.heap[max_index]
                self.heap[max_index] = parent
                self._siftup_max(self.heap, max_index)
