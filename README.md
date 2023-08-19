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
VERY IMPORTANT: This is not a production level project. It is currently meant to be setup and run on your own
machine. It is not secure at this point in the project. That will come later as a way to practice those skills.

The backend of this particular application is using Python and will hook into either the
CPU or GPU as specified. Each image for each storyboard frame will take a fairly long
time to load depending on the users hardware.

The best option is to use a dedicated GPU when possible.

Also, this is still "AI" generated imagery. It will probably have issues. Choosing or training a better
data set is probably not a bad idea, but mdjrny will do for now. Changes to the base prompt and negative prompt
will also help.

### Stable Diffusion Notes
This project usese the following datasets for creating the images with Stable Diffusion: 
- [Prompt Hero's OpenJourney](https://huggingface.co/prompthero/openjourney)

