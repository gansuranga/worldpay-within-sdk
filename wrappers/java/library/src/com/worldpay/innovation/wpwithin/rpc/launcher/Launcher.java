package com.worldpay.innovation.wpwithin.rpc.launcher;

import com.worldpay.innovation.wpwithin.WPWithinGeneralException;

import java.io.*;
import java.util.Map;

public class Launcher {

    private Process processHandle;

    private StringBuilder errorOutput;
    private StringBuilder stdOutput;

    private static final String NEW_LINE = System.getProperty("line.separator", "\n");

    public void startProcess(Map<OS, PlatformConfig> launchConfig, final Listener listener) throws WPWithinGeneralException {

        OS hostOS = detectHostOS();
        Architecture hostArch = detectHostArchitecture();


        if (validateConfig(launchConfig, hostOS, hostArch)) {

            String command = launchConfig.get(hostOS).getCommand(hostArch);

            try {

                processHandle = Runtime.getRuntime().exec(command);

                doReadErrOutput();
                doReadStdOutput();

                new Thread(new Runnable() {
                    @Override
                    public void run() {

                        try {

                            int exitCode = processHandle.waitFor();

                            if(listener != null) {

                                listener.onApplicationExit(exitCode, stdOutput.toString(), errorOutput.toString());
                            }

                        } catch (Exception e) {

                            e.printStackTrace();
                        }
                    }
                }).start();

                // Here we will pause for 0.5 seconds to allow the agent to start up and set up the server listener
                // The reason is that I think there is a race condition where the process has been started and this function returns
                // but the RPC Agent hasn't yet set up the socket listener to accept connections, but in the mean time this Java
                // application is proceeding forward in it's flow and attempts to connect to the RPC Agent server, which sometimes has not
                // yet been setup, in which case results in a refused connection exception.

                // You may ask why this sleep block is here an not somewhere else?
                // It's because this particular function block is responsible for starting the RPC Agent, which appears to
                // require 500ms to "warm up". This function is also responsible for ensuring a state where the application can
                // connect to the RPC Agent once this "start" function returns.
                try {
                    Thread.sleep(500);
                } catch (InterruptedException ie) {

                    ie.printStackTrace();
                }

            } catch (IOException ioe) {

                ioe.printStackTrace();

                throw new WPWithinGeneralException("Unable to launch process: " + ioe.getMessage());
            }

        } else {

            throw new WPWithinGeneralException("Invalid launch configuration detected, cannot launch application.");
        }
    }

    public void stopProcess() {

        if (processHandle != null) {

            processHandle.destroy();
        }
    }

    private OS detectHostOS() {

        String hostOS = System.getProperty("os.name");

        if (hostOS == null || hostOS.length() == 0) {

            return OS.UNKNOWN;
        } else if (hostOS.toLowerCase().contains("win")) {

            return OS.WINDOWS;

        } else if (hostOS.toLowerCase().contains("darwin") || hostOS.toLowerCase().contains("mac")) {

            return OS.MAC;
        } else if (hostOS.toLowerCase().contains("linux")) {

            return OS.LINUX;
        } else {

            return OS.UNKNOWN;
        }
    }

    private Architecture detectHostArchitecture() {

        String arch = System.getProperty("os.arch");

        if (arch == null || arch.length() == 0) {

            return Architecture.UNKNOWN;
        } else if (arch.toLowerCase().contains("64")) {

            return Architecture.X86_64;
        } else if (arch.toLowerCase().contains("arm")) {

            return Architecture.ARM32;
        } else if (arch.toLowerCase().equals("x86")) {

            return Architecture.IA32;
        } else {

            return Architecture.UNKNOWN;
        }
    }

    private boolean validateConfig(Map<OS, PlatformConfig> launchConfig, OS hostOS, Architecture hostArchitecture) {

        return launchConfig.containsKey(hostOS) && (launchConfig.get(hostOS).getCommand(hostArchitecture) != null && launchConfig.get(hostOS).getCommand(hostArchitecture).length() > 0);
    }

    public String getErrorOutput() {
        return errorOutput.toString();
    }

    public String getStdOutput() {
        return stdOutput.toString();
    }

    private void doReadStdOutput() {

        new Thread(new Runnable() {

            @Override
            public void run() {

                try {

                    stdOutput = new StringBuilder();

                    BufferedReader br = new BufferedReader(new InputStreamReader(processHandle.getInputStream()));

                    String line;
                    while ((line = br.readLine()) != null) {

                        stdOutput.append(line + NEW_LINE);
                    }
                } catch (IOException e) {

                    if(!e.getMessage().toLowerCase().contains("stream closed")) {

                        e.printStackTrace();
                    }
                }

            }
        }).start();
    }

    private void doReadErrOutput() {

        new Thread(new Runnable() {

            @Override
            public void run() {

                try {

                    errorOutput = new StringBuilder();

                    BufferedReader br = new BufferedReader(new InputStreamReader(processHandle.getErrorStream()));

                    String line;
                    while ((line = br.readLine()) != null) {

                        errorOutput.append(line + NEW_LINE);
                    }
                } catch (IOException e) {

                    if(!e.getMessage().toLowerCase().contains("stream closed")) {

                        e.printStackTrace();
                    }
                }

            }
        }).start();
    }
}
