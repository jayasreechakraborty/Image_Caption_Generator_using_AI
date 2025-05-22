from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
model.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_caption(image_path):
    image = Image.open(image_path).convert('RGB')
    inputs = processor(images=image, return_tensors="pt").to(model.device)
    with torch.no_grad():
        ids = model.generate(**inputs, max_length=50)
    return processor.decode(ids[0], skip_special_tokens=True)

if __name__ == "__main__":
    caption = generate_caption("your_image.jpg")
    print("🖼️ Generated Caption:", caption)
