import cloudinary
import cloudinary.uploader

cloudinary.config( 
    cloud_name = "du2pl8act", 
    api_key = "647865875477856", 
    api_secret = "pKZIK9CUplTQYMk4XLkl9_r-b9E", # Click 'View API Keys' above to copy your API secret
    secure=True
)

def upload_image_to_cloudinary(image):
    """Upload an image to Cloudinary and return the URL."""
    if image:
        # Upload the image to Cloudinary
        upload_result = cloudinary.uploader.upload(image)
        return upload_result['secure_url']  # Return the URL of the uploaded image
    return None
