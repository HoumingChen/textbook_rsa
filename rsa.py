import random
from typing import Tuple


def quick_pow(n: int, k: int, p: int) -> int:
    """Find n^k % p quickly"""
    if k == 0:
        return 1
    tmp = quick_pow(n, k // 2, p) ** 2
    return tmp % p if k % 2 == 0 else tmp * n % p


def is_prime(num, bases=None) -> bool:
    """Check if a given number is prime with Millar-Rabin"""
    if bases is None:
        bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 31]
    for base in bases:
        if quick_pow(base, num, num) != base:
            return False
    return True


def generate_prime(length: int) -> int:
    """Generate a prime number with a given length in base 2"""
    assert length >= 5
    start = 1 << length
    end = 1 << (length + 1)
    while True:
        num = random.randint(start, end - 1)
        if is_prime(num):
            return num


def generate_n_and_phi_n(size: int) -> Tuple[int, int]:
    """Generate n = p * q, returns (n, phi(n))"""
    p, q = generate_prime(size // 2), generate_prime(size // 2 - 2)
    return p * q, (p - 1) * (q - 1)


def extended_gcd(a, b):
    """Find the solution of ax + by = gcd(x, y), returns (x, y, gcd(x, y))"""
    if b == 0:
        return 1, 0, a
    x, y, gcd = extended_gcd(b, a % b)
    return y, x - (a // b) * y, gcd


def generate_keys(size: int = 512) -> Tuple[int, int, int]:
    """Generate keys, returns (e, d, n), where e is the public key and d is the private key."""
    n, phi_n = generate_n_and_phi_n(size)
    e = generate_prime(size // 2)
    d, _, _ = extended_gcd(e, phi_n)
    if d < 0:
        d += phi_n
    return e, d, n


def encrypt(text: int, public_key: int, n: int) -> int:
    """Encrypt a text with a public key and n"""
    return quick_pow(text, public_key, n)


def decrypt(ciphertext: int, private_key: int, n: int) -> int:
    """Decrypt a text with a private key and n"""
    return quick_pow(ciphertext, private_key, n)
