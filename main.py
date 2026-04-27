import requests
from bs4 import BeautifulSoup


def fetch_laptops():
    base = "https://discountelectronics.com/refurbished-laptops/"
    for i in range(1, 14):
        url = base + f"?page={i}"
        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
            },
        )
        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.find_all("article", class_="card")
        for card in cards:
            title = card.find("h3", class_="card-title").find("a")["aria-label"]
            name, price = title.split(", $")
            yield name, "$" + price.strip()


def search(query):
    for name, price in fetch_laptops():
        if query.lower() in name.lower():
            print(f"Name: {name}\nPrice: {price}\n\n")


def view_all():
    for name, price in fetch_laptops():
        print(f"Name: {name}\nPrice: {price}\n\n")


if __name__ == "__main__":
    while True:
        choice = (
            input(
                "Enter 'search' to search for a laptop, 'view' to view all laptops, or 'exit' to quit: "
            )
            .strip()
            .lower()
        )
        if choice == "search":
            query = input("Enter the laptop name to search for: ")
            print(f"Searching for laptops matching '{query}'...\n")
            search(query)
        elif choice == "view":
            view_all()
        elif choice == "exit":
            break
        else:
            print("Invalid choice. Please try again.")
