# README 

To run `flux` on `std` do 

```
$ ./test_flux
```

## To enable flux on the library add 

[package.metadata.flux]
enabled = true

[dependencies]
flux-attrs = { git = "https://github.com/flux-rs/flux.git" }

## To use flux_assume
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (b:bool) ensures b)]
fn flux_assume(_:bool) {}
