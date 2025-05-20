import speech_recognition as sr

def reconocimiento_microfono():
    audio = sr.Recognizer()
    asistente = "Asistente de voz:"
    while True:
        with sr.Microphone() as source:
            print("Habla algo...")
            audio_data = audio.listen(source)
        try:
            texto = audio.recognize_google(audio_data, language="es-ES")
            print("Has dicho: " + texto)
            if texto.strip().lower() == "hola":
                print(asistente + " hola, como estas?")
            elif texto.strip().lower() == "Salir" or "Adios":
                print("hasta luego.")
                break    
        except sr.UnknownValueError:
            print("No se pudo entender el audio, intenta de nuevo.")
        except sr.RequestError as e:
            print(f"Error al solicitar resultados; {e}")
            break

if __name__ == "__main__":
    reconocimiento_microfono()

