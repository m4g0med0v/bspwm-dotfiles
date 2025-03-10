import os
from pathlib import Path

import packages
from logger import Logger, LoggerStatus

from creators.daemons import Daemons
from creators.drivers import GraphicDrivers
from creators.patches import PatchSystemBugs
from creators.software import AurBuilder, PythonBuilder

# TODO: Implement error handling for package installation


class SystemConfiguration:
    def start(*args):
        start_text = f"[+] Starting assembly. Options {args}"
        Logger.add_record(start_text, status=LoggerStatus.SUCCESS)
        if args[0]:
            SystemConfiguration.__start_option_1()
        if args[1]:
            SystemConfiguration.__start_option_2()
        if args[2]:
            SystemConfiguration.__start_option_3()
        if args[3]:
            SystemConfiguration.__start_option_4()
        if args[4]:
            SystemConfiguration.__start_option_5()
        if args[5]:
            GraphicDrivers.build()
        if args[6]:
            SystemConfiguration.__start_option_6()
            ...
        # TODO: The process should not be repeated when reassembling, important components should only be updated with new ones
        Daemons.enable_all_daemons()
        PatchSystemBugs.enable_all_patches()

    @staticmethod
    def __start_option_1():
        SystemConfiguration.__create_default_folders()
        SystemConfiguration.__copy_bspwm_dotfiles()

    @staticmethod
    def __start_option_2():
        Logger.add_record("[+] Updates Enabled", status=LoggerStatus.SUCCESS)
        os.system("sudo pacman -Sy")

    @staticmethod
    def __start_option_3():
        Logger.add_record(
            "[+] Installed BSPWM Dependencies", status=LoggerStatus.SUCCESS
        )
        AurBuilder.build()
        SystemConfiguration.__install_pacman_package(packages.BASE_PACKAGES)
        SystemConfiguration.__install_aur_package(packages.AUR_PACKAGES)
        # FirefoxCustomize.build()

    @staticmethod
    def __start_option_4():
        Logger.add_record(
            "[+] Installed Dev Dependencies", status=LoggerStatus.SUCCESS
        )
        SystemConfiguration.__install_pacman_package(packages.DEV_PACKAGES)
        SystemConfiguration.__install_pacman_package(
            packages.GNOME_OFFICIAL_TOOLS
        )

    @staticmethod
    def __start_option_5():
        Logger.add_record(
            "[+] Configuring Laptop", status=LoggerStatus.SUCCESS
        )
        laptop_path = Path().cwd() / "Builder/creators/laptop.py"
        os.system(f"sudo python {laptop_path}")

    @staticmethod
    def __start_option_6():
        Logger.add_record("[+] Install Python", status=LoggerStatus.SUCCESS)
        PythonBuilder.build()

    @staticmethod
    # TODO: Make a universal function for installing packages
    # TODO: Catch errors if the software is not detected
    def __install_pacman_package(package_names: list):
        for package in package_names:
            os.system(f"sudo pacman -S --noconfirm {package}")
            Logger.add_record(
                f"Installed: {package}", status=LoggerStatus.SUCCESS
            )

    @staticmethod
    # TODO: Make a universal function for installing packages
    # TODO: Catch errors if the software is not detected
    def __install_aur_package(package_names: list):
        for package in package_names:
            os.system(f"yay -S --noconfirm {package}")
            Logger.add_record(
                f"Installed: {package}", status=LoggerStatus.SUCCESS
            )

    @staticmethod
    def __create_default_folders():
        Logger.add_record(
            "[+] Create default directories", status=LoggerStatus.SUCCESS
        )
        os.system("xdg-user-dirs-update")
        os.system("mkdir -p ~/.config")
        os.system("cp -r Images/ ~/Pictures")

    @staticmethod
    def __copy_bspwm_dotfiles():
        Logger.add_record(
            "[+] Copy Dotfiles & GTK", status=LoggerStatus.SUCCESS
        )
        os.system("cp -r config/* ~/.config/")
        os.system("cp Xresources ~/.Xresources")
        os.system("cp gtkrc-2.0 ~/.gtkrc-2.0")
        os.system("cp -r local ~/.local")
        os.system("cp -r themes ~/.themes")
        os.system("cp xinitrc ~/.xinitrc")
        os.system("cp -r bin/ ~/.bin")
