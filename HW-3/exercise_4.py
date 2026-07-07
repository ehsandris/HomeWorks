import numpy as np

weather_data = np.random.randn(2, 8, 4) * 5 + 20 

def analyze_day(day):
    day_data = weather_data[day].T
    return day_data

analyze_day(0)

# ######################################
# def analyze_day(day):
#     print(day.shape)
#     return day

# # استخراج روز دوم
# day2 = weather_data[1]

# # تبدیل از (8,4) به (4,8)
# day2 = day2.T

# # ارسال به تابع
# result = analyze_day(day2)
# ######################################

new_weather_data = weather_data.reshape(-1)
print(new_weather_data.shape)

day3 = np.random.randn(8, 4).reshape(1, 8, 4)

weather_data = np.vstack((weather_data, day3))

print(weather_data.shape)