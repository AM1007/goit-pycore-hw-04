from typing import TypedDict

Cat = TypedDict("Cat", {"id": str, "name": str, "age": int})

def get_cats_info(path: str) -> list[Cat] | None:
    try:
        cats = []
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_info = line.strip().split(",")
                cats.append({"id": cat_info[0], "name": cat_info[1], "age": int(cat_info[2])})
            return cats
    except FileNotFoundError:
        print("file does not exist")
        return None
    
cats_info = get_cats_info("task_02\cats_info.txt")
print(cats_info)