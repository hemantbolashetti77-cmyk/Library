
def library_details(id, title, name, year):
    result = (
        f"Book Id:{id}\n"
        f"Book title:{title}\n"
        f"Author name:{name}\n"
        f"Published year:{year}\n"
    )
    return result

if __name__ == "__main__":
    
    print(library_details(id,title,name,year))
