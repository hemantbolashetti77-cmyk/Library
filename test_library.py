from library import library_details
def test_library_details():
    expected_output=(
    "Book Id:{id}\n",
    "Book title:{title}\n",
    "Author name:{name}\n",
    "Book Id:{year}"
    )
    assert library_details(id,title,name,year) == expected_output