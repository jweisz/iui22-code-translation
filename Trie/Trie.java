import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

/**
 * Trie Class
 * This class implements a Trie object for the storing and retrieval of strings
 * 
 * It basically builds a tree of nodes, where each node represents
 * a character in a string that has been stored in the Trie.   A stored string is 
 * represented by a path in the Trie from the root to a node marekd as an endOfWord node.
 */
public class Trie {
	
	/**
	 * The TrieNode class is used by the Trie class to store 
	 * individual nodes in the tree.  Each node represents a point
	 * in a stored string, and has a set of children nodes which represent
	 * next characters in the string, indexed by the character that leasds to that node.
	 * A isWord flag set to true means that this is the end of some string stored in the Trie, 
	 * though other strings may continue from that point if there are children.
	 */
	public class TrieNode {
		private HashMap<Character, TrieNode> children;
		private boolean isWord;

		public TrieNode() {
			children = new HashMap<Character, TrieNode>();
			isWord = false;
		}
		
		public HashMap<Character, TrieNode> getChildren() {
			return children;
		}
		
		public boolean isEndOfWord() {
			return isWord;
		}

		public void setEndOfWord(boolean isEndOfWord) {
			isWord = isEndOfWord;
		}
	}
	
	private TrieNode root;
	
	/**
	 * Constuctor
	 */
	public Trie() {
		root = new TrieNode();
	}
	
	/**
	 * Insert a string into a Trie
	 * @param word - the string to be inserted
	 */
	public void insert(String word) {
		
		TrieNode current = root;
		for (char l: word.toCharArray()) {
			current = current.getChildren().computeIfAbsent(l, (c)-> new TrieNode());
		}
		
		current.setEndOfWord(true);
	}
	
	/**
	 * Test whether a string is stored in a Trie
	 * @param word
	 * @return true if the string is stored in the Trie, false otherwise
	 */
	public boolean find(String word) {
		TrieNode current = root;
		
		for (int i = 0; i < word.length(); i++) {
			char ch = word.charAt(i);
			TrieNode node = current.getChildren().get(ch);
			if (node == null) {
				return false;
			}
			current = node;
		}
		return current.isEndOfWord();
	}
	
	/**
	 * Remove a string stored in a Trie
	 * @param word
	 */
	public void delete(String word) {
	    delete(root, word, 0);
	}
	
	/**
	 * Recursive delete method
	 * @param current - current node 
	 * @param word - the string to be deleted
	 * @param index - the current depth that we've descended
	 * @return - true if the string was deleted, false if it was not found
	 */
	public boolean delete(TrieNode current, String word, int index) {
	    if (index == word.length()) {
	        if (!current.isEndOfWord()) {
	            return false;
	        }
	        current.setEndOfWord(false);
	        return current.getChildren().isEmpty();
	    }
	    char ch = word.charAt(index);
	    TrieNode node = current.getChildren().get(ch);
	    if (node == null) {
	        return false;
	    }
	    boolean shouldDeleteCurrentNode = delete(node, word, index + 1) && !node.isEndOfWord();

	    if (shouldDeleteCurrentNode) {
	        current.getChildren().remove(ch);
	        return current.getChildren().isEmpty();
	    }
	    return false;
	}

	/**
	 * Enumerate the strings stored in the trie
	 * @return a list of strings that are in the tree
	 */
	public List<String> enumerate() {
		ArrayList<String> entries = new ArrayList<String>(); 
		enumerate(new StringBuilder(), root, entries);
		
		return entries;
	}

	
	/**
	 * recursive function to enumerate strings stored in the tree
	 * @param entry - the current state of the string we're reading out of the Trie
	 * @param node - the current node we're visiting in the tree
	 * @param entries - the list of strings found in the trie so far
	 */
	public void enumerate(StringBuilder entry, TrieNode node, List<String> entries) {
		TrieNode current = node;
		
		if (current.isEndOfWord()) {
			entries.add(entry.toString());
		}
		
		Object keys[] = current.getChildren().keySet().toArray();
		Arrays.sort(keys);		
		
		for (Object key : keys) {
			entry.append((Character)key);	
			enumerate(entry, current.getChildren().get(key), entries);
			entry.deleteCharAt(entry.length() - 1);
		}
	}
	
	/**
	 * Merge another Trie into this one
	 * @param otherTrie - the trie to be merged in
	 */
	public void merge(Trie otherTrie) {
		List<String> entries = otherTrie.enumerate();
		for (String entry : entries) {
			insert(entry);
		}
	}
}