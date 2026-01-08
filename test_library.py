
from library import library_details 

def test_library_details():
    id =101
    title ="devops"
    name ="alice"
    year =1925
    
    expected_output = (
        "Book Id:{id}\n"
        "Book title:{title}\n"
        "Author name:{name}\n"
        "Published year:{year}" 
    )
    assert (library_details(101,"devops","alice",1925)) == expected_output
