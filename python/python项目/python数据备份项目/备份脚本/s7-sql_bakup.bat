@echo off
set MYSQL_BIN="D:\Mysql\mysql_x64\bin\mysqldump.exe"
set BACKUP_DIR="E:\data_bak\s7_sql_bak"
set WINRAR="C:\Program Files (x86)\WinRAR\WinRAR.exe"

:: 检查目录是否存在，无权限时会提示
if not exist %BACKUP_DIR% (
    mkdir %BACKUP_DIR%
    if errorlevel 1 (
        echo [错误] 无法创建目录 %BACKUP_DIR%，请检查权限或路径！
        pause
        exit /b
    )
)

:: 检查 WinRAR 是否存在
if not exist %WINRAR% (
    echo [错误] WinRAR 未找到，请修改路径：%WINRAR%
    pause
    exit /b
)

:: 获取日期和时间
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value 2^>nul') do set "datetime=%%a"
if "%datetime%"=="" (
    echo [错误] 无法获取系统时间，请检查 wmic 命令！
    pause
    exit /b
)
set "current_date=%datetime:~0,4%%datetime:~4,2%%datetime:~6,2%"
set "current_time=%datetime:~8,2%%datetime:~10,2%"

:: 定义文件名
set BACKUP_FILE=%BACKUP_DIR%\s7_backup_%current_date%_%current_time%.sql
set ZIP_FILE=%BACKUP_DIR%\s7_backup_%current_date%_%current_time%.zip

:: 执行 MySQL 备份（错误时会暂停）
echo 正在备份数据库...
%MYSQL_BIN% -h 127.0.0.1 -P 3308 -u root -p123456 s7 > %BACKUP_FILE%
if errorlevel 1 (
    echo [错误] MySQL 备份失败，请检查连接参数或数据库状态！
    pause
    exit /b
)

:: 压缩为 ZIP
echo 正在压缩备份文件...
%WINRAR% a -afzip -r -df -ep1 -ibck %ZIP_FILE% %BACKUP_FILE%
if errorlevel 1 (
    echo [错误] 压缩失败，请检查 WinRAR 或文件权限！
    pause
    exit /b
)

:: 记录日志
echo [%date% %time%] 备份成功: %ZIP_FILE% >> %BACKUP_DIR%\backup_log.txt

:: 清理90天前的备份（静默执行，错误不提示）
forfiles /p %BACKUP_DIR% /m *.zip /d -90 /c "cmd /c del @path" 2>nul

echo 备份完成：%ZIP_FILE%