import sys
import os
import argparse
# FUNCTIONS
parser = argparse.ArgumentParser()
parser.add_argument('-d','--dataset',metavar="dataset",type=str,help="Dataset options, gpt2_wiki, gpt2_genesis, etc",default="gpt2_wiki/gpt2_wiki.py")
parser.add_argument('-n','--network',metavar="network",type=str,help="Subtensor network between Kusanagi and Akira, Kusanagi recommended",default="kusanagi")
parser.add_argument('-c','--command',metavar="command",type=bool,help="Start or stop options for Mining",default=True)

args=parser.parse_args()
print(args)
while args.command:
    try:
        os.system(f"python ~/.bittensor/bittensor/miners/TEXT/{args.dataset} --subtensor.network {args.network}|tee -a log.txt")
    except Exception as e:
        print(e)
else:
    exit(0)