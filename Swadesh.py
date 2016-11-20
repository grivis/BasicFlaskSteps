'''
Программа реализует анкетирование по 20 словам из списка Сводеша.
Дополнительно к программе необходимы HTML файлы в папке templates
swform.html thanks.html search.html stats.html
Реализованы страницы:
<hostname:port>/ - сама анкета
<hostname:port>/stats - статистика по анкетам
<hostname:port>/search - поиск по анкетам и результаты поиска
<hostname:port>/json - вывод данных всех анкет в формате JSON
'''

# Импортируем нужные нам модули
from flask import Flask
from flask import render_template, request
from time import *
import pickle
import glob, os
import json

app = Flask(__name__)

# Две выборки из списка Сводеша для русского языка
# swlst = ['грудь','сердце','печень','пить','кушать','кусать','видеть','слышать','знать','спать','умирать',
#          'убивать','плавать', 'летать','гулять','приходить','лежать','сидеть','стоять', 'дать']
swlst = ['стопа', 'нога', 'колено', 'рука', 'крыло', 'живот', 'внутренности', 'шея',
         'спина', 'грудь', 'сердце', 'печень', 'пить', 'кушать', 'кусать', 'сосать',
         'плевать', 'блевать', 'дуть', 'дышать']
# Названия месяцев для вывода на страницу статистики
months = ['января', 'февраля', 'марта', 'апреля', 'мая',
          'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']


@app.route('/')
def form():
    # Дата и время для регистрации анкеты
    ticks = time()
    lt = localtime(ticks)
    ddNow = str(lt.tm_mday)
    mmNow = str(lt.tm_mon)
    hourNow = str(lt.tm_hour)
    minNow = str(lt.tm_min)
    # Дни, месяцы, часы, минуты должны быть двузначными
    if len(ddNow) < 2:
        ddNow = '0' + ddNow
    if len(mmNow) < 2:
        mmNow = '0' + mmNow
    if len(hourNow) < 2:
        hourNow = '0' + hourNow
    if len(minNow) < 2:
        minNow = '0' + minNow
    # Cловарь для хранения результатов анкеты
    swdic = {}
    # Чтение анкеты и заполнение словаря
    if request.args:
        swdic['name'] = request.args['name']
        swdic['language'] = request.args['language'].strip().capitalize()
        swdic[swlst[0]] = request.args['wrd0']
        swdic[swlst[1]] = request.args['wrd1']
        swdic[swlst[2]] = request.args['wrd2']
        swdic[swlst[3]] = request.args['wrd3']
        swdic[swlst[4]] = request.args['wrd4']
        swdic[swlst[5]] = request.args['wrd5']
        swdic[swlst[6]] = request.args['wrd6']
        swdic[swlst[7]] = request.args['wrd7']
        swdic[swlst[8]] = request.args['wrd8']
        swdic[swlst[9]] = request.args['wrd9']
        swdic[swlst[10]] = request.args['wrd10']
        swdic[swlst[11]] = request.args['wrd11']
        swdic[swlst[12]] = request.args['wrd12']
        swdic[swlst[13]] = request.args['wrd13']
        swdic[swlst[14]] = request.args['wrd14']
        swdic[swlst[15]] = request.args['wrd15']
        swdic[swlst[16]] = request.args['wrd16']
        swdic[swlst[17]] = request.args['wrd17']
        swdic[swlst[18]] = request.args['wrd18']
        swdic[swlst[19]] = request.args['wrd19']
        # Имя файла формируется по шаблону с учетом месяца, дня, часа и минуты
        # Один файл хранит одну заполненную анкету
        f = open('swdic' + mmNow + ddNow + hourNow + minNow + '.dic', 'wb')
        pickle.dump(swdic, f)
        f.close()
        return render_template('thanks.html')
    # В шаблон HTML передаются сами слова из списка Сводеша
    return render_template('swform.html', sw0=swlst[0], sw1=swlst[1], sw2=swlst[2], sw3=swlst[3], sw4=swlst[4],
                           sw5=swlst[5], sw6=swlst[6], sw7=swlst[7], sw8=swlst[8], sw9=swlst[9], sw10=swlst[10],
                           sw11=swlst[11], sw12=swlst[12], sw13=swlst[13], sw14=swlst[14],
                           sw15=swlst[15], sw16=swlst[16], sw17=swlst[17], sw18=swlst[18], sw19=swlst[19])


@app.route('/stats')
def stats():
    # Статистика по заполненным анкетам
    ticks = time()
    lt = localtime(ticks)
    hourNow = str(lt.tm_hour)
    minNow = str(lt.tm_min)
    ddNow = str(lt.tm_mday)
    mmNow = str(lt.tm_mon)
    # Дни, месяцы, часы, минуты должны быть двузначными
    if len(ddNow) < 2:
        ddNow = '0' + ddNow
    if len(mmNow) < 2:
        mmNow = '0' + mmNow
    if len(hourNow) < 2:
        hourNow = '0' + hourNow
    if len(minNow) < 2:
        minNow = '0' + minNow
    os.chdir("./")
    count = 0
    ctoday = 0
    cthishour = 0
    today = mmNow + ddNow
    langset = set()
    for file in glob.glob("swdic*.dic"):
        count += 1
        f = open(file, 'rb')
        dic = pickle.load(f)
        if file[5:9] == today:
            ctoday += 1
        if file[9:11] == hourNow:
            cthishour += 1
        langset.add(dic['language'])
        f.close()
    return render_template('stats.html', day=ddNow, month=months[int(mmNow) - 1], hour=hourNow, minute=minNow,
                           count=count, ctoday=ctoday, cthishour=cthishour, clang=len(langset))


@app.route('/search')
def searchform():
    # Поиск по анкетам - выбрать одно слова из выпадающего меню
    # HTML текст, который надо выводить в браузер
    ResultHTML =   '''
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Результаты поиска</title>
        <style>
        table, th, td {
        border: 2px solid #381c76;
        border-collapse: collapse;}
        th, td {
        padding: 15px;}
    </style>
    </head>
    <body style="font-family:Arial;">
    <h1 style="color:#381c76">Значения выбранного слова:</h1>

    <p></p>
    <table style="width:50%">
      <tr>
        <th>Респондент</th>
        <th>Язык</th>
        <th>Значение слова</th>
      </tr>
    '''
    # Окончание HTML текста
    ResultHTMLEnd = '''
    </table>
    <p style="color:#381c76">Благодарим за использование нашего сервиса!</p>
    </body>
    </html>
        '''


    if request.args:
        # Выбор слова для подбора вариантов
        searchindex = request.args['searchword']
        searchword = swlst[int(searchindex)]
        # Обход имеющихся анкет
        os.chdir("./")
        resultstring = ''
        for file in glob.glob("swdic*.dic"):
            f = open(file, 'rb')
            dic = pickle.load(f)
            word = dic.get(searchword, '---')
            language = dic.get('language', '---')
            responder = dic.get('name', '---')
            resultstring += '<tr>'+'<td>'+responder+'</td>' \
                             +'<td>'+language+'<td>'+word+'</td>'+'</tr>'+'\n '
            f.close()

        # Выдаем результат в виде HTML документа, в который вставлена таблица результатов поиска
        # Шаблон HTML для результатов не готовится заранее в виде файла, формируется на лету
        return ResultHTML + resultstring + ResultHTMLEnd
    # вновь возвращаем исходную форму, если не выбран предмет поиска
    return render_template('search.html', sw0=swlst[0], sw1=swlst[1], sw2=swlst[2], sw3=swlst[3], sw4=swlst[4],
                           sw5=swlst[5], sw6=swlst[6], sw7=swlst[7], sw8=swlst[8], sw9=swlst[9], sw10=swlst[10],
                           sw11=swlst[11], sw12=swlst[12], sw13=swlst[13], sw14=swlst[14],
                           sw15=swlst[15], sw16=swlst[16], sw17=swlst[17], sw18=swlst[18], sw19=swlst[19])



@app.route('/json')
def jsonout():
    # Выводим все анкеты в виде JSON
    os.chdir("./")
    alldicts = {}
    for file in glob.glob('swdic*.dic'):
        f = open(file, 'rb')
        dic = pickle.load(f)
        alldicts[file] = dic
        f.close()
    json_string = json.dumps(alldicts)
    return json_string

# Вот, собственно, и все!

if __name__ == '__main__':
    app.run(debug=True)
