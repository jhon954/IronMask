import pyaudio, wave, serial, time
from pydub import AudioSegment
from tensorflow.keras.models import model_from_json 
import scipy.io.wavfile as wav
from python_speech_features import mfcc
import numpy as np





# carga el json y crea el modelo
json_file = open('model/model2silencios.json', 'r')
loaded_model_json = json_file.read()
 
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# se cargan los pesos (weights) en el nuevo modelo
loaded_model.load_weights("model/model2silencios.h5")
print("Modelo cargado desde el PC")
# se evalua el modelo cargado con los datos de los test
#loaded_model.compile(optimizer = "adam", loss = "categorical_crossentropy", metrics = ["accuracy"])
#score = loaded_model.evaluate(X_test_std, Y_test, verbose=0)
#print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))

def feature_extraction(path):
    (rate, signal) = wav.read(path)
    mfcc0 = mfcc(signal, rate, nfft=1200)

    return mfcc0


def grabacion(pathDest):
    Format=pyaudio.paInt16
    Channels=1
    Rate=44100
    Chunk=1024
    Duracion=5

    audio=pyaudio.PyAudio()

    stream=audio.open(format=Format, channels=Channels,
                        rate=Rate, input=True,
                        frames_per_buffer=Chunk)

    print('grabando....')
    frames=[]

    for i in range(0,int(Rate/Chunk*Duracion)):
        data=stream.read(Chunk)
        frames.append(data)
    print('grabacion terminada')


    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile=wave.open(pathDest, 'wb')
    waveFile.setnchannels(Channels)
    waveFile.setsampwidth(audio.get_sample_size(Format))
    waveFile.setframerate(Rate)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    print('Guardado')

    print('Recortando')
    audSeg = AudioSegment.from_wav(pathDest)
    audSeg = audSeg[2000:4000]
    dst='grabaciones/grabacion2seg.wav'
    audSeg.export(dst, format="wav")
    print('Recortado')
    
    features = feature_extraction(dst)
    mfff_ = np.reshape(features, (features.shape[0]*features.shape[1]))
    mff_ = np.reshape(mfff_, (1,-1))
    print('Caracteristicas extraidas')

    #os.remove(dst)
    #os.remove(pathDest)

    return mff_


def IronMask(port):
    a = 0
    ser = serial.Serial(port, 9600)
    #ser.open()
    time.sleep(2)
    while a==0:
        features = grabacion('grabaciones/grabacion.wav')
        ans = loaded_model.predict(features)
        for i in range(2):
            if(ans[0,i] < 0.5):
                ans[0,i]=0
            else:
                ans[0,i]=1

        if ans[0][1] == 1:
            ser.write(b'A')
            print("King")
            print(ans)
        else:
            ser.write(b'B')
            print("Another One")
            print(ans)
        
        print("A")
        print('Presiona 0 para una nueva grabacion')
        a = int(input())

if __name__ == "__main__":
    IronMask('/dev/ttyACM0')