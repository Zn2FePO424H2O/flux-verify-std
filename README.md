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

## Scripts

  - counter.py: count the errors in log.txt and generate log\[E0999\].txt
  - show.py: show the location of sepecific type of error
  - qa.py: check if all flux_assume and trusted have comments.
  - statistic.py: count the comments in library.

## Comments

Each flux_assume and trusted have a comment to show their purpose. The format is flux_verify_\[class\]: \[type\]
  - mark: functional trusted.
  - complex: refinement errors solved by trusted
  - error: refinement errors solved by assume
  - ice: catched panics and internel flux errors
  - panic: uncatched panics

## Eror types

  - 3 ZST: none ZST type have non zero size
  - 6 bit mask: 
  - 13 bit shift: 
  - 2 char cast magic: s.read_u64() must between 0x3030_3030_3030_3030 and 0x3939_3939_3939_3939
  - 10 condition matching: Flux worry about condition that not in this brunch
  - 12 logic constrain: error impossibile because the logic of the program
  - 7 loop: for i in a..b a <= i < b
  - 6 sub vector length: 
  - 4 type cast: lost information on the variable during type cast
  - 17 vector length: 

  - refinement type error: not showing what the refinement is
  - member and -=: self.var -= 1 should be same as self.var = self.var - 1

## Document for the errors
  https://hackmd.io/@47Z2wNHXRvOTVNfT7WF7OQ/B1N9EFEaye

## To use flux_assume
// flux_verify_mark: assume
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (b:bool) ensures b)]
const fn flux_assume(_:bool) {}

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

