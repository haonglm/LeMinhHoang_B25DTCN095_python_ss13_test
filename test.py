staff_list = []

while True:
    print("""
    =======================================
        QUẢN LÝ NHÂN SỰ - STAFF MANAGER
    =======================================
        1. thêm nhân viên mới
        2. danh sách nhân viên
        3. tìm kiếm nhân viên
        4. xóa nhân viên khỏi hệ thống
        5. thoát chương trình
""")
    
    choice = int(input("nhập lựa chọn từ 1 đến 5: "))

    match choice:
        case 5:
            print("thoát chương trình !!!")
            break
        case 1:
            while True:
                staff_name = input("nhập tên nhân viên: ").strip()
                
                if staff_name == '':
                    print("tên không được để trống")
                    continue
                else:
                    break
            
            while True:
                staff_salary = input("nhập lương nhân viên: ").strip()

                if not staff_salary or float(staff_salary) < 0:
                    print("mức lương không hợp lệ")
                    continue
                if staff_salary:
                    break
            
            new_staff = {
                'id' : 101 if len(staff_list) == 0 else staff_list[len(staff_list) - 1]['id'] + 1,
                'name' : staff_name,
                'salary' : float(staff_salary)
            }

            staff_list.append(new_staff)
            print(f"Thêm nhân viên thành công! ID: {new_staff['id']}")
        case 2:
            if staff_list == []:
                print("Chưa có dữ liệu nhân sự!")
            else:
                print("ID       | TÊN NHÂN VIÊN         | MỨC LƯƠNG")
                for staff in staff_list:
                    print(f"{staff["id"]}       | {staff['name']}       | {staff['salary']}")
        case 3:
            search_id = input("nhập id nhân viên muốn tìm: ").strip()
            if search_id == '':
                print("id không được để trống")
                continue

            found = False
            for staff in staff_list:
                if staff['id'] == int(search_id):
                    found = True
                    print(f"thông tin nhân viên: {staff}")
            
            if not found :
                print("không tìm thấy thông tin nhân viên")
        case 4:
            delete_id = input("nhập id muốn xóa: ").strip()
            found = False

            for staff in staff_list:
                if staff['id'] == int(delete_id):
                    found = True
                    staff_list.remove(staff)
                    print("đã xóa thành công")

            if not found:
                print("không tìm thấy nhân viên")

        case _:
            print("lựa chọn không hợp lệ !!!")
