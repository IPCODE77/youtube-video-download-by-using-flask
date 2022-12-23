from flask import Flask,render_template,redirect,request,jsonify
from pytube import YouTube
app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def download():
    return render_template('index.html')
@app.route('/video',methods = ['GET','POST'])
def check():
    if request.method == "POST":
        qtc_data = request.get_json()
        print(qtc_data)
        print(qtc_data[0]['url'])
        print(type(qtc_data))
        video_link = video_down(qtc_data[0]['url'])
        print(f'test {video_link}')
    results = {'processed': video_link}
    # all set just change the result value with video_down eturn value
    return jsonify(results)
def video_down(url1):
    video = False
    if request.method == 'POST':
        try:
            yt = YouTube(url1)
            yt.streams.filter(file_extension="mp4").get_lowest_resolution().download('./youtube_video')
            video = True
        except:
            video = False
    return video

@app.route('/medium',methods = ['GET','POST'])
def medium():
    if request.method == "POST":
        qtc_data = request.get_json()
        print(qtc_data[0]['url'])
        video_link = video_down2(qtc_data[0]['url'])
        # print(f'test {video_link}')
    results = {'processed': video_link}
    # all set just change the result value with video_down eturn value
    return jsonify(results)
def video_down2(url1):
    video = False
    if request.method == 'POST':
        try:
            yt = YouTube(url1)
            yt.streams.filter(file_extension="mp4").get_by_resolution('360p').download('./youtube_video')
            video = True
        except:
            video = False
    return video


@app.route('/low',methods = ['GET','POST'])
def low():
    if request.method == "POST":
        qtc_data = request.get_json()
        print(qtc_data)
        print(qtc_data[0]['url'])
        print(type(qtc_data))
        video_link = video_down3(qtc_data[0]['url'])
        print(f'test {video_link}')
    results = {'processed': video_link}
    # all set just change the result value with video_down eturn value
    return jsonify(results)
def video_down3(url1):
    video = False
    if request.method == 'POST':
        try:
            yt = YouTube(url1)
            yt.streams.filter(file_extension="mp4").get_lowest_resolution().download('./youtube_video')
            video = True
        except:
            video = False
    return video

@app.route('/audio',methods = ['GET','POST'])
def audio():
    return render_template('audio.html')

@app.route('/onlyaudio',methods = ['GET','POST'])
def onlyaudio():
    if request.method == "POST":
        qtc_data = request.get_json()
        print(qtc_data)
        print(qtc_data[0]['url'])
        print(type(qtc_data))
        video_link = video_down4(qtc_data[0]['url'])
        print(f'test {video_link}')
    results = {'processed': video_link}
    # all set just change the result value with video_down eturn value
    return jsonify(results)
def video_down4(url1):
    video = False
    if request.method == 'POST':
        try:
            yt = YouTube(url1)
            yt.streams.filter(file_extension="mp4").get_audio_only().download('./youtube_video')
            video = True
        except:
            video = False
    return video



if __name__=='__main__':
    app.run(debug=True)      