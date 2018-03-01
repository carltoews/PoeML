#PoeML

**Description:**

Exploratory code for an application to match images to poetry snippets. The live app can be found at www.poeml.us.

**Details:**

During the first three weeks of my time at Insight Data Science, I worked on a project to match collections of images to relevant snippets of poetry. The project involved several steps:

I had to scrape a bunch of poems from the web, since I couldn't find a very complete or well described pre-existing poetry database. Some of this code is scraping code.
I end up databasing the poems in a PostgresSQL data base. Some of this code is Python-SQL interface code.
Matching is done by first extracting labels from each image, a process I achieve via Google's Cloud-Vision API. Some of this code requires getting a cloud vision account and your own key.
