from notes_manager import NotesManager

def print_notes(notes):
    for n in notes:
        print(f"[{n[0]}] {n[1]} ({n[3]}) - {n[2]}")

def main():
    manager = NotesManager()
    
    while True:
        print("\n1. Добавить 2. Все заметки 3. Удалить 4. Редактировать 5. Поиск 6. По категории 7. Категории 0. Выход")
        choice = input("Выбор: ")
        
        if choice == '1':
            title = input("Название: ")
            content = input("Текст: ")
            category = input("Категория: ")
            try:
                manager.add_note(title, content, category)
                print("Добавлено.")
            except ValueError as e:
                print(e)
        elif choice == '2':
            print_notes(manager.get_all())
        elif choice == '3':
            nid = input("ID для удаления: ")
            if manager.delete_note(nid):
                print("Удалено.")
            else:
                print("Не найдено.")
        elif choice == '4':
            nid = input("ID для редактирования: ")
            title = input("Новое название: ")
            content = input("Новый текст: ")
            category = input("Новая категория: ")
            if manager.update_note(nid, title, content, category):
                print("Обновлено.")
            else:
                print("Не найдено.")
        elif choice == '5':
            kw = input("Поиск: ")
            print_notes(manager.search(kw))
        elif choice == '6':
            cat = input("Категория: ")
            print_notes(manager.get_by_category(cat))
        elif choice == '7':
            cats = manager.get_categories()
            print("Категории:", ", ".join(cats))
        elif choice == '0':
            break

if __name__ == "__main__":
    main()
