var wpwithin = require('../../library/wpwithin');
var wpwConstants = require('../../library/constants');
var types = require('../../library/types/types');
var typesConverter = require('../../library/types/converter');

var eventListener = {
  beginServiceDelivery: function(clientId, serviceDeliveryToken, unitsToSupply, callback) {

    console.log("Node js event:: beginServiceDelivery");

    console.log("clientId: %s", clientId);
    console.log("unitsToSupply: %d", unitsToSupply);
    console.log("serviceDeliveryToken: %j", serviceDeliveryToken);

  },
  endServiceDelivery: function(clientId, serviceDeliveryToken, unitsReceived, callback) {

    console.log("Node js event:: endServiceDelivery");

    console.log("clientId: %s", clientId);
    console.log("unitsToSupply: %d", unitsReceived);
    console.log("serviceDeliveryToken: %j", serviceDeliveryToken);
  }
};

var client

wpwithin.createClient("127.0.0.1", 9088, true, function(err, response){

  console.log("createClient.callback")
  console.log("createClient.callback.err: " + err)
  console.log("createClient.callback.response: %j", response);

  if(err == null) {

    client = response;

    setup();
  }

}, eventListener, 9092);

function setup() {

  client.setup("NodeJS-Device", "Sample NodeJS producer device", function(err, response){

    console.log("setup.callback.err: " + err);
    console.log("setup.callback.response: %j", response);

    if(err == null) {

      addService();
    }
  });
}

function addService() {

  var service = new types.Service();

  service.id = 1;
  service.name = "RoboWash";
  service.description = "Car washed by robot";

  var rwPrice = new types.Price();
  rwPrice.id = 1;
  rwPrice.description = "Car wash";
  rwPrice.unitId = 1;
  rwPrice.unitDescription = "Single wash";
  var pricePerUnit = new types.PricePerUnit();
  pricePerUnit.amount = 650;
  pricePerUnit.currencyCode = "GBP";
  rwPrice.pricePerUnit = pricePerUnit;
  service.prices = new Array();
  service.prices[0] = rwPrice;

  client.addService(service, function(err, response) {

      console.log("addService.callback");
      console.log("err: " + err)
      console.log("response: %j", response)

      if(err == null) {

        initProducer();
      }
  });
}

function initProducer() {

  var pspConfig = new Array();

  // Worldpay Online Payments
  // pspConfig[wpwConstants.PSP_NAME] = wpwConstants.WORLDPAY_ONLINE_PAYMENTS
  // pspConfig[wpwConstants.API_ENDPOINT] = "https://api.worldpay.com/v1";
  // pspConfig[wpwConstants.HTE_PUBLIC_KEY] = "T_C_03eaa1d3-4642-4079-b030-b543ee04b5af"
  // pspConfig[wpwConstants.HTE_PRIVATE_KEY] = "T_S_f50ecb46-ca82-44a7-9c40-421818af5996"
  // pspConfig[wpwConstants.MERCHANT_CLIENT_KEY] = "T_C_03eaa1d3-4642-4079-b030-b543ee04b5af"
  // pspConfig[wpwConstants.MERCHANT_SERVICE_KEY] = "T_S_f50ecb46-ca82-44a7-9c40-421818af5996"

  // Worldpay Total US / SecureNet
  pspConfig[wpwConstants.PSP_NAME] = wpwConstants.SECURE_NET
  pspConfig[wpwConstants.API_ENDPOINT] = "https://gwapi.demo.securenet.com/api"
  pspConfig[wpwConstants.HTE_PUBLIC_KEY] = "8c0ce953-455d-4c12-8d14-ff20d565e485"
  pspConfig[wpwConstants.HTE_PRIVATE_KEY] = "KZ9kWv2EPy7M"
  pspConfig[wpwConstants.DEVELOPER_ID] = "12345678"
  pspConfig[wpwConstants.APP_VERSION] = "0.1"
  pspConfig[wpwConstants.PUBLIC_KEY] = "8c0ce953-455d-4c12-8d14-ff20d565e485"
  pspConfig[wpwConstants.SECURE_KEY] = "KZ9kWv2EPy7M"
  pspConfig[wpwConstants.SECURE_NET_ID] = "8008609"

  client.initProducer(pspConfig, function(err, response) {

    console.log("initProducer.callback");
    console.log("initProducer.err: " + err)
    console.log("initProducer.response: %j", response)

    if(err == null) {

      startBroadcast();
    }
  });
}

function startBroadcast() {

  client.startServiceBroadcast(0, function(err, response){

    console.log("startServiceBroadcast.callback");
    console.log("startServiceBroadcast.err: " + err)
    console.log("startServiceBroadcast.response: %j", response)
  });
}
