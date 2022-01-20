class TrieNode:
    """
    The  TrieNode  class  is  used  by  the  Trie  class  to  store
    individual  nodes  in  the  tree .  Each  node  represents  a  point
    in  a  stored  string ,  and  has  a  set  of  children  nodes  which  represent
    next  characters  in  the  string ,  indexed  by  the  character  that  leasds  to  that  node .
    A  is _ word  flag  set  to  true  means  that  this  is  the  end  of  some  string  stored  in  the  Trie ,
    though  other  strings  may  continue  from  that  point  if  there  are  children .
    """

    def __init__(self):
        self.children = {}
        self.isWord = False

    def getChildren(self):
        return self.children

    def isEndOfWord(self):
        return self.isWord

    def setEndOfWord(self, isEndOfWord):
        self.isWord = isEndOfWord


class Trie:
    """
    Trie  Class
    This  class  implements  a  Trie  object  for  the  storing  and  retrieval  of  strings
    It  basically  builds  a  tree  of  nodes ,  where  each  node  represents
    a  character  in  a  string  that  has  been  stored  in  the  Trie .  A  stored  string  is
    represented  by  a  path  in  the  Trie  from  the  root  to  a  node  marekd  as  an  endOfWord  node ."""

    def __init__(self):
        """ Constuctor """
        self.root = TrieNode()

    def insert(self, word):
        """ Insert a  string  into  a  Trie """

        current = root

        for l in word:
            current = current.children.setdefault(l, (c for c in current.children))

        current.setEndOfWord(True)
        return current

    def find(self, word):
        """ Test  whether  a  string  is  stored  in  a  Trie """
        current = root
        for ch in word:
            node = current.children[ch]
            if node is None:
                return False
            current = node
        return current.isEndOfWord()

    def delete(self, word):
        """Remove a string stored in a Trie
        : param  word :"""

        delete(root, word, 0)

    def delete(self, current, word, index):
        """Recursive  delete  function
        @param current  -  current  node
        @param word  -  the  string
        @param index  -  the  current  depth  that  we 've  descended"""

        if index == len(word):
            if not current.isEndOfWord():
                return False
            current.setEndOfWord(False)
            return current.getChildren()

        ch = word[index]
        node = current.getChildren()[ch]
        if node is None:
            return False
        should_delete_current_node = (
            self.delete(node, word, index + 1) and not node.isEndOfWord()
        )
        if should_delete_current_node:
            current.getChildren().remove(ch)
            return current.getChildren()[ch]
        return False

    def enumerate(self):
        """Enumerate the strings stored in the trie."""

        entries = []
        self.enumerate("".join(entry) for entry in entries)
        return entries

    def enumerate(self, entry, node, entries):
        """recursive  function  to  enumerate  strings  stored  in  the  tree
        entry  -  the  current  state  of  the  string  we 're  reading  out  of  the  Trie
         node  -  the  current  node  we 're  visiting  in  the  tree
        entries  -  the  list  of  strings  found  in  the  trie  so  far"""

        current = node
        if current.isEndOfWord():
            entries.append(entry.pop())
        keys = current.getchildren().keys()
        keys.sort()
        for key in keys:
            entry.append(chr(key))
            enumerate(entry, current.getChildren()[key], entries)
            entry.pop()

    def merge(self, other_trie):
        """ Merge another Trie into this one """

        entries = other_trie.enumerate()
        for entry in entries:
            insert(entry)
        return other_trie.copy()
