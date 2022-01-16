# AI-Assistant
This AI Assistant is a utility tool which acts as a companion and 
direct user in his/her daily tasks in the system. It is also powered by a recommender 
system which recommends which movie to watch based on different parameters. 
The general operating principle of artificial intelligence assistants is the ability to 
make personal decisions based on incoming data and we have tried to apply these 
principles in our assistant. The assistant is also capable of helping the user navigate 
through the system by opening/closing applications and typing documents and 
email as directed by the user. This assistant will also be of great use to people with 
special ability (impaired vision, etc). The Fig 1. describe the basic outline of the assistant. <br />

![](readme%20images/assistant.JPG)

** Note: ** 
interface.py  : This the main file to run Ai assistant with voice interaction.<br />
interface_write.py: Same as above but have written interface.<br />
Downlaod reddit dataset for january month 2015 from link below:<br />
https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/?st=j9udbxta&sh=69e4fee7  <br />
(Can pull much more bigger dataset like of 3 years by use of big query) - optional<br />

The snapshot below shows the database formed after preprocessing the data.

![](readme%20images/reddit.JPG)

# Module Decomposition
The description for Module shown in Figure 5.1 is a s follows:<br />
● Chatbot: This module contains the listener object. To each Voice input from user it 
will first try to match with keywords for any initiation of the particular task or 
module. If there is no match the reply from assistant will be according to deep 
learning model by which it is trained from reddit dataset.<br />
● Voice Typing: Voice typing module is using google speech recognition API which 
listen from user source and convert speech-to-text. User can ask to save file in any 
name. File will be saved on Desktop and user can access it once it typed by 
command instruction. Genreally it will be activated by keywords “Send Message” or 
“Type document”.<br />
● Navigation : This module have various path of application stored and once the 
name of the application match with user voice input it call the path and application 
gets opened. It is activated by keywords “Open”.
Also user can search on goggle in the default browser (Google Chrome) using Search 
keyword which will be used to search the word or phrase “X”.<br />
And „Play‟ keyword will be used to search the videos in YouTube search bar to play 
in the default browser.<br />
● Wikipedia: This module is made by using the Wikipedia library in python which 
provides control to search wikipedia for particular topics as required by the user and 
revert the information back to it. Generally it will be activated by keywords 
“Wikipedia Search”.<br />
● Recommendation: This module will contain access to user past history saved in 
feature vector format. The other movie rating list, category and like-minded user 
information will be present in feature vector format to the recommendation model to 
access and provide users with proper recommendation. Generally it will be activated 
by keywords “What to watch” or “Recommend me”.<br />

![](readme%20images/module.JPG)


# Python external Packages Used in Assistant
 SpeechRecognition: For recognition of all communication between user and assistant. It 
is a library for performing speech recognition, with support provided for several APIs 
and engines, offline and online. <br />
 PyAudio: For getting an I/O port for audio. To save and record audio as required. <br />
 Wikipedia: Python provides a Wikipedia API for collecting information from wikipedia 
about particular subjects enquired by users.<br />
 gTTS: Google Text To Speech, for converting the given text received as parameter to 
speech. It is a a Python library and CLI tool to interface with Google Translate's text-tospeech API.<br />
 Pygame: for playing the saved audio (.mp3) file received depending on user queries. It 
is a pure python, cross platform, single function module with no dependencies for 
playing sounds. The mixer() function is used to play the mp3 in the terminal.<br />
 webbrowser: Python webbrowser module provided convenient API to control web 
browser that is, open web browser window or new tab with python. By default, the default 
browser of the system will be opened or controlled.<br />


For methodology of the chatbot one can read my research paper for the same.
DOI: https://doi.org/10.1016/j.matpr.2020.05.450

The snapshot below shows the AI Assistant on a run.


![](readme%20images/chatbot.JPG)

![](readme%20images/navigation.JPG)

![](readme%20images/play.JPG)

![](readme%20images/search.JPG)

![](readme%20images/write.JPG)

![](readme%20images/wiki.JPG)

![](readme%20images/content.JPG)

![](readme%20images/collab.JPG)

** NOTE: **
The Assistant can work on Windows, MacOS, and LINUX. Just can the path files supported by the respective OS.<br />
The output.mp3 is the file generated by chatbot. It always contain the sentence which was last said by the chatbot.<br />
The message.mp3 contains "Done" sound used to notify user of the completion of the requested task.<br />
The messagec.mp3 and messagecb.mp3 are generated by content and collaborative based recommender system.<br />
The movie and rating csv files are used in the recommender system.
**The other training and setup code for the chatbot is uploaded to a priv repo. This repo is to give a brief idea on our overall project and code in this repo is free to use.**
