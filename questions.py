# create questions as a json file 
import json 

questions_data = {
    "questions": [
        {"question": "Does the text follow a linear narrative structure?"},
        {"question": "Does the text follow a non-linear narrative structure?"},
        {"question": "Does the text follow a circular narrative structure, the story ends where it began?"},
        {"question": "Does the text have a multiple storyline narrative structure?"},
        {"question": "Does the text have subplot threads interwoven into the main narrative?"},
        {"question": "Is the text organized into a standard three act structure (beginning, middle, end)?"},
        {"question": "Is the theme of good vs evil explored in this text?"},
        {"question": "Is the theme of love explored in this text?"},
        {"question": "Is the theme of family explored in this text?"},
        {"question": "Is the theme of loneliness explored in this text?"},
        {"question": "Is the theme of revenge explored in this text?"},
        {"question": "Is the theme of identity and self exploration explored in this text?"},
        {"question": "Is the theme of social and political issues explored in this text?"},
        {"question": "Is the theme of power and corruption explored in this text?"},
        {"question": "Is the theme of loss and grief explored in this text?"},
        {"question": "Is the theme of nature and environment explored in this text?"},
        {"question": "Are there repeating thematic patterns or symbols in the text?"},
        {"question": "Is there one clear main character in the text?"},
        {"question": "Are there multiple side characters that are important to the plot?"},
        {"question": "Is there a clear antagonist character in the text?"},
        {"question": "Is the protagonists main goal/desire one that is moral?"},
        {"question": "Does the main character undergo character growth?"},
        {"question": "Is the authors primary message of this text to entertain?"},
        {"question": "Is the authors primary message of this text to inform?"},
        {"question": "Is the authors primary message of this text to persuade?"},
        {"question": "Is the authors primary message of this text to critique?"},
        {"question": "Is the authors primarily aiming to evoke positive emotions with this text?"},
        {"question": "Is the authors primarily aiming to evoke negative emotions with this text?"},
        {"question": "Is the authors primarily aiming to evoke thought provoking emotions with this text?"},
        {"question": "Is the authors primarily aiming to evoke contradictory emotions with this text?"},
        {"question": "Does the story in the text involve many different settings?"},
        {"question": "How integral is the setting seem to the story based on the text?"},
        {"question": "Does the story take place in modern society?"},
        {"question": "Does the story take place in a fantasy world?"},
        {"question": "Does the story take place in a historical setting?"},
        {"question": "Does the story in this text suggest adherence to the genre of Action?"},
        {"question": "Does the story in this text suggest adherence to the genre of Adventure?"},
        {"question": "Does the story in this text suggest adherence to the genre of Comedy?"},
        {"question": "Does the story in this text suggest adherence to the genre of Drama?"},
        {"question": "Does the story in this text suggest adherence to the genre of Fantasy?"},
        {"question": "Does the story in this text suggest adherence to the genre of Science Fiction?"},
        {"question": "Does the story in this text suggest adherence to the genre of Thriller?"},
        {"question": "Does the story in this text suggest adherence to the genre of Horror?"},
        {"question": "Does the story in this text suggest adherence to the genre of Romance?"},
        {"question": "Does the story in this text suggest adherence to the genre of Crime & Mystery?"},
        {"question": "Is the plot of this text predictable?"},
        {"question": "Does the text contain a major twist?"},
        {"question": "Does the text contain a central conflict?"},
        {"question": "Is the plot of this text engaging?"},
        {"question": "Does the plot of the text come to a satisfying resolution?"},
        {"question": "Does the plot end in a cliffhanger?"},
        {"question": "Is the target audience for this text Children/Teens?"},
        {"question": "Is the target audience for this text Young Adults?"},
        {"question": "Is the target audience for this text Middle Age Adults?"},
        {"question": "Is the target audience for this text the Elderly?"},
        {"question": "Does the text engage diverse demographic or cultural groups?"},
        {"question": "After reading this text are you in a positive mood?"},
        {"question": "After reading this text are you in a negative mood?"}
    ]
}

# Save to a JSON file
with open("questions.json", "w") as file:
    json.dump(questions_data, file, indent=4)

print("JSON file created successfully!")