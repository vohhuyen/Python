def display_todos(todos):
    print("\nDanh sách việc cần làm:")
    if not todos:
        print("Không có việc nào!")
    else:
        for index, todo in enumerate(todos, start=1):
            print(f"{index}. {todo}")

def main():
    todos = []
    
    while True:
        print("\nChọn một tùy chọn:")
        print("1. Thêm việc")
        print("2. Xem việc")
        print("3. Xóa việc")
        print("4. Thoát")
        
        choice = input("Nhập tùy chọn của bạn (1/2/3/4): ")

        match choice:
            case '1':
                todo = input("Nhập việc cần thêm: ")
                todos.append(todo) 
                print(f"Đã thêm việc: {todo}")

            case '2':
                display_todos(todos) 

            case '3':
                display_todos(todos)
                index = int(input("Nhập số thứ tự việc cần xóa: ")) - 1
                if 0 <= index < len(todos):
                    removed = todos.pop(index) 
                    print(f"Đã xóa việc: {removed}")
                else:
                    print("Số thứ tự không hợp lệ!")

            case '4':
                print("Cảm ơn đã sử dụng ứng dụng Todo List!")
                break

            case _:
                print("Tùy chọn không hợp lệ! Vui lòng thử lại.")

if __name__ == "__main__":
    main()
