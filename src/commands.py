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
        