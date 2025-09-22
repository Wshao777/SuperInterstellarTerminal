#!/usr/bin/env python3

from automation import task_scheduler
from monitor import monitor_system
from laser_cat_guard import check_guard

def main():
    print("🚀 Super Interstellar Terminal 啟動中...")
    check_guard()
    monitor_system()
    task_scheduler.run_tasks()

if __name__ == "__main__":
    main()
