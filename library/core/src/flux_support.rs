#[stable(feature = "downgraded_weak", since = "1.10.0")]
#[rustc_const_stable(feature = "const_weak_new", since = "1.73.0")]
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (a: u8, b: u8) -> u8{v: v <= a && v <= b})]
pub const fn my_and_u8(a: u8, b: u8) -> u8 { a & b }

#[stable(feature = "downgraded_weak", since = "1.10.0")]
#[rustc_const_stable(feature = "const_weak_new", since = "1.73.0")]
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (a: u16, b: u16) -> u16{v: v <= a && v <= b})]
pub const fn my_and_u16(a: u16, b: u16) -> u16 { a & b }

#[stable(feature = "downgraded_weak", since = "1.10.0")]
#[rustc_const_stable(feature = "const_weak_new", since = "1.73.0")]
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (a: u64, b: u64) -> u64{v: v <= a && v <= b})]
pub const fn my_and_u64(a: u64, b: u64) -> u64 { a & b }

#[stable(feature = "downgraded_weak", since = "1.10.0")]
#[rustc_const_stable(feature = "const_weak_new", since = "1.73.0")]
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (a: u128, b: u128) -> u128{v: v <= a && v <= b})]
pub const fn my_and_u128(a: u128, b: u128) -> u128 { a & b }

#[stable(feature = "downgraded_weak", since = "1.10.0")]
#[rustc_const_stable(feature = "const_weak_new", since = "1.73.0")]
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (a: usize, b: usize) -> usize{v: v <= a && v <= b})]
pub const fn my_and_usize(a: usize, b: usize) -> usize { a & b }

#[stable(feature = "downgraded_weak", since = "1.10.0")]
#[rustc_const_stable(feature = "const_weak_new", since = "1.73.0")]
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (a: u8, b: u8) -> u8{v: v >= a})]
pub const fn my_left_shift_u8(a: u8, b: u8) -> u8 { a << b }

#[stable(feature = "downgraded_weak", since = "1.10.0")]
#[rustc_const_stable(feature = "const_weak_new", since = "1.73.0")]
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (a: u32, b: u32) -> u32{v: v >= a})]
pub const fn my_left_shift_u32(a: u32, b: u32) -> u32 { a << b }

#[stable(feature = "downgraded_weak", since = "1.10.0")]
#[rustc_const_stable(feature = "const_weak_new", since = "1.73.0")]
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (a: u64, b: u64) -> u64{v: v >= a})]
pub const fn my_left_shift_u64(a: u64, b: u64) -> u64 { a << b }

#[stable(feature = "downgraded_weak", since = "1.10.0")]
#[rustc_const_stable(feature = "const_weak_new", since = "1.73.0")]
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (a: u64, b: usize) -> u64{v: v >= a})]
pub const fn my_left_shift_u64_usize(a: u64, b: usize) -> u64 { a << b }

#[stable(feature = "downgraded_weak", since = "1.10.0")]
#[rustc_const_stable(feature = "const_weak_new", since = "1.73.0")]
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (a: u128, b: u128) -> u128{v: v >= a})]
pub const fn my_left_shift_u128(a: u128, b: u128) -> u128 { a << b }

#[stable(feature = "downgraded_weak", since = "1.10.0")]
#[rustc_const_stable(feature = "const_weak_new", since = "1.73.0")]
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (a: u8, u8 {b: b == 4}) -> u8{v: v < 16})]
pub const fn my_right_shift_u8_by4(a: u8, b: u8) -> u8 {
    a >> b
}

#[stable(feature = "downgraded_weak", since = "1.10.0")]
#[rustc_const_stable(feature = "const_weak_new", since = "1.73.0")]
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (usize {a: a<16}, usize {b: b == 1}) -> usize{v: v < 7})]
pub const fn my_right_shift_usize_by1(a: usize, b: usize) -> usize {
    a >> b
}

#[stable(feature = "downgraded_weak", since = "1.10.0")]
#[rustc_const_stable(feature = "const_weak_new", since = "1.73.0")]
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (u64 {a: a == 10000000000000000000}, usize {b: b == 19}) -> u64{v: v == 1})]
pub const fn my_right_shift_u64_1e19_by19(a: u64, b: usize) -> u64 {
    a >> b
}

#[stable(feature = "downgraded_weak", since = "1.10.0")]
#[flux_attrs::trusted]
#[flux_attrs::sig(fn (a: u8) -> usize {v: v == a})]
pub fn my_from_usize_u8(a: u8) -> usize { usize::from(a) }

