from suffixtree import SuffixTree

WHITE_KEYS = ['\n',' ','\t']
SPECIAL_CHARS = ['(',')','=','-']

class Notebook(object):
    
    def __init__(self, file_path):
        self.file_path = file_path
            
        self.suffix_tree = SuffixTree()    
        self._parse_file(self.file_path)
        
    def _parse_file(self, file_path):
        notebook = open(file_path,'r')
        
        # build the contents found in the file
        for i, line in enumerate(notebook.readlines()):
            word = '' # word buffer
            start = -1
            
            for j, char in enumerate(line):
                if char in WHITE_KEYS or char in SPECIAL_CHARS:
                    self._add_suffixes(word, i, start)
                    word = ''
                    start = -1
                else:
                    if start==-1: 
                        start = j
                    word += char
                    
    # Adds a word and all of its suffixes
    def _add_suffixes(self, word, line_no, position, whole_word=True):
        if len(word) == 0:
            return 
        
        self.suffix_tree.add_word(word, ((line_no, position), whole_word))
        # TEMP: Disabled until querying power is given to suffix tree
        # self._add_suffixes(word[1:], line_no, position + 1, suffix_tree, whole_word=False)    