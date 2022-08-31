"""
VIRTUAL ENVIRONMENT
-------------------
OPTIONAL:

```
python3 -m venv cogsrv-vision-env
source cogsrv-vision-env/bin/activate
```

INSTALLATION
------------
```
pip install azure-cognitiveservices-vision-computervision
```

RESOURCES
---------
[PyPi](https://pypi.org/project/azure-cognitiveservices-vision-computervision/)

[GitHub](https://github.com/Azure/azure-sdk-for-python)

[Azure Cognitive Services Computer Vision SDK for Python](https://docs.microsoft.com/en-us/python/api/overview/azure/cognitiveservices-vision-computervision-readme?view=azure-python)

[`computervision` Package](https://docs.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-computervision/azure.cognitiveservices.vision.computervision?view=azure-python)

[Parameters for `analyze_image()`](https://docs.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-computervision/azure.cognitiveservices.vision.computervision.operations.computervisionclientoperationsmixin?view=azure-python#azure-cognitiveservices-vision-computervision-operations-computervisionclientoperationsmixin-analyze-image)

[`VisualFeatureTypes`](https://docs.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-computervision/azure.cognitiveservices.vision.computervision.models.visualfeaturetypes?view=azure-python)

[DetectedObject Class (for Java)](https://docs.microsoft.com/en-us/java/api/com.microsoft.azure.cognitiveservices.vision.computervision.models.detectedobject?view=azure-java-legacy)

"""

# # # ### ----- WARNING ----- ### # # #
# # # KEY information should NOT  # # #
# # # be saved inside a file.     # # #
# # # A better practice is to     # # #
# # # save keys as an environment # # #
# # # variable on the local OS    # # #
# # # environment or container.   # # #
# # # ### ---- /WARNING ----- ### # # #
key = "YOUR_KEY"
ACCOUNT_REGION = 'YOUR_REGION' # 'eastus2'
ENDPOINT = f'https://{ACCOUNT_REGION}.api.cognitive.microsoft.com/'

# # For using your `key` to get credentials
from msrest.authentication import CognitiveServicesCredentials
# # Connects to ComputerVision Cognitive Service, associated with your `key`
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
# # Defines what types of Visual Features to collect from analysis
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
# # For getting command line arguments
import sys

# # Set default for `img_file`
# # Update `img_file` if CLI arg is found in `img_list`
args = sys.argv[1:]
img_file = 'store-camera-1.jpg'
img_list = ["store-camera-1.jpg", "store-camera-2.jpg", "store-camera-3.jpg", "store-camera-4.jpg"]
if len(args) > 0 and args[0] in img_list:
    img_file = args[0]

# # Append `img_file` to Microsoft Learning URL where images are located
img = f'https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/vision/{img_file}'

# # Connect to Computer Vision service
credentials = CognitiveServicesCredentials(key)
client = ComputerVisionClient(endpoint=ENDPOINT, credentials=credentials)

# # Code to call Computer Vision image analysis
print('Analyzing image...')
viz_features = [
    VisualFeatureTypes.description, 
    VisualFeatureTypes.objects, 
#     VisualFeatureTypes.image_type,
#     VisualFeatureTypes.faces,
#     VisualFeatureTypes.categories,
#     VisualFeatureTypes.color,
    VisualFeatureTypes.tags
]
analysis = client.analyze_image(img, visual_features=viz_features)


# # Print descriptive analysis results to console
print('\nDescription:')
for caption in analysis.description.captions:
    print(caption.text)

print('\nObjects in this image:')
for analysis_object in analysis.objects:
    print(f' - {analysis_object.object_property}')

print('\nTags relevant to this image:')
for tag in analysis.description.tags:
    print(f' - {tag}')

print('\n')
