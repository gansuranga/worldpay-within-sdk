using System;
using Common.Logging;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Worldpay.Innovation.WPWithin;
using Worldpay.Innovation.WPWithin.AgentManager;

namespace Worldpay.Within.Tests
{
    /// <summary>
    /// Summary description for ConsumerTest
    /// </summary>
    [TestClass]
    public class ConsumerTest
    {

        private static readonly ILog Log = LogManager.GetLogger<ConsumerTest>();
        private static RpcAgentManager _mgr;

        #region Additional test attributes
        //
        // You can use the following additional attributes as you write your tests:
        //
        // Use ClassInitialize to run code before running the first test in the class
        // [ClassInitialize()]
        // public static void MyClassInitialize(TestContext testContext) { }
        //
        // Use ClassCleanup to run code after all tests in a class have run
        // [ClassCleanup()]
        // public static void MyClassCleanup() { }
        //
        // Use TestInitialize to run code before running each test 
        // [TestInitialize()]
        // public void MyTestInitialize() { }
        //
        // Use TestCleanup to run code after each test has run
        // [TestCleanup()]
        // public void MyTestCleanup() { }
        //
        #endregion
        [TestInitialize]
        public void StartThriftRpcService()
        {
            _mgr = new RpcAgentManager(new RpcAgentConfiguration());
            _mgr.StartThriftRpcAgentProcess();
        }

        [TestCleanup]
        public void StopThriftRpcService()
        {
            _mgr.StopThriftRpcAgentProcess();
        }

        [TestMethod]
        public void CarWashConsumer()
        {
            string defaultDeviceName = Environment.MachineName;
            string defaultDeviceDescription =
                $".net wrapper unit test.  Class: {this.GetType().Name}.  Method: {System.Reflection.MethodBase.GetCurrentMethod().Name}";
            WPWithinService thriftClient = new WPWithinService(new RpcAgentConfiguration());
            thriftClient.SetupDevice(defaultDeviceName, defaultDeviceDescription);
            foreach (ServiceMessage service in thriftClient.DeviceDiscovery(2000))
            {
                Log.InfoFormat("Found service: ", service);
            }

        }
    }
}
