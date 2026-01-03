# 导入所需库
from openpyxl import load_workbook  # 用于操作Excel文件（虽然这里未使用）
import xlrd  # 用于读取.xls格式的Excel文件
import pandas as pd  # 用于数据处理（虽然这里未使用）

# 打开.xls格式的Excel文件
workbook = xlrd.open_workbook(r'D:\DATA\SVN本地库\考勤核算\7月份-办公室人员-考勤机原始记录.xls')
# 获取工作簿中的第三个工作表（索引从0开始，所以索引2表示第三个工作表）
sheet = workbook.sheet_by_index(2)

zz_data = []

# 处理主标题：从第1行（索引0）读取数据
row = 0
# 获取第1行第1列的值，并去除空格
row_data_biaoti = sheet.row_values(row)[0].replace(" ", "")

# 处理副标题：从第3行（索引2）读取考勤月份数据
row = 2
# 获取第3行第3列的值，截取前7个字符，然后加上"月份"二字
row_data_yuefen = sheet.row_values(row)[2][0:7] + '月份'

# 组合主标题和副标题，格式为"主标题(副标题)"
row1 = [row_data_biaoti + '(' + row_data_yuefen + ')']
zz_data.append(row1)
# print(row1)

# 定义表格的列标题（字段名）
head = ['工号', '姓名', '1号', '2号', '3号', '4号', '5号', '6号', '7号', '9号', '10号', '11号', '12号', '13号', '14号',
        '15号','16号', '17号', '18号', '19号', '20号', '21号', '22号', '23号', '24号', '25号', '26号', '27号', '28号',
        '29号','30号','31号', ]
print(head)
zz_data.append(head)
# 创建一个空列表，用于存储合并后的行数据


# 从第5行（索引4）开始，以步长2（每次处理两行）遍历所有行
for row in range(4, sheet.nrows, 2):
    # 获取当前偶数行的数据，并过滤掉空值（空字符串、None等）
    even_row_data = [item for item in sheet.row_values(row) if item]
    even_row_data = [item for item in even_row_data if item not in ['工 号:', '姓 名:', '部 门:']]
    # 检查是否存在下一行（奇数行），避免索引越界错误
    if row + 1 < sheet.nrows:
        # 获取下一行（奇数行）的数据，并过滤空值
        odd_row_data = [item for item in sheet.row_values(row + 1) if item]
        # 将偶数行和奇数行的数据合并为一个列表
        combined_data = even_row_data + odd_row_data

        # 将合并后的数据添加到结果列表merged_data中
        zz_data.append(combined_data)

        # 打印合并信息，便于调试和查看
        # print(f"合并第{row}行和第{row + 1}行: {combined_data}")

    else:
        # 如果当前行是最后一行且没有下一行，则单独处理该行
        print('警告数据错位，不可用')

print(zz_data)

# 写入文件

# 不指定 columns 参数，这样就没有列标题
df = pd.DataFrame(zz_data)

# 写入Excel时也不需要额外设置
df.to_excel('cities.xlsx', index=False, header=False)

print('写入完成！')