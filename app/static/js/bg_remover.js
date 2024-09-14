document.addEventListener('DOMContentLoaded', function() {
    const imageInput = document.getElementById('imageInput');
    const imagePreview = document.getElementById('imagePreview');
    const downloadButton = document.getElementById('download-button');

    // Function to update the download button URL
    function updateDownloadUrl(url) {
        downloadButton.href = url;
        downloadButton.download = 'bg-removed';
    }

    // Handle sample image selection
    document.getElementById('sampleImages').addEventListener('click', function(event) {
        if (event.target && event.target.matches('.sample-image')) {
            const src = event.target.src;

            // Set the image preview
            imagePreview.src = src;

            // Set the download URL to the selected image
            updateDownloadUrl(src);

            // Simulate file selection
            fetch(src)
                .then(response => response.blob())
                .then(blob => {
                    const file = new File([blob], 'sample-image.jpg', { type: blob.type });
                    const dataTransfer = new DataTransfer();
                    dataTransfer.items.add(file);
                    imageInput.files = dataTransfer.files;
                    document.querySelector('.preview-container').style.display = 'block';
                });
        }
    });

    // Handle file input change
    imageInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.src = e.target.result;
                document.querySelector('.preview-container').style.display = 'block';
                updateDownloadUrl(e.target.result);
            };
            reader.readAsDataURL(file);
        }
    });

    // Handle clear button click
    document.getElementById('clearButton').addEventListener('click', function() {
        imageInput.value = ''; // Clear file input
        imagePreview.src = ''; // Clear image source
        document.querySelector('.preview-container').style.display = 'none'; // Hide preview container
    });

    // Handle submit button click
    document.getElementById('submitButton').addEventListener('click', function() {
        if (imageInput.files.length === 0) {
            alert("No image selected!!");
            return;
        }

        showLoader();
        const formData = new FormData();
        formData.append('image', imageInput.files[0]);

        $.ajax({
            type: "POST",
            url: "process",
            data: formData,
            async: true,
            enctype: "multipart/form-data",
            cache: false,
            processData: false,
            contentType: false,
            xhrFields: {
                responseType: 'blob' // Ensure the response is treated as binary
            },
            success: function(response) {
                hideLoader();
                const url = URL.createObjectURL(response);
                imagePreview.src = url;
                updateDownloadUrl(url);
                document.querySelector('.preview-container').style.display = 'block';
            },
            error: function(xhr, status, error) {
                hideLoader();
                console.error("Error occurred: ", status, error);
            }
        });
    });
});
