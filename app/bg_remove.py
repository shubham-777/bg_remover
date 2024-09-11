"""
Author      : Shubham Ahinave
Created at  : 02/09/24
"""
import os
from datetime import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, send_from_directory
)
from PIL import Image
from rembg import remove, new_session

bp = Blueprint('bg_remove', __name__, url_prefix='/bg_remove', template_folder='templates/bg_remove')


@bp.route('/')
def index():
    return render_template('bg_remove/index.html')

@bp.route('/process', methods=['POST', 'GET'])
def process():
    if request.method =='POST':
        if 'image' not in request.files:
            return jsonify({'error': 'No image file found in request'}), 400

        image_file = request.files['image']
        if not image_file:
            return jsonify({'error': 'No file selected'}), 400

        try:
            pil_image_obj = Image.open(image_file.stream)
            model_name = "unet"
            rembg_session = new_session(model_name)
            output_image = remove(pil_image_obj, bgcolor=(255, 255, 255, 255), session=rembg_session,
                                  alpha_matting=True, alpha_matting_foreground_threshold=270,
                                  alpha_matting_background_threshold=20, alpha_matting_erode_size=11,
                                  post_process_mask=True)
            process_image_dir = os.path.join(bp.root_path, 'static', 'processed_img')
            if not os.path.exists(process_image_dir):
                os.mkdir(process_image_dir)
            output_img_path = os.path.join(process_image_dir, image_file.filename)
            if output_image.mode == 'RGBA':
                background = Image.new('RGB', output_image.size, (255, 255, 255))
                background.paste(output_image, (0, 0), output_image)
                output_image = background
            output_image.save(output_img_path)
            url_for_image = f"/static/processed_img/{image_file.filename}"
            return jsonify({'image_url': url_for_image})
            # return render_template('bg_remove/index.html', img_src=url_for_image)
        except Exception as e:
            print(e)
            return jsonify({'error': str(e)}), 500
    else:
        return render_template('bg_remove/index.html')

@bp.route('/feedback', methods=['POST', 'GET'])
def feedback():
    if request.method == 'POST':
        print('Form received!')
        feedback_dct = request.form.to_dict()
        feedback_dct['received_at'] = datetime.now().strftime('%d %b, %Y, %H:%M:%S')
        print(feedback_dct)
        return render_template('bg_remove/feedback.html')
    elif request.method == 'GET':
        return render_template('bg_remove/feedback.html')