tasks = [
    {"title": "阅读课本", "course": "Python 基础", "completed": False},
    {"title": "整理笔记", "course": "数据库基础", "completed": True},
    {"title": "完成习题", "course": "Python 基础", "completed": False},
]

print(tasks[1]["title"])

tasks.append(
    {"title": "练习列表和字典", "course": "Python 基础", "completed": False}
)
print(len(tasks))

print("修改前：")
print(tasks[0]["completed"])
print(tasks[1]["completed"])
print(tasks[2]["completed"])

tasks[0]["completed"] = True

print("修改后：")
print(tasks[0]["completed"])
print(tasks[1]["completed"])
print(tasks[2]["completed"])
