"""Launcher for RPC Agent.

File name should be rpc-agent-[system]-[architecture], ie rpc-agent-darwin-amd64.
"""

import time
from subprocess import Popen
import sys
import platform
import os
from os.path import normpath, join

DEFAULT_PATH = './wpw-bin/'
DEFAULT_ENV = 'WPW_HOME'

def os_arch():
    """Return the architecture as '386', 'amd64', 'arm32' or 'arm64'."""
    out = ''
    if platform.machine().lower()[:3] == 'arm':
        out += 'arm'
    if sys.maxsize > 2**32:
        if out == 'arm':
            out += '64'
        else:
            out = 'amd64'
    else:
        if out == 'arm':
            out += '64'
        else:
            out = '386'
    return out

def os_platform():
    """Return the operating system as 'windows', 'darwin' or 'linux'."""
    os_name = platform.system().lower()
    if os_name == 'windows' or os_name == 'darwin':
        return os_name
    else:
        return 'linux'

def run_rpc_agent(port,
                  rpc_dir=None,
                  start_callback_server=False,
                  callback_port=None):
    """Run RPC Agent.

    Args:
        port (integer): port to run RPC agent on
        (optional) rpc_dir (string): path to directory with rpc agent launchers. If not specified,
        will search for the files in ./wpw-bin/ and $WPW_HOME/bin, in that order.
        (optional) start_callback_server (boolean): whether to start a callback server
        (optional) callback_port (integer): port to listen for callback events
    """
    suffix = os_platform()
    agent = 'rpc-agent-' + os_platform() + '-' + os_arch()
    if suffix == 'win':
        agent += '.exe'

    if rpc_dir is None:
        if os.path.isfile(normpath(join(DEFAULT_PATH, agent))):
            rpc_dir = DEFAULT_PATH
        elif os.getenv(DEFAULT_ENV, default=False):
            env_path = join(os.getenv(DEFAULT_ENV), '/bin/')
            if os.path.isfile(normpath(join(env_path, agent))):
                rpc_dir = env_path
        else:
            raise ValueError('RPC Agent binary not found at the default locations,\
 please specify a directory.')

    args = [rpc_dir + agent,
            '-port='+str(port),
            '-logfile=wpwithin.log',
            '-loglevel=debug,error,warn,info,fatal']

    if start_callback_server:
        args.append('-callbackport='+str(callback_port))

    proc = Popen(args)
    time.sleep(2)
    return proc

def start_server(server):
    """Start callback server."""
    server.serve()
