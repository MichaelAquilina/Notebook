from suffixtree import SuffixTree, Node

WHITE_KEYS = ['\n',' ','\t']
SPECIAL_CHARS = ['(',')','=','-']

class Notebook(object):
    
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
        
        self.suffix_tree.add_word(word, ((position, line_no), whole_word))
        # TEMP: Disabled until querying power is given to suffix tree
        # self._add_suffixes(word[1:], line_no, position + 1, suffix_tree, whole_word=False)    