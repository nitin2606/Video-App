from flask import Flask, render_template

app = Flask(__name__)

# Replace 'video_url' with the actual video URL from Cloudinary
video_url = "https://res.cloudinary.com/dam12ojlp/video/upload/v1703835359/reels/vid1_eq0z7e.mp4"

@app.route('/')
def index():
    return render_template('index.html', video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True)
