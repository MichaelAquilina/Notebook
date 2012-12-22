from suffixtree import SuffixTree
import sys
import os

WHITE_KEYS = ['\n',' ','\t']
SPECIAL_CHARS = ['(',')','=','-']

def parse_file(notebook, suffix_tree):
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

# Adds a word and all of its suffixes
def add_suffixes(word, line_no, position, suffix_tree, whole_word=True):
    if len(word) == 0:
        return 
    
    suffix_tree.add_word(word, ((line_no, position), whole_word))
    # TEMP: Disabled until querying power is given to suffix tree
    # add_suffixes(word[1:], line_no, position + 1, suffix_tree, whole_word=False)
    
# ======= COMMANDS ========
    
def has_command(arg, suffix_tree):
    if arg:    
        print suffix_tree.has_word(arg)
    else:
        print 'Argument expected'

def lswords_command(arg, suffix_tree):
    print suffix_tree.words()
            
def get_command(arg, suffix_tree):
    if arg:
        data = suffix_tree.get_data(arg)
        if data: 
            for entry in data:
                print 'position=%s, whole_word=%s' % entry.meta
            
            print '(%s entries)' % len(data)
        else:
            print '\'%s\' not found' % arg
    else:
        print 'Argument expected'
        
            
if __name__ == '__main__':
    
    if len(sys.argv) > 1:   
        file_path = sys.argv[1]
        
        if os.path.exists(file_path):
            notebook = open(file_path,'r')
            
            suffix_tree = SuffixTree()    
            parse_file(notebook, suffix_tree)
            
            # Dictionary of command names and executable functions
            commands = {
                'has':has_command, 
                'lswords':lswords_command,
                'get':get_command
            }
            
            user_input = ''
            while user_input!='quit':
                user_input = raw_input()
                
                tokens = user_input.split()
                
                if len(tokens)==0:
                    continue
                
                cmd = tokens[0]
                arg = tokens[1] if len(tokens)>1 else None
                
                if cmd in commands:
                    # Execute the specified command with the argument
                    commands[cmd](arg, suffix_tree)
                else:
                    print 'Unknown command specified.\nAccepted commands = %s' % commands.keys()
    else:
        print 'expected file argument'
            
            
