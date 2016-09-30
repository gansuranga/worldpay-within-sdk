package types

// Device details of a device
type Device struct {
	UID         string           `json:"uid"`
	Name        string           `json:"name"`
	Description string           `json:"description"`
	Services    map[int]*Service `json:"services"`
	IPv4Address string           `json:"ipv4Address"`
}

// NewDevice create a new device
func NewDevice(name, description, uid, ipv4Address, currencyCode string) (*Device, error) {

	result := &Device{
		Name:        name,
		Description: description,
		UID:         uid,
		IPv4Address: ipv4Address,
	}

	return result, nil
}
