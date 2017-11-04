from BeautifulSoup import BeautifulSoup
import urllib
import random

print "Motivational Marriage Quote for every day...\n\n\n"
quote_write_to_file = open("Quotes about marriage.txt", "w+")
quote_write_to_file.write ("Your special dose of quotes...\n\n\n\n")

marriageUrl = 'http://quotes.yourdictionary.com/theme/marriage/'
marriageHtml = urllib.urlopen(marriageUrl).read()
soupHelp = BeautifulSoup(marriageHtml)

quotes = soupHelp.findAll('p', attrs={'class': 'quoteContent'})
quote_list = []
for quote in quotes:
    quote_list.append(quote.text)

generator = random.sample(quote_list, 5)
for item in generator:
    quote_write_to_file.writelines(item)
    quote_write_to_file.write("\n")
    print (item)

quote_write_to_file.close()