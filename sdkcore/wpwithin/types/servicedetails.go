package types

// ServiceDetails Details of a service
type ServiceDetails struct {
	ServiceID          int    `json:"serviceID"`
	ServiceDescription string `json:"serviceDescription"`
	ServiceName        string `json:"serviceName"`
}
