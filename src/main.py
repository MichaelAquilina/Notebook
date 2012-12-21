from suffixtree import SuffixTree

file_path = 'C:\\todo.txt'
WHITE_KEYS = ['\n',' ','\t']
SPECIAL_CHARS = ['(',')','+','=','-']

# Adds a word and all of its suffixes
def add_suffixes(word, line_no, position, suffix_tree, whole_word=True):
    if len(word) == 0:
        return 
    
    suffix_tree.add_word(word, ((line_no, position), whole_word))
    add_suffixes(word[1:], line_no, position + 1, suffix_tree, whole_word=False)
            
if __name__ == '__main__':
    notebook = open(file_path,'r')
    
    suffix_tree = SuffixTree()
    
    # build the contents found in the file
    for i, line in enumerate(notebook.readlines()):
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
    
    print suffix_tree.root   # Prints the root node of the suffix tree
    print suffix_tree.words()
    
    line_str = 'position=%s, whole_word=%s'
    
    print suffix_tree.has_word('ASUS')
    print suffix_tree.has_word('Christmas')
    
    print suffix_tree.get_data('ASUS')
    print suffix_tree.get_data('SUS')
    print line_str % suffix_tree.get_data('ASUS').meta
    print line_str % suffix_tree.get_data('Steff').meta
    print line_str % suffix_tree.get_data('Christina').meta