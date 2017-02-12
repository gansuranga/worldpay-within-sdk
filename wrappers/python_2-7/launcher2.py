import sys
import platform

def detectHostOS():
        hostOS = platform.system().lower()
        if hostOS is None or len(hostOS) == 0:
            return "UNKNOWN"
        elif "darwin" in hostOS.lower() or "mac" in hostOS.lower():
            return "MAC"
        elif "win" in hostOS.lower():
            return "WINDOWS"
        elif "linux" in hostOS.lower():
            return "LINUX"
        else: 
            return "UNKNOWN"
        

def detectHostArchitecture():
        is_64bits = sys.maxsize > 2**32
        if is_64bits:
            arch = 'x64'
        else:
            arch = 'ia32'

        if arch is None or len(arch) == 0:
            return "UNKNOWN" 
        elif "64" in arch.lower():
            return "X86_64"
        elif "arm" in arch.lower():
            return "ARM32"
        elif "x86" in arch.lower():
            return "IA32"
        elif "32" in arch.lower():
            return "IA32"
        else:
            return "UNKNOWN"

def getRpcAgentName():
   hostOS = detectHostOS()
   hostArch = detectHostArchitecture()

   rpcAgent = "rpc-agent"

   if "MAC" == hostOS and "X86_64" == hostArch:
      rpcAgent = "rpc-agent-darwin-amd64"		
   elif "MAC" == hostOS and "IA32" == hostArch:
      rpcAgent = "rpc-agent-darwin-386" 

   if "LINUX" == hostOS and "X86_64" == hostArch:
      rpcAgent = "rpc-agent-linux-arm64"
   elif "WINDOWS" == hostOS and "IA32" == hostArch:		
      rpcAgent = "rpc-agent-linux-arm32"		

   if "WINDOWS" == hostOS and "IA32" == hostArch:
      rpcAgent = "rpc-agent-windows-386.exe"
   elif "WINDOWS" == hostOS and "X86_64" == hostArch:
      rpcAgent = "rpc-agent-windows-amd64.exe"

   return rpcAgent

print getRpcAgentName()
