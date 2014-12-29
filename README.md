![seek. command line nirvana.](http://i.imgur.com/2wEYui1.png)
# seek

Display internet search results without ever leaving your terminal. Oh, and it can speed read the results as well. Basically, it's command line nirvana.

Seek is a sister to [howdoi](https://github.com/gleitz/howdoi/) and [Glance](https://github.com/Miserlou/glance/).

## Installation

    pip install seek -g

## Examples

    $ seek a nice up of tea orwell 

    If you look up 'tea' in the first cookery book that comes to hand you will probably find that it is unmentioned; or at most you will find a few lines of sketchy instructions which give no ruling on several of the most important points. [etc.]
    A Nice Cup of Tea
    http://www.booksatoz.com/witsend/tea/orwell.htm

    $ seek a nice cup of tea orwell --glance
    A Nice Cup of Tea
    http://www.booksatoz.com/witsend/tea/orwell.htm
    stimulation      <--- (This is animated)

## Features:

* [Glance](http://glance.wtf) mode!
* Diffbot article extraction
* Searches DuckDuckGo, Google coming soon (maybe).

BSD 3-clause, 2014-2015.
