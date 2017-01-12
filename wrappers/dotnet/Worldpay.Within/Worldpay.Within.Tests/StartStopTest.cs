using Common.Logging;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Worldpay.Innovation.WPWithin;
using Worldpay.Innovation.WPWithin.AgentManager;

namespace Worldpay.Within.Tests
{
    [TestClass]
    public class StartStopTest
    {
        private static readonly ILog Log = LogManager.GetLogger<StartStopTest>();

        [TestMethod]
        public void StartAndStop()
        {
            RpcAgentConfiguration cfg = new RpcAgentConfiguration
            {
                CallbackPort = 9092,
                ServicePort = 9091,
                ServiceHost = "localhost"
            };
            RpcAgentManager mgr = new RpcAgentManager(cfg);
            mgr.StartThriftRpcAgentProcess();
            try
            {
                using (WPWithinService service = new WPWithinService(cfg))
                {
                    Log.InfoFormat("Successfully created service {0}", service);
                }
            }
            finally
            {
                mgr.StopThriftRpcAgentProcess();
            }
        }
    }
}
