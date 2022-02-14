# Python Nx Parser

## Loading Nx files

#### _NxFile_

``` python
file = NxFile(`your-path-to-nx/map.nx`)
```

#### _NxFileSet_

``` python
fileSet = NxFileSet('your-path-to-nx/map.nx', 'your-path-to-nx/sound.nx')
fileSet.load(`your-path-to-nx/ui.nx')
```

## Retrieving values from data types [long, double, string, point(x, y)]

#### _NxNode_

``` python
node = file.resolve('Map/Map0/000010000.img/info/bgm')
data = node.value
```

## Retrieving buffers from images and sounds

#### _NxImage_

``` python
node = file.resolve('Tile/grassySoil.img/bsc/0')
data = node.get_image()
```

#### _NxSound_

``` python
node = file.resolve('Bgm34.img/MapleLeaf')
data = node.get_sound()
```

## Additional Resources

- [NoLifeWzToNx](https://github.com/ryantpayton/NoLifeWzToNx)
- [nxformat](https://nxformat.github.io/)
- [harepacker](https://github.com/lastbattle/Harepacker-resurrected)
