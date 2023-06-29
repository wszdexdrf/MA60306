import snscrape.modules.twitter as sntwitter
import csv

# Creating list to append tweet data to
events = ["cocacola", "ftx", "elililly", "dogecoin"]
keywords = [
    "coca cola,ronaldo,drink water,soft drink",
    "SBF,Sam Bankman-Fried,FTT,FTX,Alameda",
    "Twitter Blue,Insulin,Eli lilly,Free Insulin",
    "Dogecoin,ELon Musk,Doge",
]
sDates = ["2021-06-01", "2022-11-01", "2022-11-01", "2021-02-01"]
uDates = ["2021-07-01", "2022-12-01", "2022-12-01", "2021-03-01"]

for event, keystr, sDate, uDate in zip(events, keywords, sDates, uDates):
    keylist = keystr.split(",")
    sincedate = sDate
    untildate = uDate

    f = open(event + ".csv", "w")
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Datetime", "Tweet Id", "Text", "Username", "Followers"])

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for j in keylist:
        str = "{} since:{} until:{}"

        for i, tweet in enumerate(
            sntwitter.TwitterSearchScraper(
                str.format(j, sincedate, untildate)
            ).get_items()
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