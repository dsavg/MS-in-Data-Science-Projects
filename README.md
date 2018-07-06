# Data Science Projects

This repository hosts projects that I worked on during my Master's in Data Science at USF. 

## Hashtable in Python

A hashtable is a data structure, using a dictionary implementation that can map keys to values. The goal of a hashtable is to speed up key lookups by reducing the size of the search region. A hash table uses a hash function to indicate which bucket contains the search key.

Ideally, the hash function will assign each key to a unique bucket, but most hash tables designs employ an imperfect hash function, which might cause hash collisions where the hash function generates the same index for more than one key. Such collisions can be accommodated if we use a prime number of buckets.

Complexity: O(1)

Applications: Hashtables are often used in Search Engines, to improve the speed of search 

In [hashtable.py](https://github.com/dsavg/MS-in-Data-Science-Projects/blob/master/hashtable.py) I create a hashtable class implementation. 

## Simple ETL in Python

I created two simple scripts in Python for generating data in multiple formats. In [fromcsv.py](https://github.com/dsavg/MS-in-Data-Science-Projects/blob/master/ETL/fromcsv.py) I created a script that takes as an input a csv file and converts it to a table in html, an xml file or a json file. In order to run this script, simply type ```python fromcsv.py html < input.csv > output.csv``` in bash command line.



converting csv files to xml, json or html and backwords. 

