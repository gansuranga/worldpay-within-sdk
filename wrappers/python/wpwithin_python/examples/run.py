import time
from wpwithin_python import run_rpc_agent


def main():
    proc=run_rpc_agent("9092", "./rpc-agent/")
    print("FIRST TASK")
    time.sleep(20)
    print("SECOND TASK")
    proc.kill()
    print("KILLED")
    time.sleep(20)


if __name__ == "__main__":
    main()
