from ardesi_prime import main as _main

def test_cli_importable():
    assert callable(_main)
