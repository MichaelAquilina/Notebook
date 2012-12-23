class LeafNode(object):
    """Special type of node that represents the meta information for a word.
    Found at the end of the word traversal on nodes in a suffix tree."""
    
    def __init__(self, meta):
        self.meta = meta
        
    def __repr__(self):
        return 'LeafNode: Meta=%s' % repr(self.meta)
        
# Suffix Tree Node
class Node(object):
    """Suffix Node object that contains references to a Parent node and other
    child nodes. Each node has an associated storage value (usually a character)
    and possibly one or more LeafNodes that would contain meta information about
    a word."""
    
    def __init__(self, store='\0'):
        self.store = store  # data stored at this node
        self.children = {}  # all child nodes
        self.parent = None  # parent node
        self.data = []   # leaf node associated with this Node
        
    def __repr__(self):
        return 'Parent=%s, Store=%s, Children=%s' % (repr(self.parent), self.store, len(self.children)) 
        
class SuffixTree(object):
    """Suffix tree class that provides an interface to interact with. Allows methods
    to add words to storage, query available words and retrieve meta information
    stored with words in the tree. Also provides additional methods to enumerate words
    etc..."""
    
    def __init__(self):
        self.root = Node()
        
    def add_word(self, word, meta=None):
        """Public interface used to add words to the suffice tree."""
        self._add(self.root, word, 0, meta)
        
    def words(self, include_suffixes=False):
        """returns a list of all the words stored in the suffix tree."""
        output = []
        self._get_words(self.root, '', output, include_suffixes)
        
        return output
    
    def get_data(self, word, substrings=False):
        """Returns the data information for the specified word. If the word doesn't
        exist or no meta information was stored, then None is returned."""
        return self._get(self.root, word, 0, substrings)
    
    def has_word(self, word, substrings=False):
        """Searches the suffix tree to see if it contains the specified word and returns
        a boolean result specifying the result of the search."""
        return self.get_data(word, substrings) != None
        
    def _add(self, node, word, n, meta=None):
        """Adds the specified word to the suffix tree for 
        indexing. Meta-information may be passed optionally
        to be stored at the leaf node. The add_word method 
        should be used by external classes rather than this.
        The integer n passed in the arguments, specifies the
        location of the character in the word to store in a
        node."""
        
        if len(word) == n:
            leaf = LeafNode(meta)
            node.data.append(leaf)
            return  # Add a leaf node and return
        
        head = word[n]
        next_node = None
        
        if head in node.children:
            next_node = node.children[head]
        else:
            next_node = Node(head)
            node.children[head] = next_node
        
        self._add(next_node, word, n + 1, meta)
        
    def _get_words(self, node, word, output, include_suffixes):
        """Enumerates all the words in the suffix tree by performing a
         Depth-First-Search of the suffix tree using recursive techniques."""
        if node.children:
            for char, child in node.children.items():
                self._get_words(child, word + char, output, include_suffixes)
        
        # If the current node has data, then a word exists
        if node.data:
            # Check if at least one entry is a whole word
            for entry in node.data:
                _, whole = entry.meta
                if whole or include_suffixes:     # If the word is whole, or we want all suffixes 
                    output.append(word)
                    break
            
    def _get(self, node, word, n, substrings):
        """Gets the data information of the specified word starting from the specified
        node. Uses a recursive solution to return the final result."""
        if len(word) == n:
            return node.data
        
        head = word[n]
        if head in node.children:
            return self._get(node.children[head], word, n + 1, substrings)
        else:
            return None
