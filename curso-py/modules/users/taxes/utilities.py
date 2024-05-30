if __name__ != "__main__":
    from ..management.crud import save  # Relative import
    from users.management.crud import save  # Absolute import

    print(__name__)

    def paying_taxes():
        print("Paying taxes")
        save()

if __name__ == "__main__":
    print("Maintenance task")
