from suffixtree import SuffixTree

file_path = 'C:\\todo.txt'
WHITE_KEYS = ['\n',' ','\t']
SPECIAL_CHARS = ['(',')','+','=','-']
          
def add_line(suffix_tree, line, line_no):
    word = '' # word buffer
    start = -1
    
    for index, char in enumerate(line):
        if char in WHITE_KEYS or char in SPECIAL_CHARS:
            suffix_tree.add_word(word, (line_no, start) )
            word = ''
            start = -1
        else:
            if start==-1: 
                start = index
            word += char
            
if __name__ == '__main__':
    notebook = open(file_path,'r')
    
    suffix_tree = SuffixTree()
    
    # build the contents found in the file
    for index, line in enumerate(notebook.readlines()):
        add_line(suffix_tree, line, index)
    
    print suffix_tree.root
    print suffix_tree.words()
    
    str = 'line %s, position %s'
    
    print str % suffix_tree.get_meta('ASUS')
    print str % suffix_tree.get_meta('Steff')
    print str % suffix_tree.get_meta('Christina')