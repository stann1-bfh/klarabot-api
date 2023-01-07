import yaml
import sys
import nlpaug.augmenter.word as naw
from textblob import TextBlob
from tqdm import tqdm

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
def createVariations(sentence: str, randomness: int, iterations: int):
    # 10% Chance to create a Synonym of a word
    syn_aug = naw.SynonymAug(aug_p=randomness)
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

# Create Variations of Conversations in a YAML-Dataset
def dataAugmentation(completeDataSet: list):
    newConv = []
    counter = 1
    for set in tqdm(completeDataSet, desc="All Datasets", position=0, colour='#BE88FF'):
        #Setup the Progressbar
        currentCount = "Dataset " + str(counter)
        # Translate German Sentences to be able to create variations
        initialQuestion = toEnglish(set[0])
        answerToBeMappedTo = toEnglish(set[1])
        # Create Variations using the translated sentences
        variations = createVariations(initialQuestion, variationChange, numberOfVariations)
        for variation in tqdm(variations, desc=currentCount, colour='green'):
            newSet = []
            newSet.append(toGerman(variation))
            newSet.append(toGerman(answerToBeMappedTo))
            newConv.append(newSet)
        counter = counter + 1
    return newConv

if __name__ == '__main__':
    # Setup Constants
    file_name = str(sys.argv[1])
    variationChange = float(sys.argv[2])
    numberOfVariations = int(sys.argv[3])
    file_path = "training_data/" + file_name
    dataset = openDataset(file_path)
    data = extractConversations(dataset)

    # Add Processed Data to new dictionary to be saved
    newDataSet = dict(
        categories = dataset.get('categories'),
        conversations = dataAugmentation(data)
    )
    # Save new processed Dataset
    saveToYAMLFile(newDataSet)