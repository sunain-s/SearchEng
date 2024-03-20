# SearchEng
A CLI search engine made using Python, implementing the PageRank algorithm

## Requirements
- must have 10 webpages that can be searched for
- must sort by PageRank
- must sort by some kind of search score
- must display top 5 results based upon PR and SS
- must display a snippet of text from the relevant pages
- must display page titles

## How To Run
Install bs4 module and run 'main.py' with python3, and use in command line.\
Can add more webpages of any name - program renames them as necessary

## What I Learnt
- os.getcwd() to get the current path of the file being run
- os.listdir() to get a list of html files in a directory
- using https://www.plot-generator.org.uk/story/ to create html content
- implementing PR
- using Beautiful Soup extract elements from html files
- designing a search score algorithm and combining with PR
- retrieving a random text snippet from a html file
- how to open a file using os.startfile()

## Improvements
There is a clear improvement that can be made here:
- ==> implement it within an interface

This would involve creating my own search engine interface similar to Google's using HTML, CSS and JS and linking it to my python script and output results on the interface.\
Following on from this, is to open the webpages within the same application, essentially creating my own web browser.
