﻿using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;

namespace Worldpay.Innovation.WPWithin.Sample.Commands
{

    /// <summary>
    /// Shows how a consumer can purchase and take delivery of a service offered by a producer, such as <see cref="SimpleProducer"/>.
    /// </summary>
    internal class SimpleConsumer
    {
        private readonly TextWriter _error;
        private readonly TextWriter _output;

        public SimpleConsumer(TextWriter output, TextWriter error)
        {
            _output = output;
            _error = error;
        }

        /// <summary>
        ///  Consumes a single unit of the first price, of the first service of the first device found.
        /// </summary>
        /// <param name="service">An initialised service interface.</param>
        /// <returns>Indication of the success of the operation.</returns>
        public CommandResult MakePurchase(WPWithinService service)
        {
            service.SetupDevice("my-device", "an example consumer device");

            ServiceMessage firstDevice = DiscoverDevices(service)?.FirstOrDefault();
            if (firstDevice == null)
            {
                _error.WriteLine("No devices discovered.  Is a producer running on your network?");
                return CommandResult.NonCriticalError;
            }
            else
            {
                _output.WriteLine("Discovered device: {0}", firstDevice);
            }

            // Configure our WPWithinService as a consumer, using a dummy payment card.
            ConnectToDevice(service, firstDevice);

            // Get the first service offered by the device.
            ServiceDetails firstService = GetAvailableServices(service)?.FirstOrDefault();
            if (firstService == null)
            {
                _error.WriteLine("Couldn't find any services offered by {0}", firstDevice);
                return CommandResult.NonCriticalError;
            }
            else
            {
                _output.WriteLine("Found first service {0}", firstService);
            }

            // Get the first first offered by the first service on the first device.
            Price firstPrice = GetServicePrices(service, firstService.ServiceId)?.FirstOrDefault();
            if (firstPrice == null) return CommandResult.NonCriticalError;

            TotalPriceResponse priceResponse = GetServicePriceQuote(service, firstService.ServiceId, 1,
                firstPrice.Id);
            if (priceResponse == null) return CommandResult.CriticalError;

            PurchaseService(service, firstService.ServiceId, priceResponse);

            return CommandResult.Success;
        }

        /// <summary>
        /// Spends 5 seconds attempting to discover devices offering services to consume.
        /// </summary>
        /// <param name="service">A WPWithin service instance that will be used to do the discovery.</param>
        /// <returns>A list (possibly empty) of discovered devices/services.</returns>
        private List<ServiceMessage> DiscoverDevices(WPWithinService service)
        {
            List<ServiceMessage> devices = service.DeviceDiscovery(5000).ToList();

            if (devices.Any())
            {
                _output.WriteLine("{0} services found:\n", devices.Count);

                foreach (ServiceMessage svcMsg in devices)
                {
                    _output.WriteLine("Device Description: {0}", svcMsg.DeviceDescription);
                    _output.WriteLine("Hostname: {0}", svcMsg.Hostname);
                    _output.WriteLine("Port: {0}", svcMsg.PortNumber);
                    _output.WriteLine("URL Prefix: {0}", svcMsg.UrlPrefix);
                    _output.WriteLine("ServerId: {0}", svcMsg.ServerId);
                    _output.WriteLine("--------");
                }
            }
            else
            {
                _error.WriteLine("No services found.");
            }

            return devices;
        }

        private void ConnectToDevice(WPWithinService service, ServiceMessage svcMsg)
        {
            HceCard card = new HceCard
            {
                FirstName = "Bilbo",
                LastName = "Baggins",
                CardNumber = "5555555555554444",
                ExpMonth = 11,
                ExpYear = 2018,
                Type = "Card",
                Cvc = "113",
            };
            service.InitConsumer("http://", svcMsg.Hostname, svcMsg.PortNumber.Value, svcMsg.UrlPrefix, svcMsg.ServerId,
                card);
        }

        private List<ServiceDetails> GetAvailableServices(WPWithinService service)
        {
            List<ServiceDetails> services = service.RequestServices().ToList();
            _output.WriteLine("{0} services found", services.Count);
            foreach (ServiceDetails svc in services)
            {
                _output.WriteLine(svc);
            }
            return services;
        }

        private List<Price> GetServicePrices(WPWithinService service, int serviceId)
        {
            List<Price> prices = service.GetServicePrices(serviceId).ToList();

            _output.WriteLine("{0} prices found for service id {1}", prices.Count, serviceId);

            foreach (Price price in prices)
            {
                _output.WriteLine(
                    $"Price:\n\tId: {price.Id}\n\tDescription: {price.Description}\n\tUnitId: {price.UnitId}\n\tUnitDescription: {price.UnitDescription}\n\tUnit Price Amount: {price.PricePerUnit.Amount}\n\tUnit Price Currency: {price.PricePerUnit.CurrencyCode}");
            }
            return prices;
        }

        private TotalPriceResponse GetServicePriceQuote(WPWithinService service, int serviceId, int numberOfUnits,
            int priceId)
        {
            TotalPriceResponse tpr = service.SelectService(serviceId, numberOfUnits, priceId);

            if (tpr != null)
            {
                _output.WriteLine("Received price quote:");
                _output.WriteLine("Merchant client key: {0}", tpr.MerchantClientKey);
                _output.WriteLine("Payment reference id: {0}", tpr.PaymentReferenceId);
                _output.WriteLine("Units to supply: {0}", tpr.UnitsToSupply);
                _output.WriteLine("Total price: {0}", tpr.TotalPrice);
            }
            else
            {
                _output.WriteLine("No Total Price Response received");
            }
            return tpr;
        }

        private PaymentResponse PurchaseService(WPWithinService service, int serviceId, TotalPriceResponse pReq)
        {
            PaymentResponse pResp = service.MakePayment(pReq);

            if (pResp != null)
            {
                _output.WriteLine("Payment response: ");
                _output.WriteLine("Client ServiceId: {0}", pResp.ServerId);
                _output.WriteLine("Total paid: {0}", pResp.TotalPaid);
                _output.WriteLine("ServiceDeliveryToken.issued: {0}", pResp.ServiceDeliveryToken.Issued);
                _output.WriteLine("ServiceDeliveryToken.expiry: {0}", pResp.ServiceDeliveryToken.Expiry);
                _output.WriteLine("ServiceDeliveryToken.key: {0}", pResp.ServiceDeliveryToken.Key);
                _output.WriteLine("ServiceDeliveryToken.signature: [{0}]", ToReadableString(pResp.ServiceDeliveryToken.Signature));
                _output.WriteLine("ServiceDeliveryToken.refundOnExpiry: {0}", pResp.ServiceDeliveryToken.RefundOnExpiry);

                BeginServiceDelivery(service, serviceId, pResp.ServiceDeliveryToken, 1);
            }
            else
            {
                _error.WriteLine("Result of MakePayment call is null");
            }

            return pResp;
        }

        private string ToReadableString(byte[] ba)
        {
            StringBuilder hex = new StringBuilder();
            for (int index = 0; index < ba.Length; index++)
            {
                if (index > 0)
                {
                    hex.Append(" ");
                }
                byte b = ba[index];
                hex.AppendFormat("{0:x2}", b);
            }
            return hex.ToString();
        }

        private void BeginServiceDelivery(WPWithinService service, int serviceId, ServiceDeliveryToken token,
            int unitsToSupply)
        {
            _output.WriteLine("Calling beginServiceDelivery()");

            service.BeginServiceDelivery(serviceId, token, unitsToSupply);

            _output.WriteLine("Sleeping 10 seconds..");
            Thread.Sleep(10000);
            EndServiceDelivery(service, serviceId, token, unitsToSupply);
        }

        private void EndServiceDelivery(WPWithinService service, int serviceId, ServiceDeliveryToken token,
            int unitsReceived)
        {
            _output.WriteLine("Calling endServiceDelivery()");

            service.EndServiceDelivery(serviceId, token, unitsReceived);
        }
    }
}