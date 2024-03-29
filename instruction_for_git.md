# Инструкция по работе с Git
![git](git.jpg)
## Основы
*Git* — это набор консольных утилит, которые отслеживают и фиксируют изменения в файлах (чаще всего речь идет об исходном коде программ, но вы можете использовать его для любых файлов на ваш вкус). 
Изначально *Git* был создан **Линусом Торвальдсом** при разработке ядра *Linux*. Однако инструмент так понравился разработчикам, что в последствии, он получил широкое распространение и его стали использовать в других проектах. 
С его помощью вы можете сравнивать, анализировать, редактировать, сливать изменения и возвращаться назад к последнему сохранению. Этот процесс называется контролем версий.

Для чего он нужен? Ну во-первых, чтобы отследить изменения, произошедшие с проектом, со временем. 
Проще говоря, мы можем посмотреть как менялись файлы программы, на всех этапах разработки и при необходимости вернуться назад и что-то отредактировать. 
Часто бывают ситуации, когда, во вполне себе работающий код, вам нужно внести определенные правки или улучшить какой-то функционал, по желанию заказчика. Однако после внедрения нововведений, вы с ужасом понимаете, что все сломалось. 
У вас начинается судорожно дергаться глаз, а в воздухе повисает немой вопрос: “Что делать?” Без системы контроля версий, вам надо было бы долго напряженно просматривать код, чтобы понять как было до того, как все перестало работать. 
С *Git* же, все что нужно сделать — это откатиться на коммит назад.

Во-вторых он чрезвычайно полезен при одновременной работе нескольких специалистов, над одним проектом. 
Без *Git* случится коллапс, когда разработчики, скопировав весь код из главной папки и сделав с ним задуманное, попытаются одновременно вернуть весь код обратно.
*Git* является распределенным, то есть не зависит от одного центрального сервера, на котором хранятся файлы. Вместо этого он работает полностью локально, сохраняя данные в директориях на жестком диске, которые называются репозиторием. 
Тем не менее, вы можете хранить копию репозитория онлайн, это сильно облегчает работу над одним проектом для нескольких людей. Для этого используются сайты вроде **github** и **bitbucket**.

## Установка
Для начала нужно скачать и установить *Git* на компьютер [по ссылке](https://www.git-scm.com/downloads "Git download").

## Настройка
Итак, мы установили *Git*, теперь нужно добавить немного настроек. Есть довольно много опций, с которыми можно играть, но мы настроим самые важные: наше имя пользователя и адрес электронной почты. 
Откройте терминал и запустите команды:
```sh
git config --global user.name <My Name>
```
```sh
git config --global user.email <myEmail@example.com>
```
Теперь каждое наше действие будет отмечено именем и почтой. Таким образом, пользователи всегда будут в курсе, кто отвечает за какие изменения — это вносит порядок.
*Git* хранит весь пакет конфигураций в файле ***.gitconfig***, находящемся в вашем локальном каталоге. Чтобы сделать эти настройки глобальными, то есть применимыми ко всем проектам, необходимо добавить флаг ***–global***. 
Если вы этого не сделаете, они будут распространяться только на текущий репозиторий.
Для того, чтобы посмотреть все настройки системы, используйте команду:
```sh
git config --list
```
Для удобства и легкости зрительного восприятия, некоторые группы команд в Гит можно выделить цветом, для этого нужно прописать в консоли:
```sh
git config --global color.ui true
```
```sh
git config --global color.status auto
```
```sh
git config --global color.branch auto
```
Если вы не до конца настроили систему для работы, в начале своего пути — не беда. Git всегда подскажет разработчику, если тот запутался, например:

1. Команда ***git --help*** — выводит общую документацию по *Git*;
2. Если введем ***git log --help*** — он предоставит нам документацию по какой-то определенной команде (в данном случае это — ***log***);
3. Если вы вдруг сделали опечатку — система подскажет вам нужную команду;
4. После выполнения любой команды — отчитается о том, что вы натворили;
5. Также *Git* прогнозирует дальнейшие варианты развития событий и всегда направит разработчика, не знающего, куда двигаться дальше.

Тут стоит отметить, что подсказывать система будет на английском, но не волнуйтесь, со временем вы изучите несложный алгоритм ее работы и будете разговаривать с ней на одном языке.

## Создание нового репозитория
Как мы отметили ранее, *Git* хранит свои файлы и историю прямо в папке проекта. Чтобы создать новый репозиторий, нам нужно открыть терминал, зайти в папку нашего проекта и выполнить команду ***git init***. Это включит приложение в этой конкретной папке и создаст скрытую директорию ***.git***, где будет храниться история репозитория и настройки.
Создайте на рабочем столе папку под названием ***git_exercise***. Для этого в окне терминала введите:
```sh
mkdir Desktop/git_exercise/
```
```sh
cd Desktop/git_exercise/
```
```sh
git init
```
Командная строка должна вернуть что-то вроде:
```sh
Initialized empty Git repository in /home/user/Desktop/git_exercise/.git/
```
Это значит, что наш репозиторий был успешно создан, но пока что пуст. Теперь создайте текстовый файл под названием *hello.txt* и сохраните его в директории *git_exercise*.

### Порядок работы с репозиторием:
+ Создание;
* Изменение;
+ Публикация;
* Синхронизация.

## Определение состояния
***git status*** — это еще одна важнейшая команда, которая показывает информацию о текущем состоянии репозитория: актуальна ли информация на нём, нет ли чего-то нового, что поменялось, и так далее. Запуск ***git status*** на нашем свежесозданном репозитории должен выдать:
```sh
git status
On branch master
Initial commit
Untracked files:
(use "git add ..." to include in what will be committed)
hello.txt
```
Сообщение говорит о том, что файл *hello.txt* неотслеживаемый. Это значит, что файл новый и система еще не знает, нужно ли следить за изменениями в файле или его можно просто игнорировать. Для того, чтобы начать отслеживать новый файл, нужно его специальным образом объявить.

## Фиксация изменений
### Как сделать коммит
Представим, что нам нужно добавить пару новых блоков в *html-разметку (index.html)* и стилизовать их в файле *style.css*. 
Для сохранения изменений, их необходимо закоммитить. Но сначала, мы должны обозначить эти файлы для *Git*, при помощи команды ***git add***, добавляющей (или подготавливающей) их к коммиту. 
Добавлять их можно по отдельности:
```sh
git add index.html
```
```sh
git add css/style.css
```
Или всё сразу:
```sh
git add .
```
Конечно, добавлять всё сразу удобнее, чем прописывать каждую позицию отдельно. Однако, тут надо быть внимательным, чтобы не добавить по ошибке ненужные элементы. Если же такое произошло изъять оттуда ошибочный файл можно при помощи команды:
```sh
git reset css/style.css
```
Теперь создадим непосредственно сам коммит
```sh
git commit -m 'Add some code'
```
Флажок **-m** задаст **commit message** — комментарий разработчика. Он необходим для описания закоммиченных изменений. И здесь работает золотое правило всех комментариев в коде: «Максимально ясно, просто и содержательно обозначь написанное!»

### Как посмотреть коммиты
Для просмотра всех выполненных фиксаций можно воспользоваться историей коммитов. Она содержит сведения о каждом проведенном коммите проекта. Запросить ее можно при помощи команды:
```sh
git log
```
Чтобы посмотреть список коммитов в более сокращенном виде:
```sh
git log --oneline
```
Чтобы посмотреть список коммитов в графическом виде:
```sh
git log --graph
```
Чтобы посмотреть список коммитов в более сокращенном и графическом виде:
```sh
git log --oneline --graph
```
В ней содержится вся информация о каждом отдельном коммите, с указанием его хэша, автора, списка изменений и даты, когда они были сделаны. Отследить интересующие вас операции в списке изменений, можно по хэшу коммита, при помощи команды **git show** :
```sh
git show hash_commit
```
Ну а если вдруг нам нужно переделать **commit message** и внести туда новый комментарий, можно написать следующую конструкцию:
```sh
git commit --amend -m 'new comment'
```
В данном случае сообщение последнего коммита перезапишется. Но злоупотреблять этим не стоит, поскольку эта операция опасная и лучше ее делать до отправки коммита на сервер.

## Принцип работы файлов **.gitkeep** и **.gitignore**

В *Git* существует 2 системных файла для облегчения работы:
+ .gitkeep
+ .gitignore

### .gitkeep
При создании пустой директории *Git* не воспринимает её как изменение состояния репозитория, но в некоторых случаях необходимо закоммитить и это действие, поэтому в пустой директории создаём файл .gitkeep и после этого можно будет добавить директорию в индекс изменений и закоммитить.

### .gitignore
Для игнорирования файлов от попадпния в общий индекс репозитория необходимо выполнить следующие действия:
1. Создаём файл *.gitignore*;
2. Добавляем в индекс (git add);
3. Добавляем в файл *.gitignore* названия тех файлов, которые хотим игнорировать.
## Команды в *Git* для работы с файлами

Чтобы посмотреть список всех файлов в текущей директории нужно выполнить команду:
```sh
ls
```
Чтобы посмотреть список всех файлов, в т.ч. скрытых:
```sh
ls -a
```
Чтобы перейти в нужную нам директорию:
```sh
cd
```
Чтобы перейти в директорию на 1 уровень выше:
```sh
cd ..
```
Чтобы создать новую директорию:
```sh
mkdir <directory_name>
```
Чтобы создать новый файл:
```sh
touch <file_name>
```
Чтобы скопировать существующий файл, нужно записать сначала название того файла, который мы хотим скопировать, а затем название нового скопированного файла:
```sh
cp <file_name> <copied_file_name>
```
Чтобы переименовать файл, нужно записать сначала старое название файла, а затем новое:
```sh
mv <file_name> <new_file_name>
```
Чтобы переместить файл куда-либо, нужно записать сначала название файла, а затем путь директории, в который мы хотим переместить файл:
```sh
mv <file_name> <directory_path>
```
Чтобы записать текст в файл:
```sh
echo "text" > <file_name>
```
Чтобы прочитать содержимое файла:
```sh
cat <file_name>
```
Чтобы удалить файл:
```sh
rm <file_name>
```
Чтобы удалить директорию:
```sh
rm -R <directory_name>
```
## Работа с ветками

Чтобы посмотреть список веток, нужно выполнить команду:
```sh
git branch
```
Чтобы создать новую ветку (при создании ветки недопустимо использование пробелов!):
```sh
git branch <branch_name>
```
Чтобы переключиться на другую ветку:
```sh
git checkout <branch_name>
```
Чтобы создать и сразу переключиться на новую ветку:
```sh
git checkout -b <branch_name>
```
Чтобы слить две ветки, нужно перейти на ту ветку, в которую хотим перенести изменения и пишем название той ветки, которую хотим слить:
```sh
git merge <branch name>
```
Чтобы удалить ветку:
```sh
git branch -d <branch_name>
```
# Инструкция по работе с удалёнными репозиториями

## Первые шаги

1. Делаем fork репозитория, в которой потом хотим сделать pull request. Ищем кнопку Fork на странице репозитория <https://git@github.com:gulden-geekbrains/version_control.git>
2. Выполняем команду клонирования из своей fork-копии
```sh
git clone git@github.com:*YOURE_GITHUB*/version_control.git
```
3. Создаем новую ветку и вносим необходимые изменения в файл
```sh
git checkout -b updatereadme
vim README.md
git add README.md
git commit -m "Добавили инструкцию как создать pull request"
```
4. Делаем push  
```sh
git push --set-upstream origin updatereadme
```
5. Переходим на свою страницу репозитория. Выбираем ветку **updatereadme** и жмем кнопку **Compare & pull request**

### Заметки

Что бы сделать push от другого пользователя необходимо выполнить команду
```sh
GIT_SSH_COMMAND='ssh -i ~/.ssh/user-private-key -o IdentitiesOnly=yes' git push git@github.com:gulden-geekbrains/version_control.git
```

вместо *user-private-key* подставьте свой ключ

Можно прописать настройки для подсоединения по ssh
```sh
git config remote.origin.url git@github.com:gitusername/reponame
git config core.sshCommand "ssh -i ~/.ssh/user-private-key -o IdentitiesOnly=yes"
```
### Как подружить git с github под Windows 10

Вот видео инструкция https://youtu.be/E8cIjbJMEpE

## Что такое ssh

SSH (англ. Secure Shell — «безопасная оболочка»[1]) — сетевой протокол прикладного уровня, позволяющий производить удалённое управление операционной системой и туннелирование TCP-соединений (например, для передачи файлов). Схож по функциональности с протоколами Telnet и rlogin, но, в отличие от них, шифрует весь трафик, включая и передаваемые пароли. SSH допускает выбор различных алгоритмов шифрования. SSH-клиенты и SSH-серверы доступны для большинства сетевых операционных систем.

###  Как сгенерировать ssh ключ для github

Необходимо выполнить команду
```sh
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Фразу пароль можно оставить пустой
```sh
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
```

Задайте имя ключа. В текущей директории появится два файла:
- *new_key* - закрытый ключ. Никому его не передавайте и храните в надежном месте!!!
- *new_key.pub* - открытый ключ. Его необходимо загрузить на github

## Как включить ssh в Windows 10

В ОС Windows 10 по умолчанию уже есть ssh. Его надо только активировать.

Зайдите в Параметры - Приложения - Приложения и возможности - Дополнительные компоненты. В указанном спсике найдите **Клиент OpenSSH**, жмите установить.

Откройте cmd.

Наберите команду 
```sh
C:\Users\USER\> ssh
usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]
           [-b bind_address] [-c cipher_spec] [-D [bind_address:]port]
           [-E log_file] [-e escape_char] [-F configfile] [-I pkcs11]
           [-i identity_file] [-J [user@]host[:port]] [-L address]
           [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
           [-Q query_option] [-R address] [-S ctl_path] [-W host:port]
           [-w local_tun[:remote_tun]] destination [command]
```
Перейдите к созданию ssh ключа.

# Пример ***Pull request*** 
![Pull request](homework.png)

> Спасибо всем за внимание!
>> С уважением, Агазаде А.В.
