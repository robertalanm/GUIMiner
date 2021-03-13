import sys
import os
# FUNCTIONS

'''
def my_print(str):
    print('python-output(' + str + ')')


# CODE

my_print('Spawned from within electron (js)')

while True:
    line = sys.stdin.readline()

    if line == "terminate":
        my_print('I got a terminate request from electron (js)...terminating')
        exit(0)
    elif line == "":
        my_print('Terminating as there is no data given...terminated')
        exit(0)
    else:
        my_print('I got string: "' + line + '", from electron (js)')

'''
os.system("python .bittensor/bittensor/TEXT/gpt2_wiki/gpt2_wiki.py --subtensor.network kusanagi")
