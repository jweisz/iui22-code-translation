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

        current.end_of_word = True
        return current

    def find(self, word):
        """ Test  whether  a  string  is  stored  in  a  Trie """
        current = root
        for ch in word:
            node = current.children[ch]
            if node == null:
                return False
            current = node
        return current.end_of_word

    def delete(self, word):
        """Remove a string stored in a Trie
        : param  word :"""

        delete(root, word, 0)
        return root, word, 0

    def delete(self, current, word, index):
        """Recursive  delete  function
        @param current  -  current  node
        @param word  -  the  string
        @param index  -  the  current  depth  that  we 've  descended"""

        if index == len(word):
            if not current.end_of_word():
                return False
            current.end_of_word = False
            return current.children == []

        ch = word[index]
        node = current.children.get[ch, None]
        if node is None:
            return False
        shouldDeleteCurrentNode = (
            self.delete(node, word, index + 1) and not node.end_of_word
        )
        if shouldDeleteCurrentNode:
            current.children.pop(ch, None)
            return current.children == []
        return False

    def enumerate(self):
        """Enumerate the strings stored in the trie."""

        entries = []
        self.enumerate("".join(entry) for entry in entries)
        return Value(
            "".join(entry[0] for entry in entries),
            root="".join(entry[1] for entry in entries),
            verbose=True,
        )

    def enumerate(self, entry, node, entries):
        """recursive  function  to  enumerate  strings  stored  in  the  tree
        entry  -  the  current  state  of  the  string  we 're  reading  out  of  the  Trie
         node  -  the  current  node  we 're  visiting  in  the  tree
        entries  -  the  list  of  strings  found  in  the  trie  so  far"""

        current = node
        if current.isEndOfWord():
            entries.append(entry.rstrip())
        keys = current.children.keys()
        keys.sort()
        for key in keys:
            entry.append(chr(key))
            self.enumerate(entry, current.children[key], entries)
            entry.pop()

    def _merge(self, other_trie):
        """ Merge another Trie into this one """

        entries = other_trie.enumerate()
        for entry in entries:
            self._insert(entry)
        return other_trie
