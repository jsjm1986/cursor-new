#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import uuid
import shutil
import platform
import subprocess
from datetime import datetime
from pathlib import Path

class PathManager:
    @staticmethod
    def get_system():
        return platform.system().lower()

    @staticmethod
    def get_home():
        return str(Path.home())

    @staticmethod
    def get_app_data_path():
        system = PathManager.get_system()
        if system == "windows":
            return os.path.join(os.getenv('APPDATA'), 'Cursor')
        elif system == "darwin":
            return os.path.join(PathManager.get_home(), 'Library/Application Support/Cursor')
        else:  # Linux
            return os.path.join(PathManager.get_home(), '.config/Cursor')

    @staticmethod
    def get_updater_path():
        system = PathManager.get_system()
        if system == "windows":
            return os.path.join(os.getenv('APPDATA'), 'Local', 'cursor-updater')
        elif system == "darwin":
            return os.path.join(PathManager.get_home(), 'Library/Application Support/cursor-updater')
        else:  # Linux
            return os.path.join(PathManager.get_home(), '.config/cursor-updater')

    @staticmethod
    def is_admin():
        try:
            if PathManager.get_system() == "windows":
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin()
            else:
                return os.geteuid() == 0
        except:
            return False

class CursorHelper:
    def __init__(self):
        self.system = PathManager.get_system()
        self.storage_file = os.path.join(PathManager.get_app_data_path(), 'User/globalStorage/storage.json')
        self.backup_dir = os.path.join(PathManager.get_app_data_path(), 'User/globalStorage/backups')
        self.updater_path = PathManager.get_updater_path()
        self.lang = self._detect_language()

    def _detect_language(self):
        """检测系统语言"""
        if self.system == "windows":
            import locale
            try:
                # 获取 Windows 系统语言设置
                lang = locale.getdefaultlocale()[0]
                if lang and 'zh' in lang.lower():
                    return 'zh'
            except:
                # 如果获取失败，尝试获取环境变量
                lang = os.getenv('LANG') or os.getenv('LANGUAGE') or os.getenv('LC_ALL')
                if lang and 'zh' in lang.lower():
                    return 'zh'
        else:
            # Unix 系统获取环境变量
            lang = os.getenv('LANG', 'en_US.UTF-8').split('.')[0]
            if lang.startswith('zh'):
                return 'zh'
        return 'en'

    def log_info(self, message):
        print(f"[信息/INFO] {message}")

    def log_warn(self, message):
        print(f"[警告/WARNING] {message}")

    def log_error(self, message):
        print(f"[错误/ERROR] {message}")

    def check_permissions(self):
        if not PathManager.is_admin():
            self.log_error("请以管理员权限运行此脚本 / Please run this script with administrator privileges")
            if self.system == "windows":
                print("请右键点击并选择'以管理员身份运行' / Please right-click and select 'Run as administrator'")
            else:
                print("请使用 sudo 运行此脚本 / Please run this script with sudo")
            sys.exit(1)

    def kill_cursor_process(self):
        self.log_info("正在检查 Cursor 进程... / Checking Cursor process...")
        
        try:
            if self.system == "windows":
                # Windows: 使用 taskkill 命令
                subprocess.run(['tasklist', '/FI', 'IMAGENAME eq cursor.exe'], capture_output=True, text=True)
                result = subprocess.run(['taskkill', '/F', '/IM', 'cursor.exe'], 
                                     capture_output=True, text=True)
                if "成功" in result.stdout or "SUCCESS" in result.stdout:
                    self.log_info("Cursor 进程已终止 / Cursor process terminated")
                elif "找不到" in result.stdout or "not found" in result.stdout:
                    self.log_info("未发现运行中的 Cursor 进程 / No Cursor process found")
            else:
                # Unix: 使用 pkill 命令
                try:
                    subprocess.run(['pgrep', 'cursor'], check=True)
                    subprocess.run(['pkill', '-f', 'cursor'])
                    self.log_info("Cursor 进程已终止 / Cursor process terminated")
                except subprocess.CalledProcessError:
                    self.log_info("未发现运行中的 Cursor 进程 / No Cursor process found")
                    
        except Exception as e:
            self.log_error(f"终止进程时出错 / Error terminating process: {str(e)}")

    def backup_config(self):
        if not os.path.exists(self.storage_file):
            self.log_warn("配置文件不存在，跳过备份 / Config file doesn't exist, skipping backup")
            return

        os.makedirs(self.backup_dir, exist_ok=True)
        backup_file = os.path.join(self.backup_dir, 
                                 f"storage.json.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}")

        try:
            shutil.copy2(self.storage_file, backup_file)
            self.log_info(f"备份已创建 / Backup created: {backup_file}")
        except Exception as e:
            self.log_error(f"备份失败 / Backup failed: {str(e)}")
            sys.exit(1)

    def generate_new_config(self):
        if not os.path.exists(self.storage_file):
            self.log_error(f"未找到配置文件 / Config file not found: {self.storage_file}")
            self.log_warn("请先安装并运行一次 Cursor / Please install and run Cursor first")
            sys.exit(1)

        try:
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                config = json.load(f)

            # 生成新的唯一标识符
            config["telemetry.machineId"] = f"authuser_{uuid.uuid4().hex}"
            config["telemetry.macMachineId"] = uuid.uuid4().hex
            config["telemetry.devDeviceId"] = str(uuid.uuid4())
            config["telemetry.sqmId"] = "{" + str(uuid.uuid4()).upper() + "}"

            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2)

            self.log_info("配置已更新 / Configuration updated")

        except Exception as e:
            self.log_error(f"更新配置失败 / Failed to update config: {str(e)}")
            sys.exit(1)

    def disable_auto_update(self):
        try:
            if os.path.exists(self.updater_path):
                if os.path.isdir(self.updater_path):
                    shutil.rmtree(self.updater_path)
                else:
                    os.remove(self.updater_path)

            Path(self.updater_path).touch()
            
            if self.system == "windows":
                subprocess.run(['attrib', '+R', self.updater_path], check=True)
            else:
                os.chmod(self.updater_path, 0o444)

            self.log_info("自动更新已禁用 / Auto-update disabled")
            
        except Exception as e:
            self.log_error(f"禁用自动更新失败 / Failed to disable auto-update: {str(e)}")
            self.show_manual_steps()

    def show_manual_steps(self):
        print("\n手动操作步骤 / Manual Steps:")
        if self.system == "windows":
            print("""
1. 以管理员身份打开命令提示符 / Open Command Prompt as Administrator
2. 执行以下命令 / Run these commands:
   del /F /Q "%APPDATA%\\Local\\cursor-updater"
   type nul > "%APPDATA%\\Local\\cursor-updater"
   attrib +R "%APPDATA%\\Local\\cursor-updater"
            """)
        else:
            print(f"""
1. 打开终端 / Open Terminal
2. 执行以下命令 / Run these commands:
   sudo rm -rf "{self.updater_path}"
   sudo touch "{self.updater_path}"
   sudo chmod 444 "{self.updater_path}"
            """)

    def show_banner(self):
        print("\n=== Cursor New ===")
        print(f"版本 / Version: 1.0.0")
        print(f"支持的 Cursor 版本 / Supported Cursor Version: 0.45.11")
        print(f"项目主页 / Homepage: https://github.com/jsjm1986/cursor-new")
        print("=" * 50)

    def select_language(self):
        print("\n选择语言 / Select Language:")
        print("1) English / 英文")
        print("2) 中文 / Chinese")
        choice = input("\n>>> ")
        if choice == "2":
            self.lang = "zh"
        else:
            self.lang = "en"
        self.show_banner()

    def run(self):
        try:
            self.show_banner()
            self.check_permissions()
            
            while True:
                print("\n" + ("请选择操作 / Select Operation:"))
                print("1) " + "重置 Cursor ID（移除试用限制）/ Reset Cursor ID (removes trial limitations)")
                print("2) " + "禁用自动更新 / Disable Auto-update")
                print("3) " + "显示手动更新说明 / Show Manual Update Instructions")
                print("4) " + "切换语言 / Switch Language")
                print("5) " + "退出 / Exit")
                
                choice = input("\n>>> ")
                
                if choice == "1":
                    self.kill_cursor_process()
                    self.backup_config()
                    self.generate_new_config()
                elif choice == "2":
                    self.kill_cursor_process()
                    self.disable_auto_update()
                elif choice == "3":
                    self.show_manual_steps()
                elif choice == "4":
                    self.select_language()
                    continue
                elif choice == "5":
                    break
                
                input("\n" + "按回车键继续... / Press Enter to continue...")
                
        except KeyboardInterrupt:
            print("\n已取消 / Cancelled")
        except Exception as e:
            self.log_error(f"发生错误 / An error occurred: {str(e)}")
        finally:
            print("\n感谢使用！请重启 Cursor 以应用更改。/ Thank you! Please restart Cursor to apply changes.")

if __name__ == "__main__":
    helper = CursorHelper()
    helper.run() 