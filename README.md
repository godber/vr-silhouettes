# Things

Split source video into individual files:

```bash
ffmpeg -i ~/TOL.ts  /srv/godber/temp/TOL/TOL%07d.jpg
```

Run on a single file:

```bash
./binarize.py /srv/godber/TOL/xxoutput_0007877.jpg
```

Run on many files with some parallelism:

```bash
find /srv/godber/TOL/ -maxdepth 1 -name "*.jpg" | parallel -j50% ./binarize.py {} :::
```

Mask:

* Top Left: 498, 370
* Bottom Right: 573, 422
