This is a demonstration of an `ImportError` with `sys.path` being correct.
The cause is `os.chdir()` followed by a package-intern import, see 
`__main__.py`. Importing the problematic module in `__init__.py` fixes the
problem.

For me this ImportError was hard to debug and the available information rather
sparse. The original issue is described at 
http://stackoverflow.com/questions/25641003/how-to-debug-importerror-with-sys-path-being-correct

## Usage
Clone the repository. Get the ImportError with:
```
python -m importerror
```
whereas this works (does not raise an ImportError):
```
python importerror/__main__.py
```
