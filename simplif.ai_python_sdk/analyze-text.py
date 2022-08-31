"""
VIRTUAL ENVIRONMENT
-------------------
OPTIONAL:

```
python3 -m venv cogsrv-textanalytics-env
source cogsrv-textanalytics-env/bin/activate
```

INSTALLATION
------------
```
pip install azure-ai-textanalytics
```

RESOURCES
---------
[PyPi](https://pypi.org/project/azure-cognitiveservices-language-textanalytics/)

[GitHub](https://github.com/Azure/azure-sdk-for-python)

[Azure Text Analytics client library for Python](https://docs.microsoft.com/en-us/python/api/overview/azure/ai-textanalytics-readme?source=recommendations&view=azure-python)

"""

# # # ### ----- WARNING ----- ### # # #
# # # KEY information should NOT  # # #
# # # be saved inside a file.     # # #
# # # A better practice is to     # # #
# # # save keys as an environment # # #
# # # variable on the local OS    # # #
# # # environment or container.   # # #
# # # ### ---- /WARNING ----- ### # # #
key = 'YOUR_KEY'
ACCOUNT_REGION = 'YOUR_REGION' # 'eastus2'
ENDPOINT = f'https://{ACCOUNT_REGION}.api.cognitive.microsoft.com/'

# # For using your `key` to get credentials
from azure.core.credentials import AzureKeyCredential
# # Connects to ComputerVision Cognitive Service, associated with your `key`
# from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from azure.ai.textanalytics import TextAnalyticsClient
# # For getting command line arguments
import sys
import requests

args = sys.argv[1:]
txt_file = "review1.txt"
txt_list = ["review1.txt", "review2.txt", "review3.txt", "review4.txt"]
if len(args) > 0 and args[0] in txt_list:
    txt_file = args[0]
url = f'https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/text/reviews/{txt_file}'

response = requests.get(url)
documents = [response.text]

# # Connect to Text Analytics service
# # NOTE: This is slightly different from Computer Vision
credentials = AzureKeyCredential(key)
text_analytics_client = TextAnalyticsClient(endpoint=ENDPOINT, credential=credentials)


# Language Detection
print("***Detecting Language***")
response = text_analytics_client.detect_language(documents)
result = [doc for doc in response if not doc.is_error]

langName = None
langCode = None
langScore = None
for doc in result:
    langName = doc.primary_language.name
    langCode = doc.primary_language.iso6391_name
    langScore = doc.primary_language.confidence_score
    print(f"  - Language: {langName}")
    print(f"  - Code:     {langCode}")
    print(f"  - Score:    {langScore}")


# Key Phrases
print("\n\n***Finding Key Phrases***")
response = text_analytics_client.extract_key_phrases(documents, language=langCode)
result = [doc for doc in response if not doc.is_error]
for doc in result:
    print("  - Key Phrases: ")
    for key_phrase in doc.key_phrases:
        print(f"    {key_phrase}")


# Sentiment
print("\n\n***Analyzing Sentiment***")
response = text_analytics_client.analyze_sentiment(documents, language=langCode)
result = [doc for doc in response if not doc.is_error]

for doc in result:
    sentiment = doc.sentiment
    positive = doc.confidence_scores.positive
    neutral = doc.confidence_scores.neutral
    negative = doc.confidence_scores.negative
    print(f"  - A {sentiment} sentiment based on these scores:")
    print(f"    - Positive: {positive}")
    print(f"    - Neutral:  {neutral}")
    print(f"    - Negative: {negative}")


# Known Entities
print("\n\n***Identifying known entities***")
response = text_analytics_client.recognize_linked_entities(documents, language=langCode)
result = [doc for doc in response if not doc.is_error]

for doc in result:
    for entity in doc.entities:
        print(f"  - {entity.name} : {entity.url}")


