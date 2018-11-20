import pandas as pd
import numpy as np
import random

library = pd.read_csv("c:\users\jen\downloads\Tracklist.csv")

key_list = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
key_list_full = key_list + key_list
key_dict = dict(zip(key_list, range(0,12)))

class Scale:
    def __init__(self, start_key):
        self.start_tonic = start_key.partition(' ')[0]
        self.scale = start_key.partition(' ')[2]
    def scale_keys(self):
        x = key_dict.get(self.start_tonic)
        if self.scale == 'maj':
            return [key_list_full[x]+' maj',key_list_full[x+2]+' maj',key_list_full[x+4]+' min',key_list_full[x+5]+' maj',
            key_list_full[x+7]+' maj',key_list_full[x+9]+' min',key_list_full[x+11]+' min',key_list_full[x]+' min']
        else:
            return [key_list_full[x]+' min',key_list_full[x+2]+' min',key_list_full[x+3]+' maj',key_list_full[x+5]+' min',
            key_list_full[x+7]+' min',key_list_full[x+8]+' maj',key_list_full[x+10]+' maj',key_list_full[x]+' maj']

def setlist(catalog,length):
    '''
    catalog = Pandas dataframe
    length = Integer, number of tracks
    '''
    initkey = np.random.choice(key_list)+np.random.choice([' maj',' min'])
    probabilities = [0.1633, 0.0408, 0.1633, 0.1633, 0.1633, 0.1633, 0.0408, 0.0816, .0203]
    counter = 2
    df = catalog[catalog['Key'] == initkey].sample(1)
    key_option = Scale(initkey).scale_keys()
    key_option.append(np.random.choice(key_list)+np.random.choice([' maj',' min']))
    new_key = np.random.choice(key_option, p=probabilities)
    while counter < length:
        df = df.append(catalog[catalog['Key'] == new_key].sample(1))
        key_option = Scale(new_key).scale_keys()
        key_option.append(np.random.choice(key_list)+np.random.choice([' maj',' min']))
        new_key = np.random.choice(key_option, p=probabilities)
        counter +=1
    return df

def guided_setlist(catalog,length,initkey):
    '''
    catalog = Pandas dataframe
    length = Integer, number of tracks
    initkey = Music key in min or maj
    '''
    probabilities = [0.1633, 0.0408, 0.1633, 0.1633, 0.1633, 0.1633, 0.0408, 0.0816, .0203]
    counter = 2
    df = catalog[catalog['Key'] == initkey].sample(1)
    key_option = Scale(initkey).scale_keys()
    key_option.append(np.random.choice(key_list)+np.random.choice([' maj',' min']))
    new_key = np.random.choice(key_option, p=probabilities)
    while counter < length:
        df = df.append(catalog[catalog['Key'] == new_key].sample(1))
        key_option = Scale(new_key).scale_keys()
        key_option.append(np.random.choice(key_list)+np.random.choice([' maj',' min']))
        new_key = np.random.choice(key_option, p=probabilities)
        counter +=1
    return df
