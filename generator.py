import yaml
import nlpaug.augmenter.word as naw
from textblob import TextBlob

# Extract the conversation strings from the YAML DataStructure
def extractConversations(data):
    
    conversations = []
    for conversation in data['conversations']:
        conversations.append(conversation)
    return conversations

# Safe Variations in new  Processed File
def saveToYAMLFile(dataStructure):
    with open("processed_training_data/" + file_name, 'w', encoding='utf-8') as outfile:
        yaml.dump(dataStructure, outfile, default_flow_style=False, allow_unicode=True)

# Create variations of a given sentence
def createVariations(sentence: str, iterations: int):
    # 10% Chance to create a Synonym of a word
    syn_aug = naw.SynonymAug(aug_p=0.1)
    return syn_aug.augment(sentence, n=iterations)

# Translate the string from German to English
def toEnglish(sentence: str):
    return TextBlob(sentence).translate(from_lang='de', to='en').string

# Translate the string from English to German
def toGerman(sentence: str):
    return TextBlob(sentence).translate(from_lang='en', to='de').string

# Open the YAML-Dataset for the Chatbot Use Case
def openDataset(file_path: str):
    # Load the YAML dataset
    with open(file_path, encoding='utf-8') as f:
        return yaml.safe_load(f)

if __name__ == '__main__':
    file_name = "training_data_papr001.yaml"
    file_path = "training_data/" + file_name
    dataset = openDataset(file_path)
    data = extractConversations(dataset)
    saveToYAMLFile(dataset)

    # TODO Refactor the variation Loop
    newConv = []
    for set in data:
        initialQuestion = toEnglish(set[0])
        answerToBeMappedTo = toEnglish(set[1])
        variations = createVariations(initialQuestion, 25)
        for variation in variations:
            newSet = []
            newSet.append(answerToBeMappedTo)
            newSet.append(toGerman(variation))
            newConv.append(newSet)

    newDataSet = dict(
        categories=dataset.get('categories'),
        conversations=newConv
    )
    saveToYAMLFile(newDataSet)