import subprocess
from tempfile import NamedTemporaryFile


class Command:
    def __init__(self, stdout, stderr, return_code):
        self.stdout = stdout
        self.stderr = stderr
        self.return_code = return_code


def run(cmd, **kw):
    """Run command

    Args:
        cmd (list): command list to run
        **kw (dict): argument to use with subprocess
    """
    shell = kw.get("shell", False)
    if shell is True:
        cmd = " ".join(cmd)
    input = kw.get("input", None)
    if "input" in kw.keys():
        kw.pop("input")

    with NamedTemporaryFile() as out:
        process = subprocess.Popen(
            cmd,
            stdout=out,
            stderr=out,
            stdin=subprocess.PIPE,
            **kw,
        )
        process.communicate(input=input)
        out.seek(0)
        stdout = out.read()
        stderr = None
        return_code = process.returncode

    return Command(stdout, stderr, return_code)
