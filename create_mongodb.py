# from pymongo import MongoClient


# client = MongoClient("mongodb://localhost:27017/")
# db = client["women_cricket_db"]
# collection = db["news_articles"]


# scraped_data = [
#     {
#         "source": "Cricket Times",
#         "followers": 3014,
#         "time": "4d",
#         "headline": "Mumbai Indians Women Outclass UP Warriorz Women with an 8-Wicket Victory!",
#         "engagement": {"likes": 66, "comments": 12, "reposts": 0}
#     },
#     {
#         "source": "WomenCricket.com",
#         "followers": 79,
#         "time": "4d",
#         "headline": "Mumbai Indians Women Outclass UP Warriorz Women with an 8-Wicket Victory!",
#         "engagement": {"likes": 35, "comments": 12, "reposts": 2}
#     },
#     {
#         "source": "Kunal Binjewar",
#         "followers": 11000,
#         "time": "1mo",
#         "headline": "Indian Women's U19 World Cup Champions 2025!",
#         "engagement": {"likes": 59, "comments": 11, "reposts": 0}
#     },
#     {
#         "source": "Cricbuzz",
#         "followers": 50000,
#         "time": "2d",
#         "headline": "Harmanpreet Kaur Leads India to Victory in T20 Series Against Australia!",
#         "engagement": {"likes": 120, "comments": 24, "reposts": 5}
#     },
#     {
#         "source": "ESPN Cricinfo",
#         "followers": 60000,
#         "time": "5d",
#         "headline": "Smriti Mandhana’s Century Powers India to a Record-Breaking Win!",
#         "engagement": {"likes": 150, "comments": 30, "reposts": 8}
#     },
#     {
#         "source": "The Hindu",
#         "followers": 45000,
#         "time": "1w",
#         "headline": "BCCI Announces Central Contracts for Women's Team: Who Made the Cut?",
#         "engagement": {"likes": 90, "comments": 15, "reposts": 3}
#     },
#     {
#         "source": "Cricket Next",
#         "followers": 20000,
#         "time": "6d",
#         "headline": "Indian Women’s Team Gears Up for World Cup with Intensive Training Camp",
#         "engagement": {"likes": 75, "comments": 10, "reposts": 2}
#     },
#     {
#         "source": "SportsKeeda",
#         "followers": 25000,
#         "time": "3d",
#         "headline": "Jemimah Rodrigues Shines as India Defeats England in a Thrilling Contest!",
#         "engagement": {"likes": 105, "comments": 22, "reposts": 6}
#     },
#     {
#         "source": "NDTV Sports",
#         "followers": 30000,
#         "time": "4d",
#         "headline": "Women’s IPL 2025: Teams, Auction Details, and Key Players to Watch",
#         "engagement": {"likes": 130, "comments": 28, "reposts": 7}
#     },
#     {
#         "source": "Times of India",
#         "followers": 55000,
#         "time": "5h",
#         "headline": "Mithali Raj’s Insights on Women’s Cricket Growth in India",
#         "engagement": {"likes": 95, "comments": 18, "reposts": 4}
#     },
#     {
#         "source": "BBC Sport",
#         "followers": 70000,
#         "time": "10h",
#         "headline": "ICC Women’s Cricket Rankings Updated: Where Does India Stand?",
#         "engagement": {"likes": 110, "comments": 25, "reposts": 6}
#     },
#     {
#         "source": "India Today",
#         "followers": 48000,
#         "time": "3d",
#         "headline": "Women’s Cricket World Cup 2025 Schedule Announced!",
#         "engagement": {"likes": 145, "comments": 32, "reposts": 9}
#     },
#     {
#         "source": "Hindustan Times",
#         "followers": 52000,
#         "time": "2d",
#         "headline": "Women’s Cricket Set to Receive Equal Pay as BCCI Announces New Policy!",
#         "engagement": {"likes": 160, "comments": 35, "reposts": 10}
#     },
#     {
#         "source": "Cricinfo",
#         "followers": 65000,
#         "time": "1w",
#         "headline": "Indian Women’s Team Makes Historic First Test Win Against Australia!",
#         "engagement": {"likes": 180, "comments": 40, "reposts": 12}
#     },
#     {
#         "source": "The Guardian",
#         "followers": 58000,
#         "time": "2w",
#         "headline": "Women’s Cricket Gains Global Popularity: A New Era Begins!",
#         "engagement": {"likes": 200, "comments": 50, "reposts": 15}
#     }
# ]


# collection.insert_many(scraped_data)


# def fetch_all_articles():
#     return list(collection.find({}, {"_id": 0}))

# def update_article(old_headline, new_headline):
#     collection.update_one({"headline": old_headline}, {"$set": {"headline": new_headline}})

# def delete_article(headline):
#     collection.delete_one({"headline": headline})


# def most_discussed_articles():
#     return list(collection.aggregate([
#         {"$project": {"headline": 1, "total_engagement": {"$sum": ["$engagement.comments", "$engagement.likes", "$engagement.reposts"]}}},
#         {"$sort": {"total_engagement": -1}},
#         {"$limit": 5}
#     ]))

# def peak_engagement_time():
#     return list(collection.aggregate([
#         {"$group": {"_id": "$time", "total_engagement": {"$sum": "$engagement.likes"}}},
#         {"$sort": {"total_engagement": -1}}
#     ]))

# print("All Articles:", fetch_all_articles())
# update_article("Mumbai Indians Women Outclass UP Warriorz Women with an 8-Wicket Victory!", "MI Women Crush UP Warriorz!")
# delete_article("Indian Women's U19 World Cup Champions 2025!")
# print("Most Discussed Articles:", most_discussed_articles())
# print("Peak Engagement Time:", peak_engagement_time())
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create a new database
new_db = client["women_cricket"]

# Create a new collection (table)
new_collection = new_db["cricket_articles"]

# Dataset with 15 articles
articles = [
    {
        "source": "Chetan Suryawanshi",
        "followers": 0,
        "time": "4mo",
        "headline": "Top 5 Indian Women Cricketers Who Are Inspiring the Next Generation of Girls",
        "engagement": {"likes": 19, "comments": 1, "reposts": 0}
    },
    {
        "source": "Tarutr Malhotra",
        "followers": 0,
        "time": "1mo",
        "headline": "The Daily Cricket Digest - Why do Indian stars need a 150 kg baggage allowance?!",
        "engagement": {"likes": 4, "comments": 0, "reposts": 0}
    },
    {
        "source": "Vipul Saxena",
        "followers": 0,
        "time": "6mo",
        "headline": "Mr Jay Shah - a new hope for world of Cricket",
        "engagement": {"likes": 11, "comments": 0, "reposts": 1}
    },
    {
        "source": "Women Entrepreneurs Review",
        "followers": 11562,
        "time": "4mo",
        "headline": "Women’s T20 World Cup 2024: 6 Indian Women Players to Watch For",
        "engagement": {"likes": 20, "comments": 1, "reposts": 1}
    },
    {
        "source": "Animesh Pandey",
        "followers": 0,
        "time": "8mo",
        "headline": "Shafali Verma Sets New Milestone in Women's Test Cricket",
        "engagement": {"likes": 2, "comments": 0, "reposts": 0}
    },
    {
        "source": "Dr Rajesh Parekh",
        "followers": 0,
        "time": "4mo",
        "headline": "Beyond Cricket: Yuvraj Singh’s Inspiring Story of Hope and Strength",
        "engagement": {"likes": 12, "comments": 2, "reposts": 0}
    },
    {
        "source": "Tarutr Malhotra",
        "followers": 0,
        "time": "2mo",
        "headline": "The Daily Cricket Digest - Konst he save Australia?",
        "engagement": {"likes": 6, "comments": 2, "reposts": 0}
    },
    {
        "source": "Mithali Raj",
        "followers": 25000,
        "time": "5mo",
        "headline": "The Evolution of Women's Cricket in India: From Struggles to Success",
        "engagement": {"likes": 45, "comments": 3, "reposts": 2}
    },
    {
        "source": "Smriti Mandhana",
        "followers": 30000,
        "time": "3mo",
        "headline": "Breaking Barriers: Indian Women Cricketers Making Global Impact",
        "engagement": {"likes": 38, "comments": 4, "reposts": 2}
    },
    {
        "source": "ESPN Cricket",
        "followers": 100000,
        "time": "7mo",
        "headline": "India's Women's Cricket Team Secures Historic Test Win Against Australia",
        "engagement": {"likes": 50, "comments": 10, "reposts": 5}
    },
    {
        "source": "Hindustan Times",
        "followers": 50000,
        "time": "6mo",
        "headline": "BCCI Announces Major Investments in Women's Cricket for the Next 5 Years",
        "engagement": {"likes": 30, "comments": 8, "reposts": 4}
    },
    {
        "source": "Women’s Sports Weekly",
        "followers": 20000,
        "time": "4mo",
        "headline": "Top 10 Upcoming Talents in Indian Women’s Cricket",
        "engagement": {"likes": 25, "comments": 5, "reposts": 3}
    },
    {
        "source": "BBC Sports",
        "followers": 75000,
        "time": "2mo",
        "headline": "How India’s Women’s Cricket Team is Changing the Game Globally",
        "engagement": {"likes": 42, "comments": 6, "reposts": 2}
    },
    {
        "source": "Sports Today",
        "followers": 32000,
        "time": "1mo",
        "headline": "Indian Women Cricketers Speak Up on Gender Pay Gap in Sports",
        "engagement": {"likes": 28, "comments": 4, "reposts": 3}
    },
    {
        "source": "Cricket World",
        "followers": 45000,
        "time": "3mo",
        "headline": "A Look Back at India's Journey in Women’s Cricket World Cups",
        "engagement": {"likes": 35, "comments": 7, "reposts": 4}
    }
]

# Insert data into the new collection
new_collection.insert_many(articles)

# Function to fetch all articles
def fetch_all_articles():
    return list(new_collection.find({}, {"_id": 0}))

# Function to update an article's headline
def update_article(old_headline, new_headline):
    new_collection.update_one({"headline": old_headline}, {"$set": {"headline": new_headline}})

# Function to delete an article
def delete_article(headline):
    new_collection.delete_one({"headline": headline})

# Function to get the most discussed articles based on engagement
def most_discussed_articles():
    return list(new_collection.aggregate([
        {"$project": {"headline": 1, "total_engagement": {"$sum": ["$engagement.comments", "$engagement.likes", "$engagement.reposts"]}}},
        {"$sort": {"total_engagement": -1}},
        {"$limit": 5}
    ]))

# Function to find the peak engagement time
def peak_engagement_time():
    return list(new_collection.aggregate([
        {"$group": {"_id": "$time", "total_engagement": {"$sum": "$engagement.likes"}}},
        {"$sort": {"total_engagement": -1}}
    ]))

# Testing the new database
print("All Articles:", fetch_all_articles())
update_article("Mr Jay Shah - a new hope for world of Cricket", "Jay Shah's Role in Transforming Indian Cricket")
delete_article("Shafali Verma Sets New Milestone in Women's Test Cricket")
print("Most Discussed Articles:", most_discussed_articles())
print("Peak Engagement Time:", peak_engagement_time())
