# Cursor New

[English](#english) | [中文](#chinese)

# <a name="chinese"></a>中文说明

跨平台的 Cursor IDE 增强工具，支持 Windows、macOS 和 Linux，无需安装任何依赖。

## 项目链接
- GitHub: https://github.com/jsjm1986/cursor-new
- 作者微信: jszmkx4

## 支持版本
- Cursor IDE: 0.45.11 及 0.45.x 系列版本
- 建议使用最新版本以获得最佳体验

## 项目简介

Cursor New 是一个专门为 Cursor IDE 开发的增强工具，旨在提供更好的用户体验。它采用纯 Python 开发，不依赖任何第三方库，支持多个操作系统平台，并提供中英文双语界面。

## 主要功能

- ✨ 重置 Cursor ID（移除试用限制）
- 🚫 禁用自动更新功能
- 💾 自动备份配置文件
- 🌏 多语言支持（中文/英文）
- 🔍 自动检测系统语言
- 💻 跨平台支持（Windows/macOS/Linux）

## Windows 用户使用指南

### 快速开始（推荐）

1. 下载 `cursor_new.exe`
2. 右键点击，选择"以管理员身份运行"
3. 根据菜单提示选择需要的操作
4. 完成后重启 Cursor

注意事项：
- 运行前请关闭 Cursor
- 程序会自动备份配置文件
- 如遇到安全提示，点击"仍要运行"

### 命令行运行

在管理员命令提示符中执行：
```cmd
cursor_new.exe
```

## macOS/Linux 用户使用指南

### 系统要求
- Python 3.6 或更高版本
- 管理员/root 权限

### 运行方法

1. 下载 `cursor-new.py`
2. 打开终端，进入文件所在目录
3. 执行命令：
```bash
# macOS
sudo python3 cursor-new.py

# Linux
sudo python3 cursor-new.py
```

## 使用说明

### 重置 Cursor ID

1. 关闭所有 Cursor 进程（程序会自动检测并关闭）
2. 选择选项 1："重置 Cursor ID"
3. 等待操作完成
4. 重启 Cursor

### 禁用自动更新

1. 关闭所有 Cursor 进程
2. 选择选项 2："禁用自动更新"
3. 等待操作完成
4. 重启 Cursor

### 手动操作说明

如果自动操作失败，可以选择选项 3 查看手动操作步骤。

## 配置文件位置

### Windows
- 配置文件：`%APPDATA%\\Cursor\\User\\globalStorage\\storage.json`
- 更新程序：`%APPDATA%\\Local\\cursor-updater`

### macOS
- 配置文件：`~/Library/Application Support/Cursor/User/globalStorage/storage.json`
- 更新程序：`~/Library/Application Support/cursor-updater`

### Linux
- 配置文件：`~/.config/Cursor/User/globalStorage/storage.json`
- 更新程序：`~/.config/cursor-updater`

## 常见问题

### 1. 为什么需要管理员权限？
- 程序需要修改系统文件和配置
- 需要管理系统进程（关闭 Cursor）
- 需要设置文件权限

### 2. 配置文件备份在哪里？
- Windows: `%APPDATA%\\Cursor\\User\\globalStorage\\backups`
- macOS: `~/Library/Application Support/Cursor/User/globalStorage/backups`
- Linux: `~/.config/Cursor/User/globalStorage/backups`

### 3. 如何恢复备份？
- 备份文件格式为：`storage.json.backup_YYYYMMDD_HHMMSS`
- 直接复制备份文件覆盖原配置文件即可

### 4. 禁用更新失败怎么办？
- 使用选项 3 查看手动操作步骤
- 按照系统对应的命令手动执行
- 确保文件权限设置正确

## 安全说明

- 所有操作前自动备份配置
- 使用 UUID 生成唯一标识符
- 不收集任何用户数据
- 源代码完全开放透明
- 支持手动操作方式

## 开发说明

### Windows 构建
```bash
# 安装 PyInstaller
pip install pyinstaller

# 构建可执行文件
pyinstaller --onefile --uac-admin --clean --name cursor_new cursor-new.py
```

### 其他平台
- 直接运行 Python 源码即可，无需构建

## 联系方式 / Contact

- 微信 / WeChat: jszmkx4
- GitHub: https://github.com/jsjm1986/cursor-new

## 许可证 / License

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 致谢 / Acknowledgments

感谢所有为本项目提供帮助和支持的开发者。

---

# <a name="english"></a>English

Cross-platform enhancement tool for Cursor IDE, supporting Windows, macOS, and Linux with no dependencies required.

## Project Link
- GitHub: https://github.com/jsjm1986/cursor-new
- WeChat: jszmkx4

## Supported Versions
- Cursor IDE: 0.45.11 and 0.45.x series
- Recommended to use the latest version for best experience

## Introduction

Cursor New is an enhancement tool specifically developed for Cursor IDE to provide a better user experience. It is built with pure Python, requires no third-party libraries, supports multiple operating systems, and offers both Chinese and English interfaces.

## Key Features

- ✨ Reset Cursor ID (removes trial limitations)
- 🚫 Disable auto-update function
- 💾 Automatic configuration backup
- 🌏 Multi-language support (Chinese/English)
- 🔍 Automatic system language detection
- 💻 Cross-platform support (Windows/macOS/Linux)

## Windows User Guide

### Quick Start (Recommended)

1. Download `cursor_new.exe`
2. Right-click and select "Run as administrator"
3. Choose desired operation from the menu
4. Restart Cursor after completion

Notes:
- Close Cursor before running
- Configuration will be automatically backed up
- If security warning appears, click "Run anyway"

### Command Line Usage

Execute in administrator command prompt:
```cmd
cursor_new.exe
```

## macOS/Linux User Guide

### System Requirements
- Python 3.6 or higher
- Administrator/root privileges

### Running Instructions

1. Download `cursor-new.py`
2. Open terminal and navigate to file directory
3. Execute command:
```bash
# macOS
sudo python3 cursor-new.py

# Linux
sudo python3 cursor-new.py
```

## Usage Instructions

### Reset Cursor ID

1. Close all Cursor processes (program will detect and close automatically)
2. Select option 1: "Reset Cursor ID"
3. Wait for completion
4. Restart Cursor

### Disable Auto-update

1. Close all Cursor processes
2. Select option 2: "Disable Auto-update"
3. Wait for completion
4. Restart Cursor

### Manual Operation Instructions

If automatic operation fails, select option 3 to view manual operation steps.

## Configuration File Locations

### Windows
- Config file: `%APPDATA%\\Cursor\\User\\globalStorage\\storage.json`
- Updater: `%APPDATA%\\Local\\cursor-updater`

### macOS
- Config file: `~/Library/Application Support/Cursor/User/globalStorage/storage.json`
- Updater: `~/Library/Application Support/cursor-updater`

### Linux
- Config file: `~/.config/Cursor/User/globalStorage/storage.json`
- Updater: `~/.config/cursor-updater`

## FAQ

### 1. Why are administrator privileges required?
- Program needs to modify system files and configurations
- Needs to manage system processes (closing Cursor)
- Needs to set file permissions

### 2. Where are configuration backups stored?
- Windows: `%APPDATA%\\Cursor\\User\\globalStorage\\backups`
- macOS: `~/Library/Application Support/Cursor/User/globalStorage/backups`
- Linux: `~/.config/Cursor/User/globalStorage/backups`

### 3. How to restore backups?
- Backup file format: `storage.json.backup_YYYYMMDD_HHMMSS`
- Simply copy backup file to replace original configuration file

### 4. What if disabling updates fails?
- Use option 3 to view manual operation steps
- Execute commands according to your system
- Ensure correct file permissions are set

## Security Notes

- Automatic configuration backup before operations
- UUID generation for unique identifiers
- No user data collection
- Fully open-source transparent code
- Manual operation support

## Development Notes

### Windows Build
```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile --uac-admin --clean --name cursor_new cursor-new.py
```

### Other Platforms
- Run Python source code directly, no build required

## Contact

- WeChat: jszmkx4
- GitHub: https://github.com/jsjm1986/cursor-new

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

Thanks to all developers who have helped and supported this project. 