def library_details(id, title, name, year):
    result = (
        f"Book Id:{id}\n"
        f"Book title:{title}\n"
        f"Author name:{name}\n"
        f"Published year:{year}\n"
    )
    return result

if __name__ == "__main__":
    
    id = input("Enter the Book ID: ")
    title = input("Enter the Book Title: ")
    name = input("Enter the Author Name: ")
    year = input("Enter the Published Year: ")
    
    print(library_details(id,title,name,year))
