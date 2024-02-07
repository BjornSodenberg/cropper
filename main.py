import cv2
from PIL import Image, ImageDraw
import os

def crop_face(image_path, scale_factor=2.5, final_size=100):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    image = cv2.imread(image_path)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    if len(faces) > 0:
        x, y, w, h = faces[0]
        
        new_w = w * scale_factor
        new_h = h * scale_factor
        new_x = x - (new_w - w) / 2
        new_y = y - (new_h - h) / 2
        
        left = max(new_x, 0)
        top = max(new_y, 0)
        right = min(new_x + new_w, image.shape[1])
        bottom = min(new_y + new_h, image.shape[0])
        
        cropped_image = image[int(top):int(bottom), int(left):int(right)]
        
        resized_image = cv2.resize(cropped_image, (final_size, final_size), interpolation=cv2.INTER_AREA)
        
        return resized_image
    else:
        print(f"No face detected in {image_path}")
        return None


def apply_circle_mask(cropped_image):
    if cropped_image is not None:
        pil_image = Image.fromarray(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
        
        mask = Image.new('L', pil_image.size, 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + pil_image.size, fill=255)
        
        result = Image.new('RGBA', pil_image.size)
        result.paste(pil_image, (0, 0), mask)
        
        return result
    else:
        return None

def process_images(directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    if not os.path.exists('cropped_images'):
        os.makedirs('cropped_images')

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png')):
            image_path = os.path.join(directory, filename)
            
            cropped_image = crop_face(image_path)
            
            circled_image = apply_circle_mask(cropped_image)
            
            if circled_image:
                output_path = os.path.join('cropped_images', f"cropped_{filename}")
                circled_image.save(output_path)
                print(f"Processed image saved to {output_path}")


process_images('assets_png')