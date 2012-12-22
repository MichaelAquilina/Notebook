from notebook import Notebook

import commands
import sys
import os    
            
# Main Entry point of the application command line interface
if __name__ == '__main__':
    
    if len(sys.argv) > 1:   
        file_path = sys.argv[1]
        
        if os.path.exists(file_path):
            notebook = Notebook(file_path)
            
            # Dictionary of command names and executable functions
            commands = {
                'has': commands.has, 
                'lswords': commands.lswords,
                'get': commands.get,
                'print': commands.printline,
                'reload': commands.reload
            }
            
            user_input = ''
            while user_input!='quit':
                user_input = raw_input()
                
                tokens = user_input.split()
                
                if len(tokens)==0:
                    continue
                
                cmd = tokens[0]
                arg = tokens[1] if len(tokens)>1 else None
                
                if cmd == 'man':
                    print commands[arg].__doc__
                    continue
                
                if cmd in commands:
                    # Execute the specified command with the argument
                    commands[cmd](notebook, arg)
                else:
                    print 'Unknown command specified.\nAccepted commands = %s' % commands.keys()
        else:
            print 'Path \'%s\' does not exist' % file_path
    else:
        print 'expected file argument'
