# -*- coding: utf-8 -*-
"""Generate Images from Text in Python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CNL-cPH5xra_tYU-UszRWuTVlMVJIhwN
"""

pip install diffusers

pip install transformers

pip install Pillow

pip install accelerate scipy safetensors

import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

# Replace the model version with your required version if needed
pipeline = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1", torch_dtype=torch.float16
)

# Running the inference on GPU with cuda enabled
pipeline = pipeline.to('cuda')

prompt = "Create an elegant and premium-looking logo for [brand name]. Use a gold, black, or deep navy color scheme with refined typography. Incorporate a subtle emblem, crown, or abstract luxury symbol to represent exclusivity and high-end appeal."

image = pipeline(prompt=prompt).images[0]

image.show()

from IPython.display import display
display(image)

