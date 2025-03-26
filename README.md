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
bit map
bit shift
type cast
vector length
complex
ZST
panic