Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from hashlib import blake2b
h = blake2b(digest_size=60)
h.update(b'Replacing SHA1 with the more secure function')
h.hexdigest()
'393eac11681523721d01c91fd570419b32f1f33b177d9f673306f685e3ebe31aaffd3b7ecb3d101b1ce7f4f15cb23b66b5d775ae9d36fe6c857d892e'
h.digest_size
60
len(h.digest())
60
