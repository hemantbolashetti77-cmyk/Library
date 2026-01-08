
def library_details(id, title, name, year):
    result = (
        f"Book Id:{id}\n"
        f"Book title:{title}\n"
        f"Author name:{name}\n"
        f"Published year:{year}\n"
    )
    return result

if __name__ == "__main__":
    id =101
    title ="The Great Gatsby"
    name ="F. Scott Fitzgerald"
    year =1925
    print(library_details(101,"The Great Gatsby","F. Scott Fitzgerald",1925))
