def clean_attendance_records(times):
    """
    清理考勤打卡记录，移除时间间隔最小的重复打卡记录

    参数:
    times: 时间字符串列表，格式为 ['HH:MM', ...]

    返回:
    清理后的时间列表
    """
    if len(times) <= 1:
        return times

    # 将时间字符串转换为分钟数，方便计算
    def time_to_minutes(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes

    # 将分钟数转换回时间字符串
    def minutes_to_time(minutes):
        hours = minutes // 60
        minutes = minutes % 60
        return f"{hours:02d}:{minutes:02d}"

    # 转换为分钟数列表
    minutes_list = [time_to_minutes(t) for t in times]

    # 找出所有需要删除的索引
    to_remove = set()

    # 遍历所有相邻的时间对，找出间隔最小的重复记录
    for i in range(len(minutes_list) - 1):
        current_time = minutes_list[i]
        next_time = minutes_list[i + 1]
        time_diff = next_time - current_time

        # 如果时间间隔很小（比如小于5分钟），认为是重复打卡
        if time_diff < 5:  # 可以根据实际情况调整这个阈值
            # 找出应该删除哪一个（通常是保留第一个，删除第二个）
            # 但为了更智能，我们可以根据业务逻辑决定
            to_remove.add(i + 1)  # 默认删除第二个

    # 构建清理后的结果
    result = []
    for i, time_str in enumerate(times):
        if i not in to_remove:
            result.append(time_str)

    return result


# 测试数据
times = ['07:24', '11:30', '11:34', '12:50', '17:03']
cleaned_times = clean_attendance_records(times)

print("原始打卡记录:", times)
print("清理后记录:", cleaned_times)