# README.md

## StoryBoard Project
The goal of this project is to create a fairly simple WebUI that allows a user to create
a simple storyboard for their own project using Stable Diffusion to create the images.

### How to Setup
Use the requirements.txt file to install the needed python packages
`pip install -r requirements.txt`

Grab the Data for Stable Diffusion & put it into the Data directory. We will use mdjrny from Hugging Face
Note: This is a pretty big file (2.3G)
`curl https://huggingface.co/prompthero/openjourney/blob/main/mdjrny-v4.safetensors >> data/mdjrny-v4.safetensors` 

To deploy development server (NOT suitable for production):
`python storyboard.py`

### Important Notes
The backend of this particular application is using Python and will hook into either the
CPU or GPU as specified. Each image for each storyboard frame will take a fairly long
time to load depending on the users hardware.

The best option is to use a dedicated GPU when possible.

### Stable Diffusion Notes
This project usese the following datasets for creating the images with Stable Diffusion: 

