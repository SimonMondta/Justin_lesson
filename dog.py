def dog(noise):
  if noise == 'bark':
    return 'warf'
  else:
    return 'confused dog grunts'

def test_barking():
  assert dog('bark') == 'woof'

def test_borking():
  assert dog('bork') != 'woof'
