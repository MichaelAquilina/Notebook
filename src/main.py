from suffixtree import SuffixTree

file_path = 'C:\\todo.txt'
WHITE_KEYS = ['\n',' ','\t']
SPECIAL_CHARS = ['(',')','+','=','-']
          
def add_line(suffix_tree, line):
    word = '' # word buffer
    
    for char in line:
        if char in WHITE_KEYS or char in SPECIAL_CHARS:
            suffix_tree.add_word(word)
            word = ''
        else:
            word += char
            
if __name__ == '__main__':
    notebook = open(file_path,'r')
    
    suffix_tree = SuffixTree()
    
    # build the contents found in the file
    for line in notebook.readlines():
        add_line(suffix_tree, line)
    
    print suffix_tree.root
    print suffix_tree.words()