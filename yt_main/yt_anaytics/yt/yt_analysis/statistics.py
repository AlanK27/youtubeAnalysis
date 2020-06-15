import json
import pandas as pd
import os

class stats:


    def __init__(self, j_file = None, path = None):
        self.j_file = j_file
        self.view_count = []
        self.comment_count = []
        self.subscribers = []
        self.vid_count = []
        self.path = path

    def load(self):
        with open(self.path, 'r') as rf:
            self.j_file = json.load(rf)

    def statistics(self):
        self.view_count = self.j_file['items'][0]['statistics']['viewCount']
        self.comment_count = self.j_file['items'][0]['statistics']['commentCount']
        self.subscribers = self.j_file['items'][0]['statistics']['subscriberCount']
        self.vid_count = self.j_file['items'][0]['statistics']['videoCount']

    def print_stats(self):
        lis = { 'View Count': self.vid_count,
                'Comment Count': self.comment_count,
                'Subscribers': self.subscribers,
                'Video Count': self.vid_count,
        }
        print(pd.Series(lis))


print(os.getcwd())

# file_path = os.getcwd() + '\\yt_main\\data\\only_in_japan__go\\only_in_japan__go.json'

# x = stats(path = file_path)
# x.load()
# x.statistics()
# x.print_stats()


    # from datetime import datetime
    # d1 = datetime.strptime('2020-06-05T04:01:49Z',"%Y-%m-%dT%H:%M:%SZ")







