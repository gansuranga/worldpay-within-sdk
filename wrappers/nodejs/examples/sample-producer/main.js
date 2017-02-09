var wpwithin = require('../../library/wpwithin');
var types = require('../../library/types/types');
var typesConverter = require('../../library/types/converter');
var client;

wpwithin.createClient("127.0.0.1", 9090, true, function(err, response){

  console.log("createClient.callback")
  console.log("createClient.callback.err: " + err)
  console.log("createClient.callback.response: %j", response);

  if(err == null) {

      client = response;

      setup();
  }
});

function setup() {

  client.setup("NodeJS-Device", "Sample NodeJS producer device", function(err, response){

    console.log("setup.callback.err: " + err);
    console.log("setup.callback.response: %j", response);

    if(err == null) {

      addService();
    }
  });
};

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
  // pspConfig["psp_name"] = "worldpayonlinepayments";
  // pspConfig["api_endpoint"] = "https://api.worldpay.com/v1";
  // pspConfig["hte_public_key"] = "T_C_03eaa1d3-4642-4079-b030-b543ee04b5af"
  // pspConfig["hte_private_key"] = "T_S_f50ecb46-ca82-44a7-9c40-421818af5996"
  // pspConfig["merchant_client_key"] = "T_C_03eaa1d3-4642-4079-b030-b543ee04b5af"
  // pspConfig["merchant_service_key"] = "T_S_f50ecb46-ca82-44a7-9c40-421818af5996"

  // Worldpay Total US / SecureNet
  pspConfig["psp_name"] = "securenet"
  pspConfig["api_endpoint"] = "https://gwapi.demo.securenet.com/api"
  pspConfig["hte_public_key"] = "8c0ce953-455d-4c12-8d14-ff20d565e485"
  pspConfig["hte_private_key"] = "KZ9kWv2EPy7M"
  pspConfig["developer_id"] = "12345678"
  pspConfig["app_version"] = "0.1"
  pspConfig["public_key"] = "8c0ce953-455d-4c12-8d14-ff20d565e485"
  pspConfig["secure_key"] = "KZ9kWv2EPy7M"
  pspConfig["secure_net_id"] = "8008609"

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

  client.startServiceBroadcast(20000, function(err, response){

    console.log("startServiceBroadcast.callback");
    console.log("startServiceBroadcast.err: " + err)
    console.log("startServiceBroadcast.response: %j", response)
  });
}
