# CHANGELOG:

## September 6th, 2019 - v2.0.0 initial release:
1. Rewrote the [Rust version](https://github.com/JosephTLyons/andromeda_rust) in
   Python in order to avoid issues directly related to the Rust implementation.
    - Because Python's integer types have no upper limit (outside the bounds of
      your computer's memory), we can create licenses of practically any length
      using 92 different types of characters (`10` numbers, `26` lowercase
      letters, `26` uppercase letters, and `32` symbols).
