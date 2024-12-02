#START Question 1
tuple1 = (99,) #a
print(tuple1)
print(type(tuple1))  # בדיקה אם זה tupel

tup2 = (77, 88, 99)
print(type(tup2)) #b
def len_tuple(t) -> int: #c
    return len(t)

def sum_tuple(t1, t2) -> int: #d
    return t1 + t2

def common_num(tup1, tup2) -> tuple: #e
    tup: list = []
    for i in tup1:
        if i in tup2:
            tup.append(i)
    return tuple(tup)

def different_num(tup1, tup2) -> tuple:
    result1 = list(filter(lambda i: i not in tup2, tup1)) #f
    result2 = list(filter(lambda x: x not in tup1, tup2))

    return tuple(result1 + result2)

def get_element_index(tup: tuple, index: int): #g
    if 0 <= index < len(tup):
        return tup[index]
    else:
        return None

def revers_tuple(tup) -> tuple: #h
    return tup[::-1]

def multiplier_tuple(tup: tuple, multiplier: int): #i
    new_tuple = tup * multiplier
    return tuple(new_tuple)

def remove_num_from_tuple(tup: tuple, num: int): #j
    new_tuple = list(tup)
    for i in new_tuple:
        if i == num:
            new_tuple.remove(i)
    return tuple(new_tuple)

def tuple_without_duplicates(tup: tuple): #k
    new_tup: list[int] = []
    for i in tup:
        if i not in new_tup:
            new_tup.append(i)
    return tuple(new_tup)

def index_tuple(tup: tuple, num: int):  #l
    tuple_index: list[int] = []
    for i in range(len(tup)):
        if tup[i] == num:
            tuple_index.append(i)
    return tuple(tuple_index)


names = []
while True:
    name = input("Enter a name : ")    #m
    if name == "done":
        break
    names.append(name)
scores = []
while True:
    try:
        score: int = int(input("Enter a score : "))
        if score == -999:
            break
        scores.append(score)
    except ValueError:
        print("Please enter a valid number ")

result = tuple(zip(names, scores))
print(result)
#END

#START Question 2
# ההבדל בין tulpe ל-list הןא ש-list ניתן לעשות בו שינויים ומשתמשים בו בעיקר למצבים בהם אנחנו זקוקים לנתונים דינמיים. ובנוסף ב-list אפשר גם להוסיף
# לעומת זאת ב-tuple לא ניתן לשינוית אין אפשרות להוסיף ערכים או לשנות ערכים אחרי יצירה שלו
#   ובגלל הוא בלתי משתנה, הוא מהיר יותר מבחינת ביצועים, כלומר משתמשים ב- tuple נטו כי הוא עובד מהר.
#END

#START Question 3
data_tuple = (
{"name": "Alice", "age": 30, "city": "New York"}, 1000, "secret-code"
)
data_tuple[0] ["age"] = 31
data_tuple[0] .clear()

#בקוד אין שגיאה כי אומנם יש פה tuple והוא לא ניתן לשינוי ועדין בתוך הקוד רוצים לשנות אובייקט אבל בתוך tuple יש dic שהוא כן ניתן לשינוי
# במילים אחרות בגלל שבתוך tuple יש dict אז תכנית הנתונים נמצאים בתוך dict ושם יש אפשרות לשינוי
#END









