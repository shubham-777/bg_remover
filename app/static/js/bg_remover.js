   document.getElementById('imageInput').addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {

                    const img = document.getElementById('imagePreview');
                    img.src = e.target.result;
                    document.querySelector('.preview-container').style.display = 'block'; // Show preview container
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
            $('#loader').show();
            console.log('loader show kar diya hai')
            var form_data = new FormData();
            form_data.append('image', $('#imageInput').prop('files')[0]);
            $.ajax({
                type: "POST",
                url: "process",
                data: form_data,
                async: true,
                enctype: "multipart/form-data",
                processData: false,
                contentType: false,
                success: function (response) {
                     const img = document.getElementById('imagePreview');
                    img.src = response.image_url;
                      $('#loader').hide();

                },
                 error: function (xhr, status, error) {
                    $('#loader').hide();
                    console.error("Error occurred: ", status, error);
                }
            });
            console.log('fat ke se bahara aarha hai..!')
        });