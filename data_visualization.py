# import matplotlib.pyplot as plt
# import seaborn as sns
# from wordcloud import WordCloud
# from collections import Counter
# import pandas as pd
# import numpy as np

# # Sample extracted data from NLP Analysis
# data = [
#     {"headline": "MI Women Crush UP Warriorz!", "entities": {'ORG': 'MI Women Crush UP Warriorz'}, "vader": -0.2244, "textblob": 0.0, "source": "Cricket Times", "likes": 66, "comments": 12, "reposts": 0, "time": "4d"},
#     {"headline": "Mumbai Indians Women Outclass UP Warriorz Women with an 8-Wicket Victory!", "entities": {'ORG': 'Mumbai Indians Women Outclass UP Warriorz Women'}, "vader": 0.0, "textblob": 0.0, "source": "Cricket Buzz", "likes": 50, "comments": 15, "reposts": 2, "time": "3d"},
#     {"headline": "Harmanpreet Kaur Leads India to Victory in T20 Series Against Australia!", "entities": {'PERSON': 'Harmanpreet Kaur', 'EVENT': 'T20 Series', 'GPE': 'Australia'}, "vader": 0.0, "textblob": 0.0, "source": "Sports India", "likes": 120, "comments": 30, "reposts": 5, "time": "2d"},
#     {"headline": "Smriti Mandhana’s Century Powers India to a Record-Breaking Win!", "entities": {'ORG': 'Century Powers India'}, "vader": 0.6239, "textblob": 1.0, "source": "Cricket Times", "likes": 200, "comments": 40, "reposts": 10, "time": "1d"},
#     {"headline": "BCCI Announces Central Contracts for Women's Team: Who Made the Cut?", "entities": {'ORG': "BCCI Announces Central Contracts for Women's Team"}, "vader": -0.2732, "textblob": 0.0, "source": "Cricket Buzz", "likes": 80, "comments": 25, "reposts": 3, "time": "5d"}
# ]


# df = pd.DataFrame(data)


# def categorize_sentiment(vader_score):
#     if vader_score > 0.2:
#         return "Positive"
#     elif vader_score < -0.2:
#         return "Negative"
#     else:
#         return "Neutral"

# df["sentiment_category"] = df["vader"].apply(categorize_sentiment)



# plt.figure(figsize=(12, 5))


# plt.subplot(1, 2, 1)
# sentiment_counts = df["sentiment_category"].value_counts()
# plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['green', 'red', 'gray'], startangle=90)
# plt.title("Sentiment Distribution")


# plt.subplot(1, 2, 2)
# sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette=['green', 'red', 'gray'])
# plt.xlabel("Sentiment")
# plt.ylabel("Count")
# plt.title("Sentiment Count")

# plt.tight_layout()
# plt.show()


# entity_list = []
# for row in df["entities"]:
#     entity_list.extend(row.values())


# entity_counts = Counter(entity_list)
# top_entities = entity_counts.most_common(10)


# wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(entity_counts)

# plt.figure(figsize=(12, 5))


# plt.subplot(1, 2, 1)
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.title("Most Mentioned Players & Teams")


# plt.subplot(1, 2, 2)
# sns.barplot(x=[e[0] for e in top_entities], y=[e[1] for e in top_entities], palette="viridis")
# plt.xticks(rotation=45)
# plt.xlabel("Players/Teams")
# plt.ylabel("Mentions")
# plt.title("Top Mentioned Entities")

# plt.tight_layout()
# plt.show()



# plt.figure(figsize=(10, 5))
# engagement_metrics = df.groupby("source")[["likes", "comments", "reposts"]].sum()

# engagement_metrics.plot(kind="bar", figsize=(10, 5), colormap="Set2")
# plt.xlabel("News Source")
# plt.ylabel("Engagement Count")
# plt.title("Engagement Metrics by Source")
# plt.xticks(rotation=45)
# plt.legend(title="Engagement Type")
# plt.show()




# df["days_ago"] = df["time"].apply(lambda x: int(x.replace("d", ""))) 


# df_sorted = df.sort_values(by="days_ago", ascending=False)

# plt.figure(figsize=(10, 5))
# sns.lineplot(x=df_sorted["days_ago"], y=df_sorted["likes"], marker="o", label="Likes", color="blue")
# sns.lineplot(x=df_sorted["days_ago"], y=df_sorted["comments"], marker="o", label="Comments", color="green")
# sns.lineplot(x=df_sorted["days_ago"], y=df_sorted["reposts"], marker="o", label="Reposts", color="red")

# plt.gca().invert_xaxis()  
# plt.xlabel("Days Ago")
# plt.ylabel("Engagement Count")
# plt.title("Time-Based Engagement Trends")
# plt.legend()
# plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import numpy as np

data = [
    {"headline": "Top 5 Indian Women Cricketers Who Are Inspiring the Next Generation of Girls", "entities": {'CARDINAL': '5'}, "vader": 0.5574, "textblob": 0.3333, "source": "Cricket Insights", "likes": 120, "comments": 35, "reposts": 5, "time": "4d"},
    {"headline": "The Daily Cricket Digest - Why do Indian stars need a 150 kg baggage allowance?!", "entities": {'ORG': 'The Daily Cricket Digest - Why', 'NORP': 'Indian', 'QUANTITY': 'a 150 kg'}, "vader": 0.0, "textblob": 0.0, "source": "Cricket Buzz", "likes": 90, "comments": 25, "reposts": 3, "time": "3d"},
    {"headline": "Jay Shah's Role in Transforming Indian Cricket", "entities": {'PERSON': "Jay Shah's"}, "vader": 0.0, "textblob": 0.0, "source": "Sports Today", "likes": 80, "comments": 20, "reposts": 2, "time": "2d"},
    {"headline": "Women’s T20 World Cup 2024: 6 Indian Women Players to Watch For", "entities": {'ORG': 'Women’s T20 World Cup 2024', 'CARDINAL': '6', 'NORP': 'Indian'}, "vader": 0.0, "textblob": 0.0, "source": "Cricket Times", "likes": 200, "comments": 50, "reposts": 8, "time": "1d"},
    {"headline": "Beyond Cricket: Yuvraj Singh’s Inspiring Story of Hope and Strength", "entities": {'PERSON': 'Yuvraj Singh’s'}, "vader": 0.836, "textblob": 0.5, "source": "Sports India", "likes": 220, "comments": 60, "reposts": 15, "time": "5d"}
]

df = pd.DataFrame(data)

def categorize_sentiment(vader_score):
    if vader_score > 0.2:
        return "Positive"
    elif vader_score < -0.2:
        return "Negative"
    else:
        return "Neutral"

df["sentiment_category"] = df["vader"].apply(categorize_sentiment)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sentiment_counts = df["sentiment_category"].value_counts()
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'], startangle=90)
plt.title("Sentiment Distribution")

plt.subplot(1, 2, 2)
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette=['#ff6666','#6699ff','#66ff66'])
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.title("Sentiment Count")

plt.tight_layout()
plt.show()

entity_list = []
for row in df["entities"]:
    entity_list.extend(row.values())

entity_counts = Counter(entity_list)
top_entities = entity_counts.most_common(10)

wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(entity_counts)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Mentioned Players & Teams")

plt.subplot(1, 2, 2)
sns.barplot(x=[e[0] for e in top_entities], y=[e[1] for e in top_entities], palette="coolwarm")
plt.xticks(rotation=45)
plt.xlabel("Players/Teams")
plt.ylabel("Mentions")
plt.title("Top Mentioned Entities")

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
engagement_metrics = df.groupby("source")[["likes", "comments", "reposts"]].sum()

engagement_metrics.plot(kind="bar", figsize=(10, 5), colormap="Spectral")
plt.xlabel("News Source")
plt.ylabel("Engagement Count")
plt.title("Engagement Metrics by Source")
plt.xticks(rotation=45)
plt.legend(title="Engagement Type")
plt.show()

df["days_ago"] = df["time"].apply(lambda x: int(x.replace("d", "")))

df_sorted = df.sort_values(by="days_ago", ascending=False)

plt.figure(figsize=(10, 5))
sns.lineplot(x=df_sorted["days_ago"], y=df_sorted["likes"], marker="o", label="Likes", color="#ffcc00")
sns.lineplot(x=df_sorted["days_ago"], y=df_sorted["comments"], marker="o", label="Comments", color="#ff6699")
sns.lineplot(x=df_sorted["days_ago"], y=df_sorted["reposts"], marker="o", label="Reposts", color="#3399ff")

plt.gca().invert_xaxis()
plt.xlabel("Days Ago")
plt.ylabel("Engagement Count")
plt.title("Time-Based Engagement Trends")
plt.legend()
plt.show()
