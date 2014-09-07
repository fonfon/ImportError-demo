import mypackage
import os

if __name__ == '__main__':
    mypackage.file1.foo()

    # os.chdir() makes importing package-intern modules (that are not loaded
    # in __init__.py) impossible, although sys.path stays exactly the same
    os.chdir('/')
    from mypackage.file2 import bar
    bar()
