# News Aggregator
The news aggregator parses news from different sites using the requests library, removes duplicate news, and combines similar news for a given period. The interface was developed using Qt Designer. 
Using the requests HTTP library, a request is sent to the desired site and the resulting HTML/XML file is parsed using the BeautifulSoup library. For each news there is its link, title and text. All news are recorded in a json file. Using the textdistance library and the sorensen.normalized_similarity() function, the headlines of all news are compared and duplicates are removed.

Агрегатор новостей парсит новости с разных сайтов с помощью библиотеки requests, удаляет дубликаты новостей, объединяет похожие новости за заданный период.
Разработка интерфейса производилась с помощью Qt Designer.
С помощью HTTP-библиотеки requests отправляется запрос нужному сайту и с помощью библиотеки BeautifulSoup разбирается полученный HTML/XML файл. В цикле для каждой новости находится ее ссылка, заголовок и текст. Все новости записываются в словарь, а после в json-файл. При помощи библиотеки textdistance и функции sorensen.normalized_similarity() сверяются заголовки всех новостей, и дубликаты удаляются.
