# Tiling

#### About

A *tiling problem* is a mathematical problem to fill a given region entirely with given tiles without any overlap and gap. A good example is Tetris.

### Problem statement

#### Problem 1

You need to fill a `W × H` rectangular region with the largest possible squares. All the squares must have the same size. The dimensions must be in natural numbers.

For exaple, the `6 × 3` region can be filled with two `3 × 3` squares.

Implement the code that computes the size of square for a given region size.

#### Problem 2

> I came up with this problem when I needed to determine the dimension of a canvas for `N` image thumbnails.

You need to determine the dimension of a `W × H` rectangular region for placing `N` numbers of the same-sized `d x d` squares orthogonally.

In this problem, you have the following conditions.

1. The dimensions must be in natural numbers (same as Problem 1).
2. You are allowed to have gaps, however, no empty row or column is allowed.
3. The aspect ratio must be as close as the TV standard size: i.e., width 4 : height 3 (or 1.33)
4. When you have more than one dimensions that satisfy the aspect ratio condition, pick the one with longer width (prefer landscape).

For example

For `12` squares, the dimension should be `4 x 3`. No gap. The aspect ration is exactly 1.33.

```
■ ■ ■ ■
■ ■ ■ ■
■ ■ ■ ■
```

For `13` squares, the dimension shoule be `5 x 3`. There are two gaps in the last row but permitted (Condition 2).

```
■ ■ ■ ■ ■
■ ■ ■ ■ ■
■ ■ ■
```

You can also place 13 squares in the `6 x 3` as below.

```
■ ■ ■ ■ ■ ■
■ ■ ■ ■ ■ ■
■
```

However, `5 x 3` is chosen because its aspect ratio (1.67) is closesr to the target (1.33) as compared to 2.0 (Condition 3).

You can also place 13 squares in the `4 x 4` region. It's aspect ratio is 1.0 (3/3) and it is as close as the aspect ration of `5 x 3` (5/3) to the target ratio 4/3 (both 1/3 apart).

```
■ ■ ■ ■
■ ■ ■ ■
■ ■ ■ ■
■
```

Yet, `5 x 3` is chosen because it has longer width (more landscape-ish) while `4 x 4` is a squre.

Implement the code.