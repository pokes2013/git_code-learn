from openpyxl import load_workbook
from itertools import dropwhile
import datetime
from typing import List, Union
from datetime import time


def process_attendance_records(records: List[Union[str, datetime.time]]) -> List[Union[str, datetime.time]]:
    """
    处理打卡记录，按照规则筛选有效打卡时间

    规则说明：
    - 早上上班：取早于9:00的最早打卡时间
    - 早上下班：取最接近11:30且大于11:30的打卡时间
    - 下午上班：取最接近13:00且小于13:00的打卡时间
    - 下午下班：取最接近17:00且大于17:00的打卡时间
    - 晚上加班：取晚于17:00的最晚打卡时间

    Args:
        records: 原始打卡记录列表，格式为 [工号, 姓名, 公司, 日期, 时间1, 时间2, ...]
                前4个元素为员工基本信息，从第5个元素开始为打卡时间

    Returns:
        处理后的打卡记录列表，包含筛选后的有效打卡时间
        格式为 [工号, 姓名, 公司, 日期, 有效时间1, 有效时间2, ...]
    """
    # 提取时间部分（从索引4开始），并过滤掉None值
    # records[4:] 获取从第5个元素开始的所有打卡时间
    times = [t for t in records[4:] if t is not None]

    # 如果没有有效打卡时间，直接返回原始记录
    if not times:
        return records

    # 初始化结果时间列表，用于存储筛选后的有效打卡时间
    result_times = []

    # 1. 处理早上上班打卡：取第一次打卡（如果早于9:00）
    morning_candidates = [t for t in times if t < datetime.time(9, 0)]  # 筛选所有早于9:00的打卡时间
    if morning_candidates:
        morning_start = min(morning_candidates)  # 取最早的一个作为早上上班时间
        result_times.append(morning_start)

    # 2. 处理早上下班打卡：最接近11:30且大于11:30
    target_am_end = datetime.time(10, 59)  # 目标时间为10:59（接近11:30）
    am_end_candidates = [t for t in times if t > target_am_end]  # 筛选所有晚于10:59的打卡时间
    if am_end_candidates:
        # 使用lambda函数计算每个候选时间与目标时间的秒数差，取差值最小的
        am_end = min(am_end_candidates,
                     key=lambda t: (datetime.datetime.combine(datetime.date.today(), t) -
                                    datetime.datetime.combine(datetime.date.today(), target_am_end)).total_seconds())

        # 确保早上下班时间在早上上班时间之后（避免时间顺序错乱）
        if not result_times or am_end > result_times[-1]:
            result_times.append(am_end)

    # 3. 处理下午上班打卡：最接近13:00且小于13:00
    target_pm_start = datetime.time(13, 0)  # 目标时间为13:00
    # 筛选所有早于13:00且晚于11:30的打卡时间（排除午休前的打卡）
    pm_start_candidates = [t for t in times if t < target_pm_start and t > datetime.time(11, 30)]
    if pm_start_candidates:
        pm_start = max(pm_start_candidates)  # 取最接近13:00的时间（最大值最接近13:00）

        # 确保下午上班时间在早上下班时间之后
        if not result_times or pm_start > result_times[-1]:
            result_times.append(pm_start)

    # 4. 处理下午下班打卡：最接近17:00且大于17:00
    target_pm_end = datetime.time(16, 59)  # 目标时间为16:59（接近17:00）
    pm_end_candidates = [t for t in times if t > target_pm_end]  # 筛选所有晚于16:59的打卡时间
    if pm_end_candidates:
        # 计算每个候选时间与目标时间的秒数差，取差值最小的
        pm_end = min(pm_end_candidates,
                     key=lambda t: (datetime.datetime.combine(datetime.date.today(), t) -
                                    datetime.datetime.combine(datetime.date.today(), target_pm_end)).total_seconds())

        # 确保下午下班时间在合理的时间顺序之后
        if not result_times or pm_end > result_times[-1]:
            result_times.append(pm_end)

    # 5. 处理晚上加班打卡：取最后一次打卡（在17:00之后）
    overtime_candidates = [t for t in times if t > datetime.time(16, 59)]  # 筛选所有晚于16:59的打卡时间
    if overtime_candidates:
        overtime_end = max(overtime_candidates)  # 取最晚的一个作为加班结束时间

        # 确保加班时间在下午下班时间之后
        if not result_times or overtime_end > result_times[-1]:
            result_times.append(overtime_end)

    # 返回处理后的记录：前4个基本信息 + 筛选后的有效打卡时间
    return records[:4] + result_times


test_data_2 = ["002", "李四", "A公司", "2024-01-15",
               datetime.time(8, 15),  # 早上上班（最早）
               datetime.time(8, 45),  # 冗余打卡
               datetime.time(11, 40),  # 接近下班时间
               datetime.time(11, 50),  # 早上下班（最接近11:30）
               datetime.time(12, 30),  # 过早打卡
               datetime.time(12, 58),  # 下午上班（最接近13:00）
               datetime.time(17, 5),  # 下午下班（最接近17:00）
               datetime.time(18, 0),  # 加班打卡
               datetime.time(20, 0)]  # 晚上加班（最晚）

result_2 = process_attendance_records(test_data_2)
print(result_2)