package main

import (
	"flag"
	"fmt"
	"net/http"
	"os"

	"github.com/gorilla/mux"
	"github.com/rifflock/lfshook"
	"github.com/sirupsen/logrus"
)

// Application flags
var flagPort string

func init() {

	flag.StringVar(&flagPort, "port", "8081", "HTTP Port to listen on")
}

func main() {

	flag.Parse()

	parseFlags()

	initLogging()

	startAPI()
}

func parseFlags() {

	fmt.Println("Begin parseFlags()")

	fmt.Println("End parseFlags()")
}

func initLogging() {

	fmt.Println("Begin initLogging()")

	logrus.SetLevel(logrus.DebugLevel)
	fmt.Println("Did set DebugLevel")

	logrus.Debug("Begin Setting up log text formatter")
	tf := &logrus.TextFormatter{}
	tf.DisableColors = true
	tf.FullTimestamp = true
	logrus.SetFormatter(tf)
	logrus.Debug("Finish Setting up log text formatter")

	logFile := "http-directory.log"

	fmt.Println("Begin set log file hooks")
	logrus.AddHook(lfshook.NewHook(lfshook.PathMap{
		logrus.PanicLevel: logFile,
		logrus.FatalLevel: logFile,
		logrus.ErrorLevel: logFile,
		logrus.WarnLevel:  logFile,
		logrus.DebugLevel: logFile,
		logrus.InfoLevel:  logFile,
	}))
	fmt.Println("End set log file hooks")

	logrus.Info("Logging setup completed")

	fmt.Println("Finish initLogging()")
}

func startAPI() {

	logrus.Info("Begin startAPI()")

	apiHandler, err := NewAPIHandler()

	if err != nil {

		fmt.Println(err.Error())
		logrus.Error(err.Error())
		os.Exit(0)
	}

	logrus.Debug("Begin setup API routes")
	router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/device/{mcc}/{lat}/{lng}/{radius}", apiHandler.GetDevices).Methods("GET")
	router.HandleFunc("/device", apiHandler.PostDevice).Methods("POST")
	router.HandleFunc("/device", apiHandler.DeleteDevice).Methods("DELETE")

	logrus.Debug("End setup API routes")

	logrus.Debug("Begin HTTP listen and serve")
	err = http.ListenAndServe(fmt.Sprintf(":%s", flagPort), router)

	ErrorCheck(err, "Error starting HTTP server: ")

	logrus.Info("End startAPI()")
}

// ErrorCheck check if the provided error is nil. If it is not nil, print the error and exit the application
// The preMessage paramater give the opportunity to prepend the error message with a custom message, allowing the
// developer to give some context to the error.
func ErrorCheck(err error, preMessage string) {

	if err != nil {

		fmt.Printf("%s %q\n", preMessage, err.Error())

		os.Exit(1)
	}
}
