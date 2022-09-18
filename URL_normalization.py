def normalize_url(url):
    url1 = url[:7]
    url2 = url[:8]
    if url1 != 'http://' and url2 != 'https://':
        return 'https://' + url
    elif url1 == 'http://':
        return 'https://' + url[7:]
    else : 
        return url
print(normalize_url('http://yandex.ru'))