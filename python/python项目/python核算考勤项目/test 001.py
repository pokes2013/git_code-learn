import pandas as pd
import numpy as np

# 假设你的DataFrame名为df
# 先创建示例数据（你可以跳过这一步，直接使用你的数据）
data = {
    '姓名': ['严钰'] * 6,
    '日期': ['11号', '12号', '13号', '14号', '15号', '16号'],
    '上班时间': ['07:25:00', '07:18:00', '07:22:00', '07:26:00', '休息', '休息'],
    '下班时间': ['11:31:00', '11:30:00', '11:59:00', '11:57:00', np.nan, np.nan]
}

df = pd.DataFrame(data)


# 方法1：过滤掉休息日，然后计算工时
def calculate_working_hours(df):
    # 复制一份数据，避免修改原数据
    temp_df = df.copy()

    # 过滤掉休息日（上班时间为"休息"或NaN的行）
    # 同时确保下班时间也不是NaN
    work_days = temp_df[
        (temp_df['上班时间'] != '休息') &
        (temp_df['下班时间'].notna()) &
        (temp_df['上班时间'].notna())
        ].copy()

    # 将时间字符串转换为datetime格式
    work_days['上班时间_dt'] = pd.to_datetime(work_days['上班时间'], format='%H:%M:%S', errors='coerce')
    work_days['下班时间_dt'] = pd.to_datetime(work_days['下班时间'], format='%H:%M:%S', errors='coerce')

    # 计算工时（小时为单位）
    work_days['工时'] = (work_days['下班时间_dt'] - work_days['上班时间_dt']).dt.total_seconds() / 3600

    return work_days


# 使用方法
result_df = calculate_working_hours(df)
print("有效工作日数据：")
print(result_df[['姓名', '日期', '上班时间', '下班时间', '工时']])

# 统计总工时
total_hours = result_df['工时'].sum()
print(f"\n总工时：{total_hours:.2f} 小时")

# 统计工作日天数
work_days_count = len(result_df)
print(f"有效工作日天数：{work_days_count} 天")


# 方法2：更简洁的一行式统计（如果你只需要总和）
def quick_total_hours(df):
    # 直接过滤并计算
    mask = (df['上班时间'] != '休息') & df['上班时间'].notna() & df['下班时间'].notna()
    total = sum(
        (pd.to_datetime(df.loc[mask, '下班时间'], format='%H:%M:%S') -
         pd.to_datetime(df.loc[mask, '上班时间'], format='%H:%M:%S')).dt.total_seconds() / 3600
    )
    return total


print(f"\n快速计算总工时：{quick_total_hours(df):.2f} 小时")