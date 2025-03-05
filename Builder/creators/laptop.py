import os
import subprocess

from logger import Logger, LoggerStatus


class LaptopConfigure:
    @staticmethod
    def configure_touchpad():
        Logger.add_record("[+] Settings up the Touchpad", status=LoggerStatus.SUCCESS)
        try:
            touchpad = subprocess.check_output(
                r"xinput list | sed -n 's/.*↳ \(.*Touchpad\).*/\1/p'",
                shell=True,
                text=True,
            ).strip()
        except subprocess.CalledProcessError as e:
            Logger.add_record(f"[-] Error configuring touchpad: {e}", status=LoggerStatus.ERROR)
            return

        config = f"""Section "InputClass"
    Identifier "{touchpad}"
    MatchIsTouchpad "on"
    Driver "libinput"

    Option "Tapping" "on"
    Option "TappingButtonMap" "lmr"
    Option "NaturalScrolling" "true"
    Option "DisableWhileTyping" "on"
    Option "ScrollMethod" "twofinger"
    Option "MiddleEmulation" "on"
EndSection
"""
        try:
            with open("/etc/X11/xorg.conf.d/30-touchpad.conf", "w") as f:
                f.write(config)
        except PermissionError:
            Logger.add_record("[-] Permission denied while writing to /etc/X11/xorg.conf.d/30-touchpad.conf", status=LoggerStatus.ERROR)
            return
        except Exception as e:
            Logger.add_record(f"[-] Error writing to touchpad config: {e}", status=LoggerStatus.ERROR)
            return

    @staticmethod
    def install_cpufreq():
        Logger.add_record("[+] Configuring mains and battery power", status=LoggerStatus.SUCCESS)
        try:
            os.system("systemctl stop auto-cpufreq.service")
            os.system("systemctl disable auto-cpufreq.service")
            output = subprocess.check_output(
                "sudo dmidecode -t processor | grep 'Max Speed'",
                shell=True,
                text=True,
            )
            max_freq = int(output.split(":")[1].strip().split()[0]) * 1000
        except subprocess.CalledProcessError as e:
            Logger.add_record(f"[-] Error configuring CPU frequency: {e}", status=LoggerStatus.ERROR)
            return

        config = f"""[charger]
governor = performance
energy_performance_preference = performance
scaling_max_freq = {max_freq * 0.92}
turbo = auto

[battery]
governor = powersave
energy_performance_preference = power
scaling_max_freq = {max_freq * 0.67}
turbo = never
"""
        try:
            with open("/etc/auto-cpufreq.conf", "w") as f:
                f.write(config)
            subprocess.check_call(["sudo", "auto-cpufreq", "--install"])
        except PermissionError:
            Logger.add_record("[-] Permission denied while writing to /etc/auto-cpufreq.conf", status=LoggerStatus.ERROR)
        except subprocess.CalledProcessError as e:
            Logger.add_record(f"[-] Error executing auto-cpufreq: {e}", status=LoggerStatus.ERROR)
        except Exception as e:
            Logger.add_record(f"[-] Error configuring CPU freq: {e}", status=LoggerStatus.ERROR)
