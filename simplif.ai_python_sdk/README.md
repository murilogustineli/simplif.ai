# Azure Cognitive Services Python SDK
### Table of Contents

<details open>
<summary><a href="#overview">Overview</a></summary>
<ul>
	<li><a href="#a-few-things-that-should-be-done-beforehand">A few things that should be done beforehand</a></li>
	<li><a href="#adapted-from">Adapted From</a></li>
	<li><a href="#videos-and-resources">Videos and Resources</a></li>
	<li><a href="#what-to-do-after">What to do after</a></li>
</ul>
</details>

<details open>
<summary><a href="#computer-vision">Computer Vision</a></summary>
<ul>
	<li><a href="#computer-vision-setup">Setup</a></li>
	<li><a href="#computer-vision-steps">Steps</a></li>
	<li><a href="#computer-vision-code">Code</a></li>
	<li><a href="#computer-vision-exercises">Exercises</a></li>
	<ul>
		<li><a href="#store-camera-1jpg">store-camera-1.jpg</a></li>
		<li><a href="#store-camera-2jpg">store-camera-2.jpg</a></li>
		<li><a href="#store-camera-3jpg">store-camera-3.jpg</a></li>
		<li><a href="#store-camera-4jpg">store-camera-4.jpg</a></li>
	</ul>
	<li><a href="#computer-vision-resources">Resources</a></li>
</ul>
</details>

<details open>
<summary><a href="#natural-language-processing">Natural Language Processing</a></summary>
<ul>
	<li><a href="#nlp-setup">Setup</a></li>
	<li><a href="#nlp-steps">Steps</a></li>
	<li><a href="#nlp-code">Code</a></li>
	<li><a href="#nlp-exercises">Exercises</a></li>
	<ul>
		<li><a href="#review1txt">review1.txt</a></li>
		<li><a href="#review2txt">review2.txt</a></li>
		<li><a href="#review3txt">review3.txt</a></li>
		<li><a href="#review4txt">review4.txt</a></li>
	</ul>
	<li><a href="#nlp-resources">Resources</a></li>
</ul>
</details>


---
## Overview

### *A few things that should be done beforehand*
<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

 * <div title="Either of the links below under 'Adapted From' can be used to follow the directions under the heading 'Create a Cognitive Services resource'.">Setup Azure Cognitive Services<sup>1</sup></div>
 * Open Azure Cloud Shell. 
 * Setup Cloud Shell, i.e., mount to storage. *If Cloud Shell is already setup, skip this step.*
 * Switch to the Bash shell. *If you are already in the Bash shell, skip this step.*
 * Navigate to the `clouddrive` directory, Run: 
	* `cd clouddrive`
 * <span title="Either of the links below under 'Adapted From' can be used to follow the directions under the heading 'Run Cloud Shell'.">Clone Microsofts AI-900 repo,<sup>2</sup></span> Run: 
	<ul><li><code>git clone https://github.com/MicrosoftLearning/AI-900-AIFundamentals ai-900</code></li></ul>
 * Open VS Code in the cloud shell, Run: `code .`
 
 > *NOTE: If you try running this code outside of the Cloud Shell, you will need to install the azure-core library, which can be installed using pip by running: <br>
 > `pip install azure-core` <br>
 > This setup should be using Python v3.9+*


### Adapted From
<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

 * [Analyze images with the Computer Vision service](https://docs.microsoft.com/en-us/learn/modules/analyze-images-computer-vision/3-analyze-images)
 * [Analyze text](https://docs.microsoft.com/en-us/learn/modules/analyze-text-with-text-analytics-service/3-exercise)

<div style=""><em>&nbsp;<sup>1</sup> Either of the above links can be used to follow the directions under the heading <strong>"Create a Cognitive Services resource"</strong>.</em><div>

<div style=""><em><sup>2</sup> Either of the above links can be used to follow the directions under the heading <strong>"Run Cloud Shell"</strong>.</em><div>


### Videos and Resources
<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

> __*NOTE: These resources are informative and are NOT needed to complete the exercises below*__

#### Videos
 * [CrashCourse: Computer Vision](https://www.youtube.com/watch?v=-4E2-0sxVUM)
 * [Intro to Azure SDK](https://www.youtube.com/watch?v=4xoJLCFP4_4) *(Quick and very broad overview from Microsoft, using Form Recognizer and Text Analytics)*
 * [Creating a Computer Vision resource](https://www.youtube.com/watch?v=k8z-RbIBh68)
	* This demo installs the Computer Vision resource. 
	* The computer vision exercise below uses the Cognitive Services resource.
	* Either are ok to use.
	* This demo also gives some good Exercises of the objects the computer vision model returns.

#### Resources
 * [Azure Cognitive Services SDK for Python: Microsoft Docs](https://docs.microsoft.com/en-us/python/api/overview/azure/cognitive-services?view=azure-python)
 * [Azure SDK for Python package releases](https://azure.github.io/azure-sdk/releases/latest/python.html)
 * [Azure SDK for Python: GitHub page](https://github.com/azure/azure-sdk-for-python/)


### What to do after
<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

After completing these exercises, it is recommended to look over the Python SDK Microsoft Documentation for [Computer Vision](https://docs.microsoft.com/en-us/python/api/overview/azure/cognitiveservices-vision-computervision-readme?view=azure-python) and [Text Analytics](https://docs.microsoft.com/en-us/python/api/overview/azure/ai-textanalytics-readme?source=recommendations&view=azure-python). 

Experimentation with each services' features is encouraged, even the ones that were not covered in the exercises.


Another resource you can use is the [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python) to look for more Exercises.



---
***

## Computer Vision


### Computer Vision Setup
<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

#### VIRTUAL ENVIRONMENT (_OPTIONAL_)
```
python3 -m venv cogsrv-vision-env
source cogsrv-vision-env/bin/activate
```

#### INSTALLATION
```
pip install azure-cognitiveservices-vision-computervision
```

---
### Computer Vision Steps
<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

1. If you have not already opened VS Code in the cloud shell, Run: `code .`

1. Switch to the Bash shell. *If you are already in the Bash shell, skip this step.*

1. In the Bash shell pane, enter the following commands to navigate inside the ai-900 folder:
	* `cd ai-900`

4. Create the file `analyze-image.py` by running the following code
	* `touch analyze-image.py`

1. In the Files pane on the left, expand ai-900 and select `analyze-image.py`. This file will be empty.

1. Paste the [code below](#computer-vision-code) into the new file, `analyze-image.py`.

1. Don't worry too much about the code, the important thing is that it needs the keys for your Cognitive Services resource. Copy the key from the Keys and Endpoints page for your resource from the [Azure portal](https://portal.azure.com) and paste it into the code editor, replacing the `YOUR_KEY` placeholder value.

1. In the [Azure portal](https://portal.azure.com), navigate back to your Cognitive Services resource page. The value for `ACCOUNT_REGION` can be found here, under "Location". The value should be altered so it is all lowercase and without spaces. 

1. After pasting the key and location values, the first two lines of code should look similar to this:
<ul><pre><code>key = "1a2b3c4d5e6f7g8h9i0j...."
ACCOUNT_REGION = 'eastus2'</code></pre></ul>

10. At the top right of the editor pane, use the ... button to open the menu and select Save to save your changes. <br> The sample client application will use your Computer Vision service to analyze the image found in [Exercise 1](#store-camera-1jpg)

1. In the Bash shell pane, enter the following commands to run the code:
	* `python analyze-image.py store-camera-1.jpg`

1. Review the results of the image analysis, which include:
	* A suggested caption that describes the image.
	* A list of objects identified in the image.
	* A list of "tags" that are relevant to the image.

1. Go ahead and try the other Exercises
	* [Exercise 2](#store-camera-2jpg) `python analyze-image.py store-camera-2.jpg`
	* [Exercise 3](#store-camera-3jpg) `python analyze-image.py store-camera-3.jpg`
	* [Exercise 4](#store-camera-4jpg) `python analyze-image.py store-camera-4.jpg`
<br>
<br>

*Adapted From [Analyze images with the Computer Vision service](https://docs.microsoft.com/en-us/learn/modules/analyze-images-computer-vision/3-analyze-images)*




---
### Computer Vision Code
<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

<details>
<summary style="font-weight:bold;color:#c00;"><em>View Code</em></summary>
<pre lang='python'><code>key = <span style="color:orange;">'YOUR_KEY'</span>
ACCOUNT_REGION = <span style="color:orange;">'YOUR_REGION'</span>
ENDPOINT = <span style="color:orange;">f'https://{ACCOUNT_REGION}.api.cognitive.microsoft.com/'</span>

<br>
<span style="color:blue;">from</span> msrest.authentication <span style="color:blue;">import</span> CognitiveServicesCredentials
<span style="color:blue;">from</span> azure.cognitiveservices.vision.computervision <span style="color:blue;">import</span> ComputerVisionClient
<span style="color:blue;">from</span> azure.cognitiveservices.vision.computervision.models <span style="color:blue;">import</span> VisualFeatureTypes
<span style="color:blue;">import</span> sys

<br>
args = sys.argv[<span style="color:green;">1</span>:]
img_file = <span style="color:orange;">'store-camera-1.jpg'</span>
img_list = [<span style="color:orange;">"store-camera-1.jpg"</span>, <span style="color:orange;">"store-camera-2.jpg"</span>, <span style="color:orange;">"store-camera-3.jpg"</span>, <span style="color:orange;">"store-camera-4.jpg"</span>]
<span style="color:blue;">if len</span>(args) > <span style="color:green;">0</span> and args[<span style="color:green;">0</span>] <span style="color:blue;">in</span> img_list:
&nbsp;&nbsp;&nbsp;&nbsp;img_file = args[<span style="color:green;">0</span>]
img = <span style="color:orange;">f'https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/vision/{img_file}'</span>

<br>
credentials = CognitiveServicesCredentials(key)
client = ComputerVisionClient(endpoint=ENDPOINT, credentials=credentials)

<br>
<span style="color:blue;">print</span>(<span style="color:orange;">'Analyzing image...'</span>)
viz_features = [VisualFeatureTypes.description, VisualFeatureTypes.objects, VisualFeatureTypes.tags]
analysis = client.analyze_image(img, visual_features=viz_features)

<br>
<span style="color:blue;">print</span>(<span style="color:orange;">'\nDescription:'</span>)
<span style="color:blue;">for</span> caption <span style="color:blue;">in</span> analysis.description.captions:
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:blue;">print</span>(caption.text)
<span style="color:blue;">print</span>(<span style="color:orange;">'\nObjects in this image:'</span>)
<span style="color:blue;">for</span> analysis_object <span style="color:blue;">in</span> analysis.objects:
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:blue;">print</span>(<span style="color:orange;">f' - {analysis_object.object_property}'</span>)
<span style="color:blue;">print</span>(<span style="color:orange;">'\nTags relevant to this image:'</span>)
<span style="color:blue;">for</span> tag <span style="color:blue;">in</span> analysis.description.tags:
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:blue;">print</span>(<span style="color:orange;">f' - {tag}'</span>)
<span style="color:blue;">print</span>(<span style="color:orange;">'\n'</span>)
</code></pre>
</details>

#### DOWNLOAD FILES
__[Powershell File](./analyze-image.ps1)__ | __[Python File](./analyze-image.py)__

### Computer Vision Exercises
<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

---
<details open>
<summary style="font-size:1em;font-weight:500;"><a id="store-camera-1jpg">store-camera-1.jpg</a></summary>

<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

<div>
<span>
<img style="display:block;float:right;width:50%;margin:10px;" src="https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/vision/store-camera-1.jpg">
</span>
<span>
<h5><em>Input:</em></h5>
<p>
<code>python analyze-image.py store-camera-1.jpg</code>
</p>
<h5><em>Output:</em></h5>
<pre style="background-color:#eef;margin:10px;padding:5px;"><code>Analyzing image...

Description:
a woman showing her phone to a child

Objects in this image:
 \- cell phone
 \- person
 \- person
 \- room

Tags relevant to this image:
 \- text
 \- person
 \- woman
 \- store
 \- shop

</code></pre>
</span>
</div>
</details>


---
<details open>
<summary style="font-size:1em;font-weight:500;"><a id="store-camera-2jpg">store-camera-2.jpg</a></summary>

<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

<div>
<span>
<img style="display:block;float:right;width:50%;margin:10px;" src="https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/vision/store-camera-2.jpg">
</span>
<span>
<h5><em>Input:</em></h5>
<p>
<code>python analyze-image.py store-camera-2.jpg</code>
</p>
<h5><em>Output:</em></h5>
<pre style="background-color:#eef;margin:10px;padding:5px;"><code>Analyzing image...

Description:
a woman holding a shopping cart in a grocery store

Objects in this image:
 \- person

Tags relevant to this image:
 \- text
 \- person
 \- woman
 \- marketplace
 \- shop

</code></pre>
</span>
</div>
</details>



---
<details open>
<summary style="font-size:1em;font-weight:500;"><a id="store-camera-3jpg">store-camera-3.jpg</a></summary>

<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

<div>
<span>
<img style="display:block;float:right;width:50%;margin:10px;" src="https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/vision/store-camera-3.jpg">
</span>
<span>
<h5><em>Input:</em></h5>
<p>
<code>python analyze-image.py store-camera-3.jpg </code>
</p>
<h5><em>Output:</em></h5>
<pre style="background-color:#eef;margin:10px;padding:5px;"><code>Analyzing image...

Description:
a person pushing a shopping cart

Objects in this image:
 \- person
 \- supermarket

Tags relevant to this image:
 \- text
 \- marketplace
 \- person
 \- scene
 \- produce
 \- shop

</code></pre>
</span>
</div>
</details>



---
<details open>
<summary style="font-size:1em;font-weight:500;"><a id="store-camera-4jpg">store-camera-4.jpg</a></summary>

<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

<div>
<span>
<img style="display:block;float:right;width:50%;margin:10px;" src="https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/vision/store-camera-4.jpg">
</span>
<span>
<h5><em>Input:</em></h5>
<p>
<code>python analyze-image.py store-camera-4.jpg</code>
</p>
<h5><em>Output:</em></h5>
<pre style="background-color:#eef;margin:10px;padding:5px;"><code>Analyzing image...

Description:
a man and woman looking at a phone in a grocery store

Objects in this image:
 \- person
 \- person
 \- person

Tags relevant to this image:
 \- text
 \- person
 \- marketplace
 \- store
 \- fruit
 \- produce
 \- shop
 \- sale
 \- fresh

</code></pre>
</span>
</div>
</details>



---
### Computer Vision Resources
<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

 * [PyPi](https://pypi.org/project/azure-cognitiveservices-vision-computervision/)
 * [GitHub](https://github.com/Azure/azure-sdk-for-python)
 * [Azure Cognitive Services Computer Vision SDK for Python](https://docs.microsoft.com/en-us/python/api/overview/azure/cognitiveservices-vision-computervision-readme?view=azure-python)
 * [`computervision` Package](https://docs.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-computervision/azure.cognitiveservices.vision.computervision?view=azure-python)
 * [Parameters for `analyze_image()`](https://docs.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-computervision/azure.cognitiveservices.vision.computervision.operations.computervisionclientoperationsmixin?view=azure-python#azure-cognitiveservices-vision-computervision-operations-computervisionclientoperationsmixin-analyze-image)
 * [`VisualFeatureTypes`](https://docs.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-computervision/azure.cognitiveservices.vision.computervision.models.visualfeaturetypes?view=azure-python)
 * [DetectedObject Class (for Java)](https://docs.microsoft.com/en-us/java/api/com.microsoft.azure.cognitiveservices.vision.computervision.models.detectedobject?view=azure-java-legacy)



---
***

## Natural Language Processing

### NLP Setup
<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

#### VIRTUAL ENVIRONMENT (_OPTIONAL_)
```
python3 -m venv cogsrv-textanalytics-env
source cogsrv-textanalytics-env/bin/activate
```

#### INSTALLATION
```
pip install azure-ai-textanalytics
```

---
### NLP Steps
<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>


1. If you have not already opened VS Code in the cloud shell, Run: `code .`

1. Switch to the Bash shell. *If you are already in the Bash shell, skip this step.*

1. In the Bash shell pane, enter the following commands to navigate inside the ai-900 folder:
	* `cd ai-900`

4. Create the file `analyze-text.py` by running the following code
	* `touch analyze-text.py`

1. In the Files pane on the left, expand ai-900 and select `analyze-text.py`. This file will be empty.

1. Paste the [code below](#nlp-code) into the new file, `analyze-text.py`.

1. Don't worry too much about the details of the code. In the [Azure portal](https://portal.azure.com), navigate to your Cognitive Services resource. Then select the Keys and Endpoints page on the left hand pane. Copy the key from the page and paste it into the code editor, replacing the `YOUR_KEY` placeholder value.

1. In the [Azure portal](https://portal.azure.com), navigate back to your Cognitive Services resource page. The value for ACCOUNT_REGION can be found here, under "Location". The value should be altered so it is all lowercase and without spaces.

1. After pasting the key and location values, the first two lines of code should look similar to this:
<ul><pre><code>key = "1a2b3c4d5e6f7g8h9i0j...."
ACCOUNT_REGION = 'eastus2'</code></pre></ul>

10. At the top right of the editor pane, use the ... button to open the menu and select Save to save your changes. <br> The sample client application will use Cognitive Services' Language service to detect language, extract key phrases, determine sentiment, and extract known entities in [Exercise 1](#review1txt)

1. In the Bash shell pane, enter the following commands to run the code:
<ul><code>python analyze-text.py review1.txt</code></ul><br>
<ul>Review the output of the <a href="https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/text/reviews/review1.txt" target="_blank">following text</a>:
</ul><br><ul>
<blockquote> Good Hotel and staff <br>
The Royal Hotel, London, UK <br>
3/2/2018 <br>
Clean rooms, good service, great location near Buckingham Palace and Westminster Abbey, and so on. We thoroughly enjoyed our stay. The courtyard is very peaceful and we went to a restaurant which is part of the same group and is Indian ( West coast so plenty of fish) with a Michelin Star. We had the taster menu which was fabulous. The rooms were very well appointed with a kitchen, lounge, bedroom and enormous bathroom. Thoroughly recommended.</blockquote>
</ul>

12. Go ahead and try the other Exercises
<ul>
<li><a href="#review2txt">Exercise 2:</a> <code>python analyze-text.py review2.txt</code></li>
<li><a href="#review3txt">Exercise 3:</a> <code>python analyze-text.py review3.txt</code></li>
<li><a href="#review4txt">Exercise 4:</a> <code>python analyze-text.py review4.txt</code></li>
</ul>
<br>


*Adapted From [Analyze text](https://docs.microsoft.com/en-us/learn/modules/analyze-text-with-text-analytics-service/3-exercise)*


### NLP Code
<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

<details>
<summary style="font-weight:bold;color:#c00;"><em>View Code</em></summary>
<pre lang='python'><code>key = <span style="color:orange;">'YOUR_KEY'</span>
ACCOUNT_REGION = <span style="color:orange;">'YOUR_REGION'</span>
ENDPOINT = <span style="color:orange;">f'https://{ACCOUNT_REGION}.api.cognitive.microsoft.com/'</span>

<br>
<span style="color:blue;">from</span> azure.core.credentials <span style="color:blue;">import</span> AzureKeyCredential
<span style="color:blue;">from</span> azure.ai.textanalytics <span style="color:blue;">import</span> TextAnalyticsClient
<span style="color:blue;">import</span> sys
<span style="color:blue;">import</span> requests

<br>
args = sys.argv[<span style="color:green;">1</span>:]
txt_file = <span style="color:orange;">'review1.txt'</span>
txt_list = [<span style="color:orange;">"review1.txt"</span>, <span style="color:orange;">"review2.txt"</span>, <span style="color:orange;">"review3.txt"</span>, <span style="color:orange;">"review4.txt"</span>]
if len(args) > <span style="color:green;">0</span> and args[<span style="color:green;">0</span>] in txt_list:
    txt_file = args[<span style="color:green;">0</span>]
url = <span style="color:orange;">f'https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/text/reviews/{txt_file}'</span>

<br>
response = requests.get(url)
documents = [response.text]

<br>
credentials = AzureKeyCredential(key)
text_analytics_client = TextAnalyticsClient(endpoint=ENDPOINT, credential=credentials)

<br>
<span style="color:blue;">print</span>(<span style="color:orange;">"***Detecting Language***"</span>)
response = text_analytics_client.detect_language(documents)
result = [doc <span style="color:blue;">for</span> doc <span style="color:blue;">in</span> response <span style="color:blue;">if not</span> doc.is_error]

<br>
langName = None
langCode = None
langScore = None
<span style="color:blue;">for</span> doc <span style="color:blue;">in</span> result:
&nbsp;&nbsp;&nbsp;&nbsp;langName = doc.primary_language.name
&nbsp;&nbsp;&nbsp;&nbsp;langCode = doc.primary_language.iso6391_name
&nbsp;&nbsp;&nbsp;&nbsp;langScore = doc.primary_language.confidence_score
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:blue;">print</span>(<span style="color:orange;">f"  - Language: {langName}"</span>)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:blue;">print</span>(<span style="color:orange;">f"  - Code:     {langCode}"</span>)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:blue;">print</span>(<span style="color:orange;">f"  - Score:    {langScore}"</span>)

<br>
<span style="color:blue;">print</span>(<span style="color:orange;">"\n\n***Finding Key Phrases***"</span>)
response = text_analytics_client.extract_key_phrases(documents, language=langCode)
result = [doc <span style="color:blue;">for</span> doc <span style="color:blue;">in</span> response <span style="color:blue;">if not</span> doc.is_error]
<span style="color:blue;">for</span> doc <span style="color:blue;">in</span> result:
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:blue;">print</span>(<span style="color:orange;">"  - Key Phrases: "</span>)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:blue;">for</span> key_phrase <span style="color:blue;">in</span> doc.key_phrases:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:blue;">print</span>(f<span style="color:orange;">"    {key_phrase}"</span>)

<br>
<span style="color:blue;">print</span>(<span style="color:orange;">"\n\n***Analyzing Sentiment***"</span>)
response = text_analytics_client.analyze_sentiment(documents, language=langCode)
result = [doc <span style="color:blue;">for</span> doc <span style="color:blue;">in</span> response <span style="color:blue;">if not</span> doc.is_error]
<span style="color:blue;">for</span> doc <span style="color:blue;">in</span> result:
&nbsp;&nbsp;&nbsp;&nbsp;sentiment = doc.sentiment
&nbsp;&nbsp;&nbsp;&nbsp;positive = doc.confidence_scores.positive
&nbsp;&nbsp;&nbsp;&nbsp;neutral = doc.confidence_scores.neutral
&nbsp;&nbsp;&nbsp;&nbsp;negative = doc.confidence_scores.negative
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:blue;">print</span>(<span style="color:orange;">f"  - A {sentiment} sentiment based on these scores:"</span>)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:blue;">print</span>(<span style="color:orange;">f"    - Positive: {positive}"</span>)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:blue;">print</span>(<span style="color:orange;">f"    - Neutral:  {neutral}"</span>)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:blue;">print</span>(<span style="color:orange;">f"    - Negative: {negative}"</span>)

<br>
<span style="color:blue;">print</span>(<span style="color:orange;">"\n\n***Identifying known entities***"</span>)
response = text_analytics_client.recognize_linked_entities(documents, language=langCode)
result = [doc <span style="color:blue;">for</span> doc <span style="color:blue;">in</span> response <span style="color:blue;">if not</span> doc.is_error]
<span style="color:blue;">for</span> doc <span style="color:blue;">in</span> result:
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:blue;">for</span> entity <span style="color:blue;">in</span> doc.entities:
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:blue;">print</span>(<span style="color:orange;">f"  - {entity.name} : {entity.url}"</span>)

<br>
</code></pre>
</details>

#### DOWNLOAD FILES
__[Powershell File](./analyze-text.ps1)__ | __[Python File](./analyze-text.py)__

### NLP Exercises


---
<details open>
<summary style="font-size:1em;font-weight:500;"><a id="review1txt">review1.txt</a></summary>

<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

Review the output of the <a href="https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/text/reviews/review1.txt" target="_blank">following text</a>:

> Good Hotel and staff  <br>
> The Royal Hotel, London, UK <br>
> 3/2/2018 <br>
> Clean rooms, good service, great location near Buckingham Palace and Westminster Abbey, and so on. We thoroughly enjoyed our stay. The courtyard is very peaceful and we went to a restaurant which is part of the same group and is Indian ( West coast so plenty of fish) with a Michelin Star. We had the taster menu which was fabulous. The rooms were very well appointed with a kitchen, lounge, bedroom and enormous bathroom. Thoroughly recommended.

<div>
<span>
<h5><em>Input:</em></h5>
<p>
<code>python analyze-text.py review1.txt</code>
</p>
<h5><em>Output:</em></h5>
<pre style="background-color:#eef;margin:10px;padding:5px;"><code>***Detecting Language***
  - Language: English
  - Code:     en
  - Score:    0.99


\*\*\*Finding Key Phrases\*\*\*
  \- Key Phrases: 
    The Royal Hotel
    Good Hotel
    good service
    great location
    Buckingham Palace
    Westminster Abbey
    same group
    West coast
    Michelin Star
    taster menu
    enormous bathroom
    Clean rooms
    staff
    London
    UK
    stay
    courtyard
    restaurant
    part
    plenty
    fish
    kitchen
    lounge
    bedroom


\*\*\*Analyzing Sentiment\*\*\*
  \- A positive sentiment based on these scores:
    \- Positive: 0.98
    \- Neutral:  0.01
    \- Negative: 0.01


\*\*\*Identifying known entities\*\*\*
  \- GOOD Music : https://en.wikipedia.org/wiki/GOOD_Music
  \- Hotel : https://en.wikipedia.org/wiki/Hotel
  \- The Royal Hotel : https://en.wikipedia.org/wiki/The_Royal_Hotel
  \- London : https://en.wikipedia.org/wiki/London
  \- Buckingham Palace : https://en.wikipedia.org/wiki/Buckingham_Palace
  \- Westminster Abbey : https://en.wikipedia.org/wiki/Westminster_Abbey
  \- India : https://en.wikipedia.org/wiki/India
  \- West Coast Main Line : https://en.wikipedia.org/wiki/West_Coast_Main_Line
  \- Michelin Guide : https://en.wikipedia.org/wiki/Michelin_Guide

</code></pre>
</span>
</div></details>



---
<details open>
<summary style="font-size:1em;font-weight:500;"><a id="review2txt">review2.txt</a></summary>

<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

Review the output of the <a href="https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/text/reviews/review2.txt" target="_blank">following text</a>:

> Tired hotel with poor service <br>
> The Royal Hotel, London, United Kingdom <br>
> 5/6/2018 <br>
> This is a old hotel (has been around since 1950's) and the room furnishings are average - becoming a bit old now and require changing. The internet didn't work and had to come to one of their office rooms to check in for my flight home. The website says it's close to the British Museum, but it's too far to walk.

<div>
<span>
<h5><em>Input:</em></h5>
<p>
<code>python analyze-text.py review2.txt</code>
</p>
<h5><em>Output:</em></h5>
<pre style="background-color:#eef;margin:10px;padding:5px;"><code>***Detecting Language***
  - Language: English
  - Code:     en
  - Score:    1.0


\*\*\*Finding Key Phrases\*\*\*
  \- Key Phrases: 
    The Royal Hotel
    Tired hotel
    old hotel
    poor service
    United Kingdom
    room furnishings
    office rooms
    flight home
    British Museum
    London
    changing
    internet
    website
    1950


\*\*\*Analyzing Sentiment\*\*\*
  \- A positive sentiment based on these scores:
    \- Positive: 0.01
    \- Neutral:  0.07
    \- Negative: 0.92


\*\*\*Identifying known entities\*\*\*
  \- The Royal Hotel : https://en.wikipedia.org/wiki/The_Royal_Hotel
  \- London : https://en.wikipedia.org/wiki/London
  \- British Museum : https://en.wikipedia.org/wiki/British_Museum

</code></pre>
</span>
</div></details>



---
<details open>
<summary style="font-size:1em;font-weight:500;"><a id="review3txt">review3.txt</a></summary>

<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

Review the output of the <a href="https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/text/reviews/review3.txt" target="_blank">following text</a>:

> Good location and helpful staff, but on a busy road. <br>
> The Lombard Hotel, San Francisco, USA <br>
> 8/16/2018 <br>
> We stayed here in August after reading reviews. We were very pleased with location, just behind Chestnut Street, a cosmopolitan and trendy area with plenty of restaurants to choose from. The Marina district was lovely to wander through, very interesting houses. Make sure to walk to the San Francisco Museum of Fine Arts and the Marina to get a good view of Golden Gate bridge and the city. On a bus route and easy to get into centre. Rooms were clean with plenty of room and staff were friendly and helpful. The only down side was the noise from Lombard Street so ask to have a room furthest away from traffic noise.

<div>
<span>
<h5><em>Input:</em></h5>
<p>
<code>python analyze-text.py review3.txt</code>
</p>
<h5><em>Output:</em></h5>
<pre style="background-color:#eef;margin:10px;padding:5px;"><code>***Detecting Language***
  - Language: English
  - Code:     en
  - Score:    0.99


\*\*\*Finding Key Phrases\*\*\*
  \- Key Phrases: 
    Golden Gate bridge
    The Lombard Hotel
    The Marina district
    San Francisco Museum
    Lombard Street
    busy road
    Chestnut Street
    trendy area
    interesting houses
    Fine Arts
    good view
    bus route
    down side
    Good location
    helpful staff
    traffic noise
    USA
    We
    August
    reviews
    cosmopolitan
    plenty
    restaurants
    city
    centre
    Rooms


\*\*\*Analyzing Sentiment\*\*\*
  \- A positive sentiment based on these scores:
    \- Positive: 0.86
    \- Neutral:  0.04
    \- Negative: 0.1


\*\*\*Identifying known entities\*\*\*
  \- Lombardy : https://en.wikipedia.org/wiki/Lombardy
  \- Hotel : https://en.wikipedia.org/wiki/Hotel
  \- San Francisco : https://en.wikipedia.org/wiki/San_Francisco
  \- Chestnut Street (Philadelphia) : https://en.wikipedia.org/wiki/Chestnut_Street_(Philadelphia)
  \- Marina District, San Francisco : https://en.wikipedia.org/wiki/Marina_District,_San_Francisco
  \- Museum of Fine Arts, Boston : https://en.wikipedia.org/wiki/Museum_of_Fine_Arts,_Boston
  \- Golden Gate Bridge : https://en.wikipedia.org/wiki/Golden_Gate_Bridge
  \- Room : https://en.wikipedia.org/wiki/Room
  \- Lombard Street (San Francisco) : https://en.wikipedia.org/wiki/Lombard_Street_(San_Francisco)

</code></pre>
</span>
</div></details>



---
<details open>
<summary style="font-size:1em;font-weight:500;"><a id="review4txt">review4.txt</a></summary>

<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

Review the output of the <a href="https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/text/reviews/review4.txt" target="_blank">following text</a>:

> Very noisy and rooms are tiny <br>
> The Lombard Hotel, San Francisco, USA <br>
> 9/5/2018 <br>
> Hotel is located on Lombard street which is a very busy SIX lane street directly off the Golden Gate Bridge. Traffic from early morning until late at night especially on weekends. Noise would not be so bad if rooms were better insulated but they are not. Had to put cotton balls in my ears to be able to sleep--was too tired to enjoy the city the next day. Rooms are TINY. I picked the room because it had two queen size beds--but the room barely had space to fit them. With family of four in the room it was tight. With all that said, rooms are clean and they've made an effort to update them. The hotel is in Marina district with lots of good places to eat, within walking distance to Presidio. May be good hotel for young stay-up-late adults on a budget

<div>
<span>
<h5><em>Input:</em></h5>
<p><code>python analyze-text.py review4.txt</code></p>
<h5><em>Output:</em></h5>
<pre style="background-color:#eef;margin:10px;padding:5px;"><code>***Detecting Language***
  - Language: English
  - Code:     en
  - Score:    1.0


\*\*\*Finding Key Phrases\*\*\*
  \- Key Phrases: 
    two queen size beds
    busy SIX lane street
    Golden Gate Bridge
    The Lombard Hotel
    Lombard street
    San Francisco
    early morning
    cotton balls
    Marina district
    good places
    walking distance
    late adults
    good hotel
    rooms
    USA
    Traffic
    night
    weekends
    Noise
    ears
    city
    TINY
    space
    family
    effort
    lots
    Presidio
    young
    budget

\*\*\*Analyzing Sentiment\*\*\*
  \- A positive sentiment based on these scores:
    \- Positive: 0.36
    \- Neutral:  0.12
    \- Negative: 0.52


\*\*\*Identifying known entities\*\*\*
  \- Lombard, Illinois : https://en.wikipedia.org/wiki/Lombard,_Illinois
  \- Hotel : https://en.wikipedia.org/wiki/Hotel
  \- San Francisco : https://en.wikipedia.org/wiki/San_Francisco
  \- Lombard Street (San Francisco) : https://en.wikipedia.org/wiki/Lombard_Street_(San_Francisco)
  \- Golden Gate Bridge : https://en.wikipedia.org/wiki/Golden_Gate_Bridge
  \- Traffic : https://en.wikipedia.org/wiki/Traffic
  \- Noise rock : https://en.wikipedia.org/wiki/Noise_rock
  \- Room : https://en.wikipedia.org/wiki/Room
  \- Marina District, San Francisco : https://en.wikipedia.org/wiki/Marina_District,_San_Francisco
  \- Presidio of San Francisco : https://en.wikipedia.org/wiki/Presidio_of_San_Francisco
  \- May : https://en.wikipedia.org/wiki/May

</code></pre>
</span>
</div></details>



---
### NLP Resources
<sup>[(back to top)](#azure-cognitive-services-python-sdk)</sup>

 * [PyPi](https://pypi.org/project/azure-cognitiveservices-language-textanalytics/)

 * [GitHub](https://github.com/Azure/azure-sdk-for-python)

 * [Azure Text Analytics client library for Python](https://docs.microsoft.com/en-us/python/api/overview/azure/ai-textanalytics-readme?source=recommendations&view=azure-python)



---
***

