from lunar_python import Solar


def query_almanac(year, month, day):
    # 创建 Solar 对象（公历日期）
    solar_date = Solar(year, month, day, 0, 0, 0)  # 默认时间为午夜 00:00:00

    # 转换为 Lunar 对象（农历日期）
    # lunar_date = solar_date.getlunar()
    lunar_date = solar_date.getLunar()

    # 显示农历日期和基本信息
    print(f"公历日期: {solar_date.toFullString()}")
    print(f"农历日期: {lunar_date.toFullString()}")
    print(f"干支纪年: {lunar_date.getYearInGanZhi()}")
    print(f"生肖: {lunar_date.getYearShengXiao()}")
    print(f"节气: {lunar_date.getJieQi()}")

    # 显示当天宜忌
    print(f"宜: {lunar_date.getDayYi()}")
    print(f"忌: {lunar_date.getDayJi()}")


def main():
    print("欢迎使用黄历查询程序！")
    year = int(input("请输入年份（公历）："))
    month = int(input("请输入月份（公历）："))
    day = int(input("请输入日期（公历）："))

    print("\n查询结果：")
    query_almanac(year, month, day)


if __name__ == "__main__":
    main()
