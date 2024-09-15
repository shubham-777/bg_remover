# BG Remover: A Flask Background Remover Web App

## Overview

This Flask web application allows users to remove backgrounds from images. It supports the upload of custom images or selection from a set of sample images. After processing, users can download the image with the background removed. The application also includes a feedback page where users can send feedback to the admin.

## Features

- **Upload Custom Image**: Allows users to upload their own image for background removal.
- **Choose from Sample Images**: Provides a selection of sample images to choose from.
- **Download Processed Image**: Users can download the image with the background removed.
- **Feedback Page**: Users can send feedback through a feedback form which is then emailed to the admin and user.

## Installation and Usage

### Using Docker

1. **Pull the Docker image:**
   ```bash
   docker pull shubham517/bg_remover
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 5000:5000 shubham517/bg_remover
   ```

   This command will start the application and map port `5000` on your local machine to port `5000` in the Docker container.

3. **Access the application:**
   Open your web browser and go to `http://localhost:5000/bg_remove/` to use the app.

## Configuration

- **Email Settings**: Ensure that your email settings are configured properly in the Flask app configuration to enable the feedback email functionality.
- **Sample Images**: Place sample images in the `static/sample_images` directory for users to choose from.

## Contributing

Feel free to submit issues, feature requests, or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact Shubham Ahinave at [codesign.developers@gmail.com
](mailto:codesign.developers@gmail.com).