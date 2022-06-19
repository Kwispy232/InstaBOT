# Press the green button in the gutter to run the script.
import image
import instagram
import quote

if __name__ == '__main__':
    q, a = quote.getTextQuote()
    image.makeImage(q, a, len(q) + len(a))
    instagram.postPicture()
