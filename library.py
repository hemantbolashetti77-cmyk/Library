
def library_details(id, title, name, year):
    result = (
        f"Book Id:{id}\n"
        f"Book title:{title}\n"
        f"Authorname:{aname}\n"
        f"Published year:{pyear}\n"
    )
    return result

if __name__ == "__main__":
    id =101
    title ="devops"
    aname ="hary"
    pyear =1925
    print(library_details(id,title,aname,pyear))
