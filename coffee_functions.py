from random import randint
from typing import Optional

order = []  # The in-progress order.
placed_order = []  # The confirmed, completed order.

def add_to_order(drink: str, modifiers: Optional[list[str]] = None) -> None:
    """Adds the specified drink to the customer's order, including any modifiers."""
    if modifiers is None:  # Ensures safe handling of None
        modifiers = []
    order.append((drink, modifiers))


def get_order() -> list[tuple[str, list[str]]]:
    """Returns the customer's order."""
    return order


def remove_item(n: int) -> str:
    """Removes the nth (one-based) item from the order.

    Returns:
        The item that was removed.
    """
    item, _ = order.pop(n - 1)
    return item


def clear_order() -> None:
    """Removes all items from the customer's order."""
    order.clear()


def confirm_order() -> str:
    """Asks the customer if the order is correct.

    Returns:
        The user's free-text response.
    """
    print("Your order:")
    if not order:
        print("  (no items)")

    for drink, modifiers in order:
        print(f"  {drink}")
        if modifiers:
            print(f'   - {", ".join(modifiers)}')

    return input("Is this correct? ")


def place_order() -> int:
    """Submit the order to the kitchen.

    Returns:
        The estimated number of minutes until the order is ready.
    """
    placed_order[:] = order.copy()
    clear_order()

    # TODO: Implement coffee fulfillment.
    return randint(1, 10)
