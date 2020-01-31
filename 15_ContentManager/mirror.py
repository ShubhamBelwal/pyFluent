class LookingGlass:

    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write #Monkey-patch sys.stdout.write
        return 'JABBERWOCKY' #Return this value to calling object
    
    def reverse_write(self, text):
        self.original_write(text[::-1])
    
    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write #Revert original ouput
        if exc_type is ZeroDivisionError:
            print('Please DO NOT DIVIDE by Zero!')
            return True