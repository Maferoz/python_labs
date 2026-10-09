
---

## Задание 1

---
## min_max
> **Описание решения:** Если x пустой, функция возвращает ValueError. min и max изначально приравнены первому числу для удобства. Простенький цикл for для перебора наибольшего и наименьшего.

**Код программы:**  
![alt text](https://github.com/Maferoz/python_labs/blob/main/images/lab02/ex01-1code.png)



**Результат выполнения:**  
<img width="542" height="374" alt="image" src="https://github.com/user-attachments/assets/1253b812-bba4-4d32-8b1f-4148c9cd3c6e" />


---

## unique_sorted

> **Описание решения:** В начале функции создал новый список, куда добавляются только оригинальные числа. Дальше сортировка пузырьком, самые большие числа идут вправо с каждом цикле, при этом не учитываются прошлые максимальные числа.


**Код программы:**  
<img width="1976" height="392" alt="image" src="https://github.com/user-attachments/assets/3da0dc92-8784-4189-8187-be0e99d1d449" />



**Результат выполнения:**  
<img width="212" height="114" alt="image" src="https://github.com/user-attachments/assets/c56b6302-f41f-4ce4-88cb-6f3065552d55" />



---

##  flatten

> **Описание решения:** ValueError, если дан не список или кортеж. Функция extend добавляет все элементы матрицы в список res.

**Код программы:**  
<img width="1966" height="292" alt="image" src="https://github.com/user-attachments/assets/8677c366-bcbb-416e-90db-7c520bfd21b4" />



**Результат выполнения:**  
<img width="1202" height="334" alt="image" src="https://github.com/user-attachments/assets/2af154fd-4da4-4af1-8c4e-76f7db54b163" />



---

##  Задание 2

---
## функция matrix_check для проверки матриц на рваность:
![alt text](https://github.com/Maferoz/python_labs/blob/main/images/lab02/image.png)
---
## transpose
> **Описание решения:** Меняем местами m и n для транспонирования, добавляем в новый список этот срез.

**Код программы:**  
![alt text](https://github.com/Maferoz/python_labs/blob/main/images/lab02/ex02-1code.png)


**Результат выполнения:**  
<img width="1216" height="368" alt="image" src="https://github.com/user-attachments/assets/844eaf01-28f4-4264-9a0e-0a65a17e9bf5" />



---

## row_sums

> **Описание решения:** Проходим по каждой строке через цикл for, складываем все элементы каждого столбца, сумму элементов добавляем в новый список как строку.

**Код программы:**  
![alt text](https://github.com/Maferoz/python_labs/blob/main/images/lab02/ex02-2code.png)



**Результат выполнения:**  
<img width="1200" height="342" alt="image" src="https://github.com/user-attachments/assets/159083d6-96d1-4e5c-8f8b-90c5470725ac" />



---

## col_sums

> **Описание решения:** В цикле for складываются элемент столбца матрицы с другим на следующей строке. 

**Код программы:**  
![alt text](https://github.com/Maferoz/python_labs/blob/main/images/lab02/ex02-3code.png)




**Результат выполнения:**  
<img width="1208" height="338" alt="image" src="https://github.com/user-attachments/assets/bb824856-8f1c-4159-b725-3844706cfb0f" />



---

##  Задание 3

> **Описание решения:** Создаем список, содержащий фамилию, имя, отчество. capitalize делает первую букву заглавной, остальные переводит в нижний регистр. Ищем первые буквы ФО по заглавности, добавляем в пустую строку для инициалов вместе с точкой.

**Код программы:**  
<img width="2004" height="1254" alt="image" src="https://github.com/user-attachments/assets/962467ef-ff86-43df-97b0-e3e1dddfd8c7" />




**Результат выполнения:**  
<img width="1196" height="114" alt="image" src="https://github.com/user-attachments/assets/aecd8796-b543-4120-9be7-3b1ade960e0c" />







