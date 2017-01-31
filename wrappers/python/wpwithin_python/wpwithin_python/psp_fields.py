"""String values for the PSP Config map."""

class CommonPSPKeys():
    """PSP Config map keys common to both Worldpay and SecureNet."""
    
    psp_name = "psp_name"
    hte_public_key = "hte_public_key"
    hte_private_key = "hte_private_key"


class WorldpayPSPKeys():
    """PSP Config map keys specific to Worldpay."""

    wp_merchant_client_key = "merchant_client_key"
    wp_merchant_service_key = "merchant_service_key"
    wp_api_endpoint = "api_endpoint"


class SecureNetPSPKeys():
    """PSP Config map keys specific to SecureNet."""

    securenet_developer_id = "developer_id"
    securenet_public_key = "public_key"
    securenet_secure_key = "secure_key"
    securenet_secure_net_id = "secure_net_id"
    securenet_app_version = "app_version"
    securenet_api_endpoint = "api_endpoint"
    securenet_http_proxy = "http_proxy"


WP_PSP_NAME = "worldpayonlinepayments"

SECURENET_PSP_NAME = "securenet"
