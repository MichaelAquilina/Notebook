# Suffix Tree Node
class Node(object):
    
    def __init__(self, store='\0'):
        self.store = store  # data stored at this node
        self.children = {}  # all child nodes
        self.parent = None  # parent node
        self.meta = None    # meta information to store
        
    def __repr__(self):
        return 'Parent=%s, Children=%s' % (repr(self.parent), len(self.children)) 
        
class SuffixTree(object):
    
    def __init__(self):
        self.root = Node()
        
    def add_word(self, word, meta=None):
        """Public interface used to add words to the suffice tree."""
        self._add(self.root, word, meta)
        
    def words(self):
        """returns a list of all the words stored in the suffix tree."""
        output = []
        self._get_words(self.root, '', output)
        
        return output
    
    def get_meta(self, word):
        """Returns the meta information for the specified word. If the word doesnt
        exist or no meta information was stored, then None is returned."""
        return self._get(self.root, word)
        
    def _add(self, node, word, meta=None):
        """Adds the specified word to the suffix tree for 
        indexing. Meta-information may be passed optionally
        to be stored at the leaf node. The add_word method 
        should be used by external classes rather than this."""
        
        # Todo: more efficient implementation by passing a pointer to the char location
        # rather than specifying word[1:] and creating a new string in memory each time
        
        if len(word) == 0:
            node.meta = meta
            return  # Add a leaf node and return
        
        head = word[0]
        next_node = None
        
        if head in node.children:
            next_node = node.children[head]
        else:
            next_node = Node(head)
            node.children[head] = next_node
        
        self._add(next_node, word[1:], meta)
        
    def _get_words(self, node, word, output):
        """Enumerates all the words in the suffix tree by performing a
         Depth-First-Search of the suffix tree using recursive techniques."""
        if node.children:
            for char, child in node.children.items():
                self._get_words(child, word + char, output)
        else:
            output.append(word)
            
    def _get(self, node, word):
        """Gets the meta information of the specified word starting from the specified
        node. Uses a recursive solution to return the final result."""
        if len(word) == 0:
            return node.meta
        
        head = word[0]
        if head in node.children:
            return self._get(node.children[head], word[1:])
        else:
            return None