"""Available commands for the Notebook program are stored in this file"""

def has(notebook, arg):
    if arg:    
        print notebook.suffix_tree.has_word(arg)
    else:
        print 'Argument expected'

def lswords(notebook, arg):
    print notebook.suffix_tree.words()
            
def get(notebook, arg):
    if arg:
        data = notebook.suffix_tree.get_data(arg)
        if data: 
            for entry in data:
                print 'position=%s, whole_word=%s' % entry.meta
            
            print '(%s entries)' % len(data)
        else:
            print '\'%s\' not found' % arg
    else:
        print 'Argument expected'
        
def print_line(notebook, arg):
    # Naive implementation, needs to be improved
    if arg:
        file = open(notebook.file_path)
        for line_no, line in enumerate(file.readlines()):
            if line_no == int(arg):
                print line
                return
        
        print 'Unable to find specified line (%s)' % arg
    else:
        print 'Line Argument expected'
        