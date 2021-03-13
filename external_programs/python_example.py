import sys
import os
import argparse
# FUNCTIONS

def main(dataset = "gpt2_wiki/gpt2_wiki.py", network = "kusanagi"):
    print("running os.system command")
    try:
        os.system(f"python ~/.bittensor/bittensor/miners/TEXT/{dataset} --subtensor.network {network}|tee -a log.txt")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
