
from library import library_details 

def test_library_details():
    id =101
    title ="devops"
    name ="hary"
    year =1925
    
    expected_output = (
        "Book Id:{id}\n"
        "Book title:{title}\n"
        "Authorname:{name}\n"
        "Publishedyear:{year}" 
    )
    assert (library_details(101,"devops","hary",1925)) == expected_output
