using System;
using System.Reflection;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Worldpay.Innovation.WPWithin.AgentManager;

namespace Worldpay.Within.Tests
{
    [TestClass]
    public class RpcAgentConfigurationTest
    {
        [TestMethod]
        public void TestPathOverride()
        {
            RpcAgentConfiguration cfg = new RpcAgentConfiguration();
            const string filename = "some random string";
            cfg.Path = filename;
            Assert.AreEqual(filename, cfg.Path);
        }


        /// <summary>
        ///     The existing available RPC Agents are:
        ///     <list type="bullet">
        ///         <item>
        ///             <term>rpc-agent-linux-arm</term>
        ///         </item>
        ///         <item>
        ///             <term>rpc-agent-linux-32</term>
        ///         </item>
        ///         <item>
        ///             <term>rpc-agent-linux-64</term>
        ///         </item>
        ///         <item>
        ///             <term>rpc-agent-mac-32</term>
        ///         </item>
        ///         <item>
        ///             <term>rpc-agent-mac-64</term>
        ///         </item>
        ///         <item>
        ///             <term>rpc-agent-mac-arm-32</term>
        ///         </item>
        ///         <item>
        ///             <term>rpc-agent-win-32.exe</term>
        ///         </item>
        ///         <item>
        ///             <term>rpc-agent-win-64.exe</term>
        ///         </item>
        ///     </list>
        /// </summary>
        [TestMethod]
        public void TestRpcAgentFilenameGenerator()
        {
            Assert.AreEqual("rpc-agent-win-64.exe",
                RpcAgentFilenameGenerator.GetForEnvironment(ProcessorArchitecture.Amd64, PlatformID.Win32Windows, true));
            Assert.AreEqual("rpc-agent-linux-arm",
                RpcAgentFilenameGenerator.GetForEnvironment(ProcessorArchitecture.Arm, PlatformID.Unix, true));
            Assert.AreEqual("rpc-agent-linux-arm",
                RpcAgentFilenameGenerator.GetForEnvironment(ProcessorArchitecture.Arm, PlatformID.Unix, false));
            Assert.AreEqual("rpc-agent-linux-32",
                RpcAgentFilenameGenerator.GetForEnvironment(ProcessorArchitecture.X86, PlatformID.Unix, false));
            // This is possibly an impossibility, X86 with 64-bit, but at least it should behave logically.
            Assert.AreEqual("rpc-agent-linux-64",
                RpcAgentFilenameGenerator.GetForEnvironment(ProcessorArchitecture.X86, PlatformID.Unix, true));
            Assert.AreEqual("rpc-agent-mac-32",
                RpcAgentFilenameGenerator.GetForEnvironment(ProcessorArchitecture.X86, PlatformID.MacOSX, false));
            Assert.AreEqual("rpc-agent-mac-64",
                RpcAgentFilenameGenerator.GetForEnvironment(ProcessorArchitecture.Amd64, PlatformID.MacOSX, true));
        }
    }
}