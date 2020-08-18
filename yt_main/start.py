from yt_anaytics import main
import os
from os import getcwd

oij_channel = 'UCDsvL48jluG3tvlyurB4K3g'

if not os.path.exists(getcwd() + '\data'):
    os.makedirs(getcwd() + '\data')

if __name__ =='__main__':
    main.start(chan_id=oij_channel)







