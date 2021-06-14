use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

struct Fastrand {
    rctr: u64
}

impl Fastrand {
    fn new() -> Fastrand {
        Fastrand { rctr: 0x956126898 }
    }

    fn splitmix64(&mut self, seed: u64) {
        self.rctr = seed;
    }

    fn rand(&mut self) -> f64 {
        self.rctr = self.rctr % 0xFFFFFFFF;
        self.rctr ^= self.rctr.wrapping_shl(13);
        self.rctr = self.rctr % 0xFFFFFFFF;
        self.rctr ^= self.rctr.wrapping_shr(7);
        self.rctr = self.rctr % 0xFFFFFFFF;
        self.rctr ^= self.rctr.wrapping_shl(17);
        self.rctr = self.rctr % 0xFFFFFFFF;
        ((self.rctr % 0xFFFFFFFF) as f64) / (0xFFFFFFFFu32 as f64)
        //self.rctr as f64 / 0xFFFFFFFFFFFFFFFFu64 as f64
    }
}

#[pyfunction]
fn mc_pi(acc: i32) -> PyResult<f64> {
    let mut rng = Fastrand::new();
    let mut hit_count = 0;
    let mut count = 0;
    for _i in 0..acc {
        let x: f64 = rng.rand();
        let y: f64 = rng.rand();
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
