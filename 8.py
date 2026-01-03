def normalize_url(url: str) -> str:
    if url[:8] == 'https://':
        return url
    if url[:7] == 'http://':
            new_url = url[7:]
            return 'https://' + new_url
    else:
        return 'https://' + url
    
print(normalize_url('https://example.com'))  # => 'https://example.com'
print(normalize_url('http://example.com'))   # => 'https://example.com'
print(normalize_url('example.com'))          # => 'https://example.com'
        
