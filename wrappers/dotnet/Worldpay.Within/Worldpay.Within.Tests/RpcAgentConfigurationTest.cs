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

    }
}