

from get_datapoints import purpose, personal_pronouns, emotion_type, persuasion_techniques
import matplotlib.pyplot as plt
from collections import Counter


# Importing Counter from collections module to count occurrences of each emotion type
counts = Counter(emotion_type)

# Unpacking items from the Counter dictionary into separate lists for labels and values
labels, values = zip(*counts.items())

# Creating a new figure with a specific size for the bar plot
plt.figure(figsize=(10, 6))

# Some configurations
plt.bar(labels, values, color='skyblue')
plt.xlabel('Emotion Type')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()

plt.show()


# I exceeded my rate limit with the call that I used so the workaround is just to use set notation 

# unique_items = list(set(purpose))
# counts = Counter(unique_items)

# plt.bar(unique_items, counts)
# plt.xlabel('Unique Items')
# plt.ylabel('Counts')
# plt.title('Counts of Unique Items')
# plt.show()