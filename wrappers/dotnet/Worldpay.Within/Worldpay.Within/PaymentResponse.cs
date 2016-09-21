namespace Worldpay.Innovation.WPWithin
{
    public class PaymentResponse
    {
        public string ServerId { get; set; }

        public string ClientId { get; set; }

        public int? TotalPaid { get; set; }

        public ServiceDeliveryToken ServiceDeliveryToken { get; set; }

        public override bool Equals(object that)
        {
            return new EqualsBuilder<PaymentResponse>(this, that)
                .With(m => m.ServerId)
                .With(m => m.ClientId)
                .With(m => m.TotalPaid)
                .With(m => m.ServiceDeliveryToken)
                .Equals();
        }

        public override int GetHashCode()
        {
            return new HashCodeBuilder<PaymentResponse>(this)
                .With(m => m.ServerId)
                .With(m => m.ClientId)
                .With(m => m.TotalPaid)
                .With(m => m.ServiceDeliveryToken)
                .HashCode;
        }

        public override string ToString()
        {
            return new ToStringBuilder<PaymentResponse>(this)
                .Append(m => m.ServerId)
                .Append(m => m.ClientId)
                .Append(m => m.TotalPaid)
                .Append(m => m.ServiceDeliveryToken)
                .ToString();
        }
    }
}
