from moviepy.editor import *
import scipy.io as sio

#   video 1_1 - 32_3

'''
for primo in range(1, 33):
    for secondo in range(1, 4):
        videoName = str(primo)+"_"+str(secondo)+"_crop.mp4"
        etichetta = str(primo) + "_" + str(secondo) + "_label.mat"

        file = sio.loadmat("C:/Users/EMANUELE/Desktop/etichette/" + etichetta)

        i = 1
        for all in file['tlabs'][0][0]:
            video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/"+videoName).subclip((all[0] / 30),
                                                                                            (all[1] / 30))
            video.write_videofile("1/1x" + str(primo) + "_" + str(secondo) + "x" + str(i) + ".mp4")
            video.close()
            i = i + 1

        i = 1
        for all in file['tlabs'][1][0]:
            video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/" + videoName).subclip((all[0] / 30),
                                                                                          (all[1] / 30))
            video.write_videofile("2/2x" + str(primo) + "_" + str(secondo) + "x" + str(i) + ".mp4")
            video.close()
            i = i + 1

        i = 1
        for all in file['tlabs'][2][0]:
            video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/" + videoName).subclip((all[0] / 30),
                                                                                          (all[1] / 30))
            video.write_videofile("3/3x" + str(primo) + "_" + str(secondo) + "x" + str(i) + ".mp4")
            video.close()
            i = i + 1

        i = 1
        for all in file['tlabs'][3][0]:
            video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/" + videoName).subclip((all[0] / 30),
                                                                                          (all[1] / 30))
            video.write_videofile("4/4x" + str(primo) + "_" + str(secondo) + "x" + str(i) + ".mp4")
            video.close()
            i = i + 1

        i = 1
        for all in file['tlabs'][4][0]:
            video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/" + videoName).subclip((all[0] / 30),
                                                                                          (all[1] / 30))
            video.write_videofile("5/5x" + str(primo) + "_" + str(secondo) + "x" + str(i) + ".mp4")
            video.close()
            i = i + 1
'''

#   video 41_2

'''
file = sio.loadmat("C:/Users/EMANUELE/Desktop/etichette/41_2_label.mat")
i = 1
for all in file['tlabs'][0][0]:
    video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/41_2_crop.mp4").subclip((all[0] / 30), (all[1] / 30))
    video.write_videofile("1/1x41_2x" + str(i) + ".mp4")
    video.close()
    i = i + 1

i = 1
for all in file['tlabs'][1][0]:
    video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/41_2_crop.mp4").subclip((all[0] / 30), (all[1] / 30))
    video.write_videofile("2/2x41_2x" + str(i) + ".mp4")
    video.close()
    i = i + 1

i = 1
for all in file['tlabs'][2][0]:
    video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/41_2_crop.mp4").subclip((all[0] / 30), (all[1] / 30))
    video.write_videofile("3/3x41_2x" + str(i) + ".mp4")
    video.close()
    i = i + 1

i = 1
for all in file['tlabs'][3][0]:
    video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/41_2_crop.mp4").subclip((all[0] / 30), (all[1] / 30))
    video.write_videofile("4/4x41_2x" + str(i) + ".mp4")
    video.close()
    i = i + 1

i = 1
for all in file['tlabs'][4][0]:
    video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/41_2_crop.mp4").subclip((all[0] / 30), (all[1] / 30))
    video.write_videofile("5/5x41_2x" + str(i) + ".mp4")
    video.close()
    i = i + 1
'''

#   video 33_1 - 41_1

'''
for primo in range(33, 42):
    for secondo in range(1, 2):
        videoName = str(primo)+"_"+str(secondo)+"_crop.mp4"
        etichetta = str(primo) + "_" + str(secondo) + "_label.mat"

        file = sio.loadmat("C:/Users/EMANUELE/Desktop/etichette/" + etichetta)

        i = 1
        for all in file['tlabs'][0][0]:
            video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/"+videoName).subclip((all[0] / 30),
                                                                                            (all[1] / 30))
            video.write_videofile("1/1x" + str(primo) + "_" + str(secondo) + "x" + str(i) + ".mp4")
            video.close()
            i = i + 1

        i = 1
        for all in file['tlabs'][1][0]:
            video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/" + videoName).subclip((all[0] / 30),
                                                                                          (all[1] / 30))
            video.write_videofile("2/2x" + str(primo) + "_" + str(secondo) + "x" + str(i) + ".mp4")
            video.close()
            i = i + 1

        i = 1
        for all in file['tlabs'][2][0]:
            video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/" + videoName).subclip((all[0] / 30),
                                                                                          (all[1] / 30))
            video.write_videofile("3/3x" + str(primo) + "_" + str(secondo) + "x" + str(i) + ".mp4")
            video.close()
            i = i + 1

        i = 1
        for all in file['tlabs'][3][0]:
            video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/" + videoName).subclip((all[0] / 30),
                                                                                          (all[1] / 30))
            video.write_videofile("4/4x" + str(primo) + "_" + str(secondo) + "x" + str(i) + ".mp4")
            video.close()
            i = i + 1

        i = 1
        for all in file['tlabs'][4][0]:
            video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/" + videoName).subclip((all[0] / 30),
                                                                                          (all[1] / 30))
            video.write_videofile("5/5x" + str(primo) + "_" + str(secondo) + "x" + str(i) + ".mp4")
            video.close()
            i = i + 1
'''

#   video dataset SA

'''
for primo in range(1, 16):
    videoName = str(primo) + ".mp4"
    etichetta = str(primo) + ".mat"

    file = sio.loadmat("C:/Users/EMANUELE/Desktop/etichette/" + etichetta)

    i = 1
    for all in file['tlabs'][0][0]:
        video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/"+ videoName).subclip((all[0]), (all[1]))
        video.write_videofile("1/1x" + str(primo) + "x" + str(i) + ".mp4")
        video.close()
        i = i + 1

    i = 1
    for all in file['tlabs'][1][0]:
        video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/" + videoName).subclip((all[0]), (all[1]))
        video.write_videofile("2/2x" + str(primo) + "x" + str(i) + ".mp4")
        video.close()
        i = i + 1

    i = 1
    for all in file['tlabs'][2][0]:
        video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/" + videoName).subclip((all[0]), (all[1]))
        video.write_videofile("3/3x" + str(primo) + "x" + str(i) + ".mp4")
        video.close()
        i = i + 1

    i = 1
    for all in file['tlabs'][3][0]:
        video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/" + videoName).subclip((all[0]), (all[1]))
        video.write_videofile("4/4x" + str(primo) + "x" + str(i) + ".mp4")
        video.close()
        i = i + 1

    i = 1
    for all in file['tlabs'][4][0]:
        video = VideoFileClip("C:/Users/EMANUELE/Desktop/video/" + videoName).subclip((all[0]), (all[1]))
        video.write_videofile("5/5x" + str(primo) + "x" + str(i) + ".mp4")
        video.close()
        i = i + 1
'''


