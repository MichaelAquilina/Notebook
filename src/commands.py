"""Available commands for the Notebook program are stored in this file"""

def has(arg, suffix_tree):
    if arg:    
        print suffix_tree.has_word(arg)
    else:
        print 'Argument expected'

def lswords(arg, suffix_tree):
    print suffix_tree.words()
            
def get(arg, suffix_tree):
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
    