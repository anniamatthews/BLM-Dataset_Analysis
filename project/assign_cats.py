import pandas as pd
from openai import OpenAI
from get_datapoints import purpose, personal_pronouns, emotion_type, persuasion_techniques
from get_datapoints import purpose_cats, personal_pronouns_cats, emotion_type_cats, persuasion_techniques_cats
client = OpenAI()
df = pd.read_csv('/Users/test/Desktop/openai-env/project/tweets_processed_using_gpt.csv')


# minimize purpose 
assigned_cats_purpose = []
for index, line  in enumerate(purpose):
    # print('index',index)
    # print('subtopic',subtopic)

    response = client.chat.completions.create(
        model='gpt-4',
        messages= [
            {"role": "user", "content": f"map ${line} into the one of these: ${purpose_cats}"}
        ],
         
    )

    result = response.choices[0].message.content
    # print("#",index,' ...  ',result)
    assigned_cats_purpose.append(result)
    if index == 5: 
        break
    




# minimize personal_pronouns 
assigned_cats_personal_pronouns = []
for index, line  in enumerate(personal_pronouns):
    # print('index',index)
    # print('subtopic',subtopic)

    response = client.chat.completions.create(
        model='gpt-4',
        messages= [
            {"role": "user", "content": f"map ${line} into the one of these: ${personal_pronouns_cats}"}
        ],
        
    )

    result = response.choices[0].message.content
    # print("#",index,' ...  ',result)
    assigned_cats_personal_pronouns.append(result)

    if index == 5: 
        break
    


# minimize emotion_type 
assigned_cats_emotion_type = []
for index, line  in enumerate(emotion_type):
    # print('index',index)
    # print('subtopic',subtopic)

    response = client.chat.completions.create(
        model='gpt-4',
        messages= [
            {"role": "user", "content": f"map ${line} into the one of these: ${emotion_type_cats}"}
        ],
        
    )

    result = response.choices[0].message.content
    # print("#",index,' ...  ',result)
    assigned_cats_emotion_type.append(result)

    if index == 5: 
        break


# minimize persuasion technique
assigned_cats_persuasion_techniques = []
for index, line  in enumerate(persuasion_techniques):
    # print('index',index)
    # print('subtopic',subtopic)

    response = client.chat.completions.create(
        model='gpt-4',
        messages= [
            {"role": "user", "content": f"map ${line} into the one of these: ${persuasion_techniques_cats}"}
        ],
        
    )

    result = response.choices[0].message.content
    # print("#",index,' ...  ',result)
    assigned_cats_persuasion_techniques.append(result)

    if index == 5: 
        break


# this code is going to take a long time to run so we will do it last 


with open('assigned_lists.txt', "w") as file1: # writes results for that factor into its own file! (hopefully)
        # Writing data to a file
        file1.write("Hello \n")
        file1.writelines(assigned_cats_emotion_type)
        file1.writelines(assigned_cats_personal_pronouns)
        file1.writelines(assigned_cats_persuasion_techniques)
        file1.writelines(assigned_cats_purpose)


# so we don't have to watch and wait....we can just come back to it 