import os

from logger import Logger, LoggerStatus


class AurBuilder:
    @staticmethod
    def build():
        os.system("git -C /tmp clone https://aur.archlinux.org/yay.git")
        os.system("cd /tmp/yay && makepkg -si")


class FirefoxCustomize:
    @staticmethod
    def build():
        os.system("timeout 10 firefox --headless")
        os.system("sh firefox/install.sh")
        Logger.add_record(
            "[+] Firefox styles installed", status=LoggerStatus.SUCCESS
        )


class PythonBuilder:
    @staticmethod
    def build():
        print("1) Enter the version of python you want to install: ", end="")
        python_version = input()
        cpu_cores = int(os.cpu_count() * 0.5)

        cd_download = "cd ~/Downloads"
        curl = f'curl -L -o "Python-{python_version}.tar.xz" "https://www.python.org/ftp/python/{python_version}/Python-{python_version}.tar.xz"'
        configure = f"./configure --prefix=$HOME/.python/python{python_version} --enable-optimizations"
        fish = rf'echo "set -x PATH \$PATH \$HOME/.python/python{python_version}/bin" >> ~/.config/fish/config.fish'

        os.system("mkdir ~/.python/")
        os.system(f'{cd_download} && {curl}"')
        os.system(f'{cd_download} && tar -xvf Python-{python_version}.tar.xz')
        os.system(f'{cd_download}/Python-{python_version} && {configure}')
        os.system(f'{cd_download}/Python-{python_version} && make -j{cpu_cores}')
        os.system(f'{cd_download}/Python-{python_version} && sudo make install')
        os.system(fish)
        Logger.add_record(
            f"[+] Python {python_version} installed", status=LoggerStatus.SUCCESS
        )
