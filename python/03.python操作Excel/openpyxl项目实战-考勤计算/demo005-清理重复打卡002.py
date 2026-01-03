def clean_attendance_records(time_list):
    if len(time_list) == 0:
        return []
    if len(time_list) == 1:
        return time_list

    low = '11:30'
    high = '13:00'
    first_overall = time_list[0]
    last_overall = time_list[-1]

    interval_times = [t for t in time_list if low <= t <= high]

    if not interval_times:
        return [first_overall, last_overall]

    first_interval = min(interval_times)
    last_interval = max(interval_times)

    result = [first_overall]

    if first_interval != first_overall and first_interval != last_overall:
        result.append(first_interval)

    if last_interval != last_overall and last_interval != first_interval:
        result.append(last_interval)

    result.append(last_overall)

    return result


# 示例使用
time_list = ['07:11', '11:32', '11:50', '12:07', '12:40', '12:59', '17:03']
cleaned_list = clean_attendance_records(time_list)
print(cleaned_list)  # 输出: ['07:11', '11:32', '12:59', '17:03']