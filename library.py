
def library_details(id, title, name, year):
    result = (
        f"Book Id:{id}\n"
        f"Book title:{title}\n"
        f"Authorname:{name}\n"
        f"Published year:{year}\n"
    )
    return result

if __name__ == "__main__":
    id =101
    title ="devops"
    name ="hary"
    year =1925
    print(library_details(id,title,name,year))
