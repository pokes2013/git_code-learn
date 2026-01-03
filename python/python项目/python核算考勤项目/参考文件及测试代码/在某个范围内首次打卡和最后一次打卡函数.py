from datetime import datetime, time


def get_first_last_punch(timestamps_list, start_time_str, end_time_str):
    """
    从考勤数据列表中获取指定时间范围内的第一次和最后一次打卡时间

    参数:
    timestamps_list: 时间字符串列表，格式为 ['HH:MM:SS', 'HH:MM:SS', ...]
    start_time_str: 开始时间字符串 (格式: HH:MM:SS)
    end_time_str: 结束时间字符串 (格式: HH:MM:SS)

    返回:
    tuple: (第一次打卡时间字符串, 最后一次打卡时间字符串)，如果没有符合条件的打卡则返回 (None, None)
    """
    # 将时间范围转换为time对象
    start_time = datetime.strptime(start_time_str, '%H:%M:%S').time()
    end_time = datetime.strptime(end_time_str, '%H:%M:%S').time()

    # 筛选在时间范围内的打卡记录
    filtered_timestamps = []
    for ts_str in timestamps_list:
        try:
            ts_time = datetime.strptime(ts_str, '%H:%M:%S').time()
            if start_time <= ts_time <= end_time:
                filtered_timestamps.append(ts_str)
        except ValueError:
            continue

    # 如果没有符合条件的打卡记录
    if not filtered_timestamps:
        return None, None

    # 找到第一次和最后一次打卡时间（按时间顺序排序）
    filtered_timestamps.sort(key=lambda x: datetime.strptime(x, '%H:%M:%S').time())

    first_punch = filtered_timestamps[0]
    last_punch = filtered_timestamps[-1]

    return first_punch, last_punch


# 更简洁的版本（使用列表推导式）



# 示例使用
if __name__ == "__main__":
    # 示例数据 - 现在是列表形式

    def get_first_last_punch_v2(timestamps_list, start_time_str, end_time_str):
        """
        简化版本，功能相同
        """
        start_time = datetime.strptime(start_time_str, '%H:%M:%S').time()
        end_time = datetime.strptime(end_time_str, '%H:%M:%S').time()

        # 筛选并排序
        filtered = sorted([
            ts for ts in timestamps_list
            if start_time <= datetime.strptime(ts, '%H:%M:%S').time() <= end_time
        ], key=lambda x: datetime.strptime(x, '%H:%M:%S').time())

        if not filtered:
            return None, None

        return filtered[0], filtered[-1]

    timestamps = ["07:15:00", "07:19:00", "07:19:00", "11:32:00", "11:33:00", "12:30:00","13:00:00", "21:03:00"]


    rs1 = get_first_last_punch_v2(timestamps, "07:00:00", "11:50:00")
    rs2 = get_first_last_punch_v2(timestamps, "12:00:00", "23:50:00")

    print(rs1)
    # 运行结果：('07:15:00', '11:32:00')
    print(rs2)
    # 运行结果：('19:03:00', '19:03:00')

