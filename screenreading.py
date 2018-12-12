import numpy as np
import cv2
import time
import os
from grabscreen import grab_screen
from getkeys import key_check
from alexnet import alexnet
from navigation import forward, left, right



WIDTH = 80
HEIGHT = 60
LR = 1e-3
EPOCH = 8
MODEL_NAME = 'hex-webgl-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2', EPOCH)
file_name = 'training_data_v2.npy'


model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

if os.path.isfile(file_name):
    print('File exists loading previous data')
    training_data = list(np.load(file_name))
else:
    print('File does not exist starting fresh')
    training_data = []




def keys_to_output(keys):
    # [A,D,up]
    output = [0,0,0]

    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[1] = 1
    else:
        output[2] = 1;

    return output

def main():

  for i in reversed(list(range(4))):
    print(i+1)
    time.sleep(1)


  last_time = time.time()
  while(True):    
    screen = (grab_screen(region=(3,120,913,697)))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    screen = cv2.resize(screen, (80,60))
    keys = key_check()
    output = keys_to_output(keys)
    training_data.append([screen,output])
    print('Loop took {} seconds'.format(time.time() - last_time))
    last_time = time.time()

    prediction = model.predict([screen.reshape(WIDTH, HEIGHT,1)])[0]
    moves = list(np.around(prediction))
    

    if moves == [1,0,0]:
        print('Predicted Left')
        left()
    elif moves == [0,1,0]:
        print('Predicted Right')
        right()
    elif moves == [0,0,1]:
        print('Predicted Forward')
        forward()


    

main()
