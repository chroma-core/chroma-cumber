import pickle
import zlib

class Chroma:
    @staticmethod
    def dumps(obj, protocol=None, fix_imports=True):
        data = pickle.dumps(obj, protocol=protocol, fix_imports=fix_imports)
        compressed_data = zlib.compress(data, level=9)
        return compressed_data

    @staticmethod
    def dump(obj, file, protocol=None, fix_imports=True):
        compressed_data = Chroma.dumps(obj, protocol=protocol, fix_imports=fix_imports)
        file.write(compressed_data)

    @staticmethod
    def loads(data, fix_imports=True, encoding="ASCII", errors="strict"):
        uncompressed_data = zlib.decompress(data)
        return pickle.loads(uncompressed_data, fix_imports=fix_imports, encoding=encoding, errors=errors)

    @staticmethod
    def load(file, fix_imports=True, encoding="ASCII", errors="strict"):
        compressed_data = file.read()
        uncompressed_data = zlib.decompress(compressed_data)
        return pickle.load(uncompressed_data, fix_imports=fix_imports, encoding=encoding, errors=errors)

    # The remaining methods are added in Python 3.8
    @staticmethod
    def protocol_version(n):
        return pickle.protocol_version(n)

    @staticmethod
    def whichmodule(obj, name):
        return pickle.whichmodule(obj, name)

    @staticmethod
    def compatible_formats():
        return pickle.compatible_formats()
