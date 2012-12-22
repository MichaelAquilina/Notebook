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
        
def printline(notebook, arg):
    # Naive implementation, needs to be improved
    if arg:
        with open(notebook.file_path) as nfile:
            for line_no, line in enumerate(nfile.readlines()):
                if line_no == int(arg):
                    print line.rstrip()
                    return
                
        print 'Unable to find specified line (%s)' % arg
    else:
        print 'Line Argument expected'
        