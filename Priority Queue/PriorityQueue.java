import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

/**
 * Java code to implement a priority-queue using an 
 * ArrayList-based implementation of a binary heap
 *
 * This class can be parameterized for any element class that supports the Comparable 
 * interface on itself
 *  
 * A priority queue allows one to store comparable elements
 * and remove them in the order defined by the comparator
 * This implementation will remove the highest priority items first
 * Insertion and removal are O(log n) operations in terms of the number of items in the queue
 */

public class PriorityQueue<T extends Comparable<T>> {
    private ArrayList<T>  heap;
    
    /**
        * Constructor
        */
    public PriorityQueue(){
        heap = new ArrayList<T>();
    }
        
    /**
        * Insert an item into the priority queue
        * @param item - to be inserted
        */
    public void insert(T item ){
        int index = heap.size();
    
        heap.add(item);
        while(index > 0) {
            int parentIndex = (index - 1) / 2;
            T parent = heap.get(parentIndex);
            if (parent.compareTo(item) < 0) {
                heap.set(parentIndex, item);
                heap.set(index, parent);
                index = parentIndex;
            }
            else {
                break;
            }
        }
    }
    
    /**
        * Remove the highest priority item from the priority queue
        * @return the removed item
        */
    public T remove(){
        if(heap.size() == 0){
            return null;
        }
        
        int index = heap.size() - 1; // swap the last item in for the first
        T element = heap.get(0);
        heap.set(0, heap.get(index));
        heap.remove(index);
        heapify(0, heap.size()); // now propagate that last item to the proper place in the heap
        
        return element;
    }
        
    /**
        * Get the number of items in the priority queue
        * @return the number of elements in the priority queue
        */
    public int size()
    {
        return heap.size();
    }

    /**
        * Return the next element to be returned by remove without removing it from the priority queue
        * @return the highest priority element in the priority queue
        */
    
    public T peek()
    {
        return heap.get(0);
    }

    /**
        * Is the Priority queue empty?
        * @return true if and only if the priority queue is empty
        */
    public boolean isEmpty()
    {
        return heap.isEmpty();
    }

    /**
        * Provide all the results in the priority queue in order
        * @return a list of all the results in the priority queue
        */
    public List<T> enumerate() {
        ArrayList<T> savedHeap = new ArrayList<T>(heap);
        ArrayList<T> results = new ArrayList<T>();
        
        while (!heap.isEmpty()) {
            results.add(remove());
        }
        
        heap = savedHeap;
        
        return results;
    }
    
    /**
        * Add the elements of a collection to the priority queue
        * @param collection - 
        */
    public void addAll(Collection<T> collection) {
        for (T element : collection) {
            insert(element);
        }
    }
    
    /**
        * Restore a section of the heap to maintain heap properties
        * @param index - the point in the heap to work on
        * If the indicated point does not have the proper relation to its descendants,
        * their values are swapped and the descendant is then processed recursively 
        */
    private void heapify(int index, int size)
    {	
        if (size > 0) {
            int leftIndex = (index * 2) + 1;
            int rightIndex = (index * 2) + 2;

            T parent = heap.get(index); 
                        
            int maxIndex = index;
            
            if (leftIndex < size && heap.get(leftIndex).compareTo(parent) > 0) {
                maxIndex = leftIndex;
            }
            
            if (rightIndex < size && heap.get(rightIndex).compareTo(heap.get(leftIndex)) > 0) {
                maxIndex = rightIndex;
            }

            if(maxIndex != index)
            {
                // swap them and recurse on the subtree rooted at minIndex
                heap.set(index, heap.get(maxIndex));
                heap.set(maxIndex, parent);
                heapify(maxIndex, size);
            }
        }
    }
}	
	