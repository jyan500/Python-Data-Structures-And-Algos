/**
 * Encodes a URL to a shortened URL.
 *
 * @param {string} longUrl
 * @return {string}
 */

// keep forwards and backwards mapping
// use an autoincrement ID as the short URL
// note that in real interview settings, they may ask for limitations,
// like a 10 character max tiny URL. In this case, using only digits would allow up to
// 9^10 possibilities, but including characters would raise the limit to 62^10

var encodeMap = {}
var decodeMap = {}
var total = 0

var encode = function(longUrl) {
    if (!(longUrl in encodeMap)){
        total++
        encodeMap[longUrl] = total
        decodeMap[total] = longUrl
        return total
    }    
};

/**
 * Decodes a shortened URL to its original URL.
 *
 * @param {string} shortUrl
 * @return {string}
 */
var decode = function(shortUrl) {
    if (shortUrl in decodeMap){
        return decodeMap[shortUrl]
    }
};

/**
 * Your functions will be called as such:
 * decode(encode(url));
 */