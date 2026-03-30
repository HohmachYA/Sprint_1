# Строка содержит пять временных значений. Они записаны через запятую:
# '1h 45m,360s,25m,30m 120s,2h 60s'.
# Напиши цикл, который посчитает общее количество минут. Результат сохрани в переменную и выведи на экран. Используй в решении методы 
# split(), replace() и оператор in.
# Обрати внимание: временное значение может состоять из одного, двух или трёх единиц времени. Значения расшифровываются так:
# часы — любое положительное целое число и символ h;
# минуты — любое положительное целое число и символ m;
# секунды — положительное целое число кратное 60 и символ s.


def time_str_value():
    times_str = ('1h 45m,360s,25m,30m 120s,2h 60s')
    count_time = 0
    time_str_replace = times_str.replace(" ", ",")
    time_str_split = time_str_replace.split(",")
    for i in time_str_split:
        if "h" in i:
            hours = int(i.replace("h", ""))
            count_time += hours * 60
        elif "m" in i:
            minutes = int(i.replace("m", ""))
            count_time += minutes
        elif "s" in i:
            seconds = int(i.replace("s", ""))
            count_time += seconds / 60
    print(count_time)
    return count_time
time_str_value()