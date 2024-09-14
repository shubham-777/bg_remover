"""
Author      : Shubham Ahinave
Created at  : 02/09/24
"""
import io
import os
from datetime import datetime

from PIL import Image
from flask import (
    Blueprint, render_template, request, jsonify, send_file
)
from flask import current_app as curr_app
from rembg import remove, new_session

from app.core.helper import send_email

bp = Blueprint('bg_remove', __name__, url_prefix='/bg_remove', template_folder='templates/bg_remove')


@bp.route('/')
def index():
    sample_img_dir = os.path.join(bp.root_path, 'static', 'sample_images')
    sample_images = [os.path.join('sample_images', file_name) for file_name in os.listdir(sample_img_dir)]
    return render_template('bg_remove/index.html', sample_images=sample_images)

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
            input_format = pil_image_obj.format if pil_image_obj.format else 'JPEG'  # Default to JPEG if format is None

            model_name = "unet"
            rembg_session = new_session(model_name)
            output_image = remove(pil_image_obj, bgcolor=(255, 255, 255, 255), session=rembg_session,
                                  alpha_matting=True, alpha_matting_foreground_threshold=270,
                                  alpha_matting_background_threshold=15, alpha_matting_erode_size=11,
                                  post_process_mask=True)
            if output_image.mode == 'RGBA':
                background = Image.new('RGB', output_image.size, (255, 255, 255))
                background.paste(output_image, (0, 0), output_image)
                output_image = background
            # Save image to a BytesIO object
            img_bytes = io.BytesIO()
            output_image.save(img_bytes, format=input_format)
            img_bytes.seek(0)
            mime_type = f'image/{input_format.lower()}'
            return send_file(img_bytes, mimetype=mime_type, as_attachment=True,
                             download_name='bg_remover_'+image_file.filename)
            # return render_template('bg_remove/index.html', img_src=url_for_image)
        except Exception as e:
            print(e)
            return jsonify({'error': str(e)}), 500
    else:
        return render_template('bg_remove/index.html')

@bp.route('/feedback', methods=['POST', 'GET'])
def feedback():
    if request.method == 'POST':
        feedback_dct = request.form.to_dict()
        feedback_dct['received_at'] = datetime.now().strftime('%d %b, %Y, %H:%M:%S')
        send_email(
            to=feedback_dct.get('email'),
            subject="BG Remover | Feedback send!",
            template_name='notify_feedback_to_user.html',
            template_context={'feedback': feedback_dct},
        )
        send_email(
            to=curr_app.config.get('MAIL_DEFAULT_SENDER'),
            subject="BG Remover | New Feedback Received!",
            template_name='notify_feedback_to_admin.html',
            template_context={'feedback': feedback_dct},
        )
        return render_template('bg_remove/feedback.html')
    elif request.method == 'GET':
        return render_template('bg_remove/feedback.html')