<<<<<<< HEAD

# Youtube Channel Analysis with V3 API

Gathering youtube data from V3 API

### Getting key token
A key token is required from 
https://developers.google.com/youtube/v3/getting-started

After getting the token put it in key.txt in the main parent folder.

### Running the app
Download the requirements and start the program with py start.py in /yt_analytics
Data folder will be created upon staring the script, that is where the data will be stored.
Currently the channel is set to gathering data from live youtube streaming channel "Only in Japan".



# Stream Youtube Channel Analysis

The following is an analysis and prediction for viewCount of a live stream youtube channel. Public data from the channel is obtained through youtube V3 API with the script in the sub folder, when the program runs it will create a data folder to store the data files. The follow data shows insights on the viewership of ‘Only in Japan’ live stream channel for the last 300 videos. The viewership count is not the live stream viewership but after. 

The benefit in obtaining data from this particular channel is the frequency that it streams at different time and also the various locations provided from the V3 API to determine the viewership.

## 1) Data Analysis

Top 10 Streaming Locations

<img src="/images/10_locations.png" width="300" height="250">
<!-- ![S_loc_viewers](/images/10_viewers_location.png) -->

Top 10 Streaming Locations with most viewers

<img src="/images/10_viewers_location.png" width="400" height="250">

Video distribution varying by month

<img src="/images/video_distribution.png" width="300" height="250">

Most viewed hour (UTC-9)

<img src="/images/views_by_hour.png" width="300" height="250">

Like/Dislike ratio by weekday

<img src="/images/like_dislike.png" width="300" height="250">


## 2) Viewer Count Prediction

Missing Data from V3 API

<img src="/images/missing_data.png" width="300" height="250">


Correlation Relationship

<img src="/images/correlation.png" width="500" height="500">


The correlation relations between the numeric features are shown above. From the scatter plots there appears to be high linearity between like, dislikes, and the comment counts. Besides that other feature correlation are not as apparent. The only other meaningful correlation could be seen in the hour feature with like, dislike, and comments. Based on these observations additional features are generated.




## 3) Model prediction

Linear regression was used to predict viewer counts. Standard procedure with splitting training and test set, fitting the train set to the model and predicting the results against the test labels. The overall result was decent achieving R2 of 0.908. Lastly the plot between the predicted result and testing label forms a linear form demonstrating a good initial impression.

<img src="/images/prediction.png" width="500" height="400">




=======
# Youtube Analysis

## Data Mining data with V3 API

Data mining live streaming youtbe data.
Multiple features can be drawn from the API such as:
1. viwership
1. location
1. comment count
1. video count
1. subscribers
1. etc.

With additional features a prediction can be made on the 
viewership of future streams.
>>>>>>> 82a65580e5d4d4884f38139628a978eab93af991
