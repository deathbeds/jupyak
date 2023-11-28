__all__ = ["__version__", "_STDOUT", "_STDERR"]
__version__ = __import__("importlib.metadata").metadata.version("jupyak")


_STDOUT = None
_STDERR = None
