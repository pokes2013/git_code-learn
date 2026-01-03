from datetime import datetime, time, timedelta
from typing import List, Dict, Optional


class PunchCardSystem:
    def __init__(self):
        self.time_ranges = {
            "morning_work": ("08:00", "09:30"),  # 上午上班
            "morning_leave": ("11:50", "13:00"),  # 上午下班
            "afternoon_work": ("12:30", "14:00"),  # 下午上班
            "afternoon_leave": ("17:00", "18:30")  # 下午下班
        }

        # 记录每天的打卡情况
        self.daily_records = {}

    def add_punch(self, date_str: str, punch_time_str: str):
        """添加打卡记录"""
        if date_str not in self.daily_records:
            self.daily_records[date_str] = []

        punch_time = datetime.strptime(punch_time_str, "%H:%M").time()
        self.daily_records[date_str].append(punch_time)
        self.daily_records[date_str].sort()

    def check_missing_punches(self, date_str: str) -> Dict[str, bool]:
        """检查某天的漏打卡情况"""
        if date_str not in self.daily_records:
            return {punch_type: False for punch_type in self.time_ranges.keys()}

        punches = self.daily_records[date_str]
        result = {}

        # 检查每个时间段是否有打卡
        for punch_type, (start_str, end_str) in self.time_ranges.items():
            start_time = datetime.strptime(start_str, "%H:%M").time()
            end_time = datetime.strptime(end_str, "%H:%M").time()

            has_punch = any(start_time <= punch <= end_time for punch in punches)
            result[punch_type] = has_punch

        return result

    def get_daily_summary(self, date_str: str) -> str:
        """获取每日考勤摘要"""
        missing_info = self.check_missing_punches(date_str)
        punches = self.daily_records.get(date_str, [])

        summary = f"日期 {date_str} 考勤情况:\n"
        summary += f"打卡记录: {[p.strftime('%H:%M') for p in punches]}\n"

        for punch_type, has_punch in missing_info.items():
            status = "✅ 正常" if has_punch else "❌ 漏打卡"
            summary += f"{punch_type}: {status}\n"

        return summary


# 使用示例
system = PunchCardSystem()

# 模拟几天的打卡数据
system.add_punch("2024-01-15", "08:30")  # 上午上班
system.add_punch("2024-01-15", "12:00")  # 上午下班
system.add_punch("2024-01-15", "17:30")  # 下午下班
# 漏打了中午上班卡

system.add_punch("2024-01-16", "08:15")  # 上午上班
system.add_punch("2024-01-16", "12:20")  # 上午下班
system.add_punch("2024-01-16", "13:45")  # 中午上班
system.add_punch("2024-01-16", "18:00")  # 下午下班

print(system.get_daily_summary("2024-01-15"))
print(system.get_daily_summary("2024-01-16"))