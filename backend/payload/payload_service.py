
import subprocess
def open_terminal():
    command = "exo-open --launch TerminalEmulator"
    ret = subprocess.run(command, capture_output=True, shell=True)
