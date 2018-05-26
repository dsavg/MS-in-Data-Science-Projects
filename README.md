# Data Science Projects

This repository hosts projects that I worked on during my Master's in Data Science at USF. 

## Hashtable in Python

A hashtable is a data structure, using a dictionary implementation that can map keys to values. The goal of a hashtable is to speed up key lookups by reducing the size of the search region. A hash table uses a hash function to indicate which bucket contains the search key.

Ideally, the hash function will assign each key to a unique bucket, but most hash tables designs employ an imperfect hash function, which might cause hash collisions where the hash function generates the same index for more than one key. Such collisions can be accommodated if we use a prime number of buckets.

Complexity: O(1)

Applications: Hashtables are often used in Search Engines, to improve the speed of search 

In [hashtable.py](https://github.com/dsavg/MS-in-Data-Science-Projects/blob/master/hashtable.py) I create a hashtable class implementation. 

