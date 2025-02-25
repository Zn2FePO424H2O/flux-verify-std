# README 

To run `flux` on `std` do 

```
$ ./test_flux
```

To enable flux on the library add 

[lints.rust.unexpected_cfgs]
level = "warn"
check-cfg = [
    'cfg(flux)'
]

[profile.dev]
incremental = true

[package.metadata.flux]
enabled = true

[dependencies]
flux-rs = { git = "https://github.com/flux-rs/flux" }