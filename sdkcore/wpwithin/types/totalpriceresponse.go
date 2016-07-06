package types

type TotalPriceResponse struct {

	ServerID string `json:"serverID"`
	ClientID string `json:"clientID"`
	PriceID int `json:"priceID"`
	UnitsToSupply int `json:"unitsToSupply"`
	TotalPrice int `json:"totalPrice"`
	CurrencyCode string `json:"currencyCode"`
	PaymentReferenceID string `json:"paymentReferenceID"`
	MerchantClientKey string `json:"merchantClientKey"`
}
