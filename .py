from PIL import Image, ImageDraw, ImageFont
import os
import random

# Define the Amharic alphabet (33 consonants, 7 vowel forms each)
amharic_chars = []
base_consonants = [
    0x1200,  # ሀ
    0x1208,  # ለ
    0x1210,  # ሐ
    0x1218,  # መ
    0x1220,  # ሠ
    0x1228,  # ረ
    0x1230,  # ሰ
    0x1238,  # ሸ
    0x1240,  # ቀ
    0x1248,  # ቈ
    0x1250,  # ቐ
    0x1258,  # ቘ
    0x1260,  # በ
    0x1268,  # ቨ
    0x1270,  # ተ
    0x1278,  # ቸ
    0x1280,  # ኀ
    0x1288,  # ኈ
    0x1290,  # ነ
    0x1298,  # ኘ
    0x12A0,  # አ
    0x12A8,  # ከ
    0x12B0,  # ኰ
    0x12B8,  # ኸ
    0x12C0,  # ዀ
    0x12C8,  # ወ
    0x12D0,  # ዐ
    0x12D8,  # ዘ
    0x12E0,  # ዠ
    0x12E8,  # የ
    0x12F0,  # ደ
    0x12F8,  # ዸ
    0x1300,  # ጀ
    0x1308,  # ገ
    0x1310,  # ጐ
    0x1318,  # ጘ
    0x1320,  # ጠ
    0x1328,  # ጨ
    0x1330,  # ጰ
    0x1338,  # ጸ
    0x1340,  # ፀ
    0x1348,  # ፈ
    0x1350,  # ፐ
]

# Generate all characters (33 consonants × 7 vowel forms)
for base in base_consonants:
    for vowel_offset in range(7):  # 7 vowel forms
        char_code = base + vowel_offset
        amharic_chars.append(chr(char_code))

# Font path for rendering the characters
font_path = os.path.expanduser("~/.fonts/AbyssinicaSIL-Regular.ttf")  # Expands ~ to /home/cs

# Verify the font file exists
if not os.path.exists(font_path):
    print(f"Font file {font_path} does not exist! Please check the path and try again.")
    exit()

# Create output directories with Amharic letter names
for char in amharic_chars:
    os.makedirs(char, exist_ok=True)

# Generate images for each character
for idx, char in enumerate(amharic_chars):
    try:
        font = ImageFont.truetype(font_path, size=40)
    except Exception as e:
        print(f"Font {font_path} not found or failed to load: {e}, exiting...")
        exit()

    # Generate 5 variations to account for slight positioning differences
    for i in range(5):
        # Create a blank 64x64 image
        image = Image.new("L", (224, 224), color=255)  # White background
        draw = ImageDraw.Draw(image)

        # Calculate text position with slight random offset
        text_bbox = draw.textbbox((0, 0), char, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        base_position = ((64 - text_width) // 2, (64 - text_height) // 2)
        offset_x = base_position[0] + random.randint(-3, 3)
        offset_y = base_position[1] + random.randint(-3, 3)
        position = (offset_x, offset_y)

        # Draw the character with a slight rotation
        temp_image = Image.new("L", (64, 64), color=255)
        temp_draw = ImageDraw.Draw(temp_image)
        temp_draw.text((32, 32), char, font=font, fill=0, anchor="mm")
        rotated_image = temp_image.rotate(random.randint(-5, 5))

        # Paste the rotated image onto the main image
        image.paste(rotated_image, (0, 0))

        # Save the image in the corresponding folder
        image.save(f"{char}/{char}_{i + 1}.png")

print("Standard font image generation complete!")