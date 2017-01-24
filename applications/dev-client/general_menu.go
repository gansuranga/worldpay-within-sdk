package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"io/ioutil"

	log "github.com/Sirupsen/logrus"
	devclienttypes "github.com/wptechinnovation/worldpay-within-sdk/applications/dev-client/types"
	"github.com/wptechinnovation/worldpay-within-sdk/sdkcore/wpwithin"
	"github.com/wptechinnovation/worldpay-within-sdk/sdkcore/wpwithin/psp"
	"github.com/wptechinnovation/worldpay-within-sdk/sdkcore/wpwithin/psp/securenet"
	"github.com/wptechinnovation/worldpay-within-sdk/sdkcore/wpwithin/rpc"
	"github.com/wptechinnovation/worldpay-within-sdk/sdkcore/wpwithin/types"
)

func mGetDeviceInfo() error {

	fmt.Println("Device Info:")

	if sdk == nil {
		return errors.New(devclienttypes.ErrorDeviceNotInitialised)
	}

	fmt.Printf("Uid of device: %s\n", sdk.GetDevice().UID)
	fmt.Printf("Name of device: %s\n", sdk.GetDevice().Name)
	fmt.Printf("Description: %s\n", sdk.GetDevice().Description)
	fmt.Printf("Services: \n")

	for i, service := range sdk.GetDevice().Services {
		fmt.Printf("   %d: Id:%d Name:%s Description:%s\n", i, service.ID, service.Name, service.Description)
		fmt.Printf("   Prices: \n")
		for j, price := range service.Prices {
			fmt.Printf("      %d: ServiceID: %d ID:%d Description:%s PricePerUnit.Amount:%d PricePerUnit.CurrencyCode:%s UnitID:%d UnitDescription:%s\n", j, service.ID, price.ID, price.Description, price.PricePerUnit.Amount, price.PricePerUnit.CurrencyCode, price.UnitID, price.UnitDescription)
		}
	}

	fmt.Printf("IPv4Address: %s\n", sdk.GetDevice().IPv4Address)

	return nil
}

func mInitNewDevice() error {

	fmt.Println("Initialising new device")

	fmt.Print("Name of device: ")
	var nameOfDevice string
	if err := getUserInput(&nameOfDevice); err != nil {
		return err
	}

	fmt.Print("Description: ")
	var description string
	if err := getUserInput(&description); err != nil {
		return err
	}

	_sdk, err := wpwithin.Initialise(nameOfDevice, description)

	if err != nil {

		return err
	}

	sdk = _sdk

	return err
}

func mResetSessionState() error {

	sdk = nil

	fmt.Println("Reset session state")

	return nil
}

func mStartRPCService() error {

	fmt.Println("Starting rpc service...")

	config := rpc.Configuration{
		Protocol:   "binary",
		Framed:     false,
		Buffered:   false,
		Host:       "127.0.0.1",
		Port:       9091,
		Secure:     false,
		BufferSize: 8192,
	}

	rpc, err := rpc.NewService(config, sdk)

	if err != nil {
		return err
	}

	chErr := make(chan error, 1)

	go func() {
		chErr <- rpc.Start()
	}()

	var rpcErr error

	// Error handling go routine
	go func() {
		rpcErr := <-chErr
		if rpcErr != nil {
			log.Debug("error ", rpcErr)
		}

		close(chErr)
	}()

	return rpcErr
}

func mLoadDeviceProfile() error {

	fmt.Print("Name of profile to load: ")
	var profileStr string
	if err := getUserInput(&profileStr); err != nil {
		return err
	}

	file, err := ioutil.ReadFile(profileStr)
	if err != nil {
		log.Debug("error ", err)
		return err
	}

	err = json.Unmarshal(file, &deviceProfile)
	if err != nil {

		fmt.Printf("Error parsing deviceProfile: %s", err.Error())
	}

	if deviceProfile.DeviceEntity != nil {

		if err := initialiseDevice(deviceProfile.DeviceEntity); err != nil {
			return err
		}
		fmt.Println("Setup device.")
	}

	if deviceProfile.DeviceEntity.Producer != nil {

		if err := setupProducer(deviceProfile.DeviceEntity.Producer); err != nil {
			return err
		}
		fmt.Println("Setup producer.")
	}

	return nil
}

func setupProducer(producer *devclienttypes.Producer) error {

	// Could come from a config file..
	var pspConfig = make(map[string]string, 0)
	pspConfig[psp.CfgPSPName] = securenet.PSPName
	pspConfig[securenet.CfgAPIEndpoint] = "https://gwapi.demo.securenet.com/api"
	pspConfig[securenet.CfgAppVersion] = "0.1"
	pspConfig[securenet.CfgDeveloperID] = "123"
	pspConfig[securenet.CfgPublicKey] = "8c0ce953-455d-4c12-8d14-ff20d565e485"
	pspConfig[securenet.CfgSecureKey] = "KZ9kWv2EPy7M"
	pspConfig[securenet.CfgSecureNetID] = "8008609"
	pspConfig[psp.CfgHTEPrivateKey] = "KZ9kWv2EPy7M"
	pspConfig[psp.CfgHTEPublicKey] = "8c0ce953-455d-4c12-8d14-ff20d565e485"
	pspConfig[securenet.CfgHTTPProxy] = "https://127.0.0.1:7001"

	if err := sdk.InitProducer(pspConfig); err != nil {
		return err
	}

	if err := addServicesAndPrices(producer.Services); err != nil {
		return err
	}

	return nil
}

func initialiseDevice(deviceEntity *devclienttypes.DeviceEntity) error {
	_sdk, err := wpwithin.Initialise(deviceEntity.Name, deviceEntity.Description)

	if err != nil {
		return err
	}

	sdk = _sdk

	return nil
}

func addServicesAndPrices(services []*devclienttypes.ServiceProfile) error {

	for _, service := range services {

		newService, _ := types.NewService()
		newService.ID = service.Id
		newService.Name = service.Name
		newService.Description = service.Description

		for _, price := range service.Prices {

			newPrice := types.Price{
				UnitID:          price.UnitID,
				ID:              price.ID,
				Description:     price.Description,
				UnitDescription: price.UnitDescription,
				PricePerUnit: &types.PricePerUnit{
					Amount:       price.PricePerUnit.Amount,
					CurrencyCode: price.PricePerUnit.CurrencyCode,
				},
			}

			newService.AddPrice(newPrice)
		}

		if err := sdk.AddService(newService); err != nil {
			return err
		}
	}

	return nil
}
