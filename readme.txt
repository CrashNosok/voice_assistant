установка python (не щабудь про галочку "add pip to PATH"
https://www.python.org/

системные модули:
pip install pywin32
pip install pypiwin32

преобразование текста в речь
https://pypi.org/project/pyttsx3/
pip install pyttsx3

запусти файл test_vote.py (он должен проговорить фразу. если не сработало, значит что-то сделано не так)

распознование речи (через google API)
https://pypi.org/project/SpeechRecognition/
pip install SpeechRecognition

считывание речи с микрофона (скорее всего не будет работать на windows, если не сработало, смотри ссылку ниже)
https://pypi.org/project/PyAudio/
pip install PyAudio

считывание речи с микрофона (собранный бинарник. я его уже скачал. он лежит в папке)
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
название - PyAudio‑0.2.11‑cp37‑cp37m‑win32.whl
эту команду надо запускать находясь в той же дирректории. или использовать абсолютный путь типа (pip install "F:\for programming\голосовой помощник\PyAudio-0.2.11-cp37-cp37m-win32.whl")
pip install PyAudio‑0.2.11‑cp37‑cp37m‑win32.whl

ищем индекс микрофона (у меня получилось device_index=1. попробуй тоже 1 использовать)
(отсюда берйм код для find_micro.py)
https://pypi.org/project/SpeechRecognition/

протестим распознавание речи:
запускаешь файл test_speach_recognition.py 
и говоришь например "собака съела товар"
потом ждёшь...
и видишь запись: "Вы сказали: собака съела товар"

устанавливаем модуль для нечёткого сравнения (чтобы можно было давать нечёткие команды)
https://pypi.org/project/fuzzywuzzy/
pip install fuzzywuzzy

установим RHVoice-v0.4-a2-setup из архива в папке для мужского голоса (на винде по дефолту только женский русский)
можно будет поменять на женский в любом случае



