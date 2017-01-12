using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Worldpay.Innovation.WPWithin.AgentManager;
using System.Threading;
using Common.Logging;

namespace Worldpay.Within.Tests
{
    [TestClass]
    public class RpcAgentManagerTest
    {
        private static readonly ILog Log = LogManager.GetLogger<RpcAgentManagerTest>();

        [TestMethod]
        public void StartAndStopViaEvent()
        {
            RpcAgentManager mgr = new RpcAgentManager(new RpcAgentConfiguration());

            bool started = false;
            mgr.OnStarted += (s,e) =>
            {
                started = true;
                Log.Info("Started RPC Agent manager ok, now stopping it");
                mgr.StopThriftRpcAgentProcess();
            };
            Log.Info("Starting RPC Agent manager with default configuration");
            mgr.StartThriftRpcAgentProcess();

            int retries = 0;
            while(!started && retries<10)
            {
                Thread.Sleep(500);
                retries++;
            }
            if (!started) Assert.Fail("Thrift RPC Agent didn't start within 5000ms");
            Log.Info("RPC Agent manager confirmed terminated");
        }

        

    }
}
