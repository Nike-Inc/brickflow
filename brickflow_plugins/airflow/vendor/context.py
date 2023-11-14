from __future__ import annotations

import contextlib
import copy
from typing import MutableMapping, Any, Iterator, KeysView, ItemsView, ValuesView


class Context(MutableMapping[str, Any]):
    """Jinja2 template context for task rendering.

    This is a mapping (dict-like) class that can lazily emit warnings when
    (and only when) deprecated context keys are accessed.
    """

    _DEPRECATION_REPLACEMENTS: dict[str, list[str]] = {
        "execution_date": ["data_interval_start", "logical_date"],
        "next_ds": ["{{ data_interval_end | ds }}"],
        "next_ds_nodash": ["{{ data_interval_end | ds_nodash }}"],
        "next_execution_date": ["data_interval_end"],
        "prev_ds": [],
        "prev_ds_nodash": [],
        "prev_execution_date": [],
        "prev_execution_date_success": ["prev_data_interval_start_success"],
        "tomorrow_ds": [],
        "tomorrow_ds_nodash": [],
        "yesterday_ds": [],
        "yesterday_ds_nodash": [],
    }

    def __init__(
        self, context: MutableMapping[str, Any] | None = None, **kwargs: Any
    ) -> None:
        self._context: MutableMapping[str, Any] = context or {}
        if kwargs:
            self._context.update(kwargs)
        self._deprecation_replacements = self._DEPRECATION_REPLACEMENTS.copy()

    def __repr__(self) -> str:
        return repr(self._context)

    def __reduce_ex__(self, protocol: int) -> tuple[Any, ...]:
        """Pickle the context as a dict.

        We are intentionally going through ``__getitem__`` in this function,
        instead of using ``items()``, to trigger deprecation warnings.
        """
        items = [(key, self[key]) for key in self._context]
        return dict, (items,)

    def __copy__(self) -> Context:
        new = type(self)(copy.copy(self._context))
        new._deprecation_replacements = self._deprecation_replacements.copy()
        return new

    def __getitem__(self, key: str) -> Any:
        # with contextlib.suppress(KeyError):
        #     warnings.warn(_create_deprecation_warning(key, self._deprecation_replacements[key]))
        with contextlib.suppress(KeyError):
            return self._context[key]
        raise KeyError(key)

    def __setitem__(self, key: str, value: Any) -> None:
        self._deprecation_replacements.pop(key, None)
        self._context[key] = value

    def __delitem__(self, key: str) -> None:
        self._deprecation_replacements.pop(key, None)
        del self._context[key]

    def __contains__(self, key: object) -> bool:
        return key in self._context

    def __iter__(self) -> Iterator[str]:
        return iter(self._context)

    def __len__(self) -> int:
        return len(self._context)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Context):
            return NotImplemented
        return self._context == other._context

    def __ne__(self, other: Any) -> bool:
        if not isinstance(other, Context):
            return NotImplemented
        return self._context != other._context

    def keys(self) -> KeysView[str]:
        return self._context.keys()

    def items(self):
        return ItemsView(self._context)

    def values(self):
        return ValuesView(self._context)
