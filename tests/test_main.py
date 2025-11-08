from app.main import greet

def test_greet(capsys):
    greet()
    captured = capsys.readouterr()
    assert "Wyzen Initiative" in captured.out
