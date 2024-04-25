import pandas as pd
from openai import OpenAI
import matplotlib.pyplot as plt
from collections import Counter
import re

from get_datapoints import purpose,persuasion_techniques,bias,subjectivity,sentiment,emotional_intensity, informality,personal_pronouns,persuasivness,fact_v_opinion,emotion_type,authenticity

print(purpose)


client = OpenAI()

df = pd.read_csv('/Users/test/Desktop/openai-env/project/tweets_processed_using_gpt.csv')

# add all array into its own object so that we don't have to repeat a ton of code 
factors = [purpose,persuasion_techniques,bias,subjectivity,sentiment,emotional_intensity,
    informality,personal_pronouns,persuasivness,fact_v_opinion,emotion_type,authenticity]



# Compare the length of each array with its respective set to see how many unique columns there are
for factor in factors:
    factor_name = [name for name, value in locals().items() if value is factor][0]
    # print('factor name: ', factor_name)
    num_rows = len(factor)
    num_unique_rows = len(set(factor))

    # print('num rows: ', num_rows)
    # print('num unique columns: ', num_unique_rows)






def get_categories(column_name): 
    # we can clean this up using GPT4: 
    response = client.chat.completions.create(
            model='gpt-4',
            messages= [
                {"role": "user", "content": f"break the contents of ${column_name} up into 20 different categories that I can classify my tweets into"}
                # 20 categories for now...trying more or less will be a good experiment if time allows
            ],
            # max_tokens= 100
        )
        
        #completion.choices[0].message
    result = response.choices[0].message.content
    return result 



# we will just write each run into a file and then manually create our categories array since GPT is random by nature
# and processing the result using regular expression will give us unwarranted results 
# now that we know all of this we can use string interpolation to automate this with a for loop, 
# therefore creating minimized category files for all of our factors in this section 

for factor in factors: 
    results = get_categories(factor) # runs gpt categorization 
    factor_name = [name for name, value in locals().items() if value is factor][0]

    

    with open(f'{factor_name}_minimized_cats', "w") as file1: # writes results for that factor into its own file! (hopefully)
        # Writing data to a file
        file1.write("Hello \n")
        file1.writelines(results)

    


# this was a success! but we will not run that loop again because it was very computationally expensive 





















