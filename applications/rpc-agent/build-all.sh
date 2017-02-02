#!/bin/bash

echo Cleanup build directory
rm -rf build
mkdir -p build

echo
echo
echo Build rpc-agent for all supported platforms..
echo
echo
echo "Target LINUX, ARM, GOARM=5"
env GOOS=linux GOARCH=arm GOARM=5 go build -ldflags "-X main.applicationVersion=0.123 -X main.applicationBuildDate=`date -u +%d-%m-%Y@%H:%M:%S` -X main.applicationPlatform=LINUX_ARM" -o build/rpc-agent-linux-arm main.go
echo "Target LINUX, 32bit"
env GOOS=linux GOARCH=386 go build -ldflags "-X main.applicationVersion=0.123 -X main.applicationBuildDate=`date -u +%d-%m-%Y@%H:%M:%S` -X main.applicationPlatform=LINUX_386" -o build/rpc-agent-linux-32 main.go
echo "Target LINUX, 64bit"
env GOOS=linux GOARCH=amd64 go build -ldflags "-X main.applicationVersion=0.123 -X main.applicationBuildDate=`date -u +%d-%m-%Y@%H:%M:%S` -X main.applicationPlatform=LINUX_AMD64" -o build/rpc-agent-linux-64 main.go
echo "Target DARWIN, 32bit"
env GOOS=darwin GOARCH=386 go build && go build -ldflags "-X main.applicationVersion=0.123 -X main.applicationBuildDate=`date -u +%d-%m-%Y@%H:%M:%S` -X main.applicationPlatform=DARWIN_386" -o build/rpc-agent-mac-32 main.go
echo "Target DARWIN 64bit"
env GOOS=darwin GOARCH=amd64 go build -ldflags "-X main.applicationVersion=0.123 -X main.applicationBuildDate=`date -u +%d-%m-%Y@%H:%M:%S` -X main.applicationPlatform=DARWIN_AMD64" -o build/rpc-agent-mac-64 main.go
echo "Target DARWIN ARM 32bit"
env GOOS=darwin GOARCH=arm go build -ldflags "-X main.applicationVersion=0.123 -X main.applicationBuildDate=`date -u +%d-%m-%Y@%H:%M:%S` -X main.applicationPlatform=DARWIN_ARM_32" -o build/rpc-agent-mac-arm-32 main.go
echo "Target WINDOWS, 32bit "
env GOOS=windows GOARCH=386 go build -ldflags "-X main.applicationVersion=0.123 -X main.applicationBuildDate=`date -u +%d-%m-%Y@%H:%M:%S` -X main.applicationPlatform=WIN_386" -o build/rpc-agent-win-32.exe main.go
echo "Target WINDOWS, 64bit"
env GOOS=windows GOARCH=amd64 go build -ldflags "-X main.applicationVersion=0.123 -X main.applicationBuildDate=`date -u +%d-%m-%Y@%H:%M:%S` -X main.applicationPlatform=WIN_AMD64" -o build/rpc-agent-win-64.exe main.go
