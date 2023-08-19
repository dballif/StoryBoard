import html
from diffusers import StableDiffusionPipeline

def splitIntoArray(frame_sentences):
    return frame_sentences.split("+")

def generateFrames(project_title,frame_sentences, style):
	newArray = splitIntoArray(frame_sentences)
	promptNum = 0
	nameArray = []
    
	#Loop through the frames and generate images
	for frame in newArray:
		promptNum = promptNum + 1
		frameName = project_title +"_prompt" + str(promptNum) + ".png"

		#Insert stable diffusion here
		base = StableDiffusionPipeline.from_single_file('./data/mdjrny-v4.safetensors', use_safetensors=True) 
		#Build the prompt
		base_prompt = "masterpiece, best quality, 8k, detailed, dramatic,"
		full_prompt = base_prompt + style + ", " + frame

		#Use a negative prompt to mtry to make picture better
		neg_prompt = "low res, ugly, bad hands, too many digits, bad teeth, blurry, blurred background"
		
		#V1 - Use cpu
		base.to("cpu")

		#Create the image
		image = base(prompt=full_prompt, negative_prompt=neg_prompt).images[0]
		
		#Save each image into images folder with name prompt#.png
		image.save(f"images/{frameName}")
		#Add name to array
		nameArray.append(frameName)
    
	#Return an array with the name of each file
	return nameArray