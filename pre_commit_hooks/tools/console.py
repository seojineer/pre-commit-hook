try:
    from py_console import console as cs
except ImportError:
    pass


class Console:
    """Show message with color"""

    _bold = "\u001b[1m"
    _red = "\u001b[31m"
    _yellow = "\u001B[33m"
    _blue = "\u001B[34m"
    _gray = "\u001b[90m"
    _reset = "\u001b[0m"

    @classmethod
    def error(cls, s):
        try:
            cs.error(s, showTime=False)
        except:
            print(f"{cls._bold}{cls._red}{s}{cls._reset}")

    @classmethod
    def warn(cls, s):
        try:
            cs.warn(s, showTime=False)
        except:
            print(f"{cls._bold}{cls._yellow}{s}{cls._reset}")

    @classmethod
    def info(cls, s):
        try:
            cs.info(s, showTime=False)
        except:
            print(f"{cls._blue}{s}{cls._reset}")
