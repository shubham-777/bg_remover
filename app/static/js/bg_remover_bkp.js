   document.getElementById('imageInput').addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {

                    const img = document.getElementById('imagePreview');
                    img.src = e.target.result;
                    document.querySelector('.preview-container').style.display = 'block'; // Show preview container
                    updateDownloadUrl(e.target.result);
                };
                reader.readAsDataURL(file);
            }
        });

      document.getElementById('clearButton').addEventListener('click', function() {
            const fileInput = document.getElementById('imageInput');
            const img = document.getElementById('imagePreview');
            fileInput.value = ''; // Clear file input
            img.src = ''; // Clear image source
            document.querySelector('.preview-container').style.display = 'none'; // Hide preview container
        });
        document.getElementById('submitButton').addEventListener('click', function() {
            if ($('#imageInput').prop('files').length ==0){
                alert("No image selected!!");
                return
            }

            showLoader();
            var form_data = new FormData();
            form_data.append('image', $('#imageInput').prop('files')[0]);
            $.ajax({
                type: "POST",
                url: "process",
                data: form_data,
                async: true,
                enctype: "multipart/form-data",
                cache: false,
				processData:false,
				contentType:false,
				 xhrFields: {
                    responseType: 'blob'  // Ensure the response is treated as binary
                },
                success: function (response) {
                    hideLoader();
                    var url = URL.createObjectURL(response);
                    const img = document.getElementById('imagePreview');
                    img.src = url;
                    updateDownloadUrl(url);
                    // Update the download button href dynamically

                },
                 error: function (xhr, status, error) {
                    hideLoader();
                    console.error("Error occurred: ", status, error);
                }
            });
        });

function updateDownloadUrl(url){
    const downloadButton = document.getElementById('download-button');
    downloadButton.href = url;
    downloadButton.download = 'bg-removed';
}