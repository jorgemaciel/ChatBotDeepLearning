import numpy as np
import tensorflow as tf
import re
import time
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, 'data/')

##### PART 1 - DATA PREPROCESSING #####

lines = open(DATA_DIR + 'movie_lines.txt', encoding='utf-8', errors='ignore').read().split('\n')
conversations = open(DATA_DIR + 'movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')




