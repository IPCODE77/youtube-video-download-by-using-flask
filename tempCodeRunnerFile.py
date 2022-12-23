'/medium',methods = ['GET','POST'])
# def check():
#     if request.method == "POST":
#         qtc_data = request.get_json()
#         print(qtc_data)
#         print(qtc_data[0]['url'])
#         print(type(qtc_data))
#         video_link = video_down(qtc_data[0]['url'])
#         print(f'test {video_link}')
#     results = {'processed': video_link}
#     # all set just change the result value with video_down eturn value
#     return jsonify(results)
# def video_down(url1):
#     video = False
#     if request.method == 'POST':
#         try:
#             yt = YouTube(url1)
#             yt.streams.filter(file_extension="mp4").get_by_resolution('360p').download('./youtube_video')
#             video = True
#         except:
#             video = False
#     return video    
