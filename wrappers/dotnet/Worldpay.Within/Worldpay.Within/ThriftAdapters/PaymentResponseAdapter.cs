using ThriftPaymentResponse = Worldpay.Innovation.WPWithin.Rpc.Types.PaymentResponse;

namespace Worldpay.Innovation.WPWithin.ThriftAdapters
{
    internal class PaymentResponseAdapter
    {
        public static PaymentResponse Create(ThriftPaymentResponse makePayment)
        {
            return new PaymentResponse()
            {
                ClientId = makePayment.ClientId,
                ServerId = makePayment.ServerId,
                ServiceDeliveryToken = ServiceDeliveryTokenAdapter.Create(makePayment.ServiceDeliveryToken),
                TotalPaid = makePayment.TotalPaid
            };
        }
    }
}