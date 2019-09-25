# Things

```bash
ffmpeg -i ~/TOL.ts  /srv/godber/temp/TOL/TOL%07d.jpg
```

```bash
find /srv/godber/TOL/ -name "*.jpg" | parallel -j100 ./binarize.py {} :::
find /srv/godber/TOL/ -maxdepth 1 -name "*.jpg" | parallel -j50% ./binarize.py {} :::
```

Mask:

* Top Left: 498, 370
* Bottom Right: 573, 422
