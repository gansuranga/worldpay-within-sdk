package main

import (
	"errors"
	"strings"

	geo "github.com/kellydunn/golang-geo"
)

// DeviceManager ..
type DeviceManager interface {
	AddDevice(*Device) error
	GetDevices(mcc string, flLat, flLng float32, radius int) ([]Device, error)
}

// DeviceManagerImpl ..
type DeviceManagerImpl struct {
	devices []Device
}

// NewDeviceManager ..
func NewDeviceManager() (DeviceManager, error) {

	result := &DeviceManagerImpl{}
	result.devices = make([]Device, 0)

	return result, nil
}

// AddDevice ..
func (dm *DeviceManagerImpl) AddDevice(device *Device) error {

	if device == nil {

		return errors.New("device is nil")
	}

	dm.devices = append(dm.devices, *device)

	return nil
}

// DeleteDevice
func (dm *DeviceManagerImpl) DeleteDevice(device *Device) error {
	if device == nil {
		return errors.New("Device is nil")
	}

	// TODO: Lock?
	// TODO: remove device

	return nil
}

// GetDevices ..
func (dm *DeviceManagerImpl) GetDevices(mcc string, flLat, flLng float32, radius int) ([]Device, error) {

	result := make([]Device, 0)

	for _, device := range dm.devices {

		inRange, err := dm.inRange(&device, flLat, flLng, radius)

		if err != nil {

			return nil, err
		}

		if strings.EqualFold(mcc, device.MCC) && inRange {

			result = append(result, device)
		}
	}

	return result, nil
}

func (dm *DeviceManagerImpl) inRange(device *Device, flLat, flLong float32, radius int) (bool, error) {

	checkPT := geo.NewPoint(float64(flLat), float64(flLong))
	devPT := geo.NewPoint(float64(device.Latitude), float64(device.Longitude))

	cd := devPT.GreatCircleDistance(checkPT)

	return cd <= float64(radius), nil
}
