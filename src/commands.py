"""Available commands for the Notebook program are stored in this file"""

def has(notebook, arg):
    """
    Checks if a word exists in the currently loaded notebook.
    """
    if arg:    
        print notebook.suffix_tree.has_word(arg)
    else:
        print 'Argument expected'

def lswords(notebook, arg):
    """
    Lists all the unique words found in the currently loaded notebook.
    """
    words = notebook.suffix_tree.words()
    print words
    print '(%s entries)' % len(words) 
            
def get(notebook, arg):
    """
    gets meta information from the specified word in the currently loaded notebook.
    """
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
    """
    prints the specified line from the currently loaded notebook.
    """
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
        
def reload(notebook, arg):
    """
    Loads the notebook with the specified file. Will reload the current file if no
    path is specified in the arguments.
    """
    notebook.reload(arg)
        
    print 'Notebook reloaded with %s' % notebook.file_path
    