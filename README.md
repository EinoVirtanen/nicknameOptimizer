## nicknameOptimizer - add noise to your nickname until it becomes uniqueish!

*Once upon a time there was a boring Sunday evening. I thought to myself: fak, my nickname has become non unique over the years. I would like my stuff to pop, when someone searches Google with my username.*

So this program adds N letters to your nickname, queries M of the variations through Google and returns a sorted list of the results.
```
$ python main.py johncena 2 3 # querying 3 variations of nick with 2 added letters
Querying nicks..

johncenate: 37
johncenatr: 10
johncenapv: 4

[nick]: [number of results]
```

### Usage
* git clone
* obtain a Google API key from cse.google.com and put it to a file named 'myApiKey'
* create a Custom Search thing at the same place
* put whatever into the queried site field and edit the Custom Search to include results from all over the web
* find the cx key of your Custom Search and put it to a file named 'myCxKey'
* run the code
* bro-tip: might make sense to do separate Google-queries of the best results of the nick variations because of:
* https://www.google.fr/search?q=unfortunate+brand+names
