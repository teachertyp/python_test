# Git за півгодини: посібник для початківців


В останні роки популярність git демонструє вибухове зростання. Ця система контролю версій використовується різними проектами з відкритим кодом.
Початківців часто лякає велику кількість хитромудрих команд і складних аргументів. Але для початку всі вони не потрібні. Можна почати з вивчення команд, які найчастіше використовуються, і після цього поступово розширювати свої знання. Саме так ми і вчинимо у цій статті. Поїхали!

# Основи
Git - це набір консольних утиліт, які відстежують і фіксують зміни у файлах (найчастіше йдеться про вихідний код програм, але ви можете використовувати його для будь-яких файлів на ваш смак). З його допомогою ви можете відкотитися на старішу версію вашого проекту, порівнювати, аналізувати, зливати зміни та багато іншого. Цей процес називається контролем версій. Існують різні системи контролю версій. Ви, можливо, про них чули: SVN, Mercurial, Perforce, CVS, Bitkeeper та інші.

Git є розподіленим, тобто не залежить від одного центрального сервера, на якому зберігаються файли. Натомість він працює повністю локально, зберігаючи дані в папках на жорсткому диску, які називаються репозиторієм. Тим не менш, ви можете зберігати копію репозиторію онлайн, це полегшує роботу над одним проектом для декількох людей. Для цього використовуються сайти на кшталт github та bitbucket.

## Встановлення
Встановити git на свою машину дуже просто:

### Linux
потрібно просто відкрити термінал і встановити програму за допомогою пакетного менеджера вашого дистрибутива. Для Ubuntu команда буде виглядати
так:
```
sudo apt-get install git
```

### Windows
Одним із найзручніших клієнтів є  [git for windows](https://gitforwindows.org/), оскільки він містить клієнт з графічним інтерфейсом, і емулятор bash.

### OS X
найпростіше скористатися homebrew. Після його встановлення запустіть у терміналі:
```
brew install git
```
Якщо ви новачок, клієнт з графічним інтерфейсом (наприклад, GitHub Desktop і Sourcetree) буде корисним, але, тим не менш, знати команди дуже важливо.

## Налаштування

Отже, ми встановили git, тепер потрібно додати трохи налаштувань. Є досить багато опцій, з якими можна гратися, але ми налаштуємо найважливіші:  ім'я користувача та адресу електронної пошти. Відкрийте термінал та запустіть команди:
```
git config --global user.name "My Name"
git config --global user.email myEmail@example.com
```
*Тепер кожну нашу дію буде відзначено ім'ям та поштою. Таким чином, користувачі завжди будуть в курсі, хто відповідає за якісь зміни — це вносить порядок.*

## Створення нового репозиторію

Як було зазначено раніше, git зберігає свої файли та історію прямо в папці проекту. Щоб створити новий репозиторій, нам потрібно відкрити термінал, **зайти до папки нашого проекту** та виконати команду:
 ```
 git init
 ```
 Ця команда активує git у цій конкретній папці та створить приховану директорію .git, де зберігатиметься історія репозиторію та налаштування.

Створіть папку у домашньому каталозі папку python_projects, а у ній папку project1. Для цього у вікні терміналу по черзі введіть:
```
mkdir python_projects
cd python_projects
mkdir project1
cd project1
```
Тепер виконуємо ініціалізацію для папки project1:
```
git init
```
Командний рядок має повернути щось на кшталт:

***Initialized empty Git repository in/home/user/python_projects/project1/.git/***

Це означає, що наш репозиторій був успішно створений, але поки що порожній. Тепер за допомогою зручного для Вас текстового редактора створіть текстовий файл під назвою *main.py* і збережіть його в директорії project1.

# Визначення стану

**status** - це ще одна найважливіша команда, яка показує інформацію про поточний стан
репозиторію: чи актуальна інформація на ньому, чи немає чого нового, що змінилося, і
так далі. Запуск команди **git status** на нашому новоствореному репозиторії повинен видати:

    $ git status

```bash
На гілці main  
Ваша гілка актуалізована з «origin/main».  
  
Зміни, що мають бути збережені в коміті  
(use "git restore --staged <file>..." to unstage)  
новий файл: main.py
```

Повідомлення говорить про те, що файл main.pyне відстежується. Це означає, що новий файл і система ще не знає, чи потрібно стежити за змінами у файлі або його можна просто ігнорувати. Щоб почати відстежувати новий файл, потрібно його спеціальним чином оголосити.

# Підготовка файлів

У git є концепція області підготовлених файлів. Можна уявити її як полотно, на яке завдають зміни, які потрібні в коміті. Спершу він порожній, але потім ми додаємо на нього файли (або частини файлів, або навіть одиночні рядки) командою **add** і, нарешті, комітимо все необхідне у репозиторій (створюємо зліпок потрібного нам стану) командою commit.
У нашому випадку у нас тільки один файл, тому додамо його ввівши команду:

```$ git add main.py```

Якщо нам потрібно додати все, що знаходиться в директорії, ми можемо використати:

```$ git add -A```

Перевіримо статус (`git status`) знову, цього разу ми маємо отримати іншу відповідь:
```bash
На гілці main  
Ваша гілка актуалізована з «origin/main».  

Зміни, що мають бути збережені в коміті  
    (use "git restore --staged <file>..." to unstage)  
	  новий файл: main.py
```
Файл готовий до комміту. Повідомлення про стан також говорить нам про те, які зміни щодо файлу були проведені в галузі підготовки - у цьому випадку це новий файл, але файли можуть бути модифіковані або видалені.

# Коміт (фіксація змін)

Коміт є стан репозиторію у певний час. Це схоже на снапшот (*~~архівна копія~~*), до якого ми можемо
повернутися та побачити стан об'єктів на певний момент часу.

Щоб зафіксувати зміни, нам потрібна хоча б одна зміна в галузі підготовки (ми щойно створили її за допомогою **git add**), після якої ми можемо комітити:

```$ git commit -m "My firs commit."```
Після виконання цієї команди на екрані буде виведено приблизно таке:

```bash
[main d0ca9f7] My first commit    
 1 file changed, 3 insertions(+)
 create mode 100644 main.py
```
Ця команда створить новий коміт з усіма змінами в галузі підготовки (додавання файлу hello.txt). Ключ -m та коментар «My firs commit» — це створений користувачем опис усіх змін, які включені до коміту. 

> Вважається гарною практикою робити комміти часто та завжди писати
> змістовні коментарі.

# Віддалені репозиторії

Зараз наш коміт є локальним - існує тільки в директорії .git на нашій файловій системі. Незважаючи на те, що сам собою локальний репозиторій корисний, в більшості випадків ми хочемо поділитися нашою роботою або доставити код на сервер, де він виконуватиметься.

## 1. Підключення до віддаленого репозиторію

Щоб завантажити щось у віддалений репозиторій, спочатку потрібно підключитися до нього. У цьому посібнику  будемо використовувати адресу https://github.com/teachertyp/python_test, але вам порадимо спробувати створити свій репозиторій у GitHub, BitBucket або будь-якому іншому сервісі. Реєстрація та встановлення може зайняти час, але всі подібні сервіси надають хорошу документацію.

Щоб зв'язати наш локальний репозиторій із репозиторієм на GitHub, виконаємо наступну команду в терміналі. **Зверніть увагу, що потрібно обов'язково змінити URI репозиторію на свій.**

    git remote add origin https://github.com/teachertyp/python_test

Проект може мати кілька віддалених репозиторіїв одночасно. Щоб їх розрізняти, ми надамо їм різні імена. Зазвичай головний репозиторій називається origin.

## 2. Надсилання змін на сервер

Зараз саме час надіслати наш локальний коміт на сервер. Цей процес відбувається
щоразу, коли ми хочемо оновити дані у віддаленому репозиторії. Команда, призначена
для цього – push. Вона приймає два параметри: ім'я віддаленого репозиторію (ми
назвали наш origin) і гілку, в яку необхідно внести зміни (master - це стандартна гілка
для всіх репозиторіїв).

   $ git push origin main 
   Після цього система попросить Вас ввести пароль від ключа
```sh
Enter passphrase for key '/home/typ/.ssh/id_rsa':  
Enumerating objects: 4, виконано.  
Підрахунок об’єктів: 100% (4/4), виконано.  
Запис об’єктів: 100% (3/3), 268 bytes | 268.00 KiB/s, виконано.  
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0  
To github.com:teachertyp/python_test.git  
    836e194..d0ca9f7 main -> main
```

Залежно від сервісу, який ви використовуєте, вам може знадобитися автентифікуватися, щоб зміни відправилися. Якщо все зроблено правильно, то коли Ви подивитеся у віддалений репозиторій за допомогою браузера, ви побачите файл main.py

## 3. Клонування репозиторію

Наразі інші користувачі GitHub можуть переглядати ваш репозиторій. Вони можуть
завантажити дані і отримати повністю працездатну копію вашого проекту за допомогою
команди clone.

```sh
$ git clone https://github.com/teachertyp/python_test
```
Новий локальний репозиторій створюється автоматично з GitHub як віддалений репозиторій.

## 4. Запит змін із сервера

Якщо ви зробили зміни у репозиторії, інші користувачі можуть завантажити зміни за
допомогою команди pull.

$ git pull origin main
Від https://github.com/tutorialzine/awesome-project
* branch master -> FETCH_HEAD
Already up-to-date.

Так як нових коммітів відколи ми схилювали собі проект, не було, жодних змін доступних для скачування немає.

## 5. Розгалуження

Під час розробки нової функціональності вважається гарною практикою працювати з копією ригінального проекту, яку називають гілкою (branch). Гілки мають свою власну історію та ізольовані одна від одної зміни до тих пір, поки ви не вирішуєте злити зміни разом. Це відбувається з ряду причин:

 - Вже робоча стабільна версія коду зберігається. 
 - Різні нові функції   можуть розроблятися паралельно до різних програмістів. 
 - Розробники  можуть працювати з власними гілками без ризику, що кодова база зміниться через чужі зміни. 
 - У разі сумнівів різні реалізації однієї і тієї ж ідеї можуть бути розроблені в різних гілках і потім
   порівнюватися.


### 5.1. Створення нової гілки

Основна гілка у кожному репозиторії називається main. Припустімо, що у нас є ідея як спростити код або додати щось нове. Ми не впевнені, що це спрацює, а тому, щоб не зламати робочий код, нам потрібно створити ще одну гілку у якій і будемо додавати щось нове чи вносити  зміни. Для цього використовуємо команду: **branch \<name>**. *Зверніть увагу, при записі імені гілки, лапки не використовують.*
```sh
$ git branch nova_gilka
```
Це створить нову гілку, поки що **точну копію гілки main**.

### 5.2. Перемикання між гілками

Зараз, якщо ми запустимо branch, ми побачимо дві доступні гілки нашого репозиторію:
```sh
$ git branch 
```
на екрані відобразиться
```sh
* main
  nova_gilka
```
Зверніть увагу, main - це активна гілка, вона позначена зірочкою. Але ми хочемо працювати з гілкою "nova_gilka", так що нам потрібно перемкнутися на іншу гілку. 
Для цього скористаємося командою **checkout**, вона приймає один параметр - ім'я гілки, на яку необхідно перейти.
```sh
$ git checkout nova_gilka
```
### 5.3. Злиття гілок

Тепер всі зміни, що будуть відбуватися у папці проекту будуть відбуватися з прицілом на гілку "nova_gilka". 
Давайте додамо ще один файл, що міститиме код якоїсь функції. Отже створимо файл **square.py** (*нагадаю, що це можна зробити прямо з текстового редактора чи у файловому менеджері, одним словом будь яким зручним для Вас способом. Головне, щоб цей файл лежав у тій же папці для якої ми ініціалізували git-репозиторій.* )
Після створення, внесемо до нього який небудь код, закоммітуємо:
```sh
$ git add square.py
$ git commit -m "Draw square function in file square.py."
```
На екрані буде відображено інформацію про  внесенеі зміни.
```sh
[nova_gilka 4e7252d] Draw square function in file square.py  
 1 file changed, 4 insertions(+)  
 create mode 100644 square.py
```
Зміни завершені, код протестовано, він робочий, ми задоволені, а отже можемо перейти назад на гілку main виконавши команду:
```sh
$ git checkout main
```

Але коли ми відкриємо наш проект у файловому менеджері, ми не побачимо файлу square.py. 
ЯК? ЩО? ДЕ МОЇ ФАЙЛИ???  Але не лякайтеся, в цьому вся суть роботи з git. Він відображає розробнику тільки ті файли, що були додані до вибраної на данаий момент гілки. 

Але якщо код з nova_gilka робочий, було б добре, щоб він з'явився і у гілці main.  А для цього нам потрібно скористатися **merge** для об'єднання гілок (*застосування змін із гілки nova_gilka до основної версії проекту*).
```sh
$ git merge nova_gilka
```
Тепер гілка master є актуальною. Гілка nova_gilka більше не потрібна, її можна  видалити командою.
```sh
$ git branch -d nova_gilka
```

Але, якщо Ви хочете залити цю гілку на віддалений сервер - виконайте команду 
```sh
$ git push origin nova_gilka
```

### Далі буде....