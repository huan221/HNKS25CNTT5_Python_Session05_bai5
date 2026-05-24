def input_positive_int(prompt):
    """Hàm nhập số nguyên >= 0"""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Giá trị không hợp lệ. Vui lòng nhập lại.")
            else:
                return value
        except:
            print("Vui lòng nhập số hợp lệ.")


def show_guide():
    print("\n--- HƯỚNG DẪN ---")
    print("1. Nhập số chi nhánh")
    print("2. Nhập số lớp mỗi chi nhánh")
    print("3. Nhập số học viên từng lớp")
    print("4. Hệ thống sẽ tự động thống kê")
    print("-----------------\n")


def handle_statistics():
    branch_count = input_positive_int("Nhập số lượng chi nhánh: ")

    branch_totals = []

    for branch in range(1, branch_count + 1):
        print(f"\nChi nhánh {branch}")
        class_count = input_positive_int("Nhập số lớp: ")

        total_students = 0
        low_classes = []

        for classroom in range(1, class_count + 1):
            student_count = input_positive_int(
                f"Nhập số học viên lớp {classroom}: "
            )

            total_students += student_count

            if student_count < 10:
                low_classes.append(classroom)

        branch_totals.append(total_students)

        print(f"Tổng học viên chi nhánh {branch}: {total_students}")

        if low_classes:
            print("Lớp có sĩ số < 10:", low_classes)
        else:
            print("Không có lớp nào dưới 10 học viên")

    # Tìm chi nhánh đông nhất
    max_students = max(branch_totals)
    best_branch = branch_totals.index(max_students) + 1

    print("\n=== TỔNG KẾT ===")
    print(f"Chi nhánh đông nhất: Chi nhánh {best_branch} ({max_students} học viên)")


# ================= MAIN =================
while True:
    print("\n===== MENU =====")
    print("1. Nhập dữ liệu và xem báo cáo")
    print("2. Hướng dẫn sử dụng")
    print("3. Thoát")
    
    choice = input("Chọn chức năng: ")

    # Bẫy menu sai
    if choice not in ["1", "2", "3"]:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        continue

    if choice == "1":
        handle_statistics()

    elif choice == "2":
        show_guide()

    elif choice == "3":
        print("Thoát chương trình")
        break