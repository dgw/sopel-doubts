# sopel-doubts

A Sopel plugin letting users "Press X to doubt".

## Installing

```sh
pip install sopel-doubts
```

## Using

Triggers on these characters (case-insensitive):

* X
* Ⓧ
* 𝕏

The X must be the only character on its line, or part of a CTCP ACTION (`/me`)
exactly matching the pattern `presse[ds] X`.

## Credits

This is a continuation of [ActionSack's `sopel-doubts`][asak-doubts-source],
which has been marked as archived and no longer maintained. It maintains the
same license and authorship credits as the original.

CTCP ACTION support is new to this fork.

[//]: # (asak-doubts-source is also used in the NEWS file appended for PyPI)
[asak-doubts-source]: https://git.actionsack.com/xnaas-archived/sopel-doubts
