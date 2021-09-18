from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
#from PIL import Image
import sys
import time

subscription_key = "56bbf74fb55940099a58bef2ad2b253d"
endpoint = "https://azcogsvcsresource.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

remote_image_url = "https://raw.githubusercontent.com/vivkap/AI102Files/Cognitive-Introduction/Computer_Vision" \
                   "/Analyze_images_using_Computer_Vision_API/Images/IMG_3323.JPG"


# Call API with content type (landmarks) and URL
detect_domain_results_landmarks = computervision_client.analyze_image_by_domain("landmarks", remote_image_url)
print("===== Detect Domain-specific Content - Remote =====")
print("Landmarks in the remote image:")
if len(detect_domain_results_landmarks.result["landmarks"]) == 0:
    print("No landmarks detected.")
else:
    for landmark in detect_domain_results_landmarks.result["landmarks"]:
        print(landmark["name"])

'''
Detect Domain-specific Content - local
This example detects landmarks in local images.
'''
print()
print("===== Detect Domain-specific Content - local =====")

# Open local image file containing a landmark
local_image_path_landmark = "Images/IMG_3323.JPG"
local_image_landmark = open(local_image_path_landmark, "rb")
# Call API with type of content (landmark) and local image
detect_domain_results_landmark_local = computervision_client.analyze_image_by_domain_in_stream("landmarks",
                                                                                               local_image_landmark)

# Print results of landmark detected
print("Landmarks in the local image:")
if len(detect_domain_results_landmark_local.result["landmarks"]) == 0:
    print("No landmarks detected.")
else:
    for landmark in detect_domain_results_landmark_local.result["landmarks"]:
        print(landmark["name"])
'''
END - Detect Domain-specific Content - local
'''
