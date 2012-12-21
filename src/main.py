from suffixtree import SuffixTree
import sys
import os

WHITE_KEYS = ['\n',' ','\t']
SPECIAL_CHARS = ['(',')','+','=','-']

def parse_file(file, suffix_tree):
    # build the contents found in the file
    for i, line in enumerate(file.readlines()):
        word = '' # word buffer
        start = -1
        
        for j, char in enumerate(line):
            if char in WHITE_KEYS or char in SPECIAL_CHARS:
                add_suffixes(word, i, start, suffix_tree)
                word = ''
                start = -1
            else:
                if start==-1: 
                    start = j
                word += char

# Adds a word and all of its suffixes
def add_suffixes(word, line_no, position, suffix_tree, whole_word=True):
    if len(word) == 0:
        return 
    
    suffix_tree.add_word(word, ((line_no, position), whole_word))
    add_suffixes(word[1:], line_no, position + 1, suffix_tree, whole_word=False)
            
if __name__ == '__main__':
    
    if len(sys.argv) > 1:   
        file_path = sys.argv[1]
        
        if os.path.exists(file_path):
            notebook = open(file_path,'r')
            
            suffix_tree = SuffixTree()    
            parse_file(notebook, suffix_tree)
            
            # Program command line interaction
            # For now the program just tells you if the input word exists in the file and if so, its meta information
            
            # Add commands like has, lswords etc
            user_input = ''
            while user_input!='quit':
                user_input = raw_input()
                
                found =  suffix_tree.has_word(user_input)
                if found:
                    print 'True: <%s>' % suffix_tree.get_data(user_input)
                else:
                    print 'False'
    else:
        print 'expected file argument'
            
            
