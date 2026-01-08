
from library import library_details 

def test_library_details():
    id =101
    title ="devops"
    aname ="hary"
    pyear =1925
    
    expected_output = (
        "Book Id:{id}\n"
        "Book title:{title}\n"
        "Authorname:{aname}\n"
        "Publishedyear:{pyear}" 
    )
    assert (library_details(101,"devops","hary",1925)) == expected_output
