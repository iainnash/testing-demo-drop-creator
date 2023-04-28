import json
import base64

def get_code(number, color_a, color_b):
  return f'''
  <svg id="numberzzz" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 808.89 824.44"><defs><style>.cls-1,.cls-3{{fill: #{color_a};}}.cls-2{{fill: #{color_b};}}.cls-3{{font-size:650px;font-family:ArialMT, Arial;}}</style></defs><rect class="cls-1" width="808.89" height="808.89"/><rect class="cls-2" x="86.09" y="90" width="634.47" height="647.88"/><text class="cls-3" x="50%" y="50%" transform="translate(-363, 180)">{number:02}</text></svg>
  '''

def get_palettes():
  with open('data.json', 'r') as f:
    return [[swatch['hex'] for swatch in file['swatches']] for file in json.load(f)['files'] if len(file['swatches']) > 1]

def make_nfts():
  print(get_palettes())
  palettes = [(indx, p[0], p[-1]) for indx, p in enumerate(get_palettes())]
  output = [(indx+1, get_code(indx, color_a, color_b), color_a, color_b) for (indx, color_a, color_b) in palettes]
  for indx, data, color_a, color_b in output:
    with open(f'./output/{indx}', 'w') as f:
      img_encoded = base64.b64encode(bytes(data, 'utf-8')).decode('utf-8')
      json.dump({
        'name': f'No. {indx:02}',
        'image': f'data:image/svg+xml;base64,{img_encoded}' ,
        'properties': {
          'color a': f'#{color_a}',
          'color b': f'#{color_b}',
        }
      }, f)

if __name__ == '__main__':
  make_nfts()
