
from library import library_details 

def test_library_details():
    id =101
    title ="The Great Gatsby"
    name ="F. Scott Fitzgerald"
    year =1925
    
    expected_output = (
        "Book Id:{id}\n"
        "Book title:{title}\n"
        "Author name:{name}\n"
        "Published year:{year}" 
    )
    assert library_details(id, title, name, year) == expected_output
