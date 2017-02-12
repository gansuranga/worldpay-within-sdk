package main

// Device defines a Worldpay Within device
type Device struct {
	DeviceDescription string  `json:"deviceDescription"`
	Hostname          string  `json:"hostname"`
	PortNumber        int     `json:"portNumber"`
	ServerID          string  `json:"serverID"`
	URLPrefix         string  `json:"urlPrefix"`
	Scheme            string  `json:"scheme"`
	Latitude          float32 `json:"latitude"`
	Longitude         float32 `json:"longitude"`
	MCC               string  `json:"mcc"`
}
