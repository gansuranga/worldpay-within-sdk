using System.Collections.Generic;

namespace Worldpay.Innovation.WPWithin.ThriftAdapters
{
    /// <summary>
    /// TODO: Fix KeyNotFoundExceptions by testing value before returning.
    /// </summary>
    public class PspConfig
    {
        public const string PspNameProperty = "psp_name";
        public const string HtePublicKeyProperty = "hte_public_key";
        public const string HtePrivateKeyProperty = "hte_private_key";
        public const string ApiEndpointProperty = "api_endpoint";
        public const string MerchantClientKeyProperty = "merchant_client_key";
        public const string MerchantServiceKeyProperty = "merchant_service_key";

        public const string PspNameDefault = "worldpayonlinepayments";
        public const string ApiEndpointDefault = "https://api.worldpay.com/v1";

        private readonly Dictionary<string, string> _properties;

        public string this[string name]
        {
            get { return _properties[name]; }
            set { _properties[name] = value; }
        }

        public PspConfig()
        {
            _properties = new Dictionary<string, string>
            {
                {PspNameProperty, PspNameDefault},
                {ApiEndpointProperty, ApiEndpointDefault}
            };
        }

        public string PspName
        {
            get { return  _properties[PspNameProperty]; }
            set { _properties[PspNameProperty] = value; }
        }

        public string HtePublicKey
        {
            get { return _properties[HtePublicKeyProperty]; }
            set { _properties[HtePublicKeyProperty] = value; }
        }

        public string HtePrivateKey
        {
            get { return _properties[HtePrivateKeyProperty]; }
            set { _properties[HtePrivateKeyProperty] = value; }
        }

        public string MerchantClientKey
        {
            get { return _properties[MerchantClientKeyProperty]; }
            set { _properties[MerchantClientKeyProperty] = value; }
        }

        public string MerchantServiceKey
        {
            get { return _properties[MerchantServiceKeyProperty]; }
            set { _properties[MerchantServiceKeyProperty] = value; }
        }

        public string ApiEndPoint
        {
            get { return _properties[ApiEndpointProperty]; }
            set { _properties[ApiEndpointProperty] = value; }
        }

        /// <summary>
        /// Exposes the configuration as the dictonary that the Thrift RPC Agent requires.
        /// </summary>
        /// <returns>A dictionary, never null, however contents depend on user's calls to other properties.</returns>
        internal Dictionary<string, string> ToThriftRepresentation()
        {
            return new Dictionary<string, string>(_properties);
        }
    }
}