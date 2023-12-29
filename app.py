from flask import Flask, render_template
#import cloudinary
#import cloudinary.uploader
#import cloudinary.api

app = Flask(__name__)

# Configure Cloudinary with your cloud_name, api_key, and api_secret
'''cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)'''

# Replace 'video_urls' with the actual video URLs from Cloudinary
video_urls = [
    "https://res.cloudinary.com/dam12ojlp/video/upload/v1703835359/reels/vid1_eq0z7e.mp4"

    # Add more video URLs as needed
]

@app.route('/')
def index():
    return render_template('index.html', video_urls=video_urls)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()
