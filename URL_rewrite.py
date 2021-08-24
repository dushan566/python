# This will remove double slashes in the URL
def http_normalize_slashes(url):
    url = str(url)
    segments = url.split('/')
    correct_segments = []
    for segment in segments:
        if segment != '':
            correct_segments.append(segment)
    first_segment = str(correct_segments[0])
    if first_segment.find('http') == -1:
        correct_segments = ['http:'] + correct_segments
    correct_segments[0] = correct_segments[0] + '/'
    normalized_url = '/'.join(correct_segments)
    print(normalized_url)
    return normalized_url

if __name__ == "__main__":
    http_normalize_slashes("https://www.example.com//x///c//v///path?foo=bar") 