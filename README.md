# News Aggregator
The news aggregator parses news from different sites using the requests library, removes duplicate news, and combines similar news for a given period. The interface was developed using Qt Designer. 
Using the requests HTTP library, a request is sent to the desired site and the resulting HTML/XML file is parsed using the BeautifulSoup library. For each news there is its link, title and text. All news are recorded in a json file. Using the textdistance library and the sorensen.normalized_similarity() function, the headlines of all news are compared and duplicates are removed.
