"""Explicit dev hostname migration shared by preparation and validation tools."""
import re

DOMAIN = 'development.oanstaging.com'
GATEWAY = 'istio-system/development'
LEGACY = re.compile(r'(?<![A-Za-z0-9_.-])([a-z0-9-]+)-development\.oanstaging\.com(?![A-Za-z0-9_.-])')


def replace_text(value, aliases=None):
    value = LEGACY.sub(lambda m: m[1] + '.' + DOMAIN, value)
    for old, new in sorted((aliases or {}).items(), key=lambda pair: -len(pair[0])):
        value = re.sub(r'(?<![A-Za-z0-9_.-])' + re.escape(old) + r'(?![A-Za-z0-9_.-])', new, value)
    return value


def migrate_values(value, aliases=None, path=()):
    if isinstance(value, dict):
        result = {k: migrate_values(v, aliases, path + (str(k),)) for k, v in value.items()}
        if path and path[-1].lower() == 'virtualservice' and 'istio' in path:
            result['gateway'] = GATEWAY
        if path and path[-1] == 'global' and 'baseDomain' in result:
            result['baseDomain'] = DOMAIN
        return result
    if isinstance(value, list):
        return [migrate_values(v, aliases, path + (str(i),)) for i, v in enumerate(value)]
    if isinstance(value, str):
        if path and ('COOKIE' in path[-1].upper() and 'DOMAIN' in path[-1].upper()) and value == '.oanstaging.com':
            return '.' + DOMAIN
        return replace_text(value, aliases)
    return value
