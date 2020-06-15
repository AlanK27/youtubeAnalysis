import json
import os


class vid_to_data:


    def __init__(self):
        pass

    def get_stats(self, data):

        p_list = []
        
        try:
            p_list.append(data['items'][0]['snippet']['categoryId'])
        except:
            p_list.append(None)

        try:
            p_list.append(data['items'][0]['statistics']['viewCount'])
        except:
            p_list.append(None)

        try:
            p_list.append(data['items'][0]['statistics']['likeCount'])
        except:
            p_list.append(None)
        
        try:
            p_list.append(data['items'][0]['statistics']['dislikeCount'])
        except:
            p_list.append(None)
        
        try:
            p_list.append(data['items'][0]['statistics']['favoriteCount'])
        except:
            p_list.append(None)
        
        try:
            p_list.append(data['items'][0]['statistics']['commentCount'])
        except:
            p_list.append(None)

        try:
            p_list.append(data['items'][0]['liveStreamingDetails']['actualStartTime'])
        except:
            p_list.append(None)

        try:
            p_list.append(data['items'][0]['liveStreamingDetails']['actualEndTime'])
        except:
            p_list.append(None)

        try:
            p_list.append(data['items'][0]['liveStreamingDetails']['scheduledStartTime'])
        except:
            p_list.append(None)

        try:
            p_list.append(data['items'][0]['status']['madeForKids'])
        except:
            p_list.append(None)

        try:
            p_list.append(data['items'][0]['topicDetails']['topicCategories'])
        except:
            p_list.append(None)

        try:
            p_list.append(data['items'][0]['topicDetails']['relevantTopicIds'])
        except:
            p_list.append(None)

        try:
            p_list.append(data['items'][0]['recordingDetails']['locationDescription'])
        except:
            p_list.append(None)

        try:
            p_list.append(data['items'][0]['recordingDetails']['location']['latitude'])
        except:
            p_list.append(None)

        try:
            p_list.append(data['items'][0]['recordingDetails']['location']['longitude'])
        except:
            p_list.append(None)   

        try:
            p_list.append(data['items'][0]['recordingDetails']['location']['altitude'])
        except:
            p_list.append(None)  


        return p_list

    @staticmethod
    def header():
        return  [
                    'categoryId',
                    'viewCount',
                    'likeCount',
                    'dislikeCount',
                    'favoriteCount',
                    'commentCount',
                    'actualStartTime',
                    'actualEndTime',
                    'scheduledStartTime',
                    'madeForkids',
                    'topicCategories',
                    'relevantTopicIds',
                    'locationDescription',
                    'latitude',
                    'longitude',
                    'altitude'
                ]

    # tags
    # data['items'][0]['snippet']['tags']








