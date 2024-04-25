
import pandas as pd


df = pd.read_csv('/Users/test/Desktop/openai-env/project/tweets_processed_using_gpt.csv')

# step 1: Gather all relevant info 

# 1: tweet purpose 
df['Persuasion_Techniques'] = df['Persuasion_Techniques'].astype(str)
purpose = df['Persuasion_Techniques'].values

# 2: persuasion techniques
df['Call_to_Action'] = df['Call_to_Action'].astype(str)
persuasion_techniques = df['Call_to_Action'].values

# 3: bias
df['Subjectivity'] = df['Subjectivity'].astype(str)
bias = df['Subjectivity'].values

# 4: subjectivity
df['Sentiment'] = df['Sentiment'].astype(str)
subjectivity = df['Sentiment'].values

# 5: sentiment 
df['Emotional_Intensity'] = df['Emotional_Intensity'].astype(str)
sentiment = df['Emotional_Intensity'].values

# 6: emotional intensity 
df['Informality'] = df['Informality'].astype(str)
emotional_intensity = df['Informality'].values

# 7: informality 
df['Personal_Pronouns'] = df['Personal_Pronouns'].astype(str)
informality = df['Personal_Pronouns'].values

# 8: personal pronouns 
df['Persuasiveness'] = df['Persuasiveness'].astype(str)
personal_pronouns = df['Persuasiveness'].values

# 9: persuasiveness
df['Factual_vs_Opinion'] = df['Factual_vs_Opinion'].astype(str)
persuasivness = df['Factual_vs_Opinion'].values

# 10: fact v opinion 
df['Political_Orientation'] = df['Political_Orientation'].astype(str)
fact_v_opinion = df['Political_Orientation'].values

# 11: emotion type 
df['Time_Reference'] = df['Time_Reference'].astype(str)
emotion_type = df['Time_Reference'].values

# 12: authenticity
df['Theme'] = df['Theme'].astype(str)
authenticity = df['Theme'].values

# 13: mentioned entities
df['Linked_URLs'] = df['Linked_URLs'].astype(str)
mentioned_entities = df['Linked_URLs'].values



purpose_cats = [
  "Expressing Feelings",
  "Informing",
  "Persuading",
  "Expressing Opinion",
  "Expressing Gratitude",
  "Criticizing",
  "Expressing Dissatisfaction",
  "Narrating an Event",
  "Advocacy for Causes/Raise Awareness",
  "Expressing Support",
  "Motivating",
  "Promoting",
  "Sharing Resources",
  "Commemorating",
  "Questioning",
  "Provoking Thought/Discussion",
  "Highlighting Issues",
  "Selling",
  "Seeking Help",
  "Expressing Condolences"
]

personal_pronouns_cats = [
  "First Person Singular (Example: I, Me, My, Myself)",
  "First Person Plural (We, Our, Us)",
  "Second Person (You, Your, Yours)",
  "Third Person Singular (He, She, It, His, Her, Its)",
  "Third Person Plural (They, Their, Them)",
  "Mixed Person (First, Second, and/or Third person in one phrase)",
  "First and Second Person Mixed",
  "First and Third Person Mixed",
  "Second and Third Person Mixed",
  "First, Second, and Third Person Singular Mixed",
  "First, Second, and Third Person Plural Mixed",
  "First Person Singular and Plural Mixed",
  "Second Person Singular and Plural Mixed",
  "Third Person Singular and Plural Mixed",
  "Not Applicable (Phrases that do not involve First, Second, or Third person)",
  "Indefinite (Nouns or pronouns without specified gender or number)",
  "Personal Names (Identified individuals)",
  "Inclusive Phrases (Includes the listener)",
  "Exclusive Phrases (Excludes the listener)",
  "Other (Anything that doesn't fit in the above categories)"
]

emotion_type_cats = ['Anger',
'Anticipation',
'Joy',
'Gratitude',
'Neutral',
'Love',
'Stress',
'Sadness',
'Surprise',
'Disgust',
'Fear',
'Appreciation',
'Confusion',
'Admiration',
'Unknown',
'Mixed',
'Stress',
'Fear',
'Love',
'Anticipation'
]

persuasion_techniques_cats = [
  "Appeal to Emotion",
  "Appeal to Authority",
  "Use of Anecdotal Evidence",
  "Name-calling and Stereotyping",
  "Repeated Messaging and Use of Hashtags",
  "Direct Challenge and Criticism",
  "Appeal to Emotion with Insults/Attacks",
  "Use of Humor",
  "Use of Rhetorical Questions",
  "Use of Loaded Language",
  "Appeal to Solidarity/Unity",
  "Appeal to Fairness/Justice",
  "Use of Scarcity",
  "Use of Contrast",
  "Use of Storytelling",
  "Bandwagon Appeal",
  "Appeal to Ethical Values/Responsibility",
  "Appeals with Elements of Irony/Sarcasm",
  "Use of Quotations",
  "Unknown/Not Applicable/Unused entries"
]
