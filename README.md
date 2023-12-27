# Draw-Bot-for-any-online-game-or-application

## works on anything with a canvas, a constant brush size and and colors such as

- skribbl.io
- gartic phone, gartic.io
- sketchful.io
- ms paint

## features
  
- outline drawing like a human (kinda)
- outline drawing with random lines
- colored dithering
- black and white dithering
- quantized drawing for faster times (color by color or line by line)
- settings for colors, brushsize, speed and drawing area
- supports image urls and file paths inside the url box

> before running, install the requirements using pip make sure to calibrate it before drawing. In case you need it, 'q' is the failsafe
>
> I belive this is the fastest and most versitile one out there and it's also very easy to use. It is recommended to use clipart images for faster drawing times (not necessary for dithering)

## UI

![image](https://github.com/Nuspli/Draw-Bot-for-any-online-game-or-application/assets/108233076/9d3e71c7-b6f5-4b2c-a881-7a86930f2dc2)

- `brush size` depends on how many pixels in a row your selected brush covers. most of the time this will not be one since most brushes cover more that a single pixel the image will get scaled according to this size
- `layers only` affect the floyd steinberg dithering option. 1 layer is usually fine, but if that takes too long you can choose to skip every 2nd, 3rd, 4th, ... pixel by splitting it into multiple layers. this will give a better overview of the full picture. checking the adaptive checkbox will only draw the last 3rd of the colors as 2 layers
- to choose the colors and drawing area, click on the calibration buttons and follow the instructions
- `Image URL` accepts system file paths and image links aswell as some dropped images from google (experimental)

## Examples:
![skribblAnything0x90](https://github.com/Nuspli/Draw-Bot-for-any-online-game-or-application/assets/108233076/3b61005d-13fc-45dc-948e-47755ce1c4d5)
![skribblAnything0x90 (1)](https://github.com/Nuspli/Draw-Bot-for-any-online-game-or-application/assets/108233076/ee13a6e1-cdc0-447d-b928-d283a73dddb7)
![skribblAnything0x90 (2)](https://github.com/Nuspli/Draw-Bot-for-any-online-game-or-application/assets/108233076/a4488698-531a-47e1-8e89-d6408ea5bd68)
![skribblAnything0x90 (3)](https://github.com/Nuspli/Draw-Bot-for-any-online-game-or-application/assets/108233076/2d6eb084-6455-4101-b6ef-77616ee9643a)
![skribblAnything0x90 (4)](https://github.com/Nuspli/Draw-Bot-for-any-online-game-or-application/assets/108233076/d6ee5f6c-0956-4a6c-b061-555c83523abb)
![skribblAnything0x90 (5)](https://github.com/Nuspli/Draw-Bot-for-any-online-game-or-application/assets/108233076/86cdf912-52db-4601-9a33-480c807d47d1)

> can't get it work? message me on discord: `kolmus`
