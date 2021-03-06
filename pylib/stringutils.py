import re
from functools import partial

def try_singularize(word):
  # not accurate but works for most cases
  if word.endswith('ies'):
    return word[:-3] + 'y'

  if word.endswith(('les', 'tes')):
    return word[:-1]
  if word.endswith('es'):
    return word[:-2]

  if word.endswith('us'):
    return word

  if word.endswith('s'):
    return word[:-1]

  return word

_camel_to_underline_re = re.compile(r'[A-Z]')
def _camel_to_underline_replacer(m):
  if m.start() == 0:
    return m.group().lower()
  return '_' + m.group().lower()

camel_to_underline = partial(
  _camel_to_underline_re.sub,
  _camel_to_underline_replacer,
)
