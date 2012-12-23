from suffixtree import SuffixTree, Node

WHITE_KEYS = ['\n',' ','\t']
SPECIAL_CHARS = ['(',')']

class Notebook(object):
    """
    Notebook object that represents a single text document that is loaded
    into memory to allow the program to query and report information about 
    its contents. The core logic of the program should be found within this
    class.
    """
    
    def __init__(self, file_path):
        self.file_path = file_path
            
        self.suffix_tree = SuffixTree()    
        self._parse_file(self.file_path)
        
    def reload(self, file_path=None):
        if file_path:
            self.file_path = file_path
        
        self.suffix_tree.root = Node()  # Restart the suffix tree
        self._parse_file(self.file_path)
        
    def _parse_file(self, file_path):
        with open(file_path,'r') as notebook:
        
            # build the contents found in the file
            for i, line in enumerate(notebook.readlines()):
                word = '' # word buffer
                start = -1
                
                for j, char in enumerate(line):
                    if char in WHITE_KEYS or char in SPECIAL_CHARS:
                        self._add_suffixes(word, start, i)
                        word = ''
                        start = -1
                    else:
                        if start==-1: 
                            start = j
                        word += char
                    
    # Adds a word and all of its suffixes
    def _add_suffixes(self, word, position, line_no, whole_word=True):
        if len(word) == 0:
            return 
        
        self.suffix_tree.add_word(word.lower(), ((position, line_no), whole_word))
        #self._add_suffixes(word[1:], position + 1, line_no, whole_word=False)    