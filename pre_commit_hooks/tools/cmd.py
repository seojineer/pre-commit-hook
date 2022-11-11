import subprocess


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

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE,
        **kw,
    )
    stdout, stderr = process.communicate(input=input)
    return_code = process.returncode

    return Command(stdout, stderr, return_code)
