package wpwandroid

import (
	"encoding/json"
	"strconv"

	"github.com/wptechinnovation/worldpay-within-sdk/sdkcore/wpwithin"
	"github.com/wptechinnovation/worldpay-within-sdk/sdkcore/wpwithin/core"
	"github.com/wptechinnovation/worldpay-within-sdk/sdkcore/wpwithin/types"
)

// Factory to allow easy creation of
var Factory core.SDKFactory

type SimpleHandler interface {
	BeginServiceDelivery(serviceID int, serviceDeliveryToken string, unitsToSupply int)
	EndServiceDelivery(serviceID int, serviceDeliveryToken string, unitsReceived int)
	GenericEvent(name string, message string, data []byte) error
}

// SimpleWPW A simple intera
type SimpleWPW interface {
	AddService(service string) error
	RemoveService(service string) error
	InitConsumer(scheme, hostname string, portNumber int, urlPrefix, clientID string, hceCard string) error
	InitProducer(merchantClientKey, merchantServiceKey string) error
	GetDevice() (string, error)
	StartServiceBroadcast(timeoutMillis int) error
	StopServiceBroadcast()
	DeviceDiscovery(timeoutMillis int) (string, error)
	RequestServices() (string, error)
	GetServicePrices(serviceID int) (string, error)
	SelectService(serviceID, numberOfUnits, priceID int) (string, error)
	MakePayment(payRequest string) (string, error)
	BeginServiceDelivery(serviceID int, serviceDeliveryToken string, unitsToSupply int) (string, error)
	EndServiceDelivery(serviceID int, serviceDeliveryToken string, unitsReceived int) (string, error)
	SetEventHandler(handler SimpleHandler) error
}

// Initialise Initialise the SDK - Returns an implementation of WPWithin
// Must provide a device name and description
func Initialise(name, description string) (SimpleWPW, error) {

	wpw, err := wpwithin.Initialise(name, description)

	if err != nil {

		return nil, err
	}

	return &WPWWrapperImpl{wpw}, nil
}

// WPWWrapperImpl native Go wrapper to allow easy compilation to SO for consumption by other languages
type WPWWrapperImpl struct {
	wpw wpwithin.WPWithin
}

func (wp *WPWWrapperImpl) AddService(strService string) error {

	var svc types.Service

	err := json.Unmarshal([]byte(strService), &svc)

	if err != nil {

		return err
	}

	return wp.wpw.AddService(&svc)
}

func (wp *WPWWrapperImpl) RemoveService(strService string) error {

	var svc types.Service

	err := json.Unmarshal([]byte(strService), &svc)

	if err != nil {

		return err
	}

	return wp.wpw.RemoveService(&svc)
}

func (wp *WPWWrapperImpl) InitConsumer(scheme, hostname string, portNumber int, urlPrefix, clientID string, strHceCard string) error {

	var hceCard *types.HCECard

	err := json.Unmarshal([]byte(strHceCard), &hceCard)

	if err != nil {

		return err
	}

	return wp.wpw.InitConsumer(scheme, hostname, portNumber, urlPrefix, clientID, hceCard)
}

func (wp *WPWWrapperImpl) InitProducer(merchantClientKey, merchantServiceKey string) error {

	return wp.wpw.InitProducer(merchantClientKey, merchantServiceKey)
}

func (wp *WPWWrapperImpl) GetDevice() (string, error) {

	device := wp.wpw.GetDevice()

	altDevice := struct {
		Services    map[string]*types.Service `json:"services"`
		UID         string                    `json:"uid"`
		Name        string                    `json:"name"`
		Description string                    `json:"description"`
		IPv4Address string                    `json:"ipv4Address"`
	}{

		UID:         device.UID,
		Name:        device.Name,
		Description: device.Description,
		IPv4Address: device.IPv4Address,
	}

	altServices := make(map[string]*types.Service, 0)

	for _, svc := range device.Services {

		altServices[strconv.Itoa(svc.ID)] = svc
	}

	altDevice.Services = altServices

	byteDevice, err := json.Marshal(altDevice)

	if err != nil {

		return "", err
	}

	return string(byteDevice), nil
}

func (wp *WPWWrapperImpl) StartServiceBroadcast(timeoutMillis int) error {

	return wp.wpw.StartServiceBroadcast(timeoutMillis)
}

func (wp *WPWWrapperImpl) StopServiceBroadcast() {

	wp.wpw.StopServiceBroadcast()
}

func (wp *WPWWrapperImpl) DeviceDiscovery(timeoutMillis int) (string, error) {

	devices, err := wp.wpw.DeviceDiscovery(timeoutMillis)

	if err != nil {

		return "", err
	}

	bytesResult, err := json.Marshal(devices)

	return string(bytesResult), err
}

func (wp *WPWWrapperImpl) GetServicePrices(serviceID int) (string, error) {

	prices, err := wp.wpw.GetServicePrices(serviceID)

	bytesResult, err := json.Marshal(prices)

	return string(bytesResult), err
}

func (wp *WPWWrapperImpl) SelectService(serviceID, numberOfUnits, priceID int) (string, error) {

	tpr, err := wp.wpw.SelectService(serviceID, numberOfUnits, priceID)

	if err != nil {

		return "", err
	}

	bytesResult, err := json.Marshal(tpr)

	return string(bytesResult), err
}

func (wp *WPWWrapperImpl) MakePayment(strRequest string) (string, error) {

	var nativeRequest types.TotalPriceResponse

	err := json.Unmarshal([]byte(strRequest), &nativeRequest)

	if err != nil {

		return "", err
	}

	pr, err := wp.wpw.MakePayment(nativeRequest)

	if err != nil {

		return "", err
	}

	bytesResult, err := json.Marshal(pr)

	return string(bytesResult), err
}

func (wp *WPWWrapperImpl) RequestServices() (string, error) {

	services, err := wp.wpw.RequestServices()

	if err != nil {

		return "", err
	}

	bytesResult, err := json.Marshal(services)

	return string(bytesResult), err
}

func (wp *WPWWrapperImpl) BeginServiceDelivery(serviceID int, strInputSDT string, unitsToSupply int) (string, error) {

	var inputSDT types.ServiceDeliveryToken

	err := json.Unmarshal([]byte(strInputSDT), inputSDT)

	if err != nil {

		return "", err
	}

	resultSDT, err := wp.wpw.BeginServiceDelivery(serviceID, inputSDT, unitsToSupply)

	if err != nil {

		return "", err
	}

	resultSDTBytes, err := json.Marshal(resultSDT)

	return string(resultSDTBytes), err
}

func (wp *WPWWrapperImpl) EndServiceDelivery(serviceID int, strInputSDT string, unitsReceived int) (string, error) {

	var inputSDT types.ServiceDeliveryToken

	err := json.Unmarshal([]byte(strInputSDT), &inputSDT)

	if err != nil {

		return "", err
	}

	resultSDT, err := wp.wpw.EndServiceDelivery(serviceID, inputSDT, unitsReceived)

	if err != nil {

		return "", err
	}

	resultSDTBytes, err := json.Marshal(resultSDT)

	return string(resultSDTBytes), err
}

func (wp *WPWWrapperImpl) SetEventHandler(handler SimpleHandler) error {

	nh := NativeHandler{}
	nh.simpleHandler = handler

	return wp.wpw.SetEventHandler(nh)
}

type NativeHandler struct {
	simpleHandler SimpleHandler
}

func (n NativeHandler) BeginServiceDelivery(serviceID int, serviceDeliveryToken types.ServiceDeliveryToken, unitsToSupply int) {

	n.BeginServiceDelivery(serviceID, serviceDeliveryToken, unitsToSupply)
}

func (n NativeHandler) EndServiceDelivery(serviceID int, serviceDeliveryToken types.ServiceDeliveryToken, unitsReceived int) {

	n.BeginServiceDelivery(serviceID, serviceDeliveryToken, unitsReceived)
}

func (n NativeHandler) GenericEvent(name string, message string, data interface{}) error {

	return n.GenericEvent(name, message, data)
}
