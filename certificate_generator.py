import streamlit as st
import base64
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import datetime

def generate_certificate(name, course, date, output_path):
    # Create a new image with pastel gradient background
    cert_width = 1200
    cert_height = 800
    background_color_top = (255, 230, 250)   # light pink
    background_color_bottom = (220, 240, 255) # light blue
    
    certificate = Image.new('RGB', (cert_width, cert_height), background_color_top)
    draw = ImageDraw.Draw(certificate)

    # Create a vertical gradient effect
    for y in range(cert_height):
        r = int(background_color_top[0] * (1 - y/cert_height) + background_color_bottom[0] * (y/cert_height))
        g = int(background_color_top[1] * (1 - y/cert_height) + background_color_bottom[1] * (y/cert_height))
        b = int(background_color_top[2] * (1 - y/cert_height) + background_color_bottom[2] * (y/cert_height))
        draw.line([(0, y), (cert_width, y)], fill=(r, g, b))

    # Load fonts (make sure you have these or fallback to default)
    try:
        title_font = ImageFont.truetype("GreatVibes-Regular.ttf", 80)
        name_font = ImageFont.truetype("Poppins-Bold.ttf", 60)
        info_font = ImageFont.truetype("Poppins-Regular.ttf", 36)
    except:
        # fallback
        title_font = ImageFont.truetype("arial.ttf", 80)
        name_font = ImageFont.truetype("arial.ttf", 60)
        info_font = ImageFont.truetype("arial.ttf", 36)

    # Draw a cute soft border
    border_color = (255, 192, 203) # Light pastel pink
    border_thickness = 10
    draw.rounded_rectangle([(20, 20), (cert_width-20, cert_height-20)], radius=30, outline=border_color, width=border_thickness)

    # Add a cute "Gold Seal" emoji 🏅
    seal_text = "🏅"
    seal_font = ImageFont.truetype("arial.ttf", 100)
    draw.text((cert_width - 160, 50), seal_text, font=seal_font, fill=(255, 215, 0)) # Gold color

    # Title
    title = "Certificate of Completion"
    title_w, title_h = draw.textsize(title, font=title_font)
    draw.text(((cert_width - title_w)/2, 120), title, font=title_font, fill=(255, 105, 180)) # Hot pink

    # Name
    name_text = name
    name_w, name_h = draw.textsize(name_text, font=name_font)
    draw.text(((cert_width - name_w)/2, 280), name_text, font=name_font, fill=(75, 0, 130)) # Indigo

    # Course info
    course_text = f"has successfully completed the course:"
    course_w, course_h = draw.textsize(course_text, font=info_font)
    draw.text(((cert_width - course_w)/2, 400), course_text, font=info_font, fill=(128, 0, 128)) # Purple

    course_name_text = f"'{course}'"
    course_name_w, course_name_h = draw.textsize(course_name_text, font=info_font)
    draw.text(((cert_width - course_name_w)/2, 450), course_name_text, font=info_font, fill=(255, 20, 147)) # Deep pink

    # Date
    date_text = f"Date: {date}"
    date_w, date_h = draw.textsize(date_text, font=info_font)
    draw.text((cert_width - date_w - 50, cert_height - date_h - 50), date_text, font=info_font, fill=(75, 0, 130)) # Indigo

    # Save the certificate
    certificate.save(output_path)
    print(f"Certificate saved at {output_path} 🎀✨")
