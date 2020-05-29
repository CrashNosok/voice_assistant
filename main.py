import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

# словарь с натройками ассистента:
opts = {
    # вариации имени помощьника
    'alias': ('пупсик', 'пупс', 'пупсимо', 'пупик', 'пупок'),
    # (to be remove) слова, который нужно будет удалить из речевой команды
    'tbr': ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', 'пожалуйста'),
    # все возможные команды ассистента
    'cmds': {
        'ctime': ('текущее время', 'сейчас времени', 'который час'),
        'radio': ('включи музыку', 'воспроизведи радио', 'включи радио'),
        'stupid1': ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты'),
    },
}


# функции
def speak(what):
    # global speak_engine, voices
    print(what)
    speak_engine = pyttsx3.init()
    voices = speak_engine.getProperty('voices')
    # женский голос
    speak_engine.setProperty('voice', voices[0].id)
    speak_engine.say(what)
    speak_engine.runAndWait()
    # speak_engine.stop()
    # del speak_engine
    # speak_engine = pyttsx3.init()
    # voices = speak_engine.getProperty('voices')
    # speak_engine.setProperty('voice', voices[4].id)


# вызывается, когда запишет какую-либо фразу
def callback(recognizer, audio):
    # пытаемся преобразовать параметры в текст
    try:
        voice = recognizer.recognize_google(audio, language='ru-RU')
        print('[log] Распознано:', voice)

        # начинаем читать команды
        if voice.lower().startswith(opts['alias']):
            # вырезаем из текста имена помощьника и слова из списка tbr
            cmd = voice
            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
            # распознаём и выполняем команду:
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print('[log] голос не распознан!')
    except sr.RequestError as e:
        print('[log] Неизвестная ошибка. Проверьте интернет!')


# поиск нечёткой команды, которую получил пупсик
def recognize_cmd(cmd):
    # сравниваем полученную команду со всеми возможными из нашего списка
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC


# преобразовываем команду в действие
def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak(f'Сейчас {now.hour}:{now.minute}')
    elif cmd == 'radio':
        # воспроизвести радио
        # нужно вставить путь до аудио файла
        os.system("hell.mp3")
    elif cmd == 'stupid1':
        speak('Сидит заяц на рельсах. К нему подходит лось из леса. И говорит "ПОДВИНЬСЯ"!!! ахахахахахахахах гыгык')
    else:
        speak('Команда не распознана. повторите!')


# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=1)
with m as source:
    # в течение 1 секунды слушаем фон, чтобы не путать шум с речью человека
    r.adjust_for_ambient_noise(source)

speak('Добрый день, хозяиен')
speak('Пупсик слушает Вас')

# начинаем слушать микрофон в фоне после приветственных фраз
stop_listening = r.listen_in_background(m, callback)
while True:
    time.sleep(0.1)
