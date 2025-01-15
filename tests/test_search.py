import pytest 

# @pytest.mark.only_browser("chromium")
# def test_h1_title(page):
#     page.goto('/')
#     assert page.inner_text('h1') == 'Όλες οι Ειδήσεις'
    
@pytest.mark.only_browser("chromium")
def test_Start_Confirm(page):
     page.goto('/')
     page.click('[aria-label="Συναίνεση"]')
     
