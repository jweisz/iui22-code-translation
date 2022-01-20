import os


class trie_node:
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
        self.is_word = False

    def get_children(self):
        return self.children

    def is_end_of_word(self):
        return self.is_Word

    def set_end_of_word(self, is_end_of_word):
        self.is_word = is_end_of_word


class trie:
    """
    Trie  Class
    This  class  implements  a  Trie  object  for  the  storing  and  retrieval  of  strings
    It  basically  builds  a  tree  of  nodes ,  where  each  node  represents
    a  character  in  a  string  that  has  been  stored  in  the  Trie .  A  stored  string  is
    represented  by  a  path  in  the  Trie  from  the  root  to  a  node  marekd  as  an  endOfWord  node ."""

    def __init__(self):
        """ Constuctor """

        self.root = trie_node()

    def insert(self, word):
        """ Insert a  string  into  a  Trie """
        current = self.root

        for l in word:
            current = current.get_children()[l]

        current.set_end_of_word(True)

    def find(self, word):
        """ Test  whether  a  string  is  stored  in  a  Trie """
        current = self.root
        for ch in word:
            node = current.get_children()[ch]
            if node is None:
                return False
            current = node
        return current.is_end_of_word()

    def delete(self, word):
        """Remove a string stored in a Trie
        : param  word :"""
        return delete(root, word, 0)

    def delete(self, current, word, index):
        """Recursive  delete  function
        current  -  current  node
        word  -  the  string
        index  -  the  current  depth  that  we 've  descended"""

        if index == len(word):
            if not current.is_end_of_word():
                return False
            current.set_end_of_word(False)
            return current.get_children()

        ch = word[index]
        node = current.get_children().get(ch, None)
        if node is None:
            return False
        should_delete_current_node = (
            self.delete(node, word, index + 1) and not node.is_end_of_word()
        )
        if should_delete_current_node:
            current.get_children().pop(ch)
            return current.get_children()
        return False

    def enumerate(self):
        """Enumerate the strings stored in the trie."""
        entries = []
        enumerate(
            [
                root
                for root, dirs, files in os.walk(". ")
                if not os.path.exists(os.path.join(root, "__init__.py "))
            ]
        )
        return [
            root
            for root, dirs, files in enumerate(files)
            if not os.path.exists(os.path.join(root, "__init__.py "))
        ]

    def enumerate(self, entry, node, entries):
        """ recursive  function  to  enumerate  strings  stored  in  the  tree """

        current = node
        if current.is_end_of_word():
            entries.append(entry.strip())
        keys = current.get_children().keys()
        keys.sort()
        for key in keys:
            entry.append(chr(key))
            self.enumerate(entry, current.get_children()[key], entries)
            entry.pop()

    def merge(self, other_trie: Trie):
        """ Merge another Trie into this one """

        entries = other_trie.enumerate()
        for entry in entries:
            self.insert(entry)
