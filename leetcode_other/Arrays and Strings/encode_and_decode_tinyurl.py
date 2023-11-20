"""
Key Concept:

I'm using Python's hash function such that
we take a given long URL and turn it into the same short URL every time,
so we don't need to worry about using random chars and checking to make sure that sequence of random chars
hasn't been used.

Just store the hashed version as the shortURL in a dict, mapping to the original long form URL,
and then retrieve that in decode 

"""
class Codec:
    def __init__(self):
        self.decoder = dict()
        self.baseUrl = "http://tinyurl.com/"
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl = self.baseUrl + str(hash(longUrl))
        
        self.decoder[shortUrl] = longUrl
        return shortUrl
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decoder[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))