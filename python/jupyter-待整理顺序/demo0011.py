import pandas as pd
from tabulate import tabulate

# 读取数据
df = pd.read_excel('测试数据.xlsx')

# 预处理数据 - 截断过长的内容
df_display = df.copy()
for col in df_display.columns:
    if df_display[col].dtype == 'object':
        df_display[col] = df_display[col].astype(str).str[:30] + '...'

# 设置显示选项
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 150)

# 显示选项菜单
print("请选择显示方式:")
print("1. Pandas默认显示")
print("2. 表格形式显示")
print("3. 动态调整列宽显示")

choice = input("请输入选择(1-3): ")

if choice == '1':
    print(df_display.to_string(index=False))
elif choice == '2':
    print(tabulate(df_display, headers='keys', tablefmt='fancy_grid', showindex=False))
elif choice == '3':
    # 动态计算每列宽度
    col_formats = {}
    for col in df_display.columns:
        max_len = max(df_display[col].astype(str).apply(len).max(), len(col))
        col_formats[col] = f"{{:<{max_len}}}".format

    # 应用格式
    formatted_df = df_display.copy()
    for col, fmt in col_formats.items():
        formatted_df[col] = formatted_df[col].astype(str).apply(lambda x: fmt(x))

    print(formatted_df.to_string(index=False, justify='left'))
else:
    print("无效选择，使用默认显示")
    print(df_display.to_string(index=False))