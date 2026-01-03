import pandas as pd

# 读取Excel文件
df = pd.read_excel('001-FormartData.xlsx', sheet_name='Sheet1')

# 使用melt进行逆透视，保留前三列（工号、姓名、部门）作为标识列
melted_df = df.melt(
    id_vars=['工号', '姓名', '部门'],  # 保留这三列不变
    var_name='日期',                  # 原列名（如“1号”、“2号”）将转为“日期”列
    value_name='打卡时间'              # 原单元格中的时间数据将转为“打卡时间”列
)

# 按工号和日期排序（可选）
melted_df = melted_df.sort_values(by=['工号', '日期']).reset_index(drop=True)

# 显示前几行查看结果
print(melted_df.head())

# 保存到新的Excel文件（可选）
melted_df.to_excel('002-NTSdata.xlsx', index=False)

