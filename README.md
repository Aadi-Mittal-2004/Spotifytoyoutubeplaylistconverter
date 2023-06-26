# Spotifytoyoutubeplaylistconverter
This is a simple Python program which helps us to solve a very annoying issue in our daily life which is "converting a Spotify playlist to youtube one ".Since I am an avid music lover and mostly use youtube music for this I need a way to convert my friend's spotify playlist to youtube.

TO use this program you have to follow these following steps:
1. go to spotify developer page and register
2. make an app and get the cliendt id and client secreat
3. go to youtube cloud console and register
4. create a project 
5. search for yotube data api 3 and enable it
6. go to youtube api and make a api key and make credientials like client id and client secreat
7. make sure to restrict the api key to youtube data api 3
8. register app as desktop app on youtube cloud console and publish the app
9. download the creadiential json file in the same folder as of the code
10. cerate an .env file in the same folder and initialize all the credientials and api keys
11. install all the modules
12. run your program sould be running fine . enjoy 🥳 

While making this project I have faced many difficulties like:
>How to connect spotify to python
>How to extract data from spotify API
>How to organise the extracted data so it will be easy to use in next steps
>How to connect to Youtube Api
>How to get around the daily quota limit of youtube API
I started the project myself but after extracting data from spotify api i felt stuck and cant figerout the way forward
after that i used chatgpt to help me in this and after a day or two of back and forth with it i am finally happy with the product

 Some places i got stuck and the way i come out of it.It will help you  if you want to make a similar project:
 >how to do the spotify Oauth and get access token : for this i used this video https://www.youtube.com/watch?v=WAmEZBEeNmg
 >since youtube has a daily quota i can't add a full playlist by searching and adding using youtube api so i used webscraping for
  searching and getting video id and use youtube api to make playlist and add songs
 >to do the youtube authentication i used chatgpt

 
 Some feature i felt that can be imporved upon:
 >the program only take the first 100 songs of a playlist (limitation on spotify): this can be solved using offset after 100 songs if there are any
>youtube daily quota: for this i do not have any idea how to solve this


i hope you would like this and i am open to any suggestions .
Thnak you
