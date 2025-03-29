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
// flux_verify_assume: assume
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (b:bool) ensures b)]
fn flux_assume(_:bool) {}

## Static vector len
#[flux_attrs::sig(fn (_) -> usize[N])]
fn flux_len<T, const N: usize>(_: [T; N]) -> usize {
    N
}

#[flux_attrs::sig(fn (_) -> usize[N])]
const fn flux_const_len_copy<T: Copy, const N: usize>(_: [T; N]) -> usize {
    N
}

#[flux_attrs::sig(fn (_) -> usize[N])]
const fn flux_const_len<T, const N: usize>(_: &[T; N]) -> usize {
    N
}

## Dynamic vector len
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (&[T][@n]) -> usize[n])]
fn flux_arr_len<T> (arr:&[T]) -> usize {arr.len()}

## Eror types
// flux_verify: [type]
#[flux_attrs::trusted]
error: errors that can be fixed
ice: catched errors
panic: uncached errors
unknown: need more information
assume/impl: functional


type constrain : show have refinement on the type defn

// flux_verify_impl: impl
#[flux_attrs::trusted]

    // flux_verify_error: type constrain
    #[flux_attrs::trusted_impl]