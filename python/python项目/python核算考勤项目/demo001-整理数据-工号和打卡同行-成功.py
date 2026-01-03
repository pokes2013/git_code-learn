# 导入所需库
import xlrd
import pandas as pd

# 打开.xls格式的Excel文件
workbook = xlrd.open_workbook(r'8月份标准报表.xls')
sheet = workbook.sheet_by_index(2)

zz_data = []

# 定义表格的列标题
head = ['工号', '姓名', '部门', '1号', '2号', '3号', '4号', '5号', '6号', '7号', '8号', '9号', '10号', '11号', '12号',
        '13号', '14号',
        '15号', '16号', '17号', '18号', '19号', '20号', '21号', '22号', '23号', '24号', '25号', '26号', '27号', '28号',
        '29号', '30号', '31号']
zz_data.append(head)

# 从第5行（索引4）开始，以步长2（每次处理两行）遍历所有行
for row in range(4, sheet.nrows, 2):

    # 处理人员信息行（偶数行）- 直接提取前几个非空值
    even_row_data = sheet.row_values(row)

    # 提取人员信息：前几个非空值就是工号、姓名、部门
    person_info = []
    for item in even_row_data:
        if item and item not in ['工 号:', '姓 名:', '部 门:']:
            person_info.append(item)
        if len(person_info) >= 3:  # 只需要工号、姓名、部门三个信息
            break

    # 如果提取的信息不足3个，用空字符串补齐
    while len(person_info) < 3:
        person_info.append('')

    # 处理考勤信息行（奇数行）- 绝对不能动，保留所有数据
    if row + 1 < sheet.nrows:
        odd_row_data = sheet.row_values(row + 1)  # 不进行任何过滤

        # 合并数据：精确提取的人员信息 + 原始的考勤信息
        combined_data = person_info + odd_row_data

        # 将合并后的数据添加到结果列表
        zz_data.append(combined_data)

        # print(f"合并第{row}行和第{row + 1}行: {combined_data}")
    else:
        print('警告数据错位，不可用')

# 写入文件
df = pd.DataFrame(zz_data)
df.to_excel('001-FormartData.xlsx', index=False, header=False)
print('写入完成！')
