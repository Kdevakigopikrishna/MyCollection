from PIL import Image

# Step 1: Uploading an Image
f = "C:\\Users\\harsh\\OneDrive\\Pictures\\Desktop\\deva.jpg.jpg"
img = Image.open(f)
img.show()

# Step 2: Rotating the Image
img = img.rotate(angle=60, fillcolor="green")
img.show()

# Step 3: Resizing the Image
print("Original size of image:", img.width, img.height)
img = img.resize((int(img.width / 2), int(img.height / 2)))
print("New size of image:", img.width, img.height)
img.show()

# Step 4: Converting the Image to Grayscale
f = "C:\\Users\\harsh\\Downloads\\abstract-autumn-beauty-multi-colored-leaf-vein-pattern-generated-by-ai.jpg"
img = Image.open(f)
gray_img = img.convert("L")
gray_img.show()
