import pygsheets

from app.schemas import Item

client = pygsheets.authorize()

sh = client.open('groceries-db')
wks = sh.sheet1
print(wks.get_all_values())

def convert_row_to_item(row: list) -> Item:
    return Item(prod_name=row[0], category=row[1], current_amount=float(row[2]), target_amount=float(row[3]), threshold_amount=float(row[4]), tags=row[5], notes=row[6])

def convert_item_to_row(item: Item) -> list:
    return [item.prod_name, item.category, item.current_amount, item.target_amount, item.threshold_amount, item.tags, item.notes]

def get_values() -> list[Item]:
    vls = wks.get_all_values()
    res = []
    for row in vls[1:]:
        if row[0] != '':
            item = convert_row_to_item(row)
            res.append(item)
        else:
            break
    return res

def get_items() -> list[Item]:
    return get_values()

def get_item(idx: int) -> Item | None:
    values = get_values()
    idx -= 2
    if len(values) <= idx or idx < 0:
        return None
    return values[idx]

def get_last_row_id() -> int:
    """
    Returns last used row id
    """
    return len(get_values()) + 1 # cause we don't count the first row that is the header

def get_new_id() -> int:
    """
    Returns an id for a new row
    """
    
    new_id = get_last_row_id() + 1
    if new_id >= wks.rows:
        wks.add_rows(100)
    return new_id

def get_id_by_prod_name(prod_name: str) -> int | None:
    for id, val in enumerate(get_values()):
        if val.prod_name == prod_name:
            return id+2  # cause we don't count the first row that is the header
    return None

def add_row(values: list) -> None:
    wks.update_row(get_new_id(), values)

def add_item(item: Item) -> None:
    add_row(convert_item_to_row(item))

def update_row(idx: int, values: list) -> None:
    wks.update_row(idx, values)

def update_item(item: Item) -> None:
    idx = get_id_by_prod_name(item.prod_name)
    if idx is None:
        add_item(item) # TODO: error
    else:
        update_row(idx, convert_item_to_row(item))


def update_row_by_name(prod_name: str, values: list) -> None:
    idx = get_id_by_prod_name(prod_name)
    if idx is None:
        add_row(values)
    else:
        update_row(idx, values)

def delete_row(idx: int) -> None:
    wks.update_row(idx, ['', '', '', '', '', '', ''])

def delete_row_by_prod_name(prod_name: str) -> None:
    idx = get_id_by_prod_name(prod_name)
    if idx is None:
        return
    else:
        delete_row(idx)

def delete_item(item: Item) -> None:
    delete_row_by_prod_name(item.prod_name)

