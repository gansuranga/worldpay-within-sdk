# Python Wrapper - Worldpay Within

This wrapper library allows Python developers to natively interact with the Worldpay Within SDK Core via thriftpy. The thrift client implementation is abstracted from the developer and exposes a simple, familiar pythonic interface.

## Support

* Python 2.7 and 3.5

## Prerequisites:
* Correctly installed and configured environment. Refer to the [WPWithin SDK documentation](https://github.com/WPTechInnovation/worldpay-within-sdk) and [wiki](https://github.com/WPTechInnovation/worldpay-within-sdk/wiki) for more details.
* Ensure that the RPC-Agent binaries are downloaded from the release you are working with. If no directory is specified in your application, the launcher will look for the binaries in `'./wpw-bin/'` and `$WPW_HOME/bin`.
* It is is best to follow the source code of the example applications to get started with development.

## Installation

* Run `pip install module_path`, where `module_path` is the directory where [`setup.py`](wpwithin_python) is.
* If you have several versions of python installed, make sure you use the right `pip`, or alternatively `pythonX -m pip install module_path`.
* For development of the wrapper, you might want to specify the `-e` flag. Changes to the files will update the module system wide.

## Running the example apps

In `examples/` there are sample consumer and producer apps demonstrating how to use the SDK in both contexts. It also contains a sample `wpwconfig.json` file which you must include in your working directory.

### Consumer app

* `consumer_main.py` creates a [SampleConsumer()](examples/consumer.py), searches the network for available services, and purchases the first service it finds at the first price available. It waits 15 seconds, then calls beginServiceDelivery and endServiceDelivery and exits.

### Producer app

* `producer.py` initialises a producer, adds a service to it, and broadcasts indefinitely to the network. Has a signal handler to shutdown on `CTRL+C`
* `producer_callbacks.py` same as `producer.py` but only broadcasts for 20 seconds and has an [event listener](examples/callbacks_event_listener.py) for the callback service.


### Next Steps
* Add tests
* Add more information to setup.py

## The flows and API

[The flows and API can be found here](http://wptechinnovation.github.io/worldpay-within-sdk/the-flows.html)
