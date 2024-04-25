import pandas as pd
import numpy as np
import seaborn as sns
import re 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from get_datapoints import mentioned_entities
from get_datapoints import purpose, personal_pronouns, emotion_type, persuasion_techniques

# create some different visuals to draw some conclusions 
df = pd.read_csv('/Users/test/Desktop/openai-env/project/tweets_processed_using_gpt.csv')

# split up tweets by their political orientation 
left_leaning_tweets = df.loc[df['Emotion_Type'] == 'Left-leaning']
right_leaning_tweets = df.loc[df['Emotion_Type'] == 'Right-leaning']


# easily analyze prominent topics just from viewing word cloud 
word_cloud_leftleaning = left_leaning_tweets['Topic']
word_cloud_rightleaning = right_leaning_tweets['Topic']
# subtopic = df.iloc[:, 2].values
subtopic = df['Subtopic']
purpose = df['Purpose']

# keywords is incorrectly named emojis for some reason so we have to get the emojis column 
# Convert 'Emojis' column to string type and handle missing values
df['Emojis'] = df['Emojis'].astype(str)
keywords = df['Emojis'].values

#same issue with hashtags...categorized as mentioned_entities
df['Mentioned_Entities'] = df['Mentioned_Entities'].astype(str)
hashtags = df['Mentioned_Entities'].values




# setup wordclouds for political orientation categories
# this shows the tweet bodies for each political orientation 
wordcloud1 = WordCloud(background_color='white').generate(' '.join(word_cloud_leftleaning))
wordcloud2 = WordCloud(background_color='white').generate(' '.join(word_cloud_rightleaning))
subtopic_wordcloud = WordCloud(background_color='white').generate(' '.join(subtopic))
purpose_wordcloud = WordCloud(background_color='white').generate(' '.join(purpose))
keywords_wordcloud = WordCloud(background_color='white').generate(' '.join(keywords))
hashtags_wordcloud = WordCloud(background_color='white').generate(' '.join(hashtags))
entities_wordcloud = WordCloud(background_color='white').generate(' '.join(mentioned_entities))
emotion_type_wc = WordCloud(background_color='white').generate(' '.join(emotion_type))
personal_pronouns_wc = WordCloud(background_color='white').generate(' '.join(personal_pronouns))
persuasion_techniques_wc = WordCloud(background_color='white').generate(' '.join(persuasion_techniques))



plt.imshow(emotion_type_wc, interpolation='bilinear') # interchange depending on which word cloud you want to see
plt.axis("off")
plt.show()




'''

(PART 2) - GPT integration 
Purpose (listed under persuasion_techniques)
Persuasion techniques (listed under call_to_action)
Bias (listed under subjectivity) 
subjectivity (listed under sentiment)
sentiment (listed under emotional_intensity)
emotional intensity (listed under informality)
informality (listed under personal_pronouns)
Personal_pronouns (listed under persuasiveness)
persuasiveness (listed under fact_vs_opinion)
fact_vs. opinion (listed under political_orientation)
emotion_type (listed under time_reference)
authenticity (listed under theme)

We want to generalize these using gpt4 so that we can get a more conclusive look at the different amount in a bar graph 

leaving out: 
-time reference (listed under directness)
-directness (listed under clarity)
-clarity (listed under tone)
-tone (listed under device usage)
-device usage (listed under style)
-style (listed under technique)
-technique (listed under authenticity)

because there are many missing values in these columns and the ones that are there don't differ that much 
we wouldn't really be getting any insightful visualizations from them 

(PART 3)
find creative ways to visualize: 
Linked_urls (listed under bias) 
Mentioned_entities (under linked_urls)

(PART 4)
If time allows, find a way to compare these: 

persuasiveness (listed under fact_vs_opinion)
fact_vs. opinion (listed under political_orientation)
emotion_type (listed under time_reference)
authenticity (listed under theme)

-doesn't have to be all at once
-something like get the count where persuasiveness = 'x' and factvsopinion = 'y' and plot those counts 

'''


# generalize the subtopics to get more intuititive data
# # print('num rows in subtopic col: ', len(right_leaning_tweets['Subtopic']))
# # print('num unique columns: ', len(get_set))

# get_set = set(right_leaning_tweets['Subtopic'])


# response = client.chat.completions.create(
#         model='gpt-4',
#         messages= [
#             {"role": "user", "content": f"break the contents of ${get_set} up into 10 different categories that I can classify my tweets into "}
#         ],
#         # max_tokens= 100
#     )
    
#     #completion.choices[0].message
# result = response.choices[0].message.content
# print(result)
   
# def process_lines(): 
#     categories = []
#     with open("/Users/test/Desktop/openai-env/project/categories_generated_by_gpt4.txt") as f: 
#         lines = f.readlines()

#         for j in range(1, len(lines)):
#             line = lines[j]
#             # now we need to do some regex 
#             # we only need to get the lines that start with an integer 
#             x = re.search("\A[0-1][0-9]",line)
#             if x: # if it's one of the lines to compare to 
#                 # do stuff 
#                 categories.append(line)

#     return categories 
                

# # map each tweet into each category 
# categories = process_lines()
# for index, subtopic  in enumerate(right_leaning_tweets['Subtopic']):
#     # print('index',index)
#     # print('subtopic',subtopic)

#     response = client.chat.completions.create(
#         model='gpt-4',
#         messages= [
#             {"role": "user", "content": f"map ${subtopic} into the one of these: ${categories}"}
#         ],
#          max_tokens= 50
#     )

#     result = response.choices[0].message.content
#     print("#",index,' ...  ',result)
    
    

    

    

    


# # with open("Presidential_Debate.txt", "rt") as f: 
# #     lines = f.readlines()
# #     
# #     for i in range(1, len(lines)):
# #         line = lines[i]
# #         suffix = lines[i-1][-5:] # last 4 characters of preceding line
# #         if is_integer(suffix) and int(suffix) / 2 == 1010 and not is_integer(line): 
# #             # get timestamp line
# #             time = lines[i-1].split(" ")[:4]
# #             minutes = time[-1]

# #             if re.search("\d{2}:\d{2}:\d{2}", minutes) != None:
# #                 if minutes in highlights: 
# #                     highlights[minutes] += 1
# #                 else: 
# #                     highlights[minutes] = 1
            
 



# # right_leaning_tweets['Subtopic'].value_counts().plot(ax=ax, kind='bar', xlabel='Tweet Subtopic', ylabel='frequency')

# # plt.show()

