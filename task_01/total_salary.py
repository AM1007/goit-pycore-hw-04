def total_salary(path: str) -> tuple[int, int]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []  
            for line in file:
                stripped_line = line.strip()
                data = stripped_line.split(",")
                salary = int(data[1])
                salaries.append(salary)
            total_sum = sum(salaries)
            average_salary = total_sum // len(salaries)
            return total_sum, average_salary
    except FileNotFoundError:
        print("file does not exist") 
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0


total, average = total_salary('task_01\salaries.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

