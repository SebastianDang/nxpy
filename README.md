# Nx-Py

## Loading Nx files

#### _NxFile_

```
file = NxFile(`your-path-to-nx/map.nx`)
```

#### _NxFileSet_

```
fileSet = NxFileSet(`your-path-to-nx/map.nx', `your-path-to-nx/sound.nx`)
fileSet.load(`your-path-to-nx/ui.nx')
```

---

## Getting raw values from data types [long, double, string, point(x, y)]

#### _NxNode_

```
node = file.resolve('Map/Map0/000010000.img/info/bgm')
data = node.value
```

---

### Getting buffer from images and sounds

#### _NxImage_

```
node = file.resolve('Tile/grassySoil.img/bsc/0')
data = node.get_image()
```

#### _NxSound_

```
node = file.resolve(`Bgm34.img/MapleLeaf')
data = node.get_sound()
```
