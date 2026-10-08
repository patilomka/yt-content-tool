import os
from flask import Flask, render_template, request, send_file
import yt_dlp

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>YouTube Downloader</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial, sans-serif; background: #f4f4f9; padding: 20px; text-align: center; }
            .container { max-width: 500px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            input[type="text"] { width: 80%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px; }
            button { background: #ff0000; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-size: 16px; }
            button:hover { background: #cc0000; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>YouTube Video Downloader</h2>
            <form action="/download" method="post">
                <input type="text" name="url" placeholder="YouTube Video URL यहाँ डालें..." required><br>
                <button type="submit">Download</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloaded_video.mp4',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return send_file('downloaded_video.mp4', as_attachment=True)
    except Exception as e:
        return f"An error occurred: {str(e)}"

port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
  
