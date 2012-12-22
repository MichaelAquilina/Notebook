from notebook import Notebook

import commands
import sys
import os

INFO =  '''
        Notebook, Developed by Michael Aquilina 2012
        contact: michaelaquilina@gmail.com
        '''
            
# Main Entry point of the application command line interface
if __name__ == '__main__':
    
    if len(sys.argv) > 1:   
        file_path = sys.argv[1]
        
        if os.path.exists(file_path):
            notebook = Notebook(file_path)
            print 'Successfully loaded \'%s\' into a notebook' % file_path
            
            # Dictionary of command names and executable functions
            commands = {
                'has': commands.has, 
                'lswords': commands.lswords,
                'get': commands.get,
                'print': commands.print_cmd,
                'reload': commands.reload_cmd,
                'info': commands.info
            }
            
            user_input = ''
            while True:
                user_input = raw_input('>')
                
                tokens = user_input.split()
                
                if len(tokens)==0:
                    continue
                
                cmd = tokens[0]
                arg = tokens[1] if len(tokens)>1 else None
                
                # exits from the application
                if cmd == 'quit':
                    break
                
                # prints out all available commands
                if cmd == 'help':
                    print INFO
                    print 'Commands: \n%s' % commands.keys()
                    continue
                
                # man prints out the doc string to provide the user with some help
                if cmd == 'man':
                    if arg in commands:
                        print commands[arg].__doc__.rstrip()[1:]
                    else:
                        print 'Unknown command specified for man pages'
                    continue
                
                # Execute the specified command with the argument
                if cmd in commands:
                    commands[cmd](notebook, arg)
                else:
                    print 'Unknown command specified.\nAccepted commands = %s' % commands.keys()
        else:
            print 'Path \'%s\' does not exist' % file_path
    else:
        print 'expected file argument'
