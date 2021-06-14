use rand::prelude::*;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn mc_pi(acc: i32) -> PyResult<f64> {
    let mut rng = rand::thread_rng();
    let mut hit_count = 0;
    let mut count = 0;
    for _i in 0..acc {
        let x: f64 = rng.gen();
        let y: f64 = rng.gen();
        if x * x + y * y <= 1. {
            hit_count += 1;
        }
        count += 1;
    }
    Ok(hit_count as f64 / count as f64 * 4.)
}

#[pymodule]
fn mc_pi_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(mc_pi, m)?)?;
    Ok(())
}
