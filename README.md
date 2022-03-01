# image-processing-tutorial

The image processing tutorial for the Machine Learning for Design course.

_How to use?_

- Put images (pnj, jpg, jpeg) into the data/assigment_1 folder
- run `python3 ass1.py` in terminal
- View results in the [google sheet](https://docs.google.com/spreadsheets/d/1eNxONIxV5BzQM4AHEs52vyfg-T0NGlLCnU0pS0Lup-o/edit?usp=sharing)

**Group G23**

In this repo group G 23 of the I0B4-T3 "Machine learning for design" course has compossed some code to provide data to evaluate the capabilities of the following ML image object recognition an classification model: 

https://huggingface.co/facebook/detr-resnet-50

In the main file for this assignment **ass1.py** we've written a function that does the following

- Iterates thought the contents of the **data/assigment_1** folder (line 18-19)
- Uses the query function from main.py to send the data over to the ML model (line 20)
- Ads the filename to each result of the function (line 22-24)
- Posts the results to a webhook endpoint that puts the data through to google sheets
- Delete the processed file from the repo

**webhook**

the webhook is hosted on the quick prototyping platform [integromat](https://www.integromat.com/en).
Here it's very easy to connect to google sheets instead of making an oAuth client or getting a GCP verification.

The scenario preforms the following operations:

- Receives the webhook
- Itterates over each image result
- Inputs all detected objects, their data and the corresponsing filename into google sheets

This is visualised below:

![ezgif com-gif-maker](https://user-images.githubusercontent.com/83215912/156182733-7200e4df-6993-47a6-9658-f4e19ac0c66d.gif)

This flow allows us to easily transfer data to the model and log the results into a dynamic google sheet.

Some things we could impove in a next itteration:

- Automatically appending URLs to the entries
- Allowing for extra image cateogirization on submitting to the model

resources used:

#https://www.kite.com/python/answers/how-to-iterate-through-the-contents-of-a-directory-in-python

#https://www.w3schools.com/python/ref_requests_post.asp
