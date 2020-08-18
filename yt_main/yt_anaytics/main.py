import csv
import json
import os
import os.path
from os import getcwd, listdir
from yt_anaytics.yt.yt_analysis.statistics import stats
from yt_anaytics.yt.yt_spider.vid_list import vid_list
from yt_anaytics.yt.yt_spider.build_yt import yt_api
from yt_anaytics.yt.yt_spider.vid_list_to_data import vid_to_data


def start(user_id=None, chan_id=None, pages= None):

    check = 0
    while check == 0:
        print('50 results/vidoes per page, max is 600 pages.')
        pages = input('How many pages would you like?')
        if (pages.isnumeric()):
            if (int(pages) >=1) & (int(pages) < 12):
                print(f'Getting {pages} pages')
                check = 1
                pages = int(pages)
            else:
                print('Incorrect input')
        else:
            print('Incorrect input')

    with open(os.path.abspath('..')+'\\key.txt', 'r') as rf:
        api_key = rf.read()

    yt_pi = yt_api(key = api_key)
    chan_info = yt_pi.channel_info(id=chan_id)
    yt_pi.js_print(chan_info)


    # create directory
    title, data_path = data_directory(chan_info)

    # create channel info json
    info_file_dir = yt_pi.js_dump(j_file = chan_info, dir=data_path,  name=title)
    print(title)

    # data folder directory
    print('loading to ' + data_path)

    # get upload tag from channel info
    video_list = vid_list(file_dir=info_file_dir)
    video_list.open_j()
    upload_id = video_list.upload_id()
    
    pagetoken = None

    for page in range(pages):

        if page == 0:
            # get video play list
            playlist = yt_pi.play_list(play_list_id=upload_id, results=50)
            pagetoken = playlist.get('nextPageToken')

        else:
            playlist = yt_pi.play_list(play_list_id=upload_id, results=50, pageToken= pagetoken)
            pagetoken = playlist.get('nextPageToken')

        full_play_list = yt_pi.js_append(j_file = playlist, dir=data_path,  name='playlist')

        list_of_vid = video_list.list_videos(playlist_json = playlist)
        data_to_csv(list_of_vid_dir= list_of_vid, data_path=data_path, title=title, yt_pi=yt_pi)

        # list of vid id and publication time
        yt_pi.csv_vid_list(j_file = list_of_vid, dir = data_path, name = 'list_of_vids')




def data_directory(json_info):

    data_dir = os.path.abspath('..')+'\\yt_main\\data'
    print(data_dir)
    title = json_info['items'][0]['snippet']['title']
    title = title.lower().replace(' ', '_')
    char = "!@#$*"

    for n in char: title = title.replace(n ,'')

    if not os.path.exists(data_dir + f'\\{title}'):
        os.makedirs(data_dir + f'\\{title}')
        data_path = data_dir + f'\\{title}'
    else: 
        data_path = data_dir + f'\\{title}'
    return title, data_path



def initiate_csv(csv_path):

    if os.path.isfile(csv_path):
        return True
    else:
        with open(csv_path, mode='a') as rf:
            data_parser = csv.writer(rf, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            data_parser.writerow(vid_to_data.header())
            
        return False


def parse_csv(csv_path, data):

    with open(csv_path , mode='a', newline='', encoding="utf-8") as csf:
        data_parser = csv.writer(csf, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_parser.writerow(data)


def data_to_csv(list_of_vid_dir, data_path, title, yt_pi):

    csv_path = data_path + f'\\{title}_data.csv'
    initated = initiate_csv(csv_path)

    data = list_of_vid_dir
    
    for n in data:
        video_id = n['videoId']
        vid_info = yt_pi.video(video_id)
        vid_data = vid_to_data()
        video_data = vid_data.get_stats(vid_info)
        parse_csv(csv_path, video_data)





