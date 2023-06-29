import snscrape.modules.twitter as sntwitter
import csv

# Creating list to append tweet data to
keywords = "SBF,Sam Bankman-Fried,FTT"
sDates = "2022-11-01"
uDates = "2022-12-01"

keylist = keywords.split(",")
sincedate = sDates
untildate = uDates

f = open("ftx1.csv", "w")
writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
writer.writerow(["Datetime", "Tweet Id", "Text", "Username", "Followers"])

# Using TwitterSearchScraper to scrape data and append tweets to list
for j in keylist:
    str = "{} since:{} until:{}"

    for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper(str.format(j, sincedate, untildate)).get_items()
    ):
        writer.writerow(
            [
                tweet.date.timestamp(),
                tweet.id,
                tweet.rawContent,
                tweet.user.username,
                tweet.user.followersCount,
            ]
        )
f.close()
