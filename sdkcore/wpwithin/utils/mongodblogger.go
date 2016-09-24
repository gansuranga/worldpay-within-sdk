package utils

import (
	"fmt"
	"os"
	"time"

	"github.com/wptechinnovation/worldpay-within-sdk/sdkcore/wpwithin/types"
	"github.com/wptechinnovation/worldpay-within-sdk/sdkcore/wpwithin/types/event"

	"gopkg.in/mgo.v2"
)

//
// Joe.Drumgoole@mongodb.com
//
// A Simple logging package for WPWWithin Framework
//

// must point at a running writeable MongoDB Server
const WPW_MONGODB_SERVER string = "WPW_MONGODB_SERVER"

// Set to anything to turn logging on
const WPW_MONGODB_LOGGING string = "WPW_MONGODB_LOGGING"

const WPW_EVENT_DATABASE string = "WPWEvents"

const WPW_EVENT_COLLECTION string = "WPWLog"

type MongoDBLogger struct {
	MgoSession *mgo.Session
	DB         *mgo.Database
	Collection *mgo.Collection
	loggingOn  bool
	connected  bool
}

type StringEvent struct {
	Name      string
	Msg       string
	Timestamp time.Time
}

type IntEvent struct {
	Name      string
	Msg       string
	Amount    int64
	Timestamp time.Time
}

type FloatEvent struct {
	Name      string
	Msg       string
	Amount    float64
	Timestamp time.Time
}

type PaymentEvent struct {
	Name      string
	Msg       string
	Payment   interface{}
	Timestamp time.Time
}

type DocEvent struct {
	Name      string
	Msg       string
	Doc       interface{}
	Timestamp time.Time
}

func NewMongoDBLogger() (event.Handler, error) {

	m := &MongoDBLogger{}

	m.loggingOn = true

	serverUrl := os.Getenv(WPW_MONGODB_SERVER)
	if serverUrl == "" {

		// Hardcoded for Worldpay Within Hackathon (23-Sep-2016 to 25-Sep-2016)
		// This is hardcoded as we want to generate a sold collection of usage data for later analysis
		// The event data is sent to a MongoDB server running at the event which will also be accessed by a Go Web server
		// that a Geckoboard dashboard will query.
		// It is intended that this hardcoding will be removed after the event
		serverUrl = "mgo.tinhat.solutions"

	} else {

		session, err := mgo.Dial(serverUrl)

		if err != nil {

			m.connected = false

			// will also return m so it can be accessed and events sent, regardless of whether we got to connect ot not
			// I don't know how I fell about this approach.
			return m, err
		}

		m.connected = true

		m.MgoSession = session
		m.DB = m.MgoSession.DB(WPW_EVENT_DATABASE)
		m.Collection = m.DB.C(WPW_EVENT_COLLECTION)
	}

	loggingOn := os.Getenv(WPW_MONGODB_LOGGING)

	if (loggingOn == "ON") && (serverUrl != "") {
		m.TurnLoggingOn()
	} else {
		m.TurnLoggingOff()
	}

	return m, nil
}

func (m *MongoDBLogger) TurnLoggingOn() bool {
	m.loggingOn = true
	return m.loggingOn

}

func (m *MongoDBLogger) TurnLoggingOff() bool {
	m.loggingOn = false
	return m.loggingOn

}

func (m *MongoDBLogger) LogEventStr(name string, message string) error {

	if m.loggingOn && m.connected {

		err := m.Collection.Insert(&StringEvent{Name: name,
			Msg:       message,
			Timestamp: time.Now()})
		return err
	}
	return nil
}

func (m *MongoDBLogger) LogEventInt(name string, message string, amount int64) error {

	if m.loggingOn && m.connected {

		err := m.Collection.Insert(&IntEvent{Name: name,
			Msg:       message,
			Amount:    amount,
			Timestamp: time.Now()})
		return err
	}
	return nil
}

func (m *MongoDBLogger) LogEventFloat(name string, message string, amount float64) error {

	if m.loggingOn && m.connected {

		err := m.Collection.Insert(&FloatEvent{Name: name,
			Msg:       message,
			Amount:    amount,
			Timestamp: time.Now()})

		return err
	}
	return nil
}

func (m *MongoDBLogger) LogEventDoc(name string, message string, doc interface{}) error {

	if m.loggingOn && m.connected {

		err := m.Collection.Insert(&DocEvent{Name: name,
			Msg:       message,
			Doc:       doc,
			Timestamp: time.Now()})

		return err
	}
	return nil
}

func (m *MongoDBLogger) LogEventPayment(name string, message string, payment interface{}) error {

	if m.loggingOn && m.connected {

		err := m.Collection.Insert(&PaymentEvent{Name: name,
			Msg:       message,
			Payment:   payment,
			Timestamp: time.Now()})

		return err
	}
	return nil
}

// BeginServiceDelivery stubbed - do not use.
func (m *MongoDBLogger) BeginServiceDelivery(serviceID int, serviceDeliveryToken types.ServiceDeliveryToken, unitsToSupply int) {

	fmt.Println("MongoDBLogger.BeginServiceDelivery() - stubbed and not implemented")
}

// EndServiceDelivery stubbed - do not use.
func (m *MongoDBLogger) EndServiceDelivery(serviceID int, serviceDeliveryToken types.ServiceDeliveryToken, unitsReceived int) {

	fmt.Println("MongoDBLogger.EndServiceDelivery() - stubbed and not implemented")
}

// GenericEvent log a generic event
func (m *MongoDBLogger) GenericEvent(name string, message string, data interface{}) error {

	if m.loggingOn && m.connected {

		return m.LogEventDoc(name, message, data)
	}

	return nil
}
