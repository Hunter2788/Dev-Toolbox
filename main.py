from tools import file_organizer, password_generator, system_info, folder_backup

def menu():
    while True:
        print("\n=== DEV TOOLBOX ===")
        print("1. File Organizer")
        print("2. Password Generator")
        print("3. System Info")
        print("4. Folder Backup")
        print("0. Exit")

        choice = input("Select option: ")

        if choice == "1":
            file_organizer.run()
        elif choice == "2":
            password_generator.run()
        elif choice == "3":
            system_info.run()
        elif choice == "4":
            folder_backup.run()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
