

print("Введите диаметр и толщину стенки")
print("Введите 'q' для завершения.")
while True:
    d = input("\nДиаметр: ")
    if d == 'q':
        break
    x = input("Стенка: ")
    if x == 'q':
        break
    m = input("Метраж: ")
    if m == 'q':
        break

    answer = ((int(d) - int(x)) * int(x)) / 40.55
    answer_total = int(m) * answer / 1000
    print(answer)
    print(answer_total)



