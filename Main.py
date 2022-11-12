from customer import Customer
from manager import BaseManager


def main():
    BaseManager.set_connection()
    print("Connection set")
    customers = Customer.objects.select('first_name')
    print(customers)


if __name__ == "__main__":
    main()
