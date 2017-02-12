package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"
	"github.com/sirupsen/logrus"
)

// APIHandler defines API functions
type APIHandler interface {
	GetDevices(w http.ResponseWriter, r *http.Request)
	PostDevice(w http.ResponseWriter, r *http.Request)
}

// APIHandlerImpl implemenentation of APIHandler
type APIHandlerImpl struct {
	deviceManager DeviceManager
}

// NewAPIHandler returns a new instance of APIHandler
func NewAPIHandler() (APIHandler, error) {

	logrus.Debug("Begin NewAPIHandler()")

	result := &APIHandlerImpl{}
	dm, err := NewDeviceManager()

	if err != nil {

		return nil, err
	}

	result.deviceManager = dm

	logrus.Debug("End NewAPIHandler()")

	return result, nil
}

// GetDevices ..
func (dm *APIHandlerImpl) GetDevices(w http.ResponseWriter, r *http.Request) {

	reqVars := mux.Vars(r)

	mcc := reqVars["mcc"]

	iRadius, err := strconv.ParseInt(reqVars["radius"], 10, 0)
	flLat, err := strconv.ParseFloat(reqVars["lat"], 32)
	flLong, err := strconv.ParseFloat(reqVars["lng"], 32)

	if err != nil {

		w.WriteHeader(http.StatusInternalServerError)
		w.Write([]byte(fmt.Sprintf(err.Error())))

		return
	}

	devices, err := dm.deviceManager.GetDevices(mcc, float32(flLat), float32(flLong), int(iRadius))

	if err != nil {

		w.WriteHeader(http.StatusInternalServerError)
		w.Write([]byte(fmt.Sprintf(err.Error())))

		return
	}

	jsonBytes, err := json.Marshal(devices)

	if err != nil {

		w.WriteHeader(http.StatusInternalServerError)
		w.Write([]byte(fmt.Sprintf(err.Error())))

		return
	}

	w.WriteHeader(http.StatusOK)
	w.Write([]byte(jsonBytes))
}

// PostDevice ..
func (dm *APIHandlerImpl) PostDevice(w http.ResponseWriter, r *http.Request) {

	decoder := json.NewDecoder(r.Body)

	device := Device{}

	err := decoder.Decode(&device)

	var respCode = 200
	var msg string

	if err != nil {

		respCode = 400
		msg = fmt.Sprintf("%d: Unable to parse request: %s", respCode, err.Error())
	}

	err = dm.deviceManager.AddDevice(&device)

	if err != nil {

		respCode = http.StatusInternalServerError
		msg = fmt.Sprintf("%d: Unable to add device: %s", respCode, err.Error())
	}

	fmt.Printf("Did parse Device: %+v\n", device)

	w.WriteHeader(respCode)
	w.Write([]byte(msg))

	fmt.Printf("Did return msg to client: %s\n", msg)
	fmt.Printf("Did return HTTP status code (%d) to client.\n", respCode)
}
