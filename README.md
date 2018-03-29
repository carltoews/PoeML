# PoeML

**Description:**

During the first three weeks of my time at Insight Data Science, I worked on a project to match snippets of poetry to sets of one or more images. This repository contains exploratory code for the project, as well as the production code that drives the associated application.  The live app can be found at www.poeml.us.

In developing the idea for this data product, I was considering a person engaged in preparing, say, a photo-book, and seeking a snippet of poetry to overlay or accompany a small set of pictures. While this project is really a 'test of concept', I believe it has marketable potential:  the photo-book business in the US is huge (on the order of two billion dollars a year), many people like to contextualize their photos with a bit of poetic text, and the process of finding the right 'snippet' can be hard.  This application promises to make the process easier.  




**Directory structure:**

* *application:*  contains the code that runs the website `poeml.us`.
* *data:*  contains poems, quotes, Shakespearean sonnes, and some test images:  all things I used in developing this project.
* *notebooks:*  contains a set of Python notebooks that I use to scrape, clean, explore, and validate.



**Details:**

The project involved several steps, principally the following:

1.  *Scraping:*  At the heart of this project is a corpus of poems.  I was unable to find a decent database of modern, short verse, and so decided to scrape my own set of poems from various websites.  Specifically, I scraped poems from:
    - www.poets.org (mostly relatively modern, sophisticated, complex poems)  
    - www.famouspoetsandpoems.com (a wildly diverse set of poems from many different eras)   
    - www.poetrysoup.com (from here I took the list "Top 100 Famous Poems"  

    The scripts that I used to scrape are in the `notebooks` directory.  

2.  *Cleaning:*  The scraped data required several levels of processing.  The basic 'cleansing' of the poems (eg. stripping of html tags, ascii encoding, etc.) is done within the scraping notebooks. Subsequent processing (eg. the stemming, lemmatizing, tokenizing, etc. used for NLP analysis) is done where necessary.

3.  *Natural language processing:*  The matching algorithm involves a thematic clumping of my poems, sentiment analysis, and vector embedding (eg. word2vec).  

4. *Image label extraction:*  In order to extract semantic information from my images, I used Google's Cloud-Vision API.  Users who are interested in using this code need to get their own API key.  I've also configured the application code to extract labels from all images within a Flickr album.  The user who wishes to implement this code will need to get their own Flickr API key.

5. *Algorithmic validation:*  I validate the matching algorithm on a test set consisting of a small core of thematically conspicuous images and poems.  

Notebooks with all this functionality are included in the "notebook" directory.  The notebooks have a numerical prefix indicating the order in which to run them if one wants to start at the beginning and proceed to the end.  On the other hand, I've also included my raw and cleansed data in the "data" directory, so it possible to skip around.  In particular, one can skip the scraping and databasing notebooks if all one wants to do is the exploratory data analysis.  

The code that drives the app is in the "application" subfolder.  The guts of the app is in the Python script called "backend".



**Comments:**  In order to have a well-functioning recommender system, the poems should be stylistically "suited" to the task.  Really that requires some custom curating:  my taste is not yours, and the "matches" will be more satisfying if the underlying set of poems is palatable.  For this project, I'll end up focusing on modern, short poems and hope for the best, but this is a good example of a project for which at least some "human in the loop" could make a big difference.  
