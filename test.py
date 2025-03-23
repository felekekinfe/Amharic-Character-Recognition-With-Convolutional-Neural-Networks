import os
from PIL import Image, ImageDraw, ImageFont
import random

def generate_test_dataset(base_dir="dataset/test", num_samples=5, img_size=(64, 64)):
    """Generate synthetic test dataset for the full Amharic character set with backgrounds.

    Args:
        base_dir (str): Base directory for test data (default: 'dataset/test').
        num_samples (int): Number of images per character per background (default: 5).
        img_size (tuple): Image size (height, width), default (64, 64).
    """
    # Full Amharic character set (43 bases × 7 forms)
    amharic_chars = []
    base_consonants = [
        0x1200, 0x1208, 0x1210, 0x1218, 0x1220, 0x1228, 0x1230, 0x1238, 0x1240, 
        0x1248, 0x1250, 0x1258, 0x1260, 0x1268, 0x1270, 0x1278, 0x1280, 0x1288, 
        0x1290, 0x1298, 0x12A0, 0x12A8, 0x12B0, 0x12B8, 0x12C0, 0x12C8, 0x12D0, 
        0x12D8, 0x12E0, 0x12E8, 0x12F0, 0x12F8, 0x1300, 0x1308, 0x1310, 0x1318, 
        0x1320, 0x1328, 0x1330, 0x1338, 0x1340, 0x1348, 0x1350
    ]
    for base in base_consonants:
        for offset in range(7):
            amharic_chars.append(chr(base + offset))
    
    # Font setup
    font_path = os.path.expanduser("~/.fonts/NotoSansEthiopic-VariableFont_wdth,wght.ttf")
    font_size = 40
    print(f"Checking font at: {font_path}")
    if not os.path.exists(font_path):
        print(f"Font not found! Download from Google Fonts and place in ~/.fonts/")
        return
    try:
        font = ImageFont.truetype(font_path, font_size)
        print("Font loaded successfully.")
    except OSError as e:
        print(f"Font load failed: {e}. Try 'NotoSansEthiopic-Regular.ttf'.")
        return
    
    # Test font rendering
    test_img = Image.new("L", img_size, 255)
    draw = ImageDraw.Draw(test_img)
    draw.text((32, 32), "ሀ", font=font, fill=0, anchor="mm")
    test_img.save("font_test.jpg")
    print("Saved font_test.jpg. Check if 'ሀ' is visible!")
    
    # Load background images
    background_dir = "background"
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    backgrounds = [os.path.join(background_dir, f) for f in os.listdir(background_dir) 
                   if f.lower().endswith(valid_extensions)]
    if not backgrounds:
        print(f"No backgrounds found in '{background_dir}'! Add images and retry.")
        return
    
    # Create base directory
    os.makedirs(base_dir, exist_ok=True)
    
    # Generate dataset
    for char in amharic_chars:
        char_dir = os.path.join(base_dir, char)
        os.makedirs(char_dir, exist_ok=True)
        
        for bg_idx, bg_path in enumerate(backgrounds):
            try:
                background = Image.open(bg_path).convert("L").resize(img_size, Image.Resampling.LANCZOS)
            except Exception as e:
                print(f"Failed to load {bg_path}: {e}. Skipping.")
                continue
            
            for i in range(num_samples):
                # Create character image
                char_img = Image.new("L", img_size, 255)  # White background
                draw = ImageDraw.Draw(char_img)
                text_bbox = draw.textbbox((0, 0), char, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]
                base_x, base_y = (img_size[0] - text_width) // 2, (img_size[1] - text_height) // 2
                x = base_x + random.randint(-3, 3)
                y = base_y + random.randint(-3, 3)
                
                # Draw with rotation
                temp_img = Image.new("L", img_size, 255)
                temp_draw = ImageDraw.Draw(temp_img)
                temp_draw.text((32, 32), char, font=font, fill=0, anchor="mm")
                rotated_img = temp_img.rotate(random.randint(-5, 5))
                
                # Create mask and composite
                mask = rotated_img.point(lambda p: 255 if p == 0 else 0)
                final_img = Image.composite(rotated_img, background, mask)
                
                # Save
                img_path = os.path.join(char_dir, f"test_{char}_bg{bg_idx + 1}_{i + 1}.jpg")
                final_img.save(img_path)
                print(f"Saved: {img_path}")
    
    print("Test dataset generation complete!")

if __name__ == "__main__":
    generate_test_dataset()