use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn mc_pi(acc: i32) -> PyResult<f64> {
    unsafe {
        let lib = libloading::Library::new("D:/noname/Projects/GitHub/PythonBindingSample/mc_pi_csharp/bin/x64/Release/net5.0/mc_pi_csharp.dll").unwrap();
        let func: libloading::Symbol<unsafe extern fn(i32) -> f64> = lib.get(b"mc_pi").unwrap();
        Ok(func(acc))
    }
}

#[pymodule]
fn mc_pi_csharp(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(mc_pi, m)?)?;
    Ok(())
}
