from subprocess import Popen, PIPE
import sys
import platform

def os_arch():
    """Give the architecture as 32 or 64"""
    if platform.machine().lower()[:3] == 'arm':
        out = 'arm'
    elif sys.maxsize > 2**32:
        out = '64'
    else:
        out = '32'
    return out

def os_platform():
    """Give the platform as win, mac or linux"""
    os = platform.system().lower()
    if os == 'windows':
        out = 'win'
    elif os == 'darwin':
        out = 'mac'
    else:
        out = os
    return out

def run_rpc_agent(port, rpc_dir, callback_port=None):
    """Run RPC Agent
    Args:
        execPath (string): path to directory with rpc agent launchers
        port (integer): port to run RPC agent on
    """
    os = os_platform()
    agent = 'rpc-agent-' + os + '-' + os_arch()
    if os == 'win':
        agent += '.exe'

    flags = '-port='+str(port)
    if callback_port is not None:
        flags += '-callbackport='+str(callback_port)

    proc = Popen([rpc_dir + agent, flags], stdout=PIPE, stderr=PIPE)
    return proc
