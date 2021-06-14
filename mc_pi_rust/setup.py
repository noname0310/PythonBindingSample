from setuptools import setup
from setuptools_rust import RustExtension, Binding

def call_setup():
    setup(
        name="mc_pi_rust",
        version="0.0.1",
        rust_extensions=[RustExtension("mc_pi_rust", binding=Binding.PyO3)],
        zip_safe=False,
    )

if __name__ == "__main__":
    call_setup()
