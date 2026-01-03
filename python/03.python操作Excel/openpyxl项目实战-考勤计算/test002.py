
import pandas as pd
import numpy as np


def read_odd_rows_from_5(file_path):
    # 读取Excel文件，跳过前4行
    df = pd.read_excel(file_path, skiprows=4, header=None)

    # 选择奇数行（注意：DataFrame索引从0开始，所以第5行对应索引0）
    odd_rows = df.iloc[::2]  # 步长为2，选择所有奇数索引行

    rows_as_lists = []
    for index, row in odd_rows.iterrows():
        # 过滤空值（NaN、None、空字符串等）
        row_list = [x for x in row.tolist()
                    if not (pd.isna(x) or x == '' or x is None)]
        if row_list:  # 只添加非空列表
            rows_as_lists.append(row_list)
            print(f"第 {index + 5} 行（奇数行）: {row_list}")

    return rows_as_lists


# # 使用示例
# file_path = '1111.xlsx'
# result = read_odd_rows_from_5(file_path)



# 读取偶数行

def read_even_rows_from_5(file_path):
    # 读取Excel文件，跳过前4行
    df = pd.read_excel(file_path, skiprows=4, header=None)

    # 选择偶数行（注意：DataFrame索引从0开始，所以第5行对应索引0是偶数行）
    even_rows = df.iloc[1::2]  # 从索引1开始，步长为2，选择所有偶数索引行

    rows_as_lists = []
    for index, row in even_rows.iterrows():
        # 保留所有值，包括空值
        row_list = row.tolist()
        rows_as_lists.append(row_list)
        actual_row_num = index + 5  # 计算实际Excel行号
        print(f"第 {actual_row_num} 行（偶数行）: {row_list}")

    return rows_as_lists


# 使用示例
file_path = '1111.xlsx'
result = read_even_rows_from_5(file_path)
