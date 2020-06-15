import csv
from googleapiclient.discovery import build
import json
import pandas as pd
import os
import requests


class yt_api:


    def __init__(self, key):
        self.dev_key = key

    def yt(self):
        return build(serviceName='youtube', version='v3',developerKey=self.dev_key)

    def channel_info(self, account_name=None, id=None):
        request = self.yt().channels().list(part = 'snippet, statistics, contentDetails', id = id, forUsername=account_name)
        return request.execute()

    def play_list(self, play_list_id, results= 5, pageToken = None):
        request = self.yt().playlistItems().list(part = 'contentDetails' ,  playlistId=play_list_id, maxResults= results, pageToken = pageToken)
        response = request.execute()
        return response

    def video(self, http):
        request = self.yt().videos().list(part = [
            'topicDetails'], id = http)

        request = self.yt().videos().list(part = ['snippet, statistics, liveStreamingDetails\
            , recordingDetails, status,topicDetails'], id = http)
        response = request.execute()
        return response


    @staticmethod
    def js(j):
        return json.dump(j)

    @staticmethod
    def js_print(j):
        return json.dumps(j, indent=5, sort_keys=True)

    @staticmethod
    def js_dump(j_file, name, dir):
        with open( str(dir) + f'\\{str(name)}.json', 'w', newline='') as wf:
            json.dump(j_file, wf, indent= 5)
        return str(dir) + f'\\{str(name)}.json'

    @staticmethod
    def js_append(j_file, name, dir):
        with open(str(dir) + f'\\{str(name)}.json', 'a+') as af:
            af.write(json.dumps(j_file, indent=5))
            af.write("\n")

    @staticmethod
    def csv_vid_list(j_file, name, dir):
        with open(str(dir) + f'\\{str(name)}.csv', 'a+') as af:
            for n in j_file:
                data_parser = csv.writer(af, delimiter=',')
                data_parser.writerow(list(n.values()))














