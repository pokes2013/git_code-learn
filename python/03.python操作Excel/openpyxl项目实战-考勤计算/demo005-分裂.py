import xlrd
import pandas as pd

# 读取Excel文件
df = pd.read_excel("melted_cities.xlsx")



# 准备一个空列表来收集所有数据
all_data = []

for index, row in df.iterrows():
    row_list = ['' if pd.isna(item) else item for item in row]
    text_q = row_list[0:4]
    text_h = row_list[4]

    # 简单的时间转换（假设格式为HHMMSS）
    text_x = []
    for i in range(0, len(text_h), 5):
        time_str = text_h[i:i + 5]
        try:
            # 转换为时间格式
            time_obj = pd.to_datetime(time_str, format='%H%M%S').time()
            text_x.append(time_obj)
        except:
            # 转换失败就保持原样
            text_x.append(time_str)

    data = text_q + text_x
    all_data.append(data)  # 将每行数据添加到总列表中
    print(data)

# 创建DataFrame并保存到Excel
result_df = pd.DataFrame(all_data)
result_df.to_excel('fenlie.xlsx', index=False, header=False)