# Image_Caption_Generator_using_AI
This project is a multimodal AI application that automatically generates smart, context-aware captions for any uploaded image using Salesforce’s BLIP (Bootstrapped Language Image Pretraining) model.  Built using Python, PyTorch, and Hugging Face Transformers, the app provides an easy-to-use Gradio interface for real-time caption generation.

Example:

Input: Image of a dog running through grass

Output: "a brown dog is running through the grass"

image-caption-generator/

├── blip_app.py                                                                # Gradio web app

├── blip_caption_generator.py                                                  # Simple script version

├── your_image.jpg                                                             # Example image

└── README.md                                                                  # This file

#Tech_Stack

-Python 3.8+

-PyTorch

-Hugging Face Transformers

-Gradio (for the web app interface)

-BLIP model: Salesforce/blip-image-captioning-base

#Installation

1.Clone the Repository

-git clone https://github.com/yourusername/image-caption-generator.git

-cd image-caption-generator

2.Install Dependencies:

-Make sure Python is installed. Then install the required packages:

-pip install torch torchvision

-pip install transformers

-pip install gradio

-pip install Pillow

#Run the App

1.Caption from a local script:

Create or run blip_caption_generator.py to generate captions for a specific image:

-python blip_caption_generator.py

2.Run the Gradio Web App:

-python blip_app.py

This will start a local server at:

http://127.0.0.1:7860

You can open it in your browser and start using the app.

To Share with Others (Optional):

To create a public link with Gradio, edit the last line of blip_app.py:

-gr.Interface(...).launch(share=True)

If Gradio fails to create the share link due to a missing file, follow these manual steps:

Download the required file from: https://cdn-media.huggingface.co/frpc-gradio-0.3/frpc_windows_amd64.exe

Rename it to: frpc_windows_amd64_v0.3

Place it in: C:\Users\YOUR_USERNAME\.cache\huggingface\gradio\frpc

#Credits

-Salesforce BLIP

-Hugging Face Transformers

-Gradio

#License

MIT License.



