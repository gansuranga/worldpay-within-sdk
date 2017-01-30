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
env GOOS=linux GOARCH=arm GOARM=5 go build && mv rpc-agent build/rpc-agent-linux-arm
echo "Target LINUX, 32bit"
env GOOS=linux GOARCH=386 go build && mv rpc-agent build/rpc-agent-linux-32
echo "Target LINUX, 64bit"
env GOOS=linux GOARCH=amd64 go build && mv rpc-agent build/rpc-agent-linux-64
echo "Target DARWIN, 32bit"
env GOOS=darwin GOARCH=386 go build && mv rpc-agent build/rpc-agent-mac-32
echo "Target DARWIN 64bit"
env GOOS=darwin GOARCH=386 go build && mv rpc-agent build/rpc-agent-mac-64
echo "Target DARWIN ARM 32bit"
env GOOS=darwin GOARCH=arm go build && mv rpc-agent build/rpc-agent-mac-arm
echo "Target WINDOWS, 32bit "
env GOOS=windows GOARCH=386 go build && mv rpc-agent.exe build/rpc-agent-win-32.exe
echo "Target WINDOWS, 64bit"
env GOOS=windows GOARCH=amd64 go build && mv rpc-agent.exe build/rpc-agent-win-64.exe
