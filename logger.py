import logging
import time

# Налаштовуємо логування
logging.basicConfig(
    filename='logs/task.log',  # Лог буде записуватись в файл task.log у папці logs
    filemode='w',  # Перезаписуємо файл при кожному запуску
    level=logging.INFO,  # Мінімальний рівень логування - INFO
)

def run_task():
    start_time = time.time()  # Час початку роботи програми
    while time.time() - start_time < 60:  # Завдання має працювати одну хвилину
        elapsed_time = time.time() - start_time
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        logging.info(f"Program has been running for {elapsed_time:.2f} seconds. Current time: {current_time}")
        time.sleep(5)  # Засипаємо на 5 секунд
    logging.error("Task completed")  # Записуємо повідомлення про завершення з рівнем ERROR

if __name__ == "__main__":
    run_task()
