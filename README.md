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

В итоге я решил проверить работоспособность данной программы и точность ее результатов. В качестве примера, я взял выдержку из книги [**"Новая хронология Египта"**](https://chronologia.org/nx_egypt/index.html) (ссылка на которую указана на странице с программой), а именно разбор [**Дендерского Зодиака**](https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D0%BD%D0%B4%D0%B5%D1%80%D1%81%D0%BA%D0%B8%D0%B9_%D0%B7%D0%BE%D0%B4%D0%B8%D0%B0%D0%BA)

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

3) Дендерский Зодиак [Zodiac of Dendera](https://collections.louvre.fr/en/ark:/53355/cl010028871)
4) Описание символов и значения Дендерского Зодиака [The Dendera zodiacs as narratives of the myth of Osiris, Isis, and the child
Horus](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/ENiM8_p133-185.pdf) ([Gyula Priskin, Eötvös Loránd University, 2015](http://www.enim-egyptologie.fr/index.php?page=enim-8&n=9))
5) Дистрибутив Windows XP 
   - файл: **ru_windows_xp_professional_with_service_pack_3_x86_cd_x14-80484.iso** 
   - MD5 = 44143210b620491eb1d21efc0b1a630a
   - примечение: установка выполнена в виде виртуальной машины VirtualBox, активация ОС произведена по телефону. Спасибо Microsoft!

## Проверка. Этап 1. Алгоритмы

Самое удивительное, что автор не приводит ни единого исходного текста программы, по результатам работы которой делаются столь замечательные выводы по датировкам событий мировой истории.

В файле [**README.TXT**]() содержатся лишь упоминания следующих работ:

   - "Расчет планет основан на программе:" [**Numerical expressions for precession formulae and mean elements for the Moon and the planets**](https://adsabs.harvard.edu/full/1994A%26A...282..663S)   [(**копия**)](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/1994A%2BA___282__663S.pdf)
   - "Расчет Луны основан на программе:" [**ELP 2000-85 - A semi-analytical lunar ephemeris adequate for historical times**](https://adsabs.harvard.edu/full/1988A%26A...190..342C)   [(**копия**)](https://github.com/ponwork/chronologia.org-horos/blob/main/resources/1988A%2BA___190__342C.pdf)

Читателю предлагается поверить наслово, что программа **horos.exe** имеет хоть какое-то отношение к расчету датировок.

Как говорится: **Source Code or GTFO**

На этом исследование можно завершить, но я все таки решил проверить работу **horos.exe**, используя различные входные данные и оценить степень правдоподобности результатов как с выводами самих авторов "Новой Хронологии", так и с независимыми источниками.

## Проверка. Этап 2. Примеры работы программы

Для начала кратко опишу работу с программой.

Берем гороскоп (изображение/описание расположения планет, луны и солнца относительно звезд, т.е. зодиакальных символов) и переносим его в виде цифр в файл INPUT.TXT

Для начала обратим внимание на фразу в **README.TXT** о том, что е




https://takemeback.to/astronomy/04-December-2021
