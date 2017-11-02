# Use sub-repos for Worldpay Within SDK
**This repository is deprecated as the main source of the code and executables, we've decomposed this into smaller repos. So please use the following directories below.**

**This repo will still be used for the list of issues and the 'hub' repo and where the documentation will sit**
**You should use one of these instead:**
* GO: https://github.com/WPTechInnovation/wpw-sdk-go
* Nodejs: https://github.com/WPTechInnovation/wpw-sdk-nodejs
* Java: https://github.com/WPTechInnovation/wpw-sdk-java
* Python: https://github.com/WPTechInnovation/wpw-sdk-python
* .Net: https://github.com/WPTechInnovation/wpw-sdk-dotnet


Worldpay Within SDK to allow payments within IoT.

The core of this SDK is written in Go with a native Go interface. Along with the native Go interface is an RPC layer (Apache Thrift) to allow communication through other languages.

Currently, therefore the SDK is available in the following languages as "wrappers", we're in the process of refactoring the repository and we'll give links to the decomposed repos here:
* Node.js The new WPW Node.js SDK can be found here: https://github.com/WPTechInnovation/wpw-sdk-nodejs
* .NET The new WPW .Net SDK can be found here: https://github.com/WPTechInnovation/wpw-sdk-dotnet
* Java - The new WPW Java SDK repo can be found here: https://github.com/WPTechInnovation/wpw-sdk-java
* Python - The new WPW Python SDK repo can be found here: https://github.com/WPTechInnovation/wpw-sdk-python
* Go - The new WPW Go SDK repo can be found here: https://github.com/WPTechInnovation/wpw-sdk-go

**Note 1**: Please note that if you intend to work with one of the wrapper frameworks, it is not required that you build the Go source code directly. With each release we will bundle pre-built binaries of the RPC-Agent application. The RPC-Agent is an application that starts the Thrift RPC interface into the Go SDK Core. Once this application is up and running the wrapper can communicate with the SDK Core. In the latest release of the SDK, the RPC-Agent is started automatically by the wrapper.

**Note 2**: To enable payments for your instance of the SDK and applications, you will need to create an account at [Worldpay Online Payments](http://online.worldpay.com). Once the account is created, please navigate to *settings* -> *API Keys* and keep note of the *service key* and *client key* for later. You will need to add these keys into your sample apps when "initialising a producer".

## The documentation site

* [Please see our documentation pages for more details on what Worldpay Within is](http://wptechInnovation.github.io/worldpay-within-sdk)
* [Also for a detailed architecture guide for Worldpay Within please see our full documentation](http://wptechinnovation.github.io/worldpay-within-sdk/architecture.html)

