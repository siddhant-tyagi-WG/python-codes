# test_print.py

def my_function():
    print("Hello, world!")

def test_my_function(capsys):
    my_function()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, world!"
