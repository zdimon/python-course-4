# BASH Алиасы.

Часто возникает необходимость в консоле создать собственную команду.

Напимер для того, чтобы запустить последовательно ряд повторяющихся команд.

К примеру, команду, которая добавляет файлы в индекс git и комитит изменения на сервер.

Такая операция проводится довольно часто и состоит из 3-х шагов.

- добавление файло в индекс для отслеживания;

- совершение комита;

- загрузка изменений на удаленный сервер.

Создадаим выполняемый скрипт для этого autocomit.sh.

    git add --all
    git commit -m 'auto commit'
    git push
    
Добавим права на выполнение.

    chmod +x ./autocomit.sh
    
Теперь чтобы создать свою команду, можно воспользоваться alias-ом, определив его в файле, который будет выполняться 
каждый раз когда вы открываете терминальную сессию.

Одним из таких файлов являются .bashrc, он запускается первым.

Добавим в него следующий alias и назовем его agit.

    alias agit='./path/to/script/autocomit.sh'     
    
Теперь при перезагрузке терминала эта команда станет доступна.
