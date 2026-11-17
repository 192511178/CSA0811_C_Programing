"""Q5: Functions, mutable defaults, parameters and scope."""

def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order

def parameter_demo(item, quantity=1, *, category="Food"):
    return item, quantity, category

def return_multiple_values():
    return "Tea", 10, True

def scope_demo():
    global global_counter
    global_counter += 1
    message = "outer"
    def inner():
        nonlocal message
        message = "modified by inner function"
    inner()
    return message, global_counter

global_counter = 0

def main():
    print("Buggy shared default:")
    print(add_item_buggy("Tea"))
    print(add_item_buggy("Vada"))
    print("Default object:", add_item_buggy.__defaults__)

    print("\nCorrected independent lists:")
    print(add_item("Tea"))
    print(add_item("Vada"))

    print("\nPositional/default/keyword parameters:")
    print(parameter_demo("Idli", 2, category="Breakfast"))
    print("Multiple return values:", return_multiple_values())
    print("Local/nonlocal/global demonstration:", scope_demo())

if __name__ == "__main__":
    main()
