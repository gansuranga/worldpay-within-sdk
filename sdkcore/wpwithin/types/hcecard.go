package types

// HCECard represents details of a payment card
type HCECard struct {
	FirstName  string `json:"firstName"`
	LastName   string `json:"lastName"`
	ExpMonth   int32  `json:"expMonth"`
	ExpYear    int32  `json:"expYear"`
	CardNumber string `json:"cardNumber"`
	Type       string `json:"type"`
	Cvc        string `json:"cvc"`
}
