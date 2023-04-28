import json
import random
import subprocess

def formatFive(number, start, end):
  return f'{number:05}'[start:end]

def get_code(number, color_a, color_b):
  return f'''
    <svg id="numberzzz" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 808.89 824.44">
      <defs><style>.cls-1,.cls-3{{fill: #{color_a};}}.cls-2{{fill: #{color_b};}}.cls-3{{font-size:375px;font-family:ArialMT, Arial;}}</style></defs>
      <rect class="cls-1" width="808.89" height="808.89"/>
      <rect class="cls-2" x="86.09" y="90" width="634.47" height="647.88"/>
      <text class="cls-3" x="50%" y="50%" transform="translate(-383, -110) scale(1.1, 1.3)" lengthAdjust="spacingAndGlyphs">{formatFive(number, 0, 2)}</text>
      <text class="cls-3" x="50%" y="50%" transform="translate(-383, 230) scale(1.1, 1.3)" lengthAdjust="spacingAndGlyphs">{formatFive(number, 2, 5)}</text>
    </svg>
  '''

def get_palettes():
  with open('data.json', 'r') as f:
    return [[swatch['hex'] for swatch in file['swatches']] for file in json.load(f)['files'] if len(file['swatches']) > 1]

def make_nfts():
  k = 20_000
  print(get_palettes())
  palettes = [(indx, p[0], p[-1]) for indx, p in enumerate(get_palettes())]
  output = [(indx+1, color_a, color_b) for (indx, color_a, color_b) in palettes]

  for at, (indx, color_a, color_b) in enumerate(random.choices(output, k=k)):
    item = at + 1
    data = get_code(item, color_a, color_b)
    with open(f'./output/{item}.svg', 'w') as f:
      f.write(data)
      # img_encoded = base64.b64encode(bytes(data, 'utf-8')).decode('utf-8')
      # json.dump({
      #   'name': f'No. {item:05}',
      #   'image': f'data:image/svg+xml;base64,{img_encoded}' ,
      #   'properties': {
      #     'color a': f'#{color_a}',
      #     'color b': f'#{color_b}',
      #     'color_index': f'{indx}'
      #   }
      # }, f)
    subprocess.call(f'rsvg-convert output/{item}.svg > ./output-png/{item}.png', shell=True)

if __name__ == '__main__':
  make_nfts()
