BASE_PACKAGES = [
    # Графическая оболочка и утилиты рабочего стола
    "tumbler",  # фоновый генератор эскизов (thumbnailer) для файловых менеджеров, например, Thunar.
    "ffmpegthumbnailer",  # создание эскизов для видеофайлов.
    "lsd",  # улучшенная версия ls, отображает файлы с красивыми иконками.
    "alacritty",  # терминальный эмулятор с аппаратным ускорением.
    "feh",  # лёгкий просмотрщик изображений, часто используется для установки обоев.
    "thunar",  # файловый менеджер XFCE.
    "lxappearance",  # инструмент для настройки GTK-тем.
    "papirus-icon-theme",  # набор иконок Papirus.
    "xfce4-power-manager",  # управление питанием.
    "xfce4-settings",  # настройки XFCE.
    "nitrogen",  # утилита для установки обоев.
    "polybar",  # настраиваемая панель для рабочего стола.
    "picom",  #  композитор для создания прозрачности и эффектов в X11.
    # Звук и мультимедиа
    "mpc",  # управление MPD из терминала
    "python-pyalsa",  # взаимодействие с ALSA в Python
    "mpd",  # музыкальный сервер.
    "mpv",  # продвинутый видеоплеер.
    "ncmpcpp",  # клиент для MPD с текстовым интерфейсом.
    "pamixer",  # микшер для PulseAudio.
    "pavucontrol",  # GUI-контроль звука для PulseAudio.
    "pulseaudio",  # звуковой сервер.
    "pulseaudio-alsa",  # совместимость PulseAudio и ALSA.
    "pulseaudio-bluetooth",  # поддержка Bluetooth-звука через PulseAudio.
    "vlc",  # популярный видеоплеер.
    "alsa-plugins",  # утилиты для работы с ALSA.
    "alsa-tools",  # утилиты для работы с ALSA.
    "alsa-utils",  # утилиты для работы с ALSA.
    "ffmpeg",  # мощный инструмент для работы с видео и аудио.
    # Сеть и интернет
    "blueman",  # GUI-менеджер Bluetooth
    "bluez",  # стек Bluetooth
    "bluez-utils",  # инструменты для Bluetooth (bluetoothctl)
    "netctl",  # управление сетевыми профилями
    "wget",  # загрузчик файлов из сети.
    "firefox",  # веб-браузер.
    "git",  # система контроля версий.
    "gnu-netcat",  # инструмент для работы с сетевыми соединениями.
    "network-manager-applet",  # графический индикатор NetworkManager.
    "openssh",  # SSH-клиент и сервер.
    "sshfs",  # монтирование удалённых файловых систем по SSH.
    "openvpn",  # VPN-клиент.
    "networkmanager-openvpn",  # поддержка OpenVPN в NetworkManager.
    # Системные утилиты
    "mat2",  # удаление метаданных из файлов
    "neofetch",  # информация о системе в терминале
    "rofi",  # мощный лаунчер приложений
    "rofi-calc",  # калькулятор для rofi
    "rofi-emoji",  # выбор эмодзи через rofi
    "sudo",  # выполнение команд от root
    "uthash",  # библиотека для C
    "bat",  #  улучшенная версия cat с подсветкой синтаксиса и номерами строк.
    "calc",  # консольный калькулятор.
    "p7zip",  #  утилиты для работы с архивами.
    "automake",  # инструменты для сборки программ.
    "fakeroot",  # позволяет создавать пакеты без root-доступа.
    "fish",  # улучшенная командная оболочка.
    "dpkg",  # пакетный менеджер Debian (может быть полезен для работы с .deb).
    "gcc",  # инструменты для сборки программ.
    "htop",  # утилиты для мониторинга системы.
    "btop",  # утилиты для мониторинга системы.
    "nano",  # текстовый редактор в терминале.
    "micro",  # текстовый редактор в терминале.
    "autoconf",  # инструменты для сборки программ.
    "ranger",  # текстовый файловый менеджер.
    "reflector",  # обновление зеркал репозиториев.
    "tree",  # вывод структуры каталогов в виде дерева.
    "unrar",  #  утилиты для работы с архивами.
    "zip",  #  утилиты для работы с архивами.
    "unzip",  #  утилиты для работы с архивами.
    "xarchiver",  #  утилиты для работы с архивами.
    "cmake",  # инструменты для сборки программ.
    "clang",  # инструменты для сборки программ.
    "gzip",  # сжатие файлов.
    "make",  # инструменты для сборки программ.
    "shellcheck",  # анализатор shell-скриптов.
    # Графические инструменты и прочее
    "xorg-xbacklight",  # управление яркостью экрана
    "usbutils",  # управление USB (lsusb)
    "dunst",  # лёгкий демон уведомлений
    "gparted",  # GUI-утилита для работы с дисками
    "ueberzug",  # отображение изображений в терминале
    "libreoffice",  # офисный пакет
    "light",  # управление яркостью экрана.
    "brightnessctl",  # тоже управление яркостью.
    "gedit",  # текстовый редактор GNOME.
    "redshift",  # изменяет цветовую температуру экрана для снижения нагрузки на глаза.
    "calcurse",  # текстовый органайзер и календарь.
    "scrot",  # инструмент для создания скриншотов.
    "slop",  # инструмент для выделения области экрана (используется в сочетании с scrot).
    "zathura",  # просмотрщики PDF и DjVu.
    "zathura-djvu",  # просмотрщики PDF и DjVu.
    "zathura-pdf-mupdf",  # просмотрщики PDF и DjVu.
    "imagemagick",  # набор инструментов для обработки изображений.
    "xclip",  # управление буфером обмена в X11.
    "gpick",  # инструмент для подбора цветов.
    # Шрифты и драйверы
    "ttf-jetbrains-mono",  # популярные шрифты с поддержкой лигатур.
    "ttf-jetbrains-mono-nerd",  # популярные шрифты с поддержкой лигатур.
    "ttf-fira-code",  # популярные шрифты с поддержкой лигатур.
    "ttf-iosevka-nerd",  # популярные шрифты с поддержкой лигатур.
    "vulkan-intel",  # Vulkan-драйвер для видеокарт Intel.
    "intel-ucode",  # обновления микрокода для процессоров Intel.
    "breeze",  # тема оформления.
    "xdg-user-dirs",
]

DEV_PACKAGES = [
    "cheese",  #  утилита для веб-камер.
    "screenkey",  # показывает нажатия клавиш.
    "timeshift",  # создание резервных копий системы.
    "pinta",  # простой редактор изображений.
    "kdenlive",  # видеоредактор.
    "wireshark-qt",  # инструмент для анализа сетевого трафика.
    "filezilla",  # FTP-клиент.
    "ghex",  # шестнадцатеричный редактор.
    "chromium",  # браузер с открытым исходным кодом.
    "keepassxc",  # менеджер паролей.
    "audacity",  # аудиоредактор.
    "gufw",  # GUI для настройки файрвола UFW.
    "python-pywal",  # изменение цветовой схемы на основе обоев.
    "bleachbit",  # очистка системы от мусора.
    "veracrypt",  # инструмент для шифрования данных.
    "homebank",  # программа для управления финансами.
    "gtkhash",  # вычисление хеш-сумм файлов.
    "gnome-firmware",  # инструмент для обновления прошивки устройств.
    "touche",  # настройка мультитач-жестов.
    "dconf-editor",  # редактор конфигураций GNOME.
    "neovim",  # продвинутый текстовый редактор.
    "obs-studio",  # запись экрана и стриминг.
    "telegram-desktop",  # десктопный клиент Telegram.
    "tmux",  # мультиплексор терминала.
    "yt-dlp",  # загрузка видео с YouTube.
    "cowsay",  # вывод забавных текстовых сообщений с ASCII-коровой.
    "deluge-gtk",  # BitTorrent-клиент.
    "flameshot",  # мощный инструмент для скриншотов.
    "sqlitebrowser",  # GUI для работы с SQLite.
    "obsidian",  # инструмент для ведения заметок.
    "python-pip",  # менеджер пакетов Python.
    "bpython",  # улучшенные Python-интерпретаторы.
    "ipython",  # улучшенные Python-интерпретаторы.
    "cloc",  # утилита для подсчёта строк кода.
]

AUR_PACKAGES = [
    "cava",  # визуализатор звука в терминале.
    "i3lock-color",  # утилита блокировки экрана с кастомизацией.
    "ptpython",  # улучшенный интерактивный Python-интерпретатор.
    "visual-studio-code-bin",  # редактор кода
    "auto-cpufreq",
    "zen-browser-bin",
]

GNOME_OFFICIAL_TOOLS = [
    "evince",  # это просмотрщик PDF, а не Python-интерпретатор. Описание надо исправить.
    "gnome-calculator",  # калькулятор.
    "gnome-disk-utility",  # инструмент управления дисками.
    "gucharmap",  # таблица символов Unicode.
    "gthumb",  # просмотрщик изображений.
    "gnome-clocks",  # часы.
]
