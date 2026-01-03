import pandas as pd
import numpy as np
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# 读取Excel文件
df = pd.read_excel('004-CelldataMove.xlsx')

# 新增标记列
df['是否休息'] = df['早上上班'].apply(lambda x: '是' if x == '休息' else '否')
df['07:00缺卡'] = df['早上上班'].apply(lambda x: '是' if x == '早上班缺卡' else '否')
df['11:30缺卡'] = df['早上下班'].apply(lambda x: '是' if x == '早下班缺卡' else '否')
df['13:00缺卡'] = df['下午上班'].apply(lambda x: '是' if x == '午上班缺卡' else '否')
df['下班缺卡'] = df['最后打卡'].apply(lambda x: '是' if x == '午下班缺卡' else '否')


# 自定义舍入函数，最小单位0.5小时
def round_to_half_hour(hours):
    """将小时数舍入到最近的0.5小时"""
    if pd.isna(hours) or hours == 0:
        return 0
    return round(hours * 2) / 2


# 计算早上工时函数
def calculate_morning_hours(row):
    """计算早上工时"""
    if row['是否休息'] == '是' or pd.isna(row['早上上班']) or pd.isna(row['早上下班']):
        return 0

    try:
        # 处理时间数据
        start_time = pd.to_datetime(row['早上上班'], format='%H:%M:%S', errors='coerce')
        end_time = pd.to_datetime(row['早上下班'], format='%H:%M:%S', errors='coerce')

        if pd.isna(start_time) or pd.isna(end_time):
            return 0

        # 计算工时（小时）
        hours = (end_time - start_time).total_seconds() / 3600
        return round_to_half_hour(hours)
    except:
        return 0


def calculate_afternoon_hours(row):
    """计算下午工时"""
    if row['是否休息'] == '是' or pd.isna(row['下午上班']) or pd.isna(row['最后打卡']):
        return 0

    try:
        # 处理时间数据
        start_time = pd.to_datetime(row['下午上班'], format='%H:%M:%S', errors='coerce')
        end_time = pd.to_datetime(row['最后打卡'], format='%H:%M:%S', errors='coerce')

        if pd.isna(start_time) or pd.isna(end_time):
            return 0

        # 计算工时（小时）
        hours = (end_time - start_time).total_seconds() / 3600
        return round_to_half_hour(hours)
    except:
        return 0


def calculate_total_daily_hours(row):
    """计算每日总工时"""
    if row['是否休息'] == '是':
        return 0
    total = row['早上工时'] + row['下午工时']
    return round_to_half_hour(total)


# 计算各时段工时
df['早上工时'] = df.apply(calculate_morning_hours, axis=1)
df['下午工时'] = df.apply(calculate_afternoon_hours, axis=1)
df['每日总工时'] = df.apply(calculate_total_daily_hours, axis=1)


# 创建统计汇总信息到DataFrame
def create_summary_dataframe(df):
    """创建统计摘要DataFrame"""
    total_days = len(df)
    rest_days = len(df[df['是否休息'] == '是'])
    work_days = total_days - rest_days

    total_morning_hours = df['早上工时'].sum()
    total_afternoon_hours = df['下午工时'].sum()
    total_hours = df['每日总工时'].sum()

    # 创建统计摘要DataFrame
    summary_data = {
        '统计项目': ['总天数', '休息天数', '工作天数', '早上总工时', '下午总工时', '总工时'],
        '数值': [total_days, rest_days, work_days,
                 total_morning_hours, total_afternoon_hours, total_hours],
        '单位': ['天', '天', '天', '小时', '小时', '小时']
    }

    summary_df = pd.DataFrame(summary_data)
    return summary_df


# 创建详细统计信息（按人员分组，如果有多个人员）
def create_detailed_summary(df):
    """创建详细统计信息"""
    if '姓名' in df.columns:
        grouped = df.groupby('姓名').agg({
            '每日总工时': 'sum',
            '是否休息': lambda x: (x == '否').sum(),
            '早上工时': 'sum',
            '下午工时': 'sum'
        }).round(1)

        grouped.columns = ['总工时', '工作天数', '早上总工时', '下午总工时']
        grouped['平均每日工时'] = (grouped['总工时'] / grouped['工作天数']).round(1)
        return grouped.reset_index()
    else:
        return pd.DataFrame()  # 如果没有姓名列，返回空DataFrame


# 生成统计DataFrame
summary_df = create_summary_dataframe(df)
detailed_summary_df = create_detailed_summary(df)

# 显示统计结果
print("工时统计摘要（最小单位0.5小时）：")
print(summary_df)

if not detailed_summary_df.empty:
    print("\n按人员统计：")
    print(detailed_summary_df)

# 保存到Excel文件（包含两个sheet）
with pd.ExcelWriter('005-tongjichenggong.xlsx', engine='openpyxl') as writer:
    # Sheet1: 原始数据加工时计算
    df.to_excel(writer, sheet_name='原始数据', index=False)

    # Sheet2: 统计摘要
    summary_df.to_excel(writer, sheet_name='统计摘要', index=False)

    # Sheet3: 详细统计（如果有人员数据）
    if not detailed_summary_df.empty:
        detailed_summary_df.to_excel(writer, sheet_name='人员统计', index=False)

    # 获取workbook和worksheet对象进行格式设置
    workbook = writer.book
    worksheet = writer.sheets['统计摘要']

    # 设置列宽
    worksheet.column_dimensions['A'].width = 15
    worksheet.column_dimensions['B'].width = 12
    worksheet.column_dimensions['C'].width = 8

print("\n已将数据保存到Excel文件，包含以下工作表：")
print("- 原始数据：包含工时计算的完整数据")
print("- 统计摘要：总体统计信息")
if not detailed_summary_df.empty:
    print("- 人员统计：按人员分组的详细统计")