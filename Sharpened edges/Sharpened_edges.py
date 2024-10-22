from PIL import Image, ImageFilter
def start(input_dir, output_dir):
    image = Image.open(input_dir)
    enhanced = image.filter(ImageFilter.SHARPEN)
    enhanced.save(output_dir)

