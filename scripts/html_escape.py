#!/usr/bin/env python
# encoding: utf-8
from lxml.html.clean import Cleaner

_DEFAULT_ALLOW_TAGS = frozenset(['a', 'ins', 'del', 'pre', 'b', 'img', 'ul', 'i', 'equation', 'li', 'p', 'blockquote', 'ol', 'u', 'br', 'sup', 'video', 'div', 'strong', 'embed'])
_DEFAULT_SAFE_ATTRS = frozenset(['src', 'id', 'data-videoid', 'href', 'class', 'data_id', 'data-id'])


def select_escape(allow_tags=None, safe_attrs=None):
    _allow_tags = _DEFAULT_ALLOW_TAGS.union(allow_tags) if allow_tags else _DEFAULT_ALLOW_TAGS
    _safe_attrs = _DEFAULT_SAFE_ATTRS.union(safe_attrs) if safe_attrs else _DEFAULT_SAFE_ATTRS
    cleaner = Cleaner(allow_tags=_allow_tags, remove_unknown_tags=False, safe_attrs=_safe_attrs)
    return cleaner.clean_html
