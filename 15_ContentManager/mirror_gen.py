import contextlib

# The @contextmanager decorator reduces the boilerplate of creating a context manager:
# instead of writing a whole class with __enter__/__exit__ methods, you just implement
# a generator with a single yield that should produce whatever you want the __en
# ter__ method to return.

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    
    # the code after yield will run
    # when __exit__ is called at the end of the block.
    sys.stdout.write = original_write