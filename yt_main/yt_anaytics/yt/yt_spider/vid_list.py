import ijson
import json


class vid_list:


    def __init__(self, file_dir): 
        self.j_file = None
        self.file_dir = file_dir
        self.data = None

    def open_j(self):
        with open(self.file_dir, 'r') as rf:
            self.data = json.load(rf)

    def upload_id(self):
        return self.data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    def nextpage(self):
        return self.data.get('nextPageToken')

        
    @staticmethod
    def list_videos(playlist_json):
        lis = []
        for n in playlist_json['items']:
            lis.append(n['contentDetails'])
        print(f'{len(lis)} number of videos')
        return lis

    # def dump_j(self, name):







# filee = 'C:\\Users\\kai_t\\Desktop\\projects\\youtube_analysis\\yt_main\\data\\oij_vid_list.json'

# with open(filee , 'r') as rf:
#     obj = ijson.items(rf, 'items.item')
#     col = list(obj)

# s_row = []
# for n in col:
#     s_row.append(n['contentDetails'])

# print(s_row)






