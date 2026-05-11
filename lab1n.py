import random
import sys
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def get_input_mode():
    while True:
        print("\nспособ ввода списка:")
        print("1. Ввод с клавиатуры")
        print("2. Автоматическая генерация")
        choice = input("Ваш выбор: ")
        
        if choice == '1':
            return 1
        elif choice == '2':
            return 2
        else:
            print("Введите 1 или 2.")

def inputListManual():
    while True:
        try:
            raw_input = input("\nВведите элементы списка через пробел: ")
            if not raw_input.strip():
                print("Список не может быть пустым.")
                continue
            
            lst = list(map(int, raw_input.split()))
            
            if len(lst) == 0:
                print("Введено пустое значение.")
                continue
                
            return lst
        except ValueError:
            print("Ввод должен содержать только целые числа!")

def inputListAuto():
    while True:
        try:
            size = int(input("\nВведите размер списка: "))
            if size <= 0:
                print("Размер должен быть больше 0.")
                continue
            
            lst = [random.randint(1, 20) for _ in range(size)]
            return lst
        except ValueError:
            print("Введите корректное число для размера.")

def even(n):
    return n % 2 == 0

def processListNoStd(lst):
    if not lst:
        return []
    
    result = []
    i = 0
    n = len(lst)
    
    while i < n:
        if not even(lst[i]):
            result.append(lst[i])
            i += 1
        else:
            start_chain = i
            
            while i < n and even(lst[i]):
                i += 1
            end_chain = i
            
            min_val = lst[start_chain]
            min_index = start_chain
            
            for k in range(start_chain + 1, end_chain):
                if lst[k] < min_val:
                    min_val = lst[k]
                    min_index = k
            
            for k in range(start_chain, end_chain):
                if k != min_index:
                    result.append(lst[k])
            
    return result

def process_list_with_std(lst):
    if not lst:
        return []
    
    result = []
    i = 0
    n = len(lst)
    
    while i < n:
        if not even(lst[i]):
            result.append(lst[i])
            i += 1
        else:
            start_chain = i
            while i < n and even(lst[i]):
                i += 1
            end_chain = i
            
            chain = lst[start_chain:end_chain]
            min_val = min(chain)
            chain.remove(min_val)
            result.extend(chain)
            
    return result

def print_result(original, processed, method_name):
    print("\n" + "-" * 40)
    print(f"Метод обработки: {method_name}")
    print(f"Исходный список: {original}")
    print(f"Результат:       {processed}")
    print("-" * 40)

def main():
    while True:
        mode = get_input_mode()
        original_list = []
        
        if mode == 1:
            original_list = inputListManual()
        else:
            original_list = inputListAuto()
        
        print(f"\nСформирован список: {original_list}")
        
        print("\nВыберите вариант реализации алгоритма:")
        print("1. Без стандартных функций (min, remove)")
        print("2. Со стандартными функциями")
        print("3. Выход из программы")
        
        algo_choice = input("Ваш выбор (1-3): ")
        
        if algo_choice == '3':
            print("Завершение работы программы.")
            break
        
        if algo_choice == '1':
            lst_copy = original_list[:] 
            res = processListNoStd(lst_copy)
            print_result(original_list, res, "Ручная реализация (без std функций)")
        elif algo_choice == '2':
            lst_copy = original_list[:]
            res = process_list_with_std(lst_copy)
            print_result(original_list, res, "Стандартная реализация (с std функциями)")
        else:
            print("Некорректный выбор алгоритма.")
            continue
            
        repeat = input("\nПродолжить работу? (0/1): ").lower()
        if repeat != '0':
            print("Завершение работы программы.")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
        sys.exit(0)
    except Exception as e:
        print(f"\nПроизошла непредвиденная ошибка: {e}")
        sys.exit(1)