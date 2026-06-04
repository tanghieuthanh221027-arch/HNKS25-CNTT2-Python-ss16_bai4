from datetime import datetime

patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]

def find_patient_index(records, patient_id):
    patient_id = patient_id.strip().upper()

    for index, record in enumerate(records):
        if record.startswith(patient_id + "-"):
            return index

    return -1

def display_records(records):
    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("--- DANH SÁCH BỆNH NHÂN ---")

    for index, record in enumerate(records, start=1):
        patient_id, name, birth_year, diagnosis = record.split("-")

        print(
            f"{index}. [{patient_id}] {name:<20} | "
            f"Năm sinh: {birth_year} | "
            f"Chẩn đoán: {diagnosis}"
        )

def add_patient(records):
    print("--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    valid_id = False

    while not valid_id:
        patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

        if patient_id == "":
            print("Mã bệnh nhân không được để trống!")
        elif find_patient_index(records, patient_id) != -1:
            print("Mã bệnh nhân đã tồn tại!")
            return
        else:
            valid_id = True

    valid_name = False

    while not valid_name:
        name = input("Nhập tên bệnh nhân: ").strip()

        if name == "":
            print("Tên bệnh nhân không được để trống!")
        else:
            name = name.replace("-", " ").title()
            valid_name = True

    current_year = datetime.now().year
    valid_year = False

    while not valid_year:
        birth_year = input("Nhập năm sinh: ").strip()

        if not birth_year.isdigit():
            print("Năm sinh không hợp lệ, vui lòng nhập lại!")
        elif int(birth_year) < 1900 or int(birth_year) > current_year:
            print("Năm sinh không hợp lệ, vui lòng nhập lại!")
        else:
            valid_year = True

    valid_diagnosis = False

    while not valid_diagnosis:
        diagnosis = input("Nhập chẩn đoán: ").strip()

        if diagnosis == "":
            print("Chẩn đoán không được để trống!")
        else:
            diagnosis = diagnosis.replace("-", " ").capitalize()
            valid_diagnosis = True

    new_record = "-".join([
        patient_id,
        name,
        birth_year,
        diagnosis
    ])

    records.append(new_record)

    print("Thêm hồ sơ bệnh nhân thành công!")
    print("Sau khi chuẩn hóa, dữ liệu được lưu là:")
    print(new_record)


def update_diagnosis(records):
    print("--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()

    index = find_patient_index(records, patient_id)

    if index == -1:
        print(f"Không tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    patient_info = records[index].split("-")

    print(f"Tìm thấy bệnh nhân: {patient_info[1]}")
    print(f"Chẩn đoán hiện tại: {patient_info[3]}")

    valid_diagnosis = False

    while not valid_diagnosis:
        new_diagnosis = input("Nhập chẩn đoán mới: ").strip()

        if new_diagnosis == "":
            print("Chẩn đoán không được để trống!")
        else:
            new_diagnosis = new_diagnosis.replace("-", " ").capitalize()
            valid_diagnosis = True

    patient_info[3] = new_diagnosis

    records[index] = "-".join(patient_info)

    print("Cập nhật chẩn đoán thành công!")


def generate_age_report(records):
    print("--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")

    current_year = datetime.now().year

    children = 0
    adult = 0
    elderly = 0

    for record in records:
        data = record.split("-")

        birth_year = int(data[2])

        age = current_year - birth_year

        if age < 16:
            children += 1
        elif age <= 60:
            adult += 1
        else:
            elderly += 1

    print(f"Trẻ em: {children} bệnh nhân")
    print(f"Trưởng thành: {adult} bệnh nhân")
    print(f"Người cao tuổi: {elderly} bệnh nhân")
    print("--------------------------------------")


while True:
    print("===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
    print("1. Xem danh sách hồ sơ bệnh án")
    print("2. Thêm hồ sơ bệnh nhân mới")
    print("3. Cập nhật chẩn đoán theo Mã BN")
    print("4. Báo cáo phân loại theo độ tuổi")
    print("5. Thoát chương trình")
    print("==================================================")

    choice = input("Chọn chức năng (1-5): ").strip()

    if choice == "1":
        display_records(patient_records)

    elif choice == "2":
        add_patient(patient_records)

    elif choice == "3":
        update_diagnosis(patient_records)

    elif choice == "4":
        generate_age_report(patient_records)

    elif choice == "5":
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ!")
