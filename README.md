# Анализ программы horos.exe (https://chronologia.org/horos.html)

## Для чего это все:

Где-то год-два назад я познакомился с так называемой **«Новой хронологией»** и, как и многие люди знакомые со школьным курсом Всемирной истории, был удивлен выводами данной теории.

Ознакомиться с теорией и ее выводами можно на официальном сайте [chronologia.org](https://chronologia.org/horos.html), а также на многочисленных интернет-ресурсах, включая:
   - [Wikipedia.org - Новая хронология (Фоменко)](https://ru.wikipedia.org/wiki/%D0%9D%D0%BE%D0%B2%D0%B0%D1%8F_%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F_(%D0%A4%D0%BE%D0%BC%D0%B5%D0%BD%D0%BA%D0%BE));
   - [Wikipedia.org - История «Новой хронологии» (Фоменко)](https://ru.wikipedia.org/wiki/%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F_%C2%AB%D0%9D%D0%BE%D0%B2%D0%BE%D0%B9_%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8%C2%BB_(%D0%A4%D0%BE%D0%BC%D0%B5%D0%BD%D0%BA%D0%BE));

   - [Lurkmore - Фоменко](https://lurkmore.to/%D0%A4%D0%BE%D0%BC%D0%B5%D0%BD%D0%BA%D0%BE)

Мое особое внимание привлекла программа [**horos.exe**](https://chronologia.org/horos.html ), которая служит основным источником проверки точности датировок при изучении древних гороскопов (например в книге ["НОВАЯ ХРОНОЛОГИЯ ЕГИПТА"](https://chronologia.org/bibliography.html))

Файл [README.TXT](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/HOROS/README.TXT) (расположенный в архиве с программой horos.exe). Оригинальная кодировка CP 866.

![README.TXT-01.jpg](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/HOROS/README.TXT-01.jpg)
![README.TXT-02.jpg](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/HOROS/README.TXT-02.jpg)
![README.TXT-03.jpg](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/HOROS/README.TXT-03.jpg)
![README.TXT-04.jpg](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/HOROS/README.TXT-04.jpg)

В итоге я решил проверить работоспособность данной программы и точность ее результатов. В качестве примера, я взял выдержку из книги [**"Новая хронология Египта"**](https://chronologia.org/nx_egypt/index.html) (ссылка на которую указана на странице с программой), а именно разбор [**Дендерского Зодиака**](https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D0%BD%D0%B4%D0%B5%D1%80%D1%81%D0%BA%D0%B8%D0%B9_%D0%B7%D0%BE%D0%B4%D0%B8%D0%B0%D0%BA).

Оригинал на сайте Лувра: [Zodiac of Dendera](https://collections.louvre.fr/en/ark:/53355/cl010028871)

![Dendera zodiac](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/Dendera-and-the-Temple-of-Hathor.jpg)

## Исходные данные для проверки:

1) Архив [**zodiak02.zip**](https://chronologia.org/zodiak02.zip) с программой **horos.exe** ([https://chronologia.org/horos.html](https://chronologia.org/horos.html))

![horos-web-info](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/HOROS/horos-web-info.jpg)

Копии архивов расположены в разделе [resources/HOROS](https://github.com/ponwork/chronologia.org-horos/tree/main/resources/HOROS)

   * [**zodiac.ARJ**](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/HOROS/zodiac.ARJ) MD5 = 9e8e92018e1d530c8c886815df8acb37
   * [**zodiac.zip**](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/HOROS/zodiac.zip) MD5 = a207c77c068e3272e1d65f1c296fd2f7
   * [**zodiak02.rar**](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/HOROS/zodiak02.rar) MD5 = 55f9c69c88619005cec927ce57cb89dd
   * [**zodiak02.zip**](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/HOROS/zodiak02.zip) MD5 = 22c7bd745c6e1c0c63d2bb4ce9287a66

2) Издание ["Новая хронология Египта"](https://chronologia.org/nx_egypt/index.html) Г.В.Носовский и А.Т.Фоменко. Исследования 2000-2001 годов.

![chronologia-dendera.jpg](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/chronologia-dendera.jpg)

3) Дистрибутив Windows XP 
   - файл: **ru_windows_xp_professional_with_service_pack_3_x86_cd_x14-80484.iso** 
   - MD5 = 44143210b620491eb1d21efc0b1a630a
   - примечение: установка выполнена в виде виртуальной машины VirtualBox, активация ОС произведена по телефону. Спасибо Microsoft!

## Проверка. Этап 1. Алгоритмы

Самое удивительное, что автор не приводит ни единого исходного текста программы, по результатам работы которой делаются столь замечательные выводы по датировкам событий мировой истории.

В файле [**README.TXT**]() содержатся лишь упоминания следующих работ:

   - "Расчет планет основан на программе:" [**Numerical expressions for precession formulae and mean elements for the Moon and the planets**](https://adsabs.harvard.edu/full/1994A%26A...282..663S)   [(**копия**)](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/1994A%2BA___282__663S.pdf)
   - "Расчет Луны основан на программе:" [**ELP 2000-85 - A semi-analytical lunar ephemeris adequate for historical times**](https://adsabs.harvard.edu/full/1988A%26A...190..342C)   [(**копия**)](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/1988A%2BA___190__342C.pdf)

Читателю предлагается поверить наслово, что программа **horos.exe** имеет хоть какое-то отношение к расчету датировок.

На этом исследование можно завершить, но я все таки решил проверить работу **horos.exe**, используя различные входные данные и оценить степень правдоподобности результатов как с выводами самих авторов "Новой Хронологии", так и с независимыми источниками.

## Проверка. Этап 2. Примеры работы программы. Вариант полной неопределенности

Для начала кратко опишу работу с программой.

Берем гороскоп (изображение/описание расположения планет, луны и солнца относительно звезд, т.е. зодиакальных символов) и переносим его в виде цифр в файл INPUT.TXT

![README.TXT INPUT.TXT example](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/example-input.txt.jpg)

Также, в описании указано, что:

>ЕСЛИ ПЛАНЕТА НЕ УКАЗАНА В ГОРОСКОПЕ, ТО ЕЕ ГРАНИЦЫ НАДО ЗАДАТЬ ОТ 0 ДО 12,
>А ТОЧКУ ПРИМЕРНОГО РАСПОЛОЖЕНИЯ - 999.

Отсюда приходим к первому, самому простому тесту: заполним все входные данные как "неопределенные", т.е. 0-12 и 999

![input-undefined](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/input-undefined.jpg)

В результате мы получим файл OTVET.TXT размером 131,5 Мб (2 739 383 строк) [**архив с файлом**](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/otvet-full.txt.zip)

Что примечательно, диапозон дат в файле начинается с **31 Декабря 501 д.н.э** и заканчивается **19 Декабря 1999 н.э.**
Таким образом до заявленного диапозона дат (до 2000 года) не хватает 12 дней.

Стоит отметить, что в расчетах присутсвует поправка на високосные года, но при этом отсутсвует поправка на смену календарей, а также на географическое местоположение "обозревателя" звездного неба.

## Проверка. Этап 3. Примеры работы программы. Вариант указанный в книге "Новая хронология Египта"

Для быстрой проверки результатов работы программы **horos.exe** мной был написан скрипт [**horos-parser.py**](https://github.com/ponwork/chronologia.org-horos/blob/main/horos-parser.py) который:

   - в качестве аргумента принимает файл-результат (если не указан, берет файл **OTVET.TXT** в диреткории со скриптом);
   - считает количество решений;
   - ищет все строки с указанием на то, что порядок планет не менялся (критерий, по которому отобран ответ в книге "Новая хронология Египта");
   - создает словарь с номерами строк оригинального файла и соотвествующих им значениий "отклонения от лучших точек"
   - выдает в качестве результата ответ с минимальным показателем "отклонения от лучших точек" (также критерий, указанный автором книги "Новая хронология Египта")

В итоге, результат работы скрипта [**horos-parser.py**](https://github.com/ponwork/chronologia.org-horos/blob/main/horos-parser.py) над фалом результатов работы программы **horos.exe** с данными, взятыми из книги "Новая хронология Египта" (файл ["**otvet-fn.txt**"](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/otvet-fn.txt)) дает следующий результат:

![result-fn](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/result-fn.jpg)

Как видно из результата, минимальное "отклонение от лучших точек" дает дата **"11 Марта 1422"** (**4.4 deg**) года , а не **"20 Марта 1185"** (**8.5 deg**) года, как указано в книге.

Таким образом результаты программы **horos.exe** противоречат выводам указанным в книге "Новая хронология Египта".

Отмечу также, что результат **"20 Марта 1185"** с отклонением в **8.5 deg** также присутвует в файле ["**otvet-fn.txt**"](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/otvet-fn.txt), но почему был выбран именно этот результат, а не более точный -- ответ остается на совести автора книги.

## Проверка. Этап 4. Примеры работы программы. Вариант День Рождения автора

На данном этапе проверки предлаю рассмотерть результат работы программы **horos.exe** для входных данных, соотвествующих дате рождения автора "Новой Хронологии" -- Фоменко Анатолия Тимофеевича.

Согласно [wikipedia.org](https://ru.wikipedia.org/wiki/%D0%A4%D0%BE%D0%BC%D0%B5%D0%BD%D0%BA%D0%BE,_%D0%90%D0%BD%D0%B0%D1%82%D0%BE%D0%BB%D0%B8%D0%B9_%D0%A2%D0%B8%D0%BC%D0%BE%D1%84%D0%B5%D0%B5%D0%B2%D0%B8%D1%87) день рождения автора "Новой Хронологии" указан как **13 марта 1945 года**.

Предлагается не учитывать погрешностей, выявленных на Этапе №2, а именно:

   - отсуствие поправки на географическое положение "наблюдателя";
   - отсуствие поправки на смену календарей в период с 500 года д.н.э. по 2000 год н.э.

и произвести расчет даты рождения Фоменко А.Т. используя геоцентрическую карту звездного неба на 13 марта 1945 и программу **horos.exe**.

Расположение звезд и планет берем с сайта [https://takemeback.to/astronomy/13-March-1945](https://takemeback.to/astronomy/13-March-1945)

![zodiac-1945-03-13](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/zodiac-1945-03-13.jpg)

[Файл данных](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/INPUT-1945-03-13.TXT) для программы **horos.exe** таким образом получается следующим:

![input-1945-03-13](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/input-1945-03-13.jpg)

Примечание: положение Луны явно не указано, поэтому берем его равным 0-12 999, как указано в описании к программе.

Результат работы **horos.exe**:

![result-1945-03-13](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/result-1945-03-13.gif)

Как видно, программа ни одного решения не нашла.

## ВЫВОДЫ:

1) Ввиду отсутсвия исходного кода программы и параметров ее компиляции утверждать о достоверности ее результатов не представляется возможным;
2) При вооде данных в программу не предусмотрена возможность учета местоположения "наблюдателя", а также отсуствует поправка на смену календарей в период с 500 года д.н.э. по 2000 год н.э.;
3) Результат работы программы противоречит выводам, описанным в книге (при условии выбора результата с наименьшим отклонением, при отсутсвии изменения порядка планет);
4) При расчете результата на заведомо известную дату программа не дает решений.

Я оставляю за автором программы **horos.exe** возможность предоставить:
   - исходные коды программы и параметры ее компиляции;
   - параметры для INPUT.TXT на заведомо известную дату (например 13 Марта 1945 года), которые приведут к ожидаемому результату;
   - любые другие комментарии, указывающие на неточность приведенных выше исследований.

# Без предоставления указанных выше данных у меня есть все основания заявлять, что данные, изложенные в "Новой Хронологии" Г.В.Носовского и А.Т.Фоменко являются результатом манипуляции и подтасовок и никакого отношения к реальным событиям истории Древнего мира не имееют.










