# Valid Parentheses

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
1. Open brackets must be closed in the correct order.
 

**Example 1:**
```py
Input: s = "()"
Output: true
```
**Example 2:**
```py
Input: s = "()[]{}"
Output: true
```
**Example 3:**
```py
Input: s = "(]"
Output: false
```
**Example 4:**
```py
Input: s = "([)]"
Output: false
```
**Example 5:**
```py
Input: s = "{[]}"
Output: true
```

**Constraints:**

* <code>1 <= s.length <= 10<sup>4</sup></code>
* `s` consists of parentheses only `'()[]{}'`.
